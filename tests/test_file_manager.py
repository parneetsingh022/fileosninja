import unittest
import tempfile
import os
import shutil


from fileosninja.file_manager import (
    read_file, 
    write_file,
    copy_file,
    copy_folder,
    rename_directory,
    move_file,
    delete_file
)
class TestFileOperations(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory and its contents after each test
        shutil.rmtree(self.temp_dir)

    def test_read_file(self):
        # Create a temporary file with some content
        test_file = os.path.join(self.temp_dir, 'test.txt')
        with open(test_file, 'w') as file:
            file.write('Test content')

        # Test if read_file reads the content correctly
        content = read_file(test_file)
        self.assertEqual(content, 'Test content')

        # Test if read_file raises FileNotFoundError for non-existent file
        with self.assertRaises(FileNotFoundError):
            read_file('nonexistent.txt')

    def test_write_file(self):
        # Test writing content to a file
        test_file = os.path.join(self.temp_dir, 'test.txt')
        write_file(test_file, 'Test content')
        with open(test_file, 'r') as file:
            content = file.read()
        self.assertEqual(content, 'Test content')

        # Test appending content to a file
        write_file(test_file, 'Additional content', append=True)
        with open(test_file, 'r') as file:
            content = file.read()
        self.assertEqual(content, 'Test contentAdditional content')

        # Test overwriting content in a file
        write_file(test_file, 'New content', append=False)
        with open(test_file, 'r') as file:
            content = file.read()
        self.assertEqual(content, 'New content')

        # Test if write_file raises IOError for a read-only directory
        with self.assertRaises(IOError):
            write_file('/readonly/test.txt', 'Test content')

    def test_move_file(self):
        # Create a temporary file
        test_file = os.path.join(self.temp_dir, 'test.txt')
        with open(test_file, 'w') as file:
            file.write('Test content')

        # Create a temporary destination folder
        dest_folder = os.path.join(self.temp_dir, 'destination')

        # Test moving the file to the destination folder
        move_file(test_file, dest_folder)

        # Check if the file exists in the destination folder
        dest_file = os.path.join(dest_folder, 'test.txt')
        self.assertTrue(os.path.exists(dest_file))

        # Test if move_file raises FileNotFoundError for a non-existent file
        with self.assertRaises(FileNotFoundError):
            move_file('nonexistent.txt', dest_folder)

    def test_rename_directory(self):
        # Create a temporary directory
        test_dir = os.path.join(self.temp_dir, 'test')
        os.makedirs(test_dir)

        # Test renaming the directory
        new_name = 'getting_tested'
        rename_directory(test_dir, new_name)

        # Check if the directory exists with the new name
        new_path = os.path.join(self.temp_dir, new_name)
        self.assertTrue(os.path.exists(new_path))



    def test_copy_file(self):
        # Create a temporary file
        test_file = os.path.join(self.temp_dir, 'test.txt')
        with open(test_file, 'w') as file:
            file.write('Test content')

        # Create a temporary destination folder
        dest_folder = os.path.join(self.temp_dir, 'destination')
        os.makedirs(dest_folder)  # Ensure destination folder exists

        # Test copying the file to the destination folder
        copy_file(test_file, dest_folder)

        # Check if the copied file exists in the destination folder
        copied_file = os.path.join(dest_folder, 'copy_of_test.txt')
        self.assertTrue(os.path.exists(copied_file))

    def test_delete_file_existing(self):
        # Test deleting an existing file
        file_path = os.path.join(self.temp_dir, 'test_delete_file.txt')

        write_file(file_path)
        self.assertTrue(os.path.exists(file_path))

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
        
    def test_copy_folder(self):
        # Create a temporary directory with some content
        test_dir = os.path.join(self.temp_dir, 'test_directory')
        os.makedirs(test_dir)
        test_file = os.path.join(test_dir, 'test.txt')
        with open(test_file, 'w') as file:
            file.write('Test content')

        # Create a temporary destination folder
        dest_folder = os.path.join(self.temp_dir, 'destination')
        os.makedirs(dest_folder)  # Ensure destination folder exists

        # Test copying the directory to the destination folder
        copy_folder(test_dir, dest_folder)

        # Check if the copied directory exists in the destination folder
        copied_dir = os.path.join(dest_folder, 'copy_of_test_directory')
        self.assertTrue(os.path.exists(copied_dir))
        copied_file = os.path.join(copied_dir, 'test.txt')
        self.assertTrue(os.path.exists(copied_file))


if __name__ == '__main__':
    unittest.main()