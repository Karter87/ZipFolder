import os
import zipfile

directory = "." 


def get_folders(directory):
    subfolders = [f.path for f in os.scandir(directory) if f.is_dir() ]
    #for folder in subfolders:
    #    print(folder)
    return subfolders

#def remove_path(list):

def archive_folder(folder):
    name = folder + '.zip' 
    zip_file = zipfile.ZipFile(name, 'w')
    with zip_file:
        for file in filePaths:
            zip_file.write(file)
    

def main():
    folders = get_folders(directory)
    for folder in folders:
        archive_folder(folder)



if __name__ == '__main__':
    main()