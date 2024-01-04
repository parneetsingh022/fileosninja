from fileosninja import file_manager
import os

class FileHandler:
    def __init__(self, filename, append=True):
        """
        Initialize a FileHandler object.

        Parameters:
        - filename (str): The name of the file to be handled.
        - append (bool, optional): A flag indicating whether to append to an existing file 
        (default is True). If False, the file will be truncated.

        Usage:
        ```python
        file = FileHandler("example.txt", append=False)
        ```
        """
        self.filename = filename
        self.append = append

    def set_append_mode(self, new_append_mode):
        """
        Sets the append mode of the file.

        Parameters:
        - new_append_mode (bool): The new append mode (True for append, False for overwrite).
        """
        self.append = new_append_mode

    def read_file(self):
        """
        Read the contents of the file associated with this FileHandler instance.

        Returns:
        str: The content of the file.
        """
        return file_manager.read_file(self.filename)
    
    def write_file(self, content=""):
        """
        Write content to the file associated with this FileHandler instance.

        Parameters:
        - content (str, optional): The content to be written to the file. Default is an empty string.
        """

        file_manager.write_file(self.filename, content=content, append=self.append)

    def move_file(self, new_location):
        """
            Move the file associated with this FileHandler instance to a new location.

            Parameters:
            - new_location (str): The path to the new location for the file.
        """
        file_manager.move_file(self.filename, new_location)
        # changing the file path for this object after it is moved.
        self.filename = os.path.join(new_location, os.path.basename(self.filename))