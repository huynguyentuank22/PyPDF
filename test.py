import os

path = "/path/to/your/file.txt"
file_name = os.path.basename(path).split('.')[0]
print(file_name)  # Output: file.txt
os.path.isdir