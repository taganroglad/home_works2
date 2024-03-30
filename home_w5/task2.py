import os

def split_path(file_path):
    path, filename = os.path.split(file_path)
    filename, ext = os.path.splitext(filename)
    return path, filename, ext

file_path = "C:/Users/tagan/Documents/moi_doci.txt"
path, filename, ext = split_path(file_path)
print("Path:", path)
print("Filename:", filename)
print("Extension:", ext)
