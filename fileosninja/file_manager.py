import os
import shutil

def read_file(filename):
    """
    Reads the contents of a file and returns the content as a string.

    Parameters:
    - filename (str): The name or path of the file to be read.

    Returns:
    str: The content of the file as a string.

    Raises:
    FileNotFoundError: If the specified file is not found.
    IOError: If an error occurs while reading the file.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    except IOError as e:
        raise IOError(f"Error reading the file '{filename}': {e}")


def write_file(filename, content="", append=True):
    """
    Creates a new file or appends content to an existing file with the specified filename.

    If no content is provided (default is an empty string), an empty file will be created or
    existing content will be preserved if the file already exists.

    Parameters:
    - filename (str): The name or path of the file to be created or appended to.
    - content (str, optional): The content to be written to the file. Defaults to an empty string.
    - append (bool, optional): If True, appends content to an existing file; if False, overwrites the file.
                              Defaults to True.

    Returns:
    None

    Raises:
    IOError: If an error occurs while creating or writing to the file.
    """
    try:
        mode = 'a' if append else 'w'
        with open(filename, mode) as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"Error creating/appending to the file '{filename}': {e}")

def delete_file(filename):
    """
    Deletes the specified file.

    Parameters:
    - filename (str): The name or path of the file to be deleted.

    Returns:
    None

    Raises:
    FileNotFoundError: If the specified file is not found.
    IOError: If an unexpected error occurs while deleting the file.

    """
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f"Couldn't find '{filename}' for deletion.")
    except IOError as e:
        raise IOError(f"Error deleting '{filename}': {e}")

def move_file(file_path, new_folder):
    """
    Moves a file to a new folder.

    Parameters:
    - file_path (str): The path to the file to be moved.
    - new_folder (str): The path to the destination folder where the file will be moved.

    Returns:
    None

    Raises:
    FileNotFoundError: If the source file is not found.
    IOError: If an error occurs while moving the file.
    """
    try:
        # Ensure the new folder exists; create it if it doesn't.
        os.makedirs(new_folder, exist_ok=True)

        # Extract the file name from the file path
        file_name = os.path.basename(file_path)

        # Construct the destination path by joining the new folder and the file name
        destination_path = os.path.join(new_folder, file_name)

        # Move the file to the new folder
        shutil.move(file_path, destination_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The source file '{file_path}' does not exist.")
    except IOError as e:
        raise IOError(f"Error moving the file from '{file_path}' to '{new_folder}': {e}")
    
def rename_directory(path, new_name):
    """
    Renames the given path (file or folder) to a new name.

    Parameters:
    - path (str): The path to the file/folder to be renamed.
    - new_name (str): The new name of the file/folder.

    Returns:
    None

    Raises:
    FileNotFoundError: If the source file is not found.
    IOError: If an error occurs while renaming the file.
    """
    try:
        # path to the file/folder excluding itself
        base_directory = os.path.dirname(path) 

        # construct the new path with the new name
        new_path = os.path.join(base_directory, new_name)

        # rename the directory
        os.rename(path, new_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The source file '{path}' does not exist.")
    except IOError as e:
        raise IOError(f"Error renaming the file from '{os.path.basename(path)}' to '{new_name}': {e}")

def copy_file(file_path, destination_folder, copy_name=None):
    """
    Copies a file to a destination folder.

    Parameters:
    - file_path (str): The path to the file to be copied.
    - destination_folder (str): The path to the destination folder where the file will be copied to.
    - copy_name (str): The name of the copied file. (copy_of_{file_name} by default)

    Returns:
    None

    Raises:
    FileNotFoundError: If the source file is not found.
    IOError: If an error occurs while copying the file.
    """
    try:
        if not copy_name:
            # name of file
            file_name = os.path.basename(file_path)
            copy_name = f"copy_of_{file_name}"

        # begin copying
        destination_path = os.path.join(destination_folder, copy_name)
        shutil.copy(file_path, destination_path)

    except FileNotFoundError:
        raise FileNotFoundError(f"The source file '{file_path}' does not exist.")
    except IOError as e:
        raise IOError(f"Error copying the file from '{file_path}' to '{destination_path}': {e}")
    
def copy_folder(folder_path, destination_folder, copy_name=None, depth=float("inf")):
    """
    Copies a folder (to the given depth) to a destination folder.

    Parameters:
    - folder_path (str): The path to the folder to be copied.
    - destination_folder (str): The path to the destination folder where the file will be copied to.
    - copy_name (str): The name of the copied folder (copy_of_{folder_name} by default)
    - depth (int): The depth at which to copy the folder. (deep copy by default)

    Returns:
    None

    Raises:
    FileNotFoundError: If the source folder is not found.
    IOError: If an error occurs while copying the folder.
    AssertionError: If the destination_folder is within the source folder.
    """
    try:
        # Ensure the destination folder is not within the source folder
        try:
            common_path = os.path.commonpath([folder_path, destination_folder])
            assert common_path != folder_path, "Destination folder should not be inside source folder"     
        except ValueError:
            # commonpath raises ValueError if the paths have no common prefix
            pass
        
        # Recursively copy directory
        def copy_current_directory(current_path, current_destination_folder, current_depth):
            if not os.path.exists(current_path):
                raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
            if current_depth <= depth:
                # Copy the current directory
                if current_depth == 0:
                    current_path_name = copy_name
                else:
                    current_path_name = os.path.basename(current_path)

                # if folder, make a new folder with the given name at destination
                if os.path.isdir(current_path):
                    # Copy the source folder into the destination folder. Consequently, this new path becomes the new destination folder.
                    new_destination_path = os.path.join(current_destination_folder, current_path_name)
                    os.makedirs(new_destination_path)

                    # Recursively copy contents for subdirectories
                    for file in os.listdir(current_path):
                        new_current_path = os.path.join(current_path, file)
                        copy_current_directory(new_current_path, new_destination_path, current_depth + 1)
                
                # if file, copy file
                else:
                    copy_file(current_path, current_destination_folder, copy_name=current_path_name)

        # Initiate copying
        if not copy_name:
            # name of file
            folder_name = os.path.basename(folder_path)
            copy_name = f"copy_of_{folder_name}"

        copy_current_directory(folder_path, destination_folder, 0)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error copying the file from '{folder_path}' to '{destination_folder}': {e}")
    except AssertionError as e:
        print(f"Error: {e}")
