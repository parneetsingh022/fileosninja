# FileOSNinja

## Installing package
```
pip install fileosninja
```

## file_manager
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
- `content` (str, optional): The content to be written to the file. Defaults to an empty string.
- `append` (bool, optional): If True, appends content to an existing file; if False, overwrites the file. **Defaults to True.**

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
file_manager.write_file(file_path, content=content, append=True)
```

### move_file
> Moves a file to a new folder.

 Parameters:

- file_path (str): The path to the file to be moved.
- new_folder (str): The path to the destination folder where the file will be moved.

`Note if the new folder does not exist, it will be created.`
```python
file_path = "folder/myfile.txt"
new_folder = "new_folder/folder1/"
move_file(file_path, new_folder)
```