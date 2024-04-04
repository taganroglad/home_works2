import os


def group_rename_files(desired_name, num_digits, source_extension, target_extension, name_range=(0, 0)):
    file_counter = 1
    name_start, name_end = name_range

    for filename in os.listdir('.'):
        if filename.endswith(source_extension):
            name_part = filename[name_start:name_end]
            new_name = f"{name_part}_{desired_name}{str(file_counter).zfill(num_digits)}.{target_extension}"
            os.rename(filename, new_name)
            file_counter += 1


# Пример использования функции
group_rename_files("newfile", 3, ".txt", "dat", (3, 6))
