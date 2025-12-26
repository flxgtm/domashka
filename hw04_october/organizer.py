import os
import shutil
import argparse

extensions_m = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".txt", ".pdf", ".docx", ".doc"],
    "audio": [".mp3", ".wav", ".ogg", ".flac"],
    "others": []
}

def create_directories(base_path):
    """создает поддиректории для каждого типа файлов, если они не существуют."""
    for folder in extensions_m.keys():
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_file(file_path, base_path):
    """перемещает файл в соответствующую папку в зависимости от расширения."""
    _, extension = os.path.splitext(file_path)
    destination_folder = "others"  # категория по умолчанию для неизвестных расширений
    
    for folder, extensions in extensions_m.items():
        if extension.lower() in extensions:
            destination_folder = folder
            break

    # полный путь к папке назначения
    destination_path = os.path.join(base_path, destination_folder, os.path.basename(file_path))
    shutil.move(file_path, destination_path)

def clean_empty_dirs(base_path):
    """удаляет пустые папки в указанной директории."""
    for dirpath, dirnames, filenames in os.walk(base_path, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)

def organize_files(directory_path):
    """основная функция для организации файлов в указанной директории."""
    # создаем нужные поддиректории
    create_directories(directory_path)

    # перемещаем файлы в соответствующие папки
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        
        # пропускаем папки
        if os.path.isfile(item_path):
            move_file(item_path, directory_path)

    # удаляем пустые папки
    clean_empty_dirs(directory_path)
    print("файлы успешно отсортированы и пустые папки удалены")

if __name__ == "__main__":
    # используем argparse для получения пути к директории от пользователя
    parser = argparse.ArgumentParser(description="сортировщик файлов по расширениям")
    parser.add_argument("directory", type=str, help="путь к директории для сортировки файлов")
    args = parser.parse_args()

    # проверяем, существует ли указанная директория
    if os.path.isdir(args.directory):
        organize_files(args.directory)
    else:
        print("указанная директория не существует")