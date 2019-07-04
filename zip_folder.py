from os import scandir, path, walk 
from zipfile import ZipFile, BadZipfile, ZIP_DEFLATED 
from sys import exit

def get_folders(directory):
    subfolders = [f.path for f in scandir(directory) if f.is_dir() ]
    return subfolders

def zip_folder(folder_path, output_path):
    """Zip the contents of an entire folder (with that folder included
    in the archive). Empty subfolders will be included in the archive
    as well.
    """
    parent_folder = path.dirname(folder_path)
    # Retrieve the paths of the folder contents.
    contents = walk(folder_path)
    try:
        zip_file = ZipFile(output_path, 'w', ZIP_DEFLATED)
        for root, folders, files in contents:
            # Include all subfolders, including empty ones.
            for folder_name in folders:
                absolute_path = path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder + '\\',
                                                      '')
                print(f'--- Adding file {absolute_path} to archive')
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder + '\\',
                                                      '')
                print(f'--- Adding file {absolute_path} to archive')
                zip_file.write(absolute_path, relative_path)
        print(f'ZipFile: {output_path} created succesfully')
    except IOError as message:
        print(message)
        exit(1)
    except OSError as message:
        print(message)
        exit(1)
    except BadZipfile as message:
        print(message)
        exit(1)
    finally:
        zip_file.close()


def main():
    print(f'\nFollowing Folders will be archived:')
    folders = get_folders('./')
    for folder in folders:
        print(folder)
    if input("\nAre you sure to archive these folders? (y/n) ") != "y":
        print('BREXITing...')
        input("\nPress ENTER to exit")
        exit()
    else:
        print(f'Starting Program::')
        for folder in folders:
            output_path = folder + '.zip'
            zip_folder(folder,output_path)
        input("\nPress ENTER to exit")

if __name__ == '__main__':
    main()