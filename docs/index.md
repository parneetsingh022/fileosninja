# FileOSNinja

## Installing package
```
pip install fileosninja
```

## file_manager {#file_manager}
The File Manager provides user-friendly functions for performing operations on a file. While it is suitable for handling a few operations on a file, when dealing with a more extensive set of operations, it is advisable to employ the [FileHandler](#filehandler). Serving as the class representation of the File Manager, the [FileHandler](#filehandler) proves to be convenient when executing multiple operations on a single file.

We can import 'file_manager' from 'fileosninja' in the following manner:

```python
from fileosninja import file_manager
```

### read_file
> This method reads the contents of a file and returns the content as a string.

Parameters:

- `filename` (str): The name or path of the file to be read.

Returns:

- str: The content of the file as a string.

```python
filename = "path/to/file/file.txt"
file_manager.read_file(filename)
```

### write_file
> Creates a new file or appends content to an existing file with the specified filename.

Parameters:

- `filename` (str): The name or path of the file to be created or appended to.
- `content` (str, optional): The content to be written to the file.
- `append` (bool, optional): If True, appends content to an existing file; if False, overwrites the file. **Default value is `True`**

Appending to a file or creating an new file.
```python
file_path = "path/to/file/file.txt"
content = "this is file content"
file_manager.write_file(file_path, content=content)
```

Writing multiple lines
```python
file_path = "path/to/file/file.txt"
file_content = '''This is line 1.
This is line 2.
This is line 3.'''
file_manager.write_file(file_path, content=file_content)
```

Overwriting content in a file
```python
file_path = "path/to/file/file.txt"
content = "this is file content"
file_manager.write_file(file_path, content=content, append=False)
```

### move_file
> Moves a file to a new folder.

 Parameters:

- `file_path` (str): The path to the file to be moved.
- `new_folder` (str): The path to the destination folder where the file will be moved.

`Note if the new folder does not exist, it will be created.`
```python
file_path = "folder/myfile.txt"
new_folder = "new_folder/folder1/"
move_file(file_path, new_folder)
```

### rename_directory

>Renames the given path (file or folder) to a new name.

Parameters:

- path (str): The path to the file/folder to be renamed.
- new_name (str): The new name of the file/folder.

Returns:
None

Raises:

- FileNotFoundError: If the source file is not found.
- IOError: If an error occurs while renaming the file.

```python
old_name="file.txt"
new_name="file_new.txt"

rename_directory(old_name,new_name)
```

### copy_file
> Copies a file to a destination folder.

Parameters:

- file_path (str): The path to the file to be copied.
- destination_folder (str): The path to the destination folder where the file will be copied to.
- copy_name (str): The name of the copied file. (copy_of_{file_name} by default)

Returns:
None

Raises:

- FileNotFoundError: If the source file is not found.
- IOError: If an error occurs while copying the file.

```python
file_path = "folder/file.txt"
destination_folder = "folder2/files"
copy_name = "final_file.txt" 
# copy_name parameter is optional
copy_file(file_path, destination_folder, copy_name=copy_name)
```

### copy_folder
> Copies a folder (to the given depth) to a destination folder.

Parameters:

- folder_path (str): The path to the folder to be copied.
- destination_folder (str): The path to the destination folder where the file will be copied to.
- copy_name (str): The name of the copied folder (copy_of_{folder_name} by default)
- depth (int): The depth at which to copy the folder. (deep copy by default)

Returns:
None

Raises:

- FileNotFoundError: If the source folder is not found.
- IOError: If an error occurs while copying the folder.
- AssertionError: If the destination_folder is within the source folder.

```python
folder_path = "folder/test_folder/"
destination_folder = "folder2/files/"
copy_name = "final_folder_name" 

# depth is set to infinity by default
copy_folder(folder_path, destination_folder, copy_name=copy_name, depth=float("inf"))
```


## classes.file_handler
This is a class representation of [file_manager](#file_manager). File Handler should be used when
we have to do multiple operations on the same file and we don't want to write the name
of the file again and again.

### FileHandler {#filehandler}
> Initialize a FileHandler object.

Parameters:

- `filename` (str): The name of the file to be handled.
- `append` (bool, optional): A flag indicating whether to append to an existing file 
(default is True). If False, the file will be truncated.

```python
'''
Note:
    If `append` is not provided or set to True, any content written to the file will be appended.
    If `append` is set to False, new content will overwrite existing content.
'''
file = FileHandler("example.txt", append=False) 
```

#### **set_append_mode**

> Sets the append mode of the file.

Parameters

- `new_append_mode` (bool): The new append mode. Set to `True` for append mode (content will be added to the end of the file), or `False` for overwrite mode (existing content will be replaced).

Usage:
```python
file = FileHandler("example.txt", append=True)
file.set_append_mode(False)
```

#### **read_file**

> Read the contents of the file associated with this `FileHandler` instance.

Returns

- `str`: The content of the file.

Usage
```python
file = FileHandler("example.txt", append=True)
file_content = file.read_file()
```

#### **write_file**

> Write content to the file associated with this `FileHandler` instance.

Parameters

- `content` (str, optional): The content to be written to the file. Default is an empty string.

Usage
```python
file = FileHandler("example.txt", append=True)
file.write_file("This is some content.")
```

#### **move_file**

> Move the file associated with this `FileHandler` instance to a new location.

Parameters

- `new_location` (str): The path to the new location for the file.

Usage
```python
file = FileHandler("example.txt", append=True)
file.move_file("/new/directory/")
```


## utils
### print_directory

> Print the structure of a folder to the given depth.

Parameters:

- `folder_path` (str): The name or path of the folder to display the structure of
- `depth` (int, optional): The depth at which to display the structure of (default depth is 3)

Returns: None

```python
from fileosninja.utils import print_directory

print_directory("root/", depth=3)
```

Output:
```
root
|-- child1
|   |-- file1.txt
|   |-- file2.txt
|-- child2
|   |-- child2_1
|   |-- child2_2
|       |-- child1.txt
|-- testfile.txt
```