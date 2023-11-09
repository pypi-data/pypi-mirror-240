from mock import Mock, patch
from unittest.mock import call, mock_open
from ara_tools.artefact_renamer import ArtefactRenamer  # Adjust this import path according to your setup
from ara_tools.classifier import Classifier  # Adjust this import path according to your setup

import mock  # Add this line at the top of your file
import pytest
import os



# Assuming that the ArtefactRenamer class is in a file named artefact_renamer.py

# Test case 1: should check if the filename exists
@patch("ara_tools.artefact_renamer.os.path.exists")
def test_rename_checks_filename_exists(mock_exists):
    mock_exists.return_value = False
    ar = ArtefactRenamer(os)
    with pytest.raises(FileNotFoundError):
        ar.rename("nonexistent_file", "new_file", "vision")

# Test case 2: should check if the classifier is valid
def test_rename_checks_classifier_valid():
    ar = ArtefactRenamer(os)
    with pytest.raises(ValueError):
        ar.rename("existing_file", "new_file", "invalid_classifier")

# Test case 3: should check if the new_name is provided
def test_rename_checks_new_name_provided():
    ar = ArtefactRenamer(os)
    with pytest.raises(ValueError):
        ar.rename("existing_file", "vision", None)



@patch("builtins.open", new_callable=mock_open, read_data="Vision statement: Old Title\nOther content.")
@patch("ara_tools.artefact_renamer.os.rename")
@patch("ara_tools.artefact_renamer.os.path.exists", side_effect=[True, True, False, False])
def test_rename_filename_with_new_name(mock_exists, mock_rename, mock_open):
    ar = ArtefactRenamer(os)
    ar.rename("existing_file", "new_file", "vision")
    assert mock_rename.call_count == 2
    mock_rename.assert_has_calls([
        call("ara/vision/existing_file.vision", "ara/vision/new_file.vision"),
        call("ara/vision/existing_file.data", "ara/vision/new_file.data")
    ])


# Test case 5: should throw an error if the new file or directory already exists
@patch("ara_tools.artefact_renamer.os.path.exists", side_effect=[True, True, True, False])
def test_rename_throws_error_if_new_file_or_directory_exists(mock_exists):
    ar = ArtefactRenamer(os)
    with pytest.raises(FileExistsError):
        ar.rename("existing_file", "existing_file", "vision")

# Test case 6: should check if the related data folder exists when renaming a file
@patch("ara_tools.artefact_renamer.os.path.exists", side_effect=[True, False, False])
def test_rename_checks_related_data_folder_exists(mock_exists):
    ar = ArtefactRenamer(os)
    with pytest.raises(FileNotFoundError):
        ar.rename("old_name", "new_name", "story")



@patch("builtins.open", new_callable=mock_open, read_data="User story: Old Title\nOther content.")
@patch("ara_tools.artefact_renamer.os.rename")
@patch("ara_tools.artefact_renamer.os.path.exists", side_effect=[True, True, False, False])
def test_rename_also_renames_related_data_folder(mock_exists, mock_rename, mock_open):
    ar = ArtefactRenamer(os)
    ar.rename("old_name", "new_name", "story")
    assert mock_rename.call_count == 2
    mock_rename.assert_has_calls([
        call("ara/stories/old_name.story", "ara/stories/new_name.story"),
        call("ara/stories/old_name.data", "ara/stories/new_name.data")
    ])



# Test case 8: should throw an error if the new data folder name already exists
@patch("ara_tools.artefact_renamer.os.path.exists", side_effect=[True, True, True])
def test_rename_throws_error_if_new_data_folder_exists(mock_exists):
    ar = ArtefactRenamer(os)
    with pytest.raises(FileExistsError):
        ar.rename("old_name", "new_name", "story")

# Test case 9: should not proceed with renaming if the old data folder does not exist
@patch("ara_tools.artefact_renamer.os.path.exists", side_effect=[True, False])
def test_rename_does_not_proceed_if_old_data_folder_missing(mock_exists):
    ar = ArtefactRenamer(os)
    with pytest.raises(FileNotFoundError):
        ar.rename("old_name", "new_name", "story")



# ... Changing title ...


@pytest.mark.parametrize("classifier,artefact_name,read_data_prefix,old_title,new_title", [
    ("vision", "Vision statement", "Vision statement: ", "Old Title", "New title"),
    ("businessgoal", "Business goal", "Business goal: ", "Old Title", "New title"),
    ("capability", "Capability", "Capability: ", "Old Title", "New title"),
    ("keyfeature", "Key feature", "Key feature: ", "Old Title", "New title"),
    ("feature", "Feature", "Feature: ", "Old Title", "New title"),
    ("epic", "Epic", "Epic: ", "Old Title", "New title"),
    ("story", "User story", "User story: ", "Old Title", "New title"),
    ("task", "Task", "Task: ", "Old Title", "New title"),
    ("task", "Task list", "Task list: ", "Old Title", "New title"),
    ("example", "Example", "Example: ", "Old Title", "New title"),
])


@patch("builtins.open", new_callable=mock_open)
def test_update_title_in_artefact(mock_file, classifier, artefact_name, read_data_prefix, old_title, new_title):
    ar = ArtefactRenamer(os)
    read_data = f"{read_data_prefix}{old_title}\nOther content that remains unchanged."
    mock_file.return_value.read = mock.Mock(return_value=read_data)
    artefact_path = f"path/to/{classifier}.artefact"

    # Ensure that the mock for get_artefact_title returns the prefix without an extra colon and space
    with patch.object(Classifier, 'get_artefact_title', return_value=artefact_name):
        ar._update_title_in_artefact(artefact_path, new_title, classifier)

    # Check that the file was opened for reading
    mock_file.assert_any_call(artefact_path, 'r')
    # Check that the file was opened for writing
    mock_file.assert_any_call(artefact_path, 'w')
    # Check that the file write was called with the correct new content
    expected_content = read_data.replace(f"{read_data_prefix}{old_title}", f"{read_data_prefix}{new_title}")
    mock_file().write.assert_called_with(expected_content)



