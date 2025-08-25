import os, shutil, sys

home_directory = os.path.expanduser('~') #gets home dir

#ask for which directory they want to back up

source_dir = input("Insert source directory path:(absolute path) ")

#get directory that you want to back up to

backup_directory = input("Input backup directory path:(absolute path) ")

for item in os.listdir(source_dir):
    full_path = os.path.join(source_dir, item) #construct full path for checks

    if os.path.isdir(full_path): #checks if dir
        print(f'{item} is a directory')
        shutil.move(full_path, backup_directory + f'/{item}')

    elif os.path.isfile(full_path): #checks if file
        print(f'{item} is a file.')
        shutil.move(full_path, backup_directory + f'/{item}')
        
    else: 
        print(f'{item} is neither. {item} not moved.')

