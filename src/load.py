import argparse
import os
import sys
import csv

# Fungsi untuk mengurai argumen folder menggunakan argparse
def parse_arguments():
    parser = argparse.ArgumentParser(description='Program OWCA')
    parser.add_argument('folder', metavar='folder', type=str, help='Path folder')
    return parser.parse_args()

# Fungsi untuk memuat data dari file CSV ke dalam dictionary
def load_data(file_path):
    data = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[row['id']] = row
    return data

# Fungsi untuk memuat semua data yang diperlukan
def load_all_data(folder):
    data_files = ['user.csv', 'monster.csv', 'item_inventory.csv', 'monster_inventory.csv', 'item_shop.csv', 'monster_shop.csv']
    data = {}
    for file in data_files:
        file_path = os.path.join(folder, file)
        if os.path.exists(file_path):
            data[file.split('.')[0]] = load_data(file_path)
        else:
            print(f'File {file} tidak ditemukan!')
    return data

# Fungsi utama
def main():
    # Mengurai argumen
    args = parse_arguments()

    # Memuat semua data dari folder yang diberikan
    data = load_all_data(args.folder)

    # Menampilkan pesan selamat datang jika folder ditemukan
    if data:
        print("Folder ditemukan!")
        os.chdir(args.folder)
        print("Selamat datang di OWCA!")
    else:
        print('Tidak ada data yang dimuat. Program berhenti.')

if __name__ == "__main__":
    main()