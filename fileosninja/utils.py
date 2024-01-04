import os
    
def print_directory(folder_path, depth=3):
    """
    Print the structure of a folder to the given depth.

    Parameters:
    - foldername (str): The name or path of the folder to display the structure of
    - depth (int): The depth at which to display the structure of (default depth is 3)

    Returns:
    None

    Raises:
    AssertionError: If the specified folder is not found.
    IOError: If an error occurs during a folder operation
    """

    # Recursively print directory
    def print_current_directory(current_path, current_depth):
        try:
            if current_depth <= depth:
                # Print the current directory
                assert os.path.exists(current_path), f"The folder '{current_path}' does not exist."
                current_folder_name = os.path.basename(current_path)
                if current_depth == 0:
                    print(current_folder_name)
                elif current_depth == 1:
                    print(f"|-- {current_folder_name}")
                else:
                    print("|   " + "    " * (current_depth - 2) + f"|-- {current_folder_name}")

                if os.path.isdir(current_path):
                    # Recursively print contents for subdirectories
                    for file in os.listdir(current_path):
                        file_path = os.path.join(current_path, file)
                        print_current_directory(file_path, current_depth + 1)
        except AssertionError as e:
            print(f"Error: {e}")
        except IOError as e:
            print(f"IOError: {e}")

    # Start printing contents from the specified folder
    print_current_directory(folder_path, 0)