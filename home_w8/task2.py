import os
import json
import csv
import pickle

def get_directory_info(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        total_size = 0
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size
            result.append({
                'parent_directory': root,
                'name': file,
                'type': 'file',
                'size_bytes': file_size
            })
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size = sum(os.path.getsize(os.path.join(dir_path, f)) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)))
            total_size += dir_size
            result.append({
                'parent_directory': root,
                'name': dir_name,
                'type': 'directory',
                'size_bytes': dir_size
            })
    return result

def save_as_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_as_csv(data, filename):
    if not data:
        print("No data to save.")
        return
    keys = data[0].keys()
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def save_as_pickle(data, filename):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

directory = './my_directory'
directory_info = get_directory_info(directory)

save_as_json(directory_info, 'directory_info.json')
save_as_csv(directory_info, 'directory_info.csv')
save_as_pickle(directory_info, 'directory_info.pickle')
