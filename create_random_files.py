import os
import random
import string
import shutil

# Шлях до кореневої директорії, в якій буде створено нові папки та файли
base_dir = 'DZ_3'
root_dir = "test_directory"

# Кількість рекурсивних рівнів директорій
levels = 3

# Кількість папок у кожному рівні
folders_per_level = 3

# Кількість файлів у кожній папці
files_per_folder = 3

# Розширення файлів
file_types = [".txt", ".jpg", ".mp4"]

# Розміри файлів
file_sizes = {
    ".txt": 100,  # 100 байтів
    ".jpg": 1024,  # 1 кілобайт
    ".mp4": 1024 * 1024,  # 1 мегабайт
}


def generate_random_filename(file_extension):
    filename = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    return filename + file_extension


def generate_random_content(size):
    return "".join(random.choices(string.ascii_letters + string.digits, k=size))


def create_files_in_folder(folder_path):
    for _ in range(files_per_folder):
        file_type = random.choice(file_types)
        file_size = file_sizes[file_type]
        file_name = generate_random_filename(file_type)
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "w") as f:
            f.write(generate_random_content(file_size))


def create_folders_recursively(base_path, level):
    if level == 0:
        return

    for _ in range(folders_per_level):
        folder_name = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        create_files_in_folder(folder_path)
        create_folders_recursively(folder_path, level - 1)


# Видалення існуючої директорії, якщо вона є, для початку з чистого аркуша
if os.path.exists(root_dir):
    shutil.rmtree(root_dir)

os.makedirs(root_dir, exist_ok=True)
create_folders_recursively(root_dir, levels)

print(f"Директорія '{root_dir}' створена з усіма файлами та папками.")
