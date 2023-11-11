from os.path import dirname, basename
from unittest.mock import patch, MagicMock
from ara_tools.directory_navigator import DirectoryNavigator  

import pytest
import os



@pytest.fixture
def navigator():
    return DirectoryNavigator()

@pytest.mark.parametrize("dirs_to_mock, expected_ara_path", [
    # Directly in the ara directory
    (["/home/user/ara"], "/home/user/ara"),

    # In a sub-directory of ara
    (["/home/user/ara/capabilities"], "/home/user/ara"),

    # In a nested sub-directory of ara
    (["/home/user/ara/capabilities/agile_artefact_command_line_management.data"], "/home/user/ara"),

    # In a totally different directory but ara exists one level up
    (["/home/user/some_other_dir", "/home/user/ara"], "/home/user/ara"),

    # In a deep nested directory inside ara, but ara is reachable
    (["/home/user/ara/features/steps"], "/home/user/ara"),

    # In a directory where ara doesn't exist at all
    (["/home/somewhere_else", "/home"], None),
])

### debug version
def test_get_ara_directory(dirs_to_mock, expected_ara_path, navigator):
    
    def mock_exists_side_effect(path):
        # Split the path into parts
        path_parts = path.split(os.sep)
        
        # Count the occurrence of 'ara'
        ara_count = path_parts.count('ara')
        
        # Return True if there's exactly one 'ara' in the path and it's either directly the path or a sub-directory of it
        result = (ara_count == 1) and (path in dirs_to_mock or path.endswith('/ara'))
        print(f"Mock exists called for path: {path}. Result: {result}.")
        return result

    def mock_listdir_side_effect(path):
        subdirs = [os.path.basename(subdir) for subdir in dirs_to_mock if os.path.dirname(subdir) == path]
        print(f"Mock listdir for path: {path}. Subdirectories found: {subdirs}.")
        return subdirs

    def mock_isdir_side_effect(path):
        # Return True if the path is in dirs_to_mock or it's a parent directory of any path in dirs_to_mock
        result = path in dirs_to_mock or any(path == os.path.dirname(subdir) for subdir in dirs_to_mock)
        print(f"Mock isdir called for path: {path}. Result: {result}.")
        return result
    
    print(f"\nTesting with starting directory: {dirs_to_mock[0]} and expected result: {expected_ara_path}")

    with patch("ara_tools.directory_navigator.os.getcwd", return_value=dirs_to_mock[0]):
        mock_exists = MagicMock(side_effect=mock_exists_side_effect)
        with patch("ara_tools.directory_navigator.exists", mock_exists):
            with patch("ara_tools.directory_navigator.isdir", side_effect=mock_isdir_side_effect):  # Use side effect for isdir
                with patch("ara_tools.directory_navigator.os.listdir", side_effect=mock_listdir_side_effect):  # Mock os.listdir
                    if expected_ara_path:
                        result = navigator.get_ara_directory()
                        print(f"Expected directory: {expected_ara_path}. Found directory: {result}.")
                        assert result == expected_ara_path
                    else:
                        print("Expecting exception to be raised...")
                        with pytest.raises(Exception):
                            navigator.get_ara_directory()
    print("Test finished.\n")
