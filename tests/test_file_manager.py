import unittest
import tempfile
import os
import shutil

from fileosninja.file_manager import read_file, write_file, move_file, delete_file

class TestFileManagerFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.temp_dir)

    def test_read_file_existing(self):
        # Test reading an existing file
        test_content = "Test content for read_file function."
        file_path = os.path.join(self.temp_dir, 'test_read_file.txt')

        with open(file_path, 'w') as test_file:
            test_file.write(test_content)

        result = read_file(file_path)
        self.assertEqual(result, test_content)

    def test_read_file_nonexistent(self):
        # Test reading a nonexistent file
        non_existent_file = os.path.join(self.temp_dir, 'non_existent_file.txt')

        with self.assertRaises(FileNotFoundError):
            read_file(non_existent_file)

    def test_write_file_create(self):
        # Test creating a new file
        file_path = os.path.join(self.temp_dir, 'test_write_file_create.txt')
        test_content = "Test content for write_file function."

        write_file(file_path, test_content)

        with open(file_path, 'r') as test_file:
            result = test_file.read()

        self.assertEqual(result, test_content)

    def test_write_file_append(self):
        # Test appending content to an existing file
        file_path = os.path.join(self.temp_dir, 'test_write_file_append.txt')
        existing_content = "Existing content."
        new_content = "Appended content."

        # Create the file with existing content
        with open(file_path, 'w') as test_file:
            test_file.write(existing_content)

        write_file(file_path, new_content, append=True)

        with open(file_path, 'r') as test_file:
            result = test_file.read()

        expected_result = existing_content + new_content
        self.assertEqual(result, expected_result)

    def test_write_file_overwrite(self):
        # Test overwriting content in an existing file
        file_path = os.path.join(self.temp_dir, 'test_write_file_overwrite.txt')
        existing_content = "Existing content."
        new_content = "New content."

        # Create the file with existing content
        with open(file_path, 'w') as test_file:
            test_file.write(existing_content)

        write_file(file_path, new_content, append=False)

        with open(file_path, 'r') as test_file:
            result = test_file.read()

        self.assertEqual(result, new_content)

    def test_delete_file_existing(self):
        # Test deleting an existing file
        file_path = os.path.join(self.temp_dir, 'test_delete_file.txt')

        write_file(file_path)
        delete_file(file_path)

        self.assertFalse(os.path.exists(file_path))

    def test_delete_file_nonexistent(self):
        # Test deleting a nonexistent file
        file_path = os.path.join(self.temp_dir, 'non_existent_file.txt')

        with self.assertRaises(FileNotFoundError):
            delete_file(file_path)

    def test_move_file(self):
        # Test moving a file to a new folder
        file_path = os.path.join(self.temp_dir, 'test_move_file.txt')
        new_folder = os.path.join(self.temp_dir, 'new_folder')
        test_content = "Test content for move_file function."

        # Create the file with content
        with open(file_path, 'w') as test_file:
            test_file.write(test_content)

        move_file(file_path, new_folder)

        # Check if the file was moved successfully
        new_file_path = os.path.join(new_folder, 'test_move_file.txt')
        with open(new_file_path, 'r') as moved_file:
            result = moved_file.read()

        self.assertEqual(result, test_content)

if __name__ == '__main__':
    unittest.main()
