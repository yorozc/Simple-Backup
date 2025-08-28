import os, shutil, sys, getpass, pyinputplus as pypi


def findExternalDrive(): #Used to find external drives for backup
    drives = os.listdir(f"/media/{getpass.getuser()}")
    print("Drives in /media directory: ",  drives) # shows users drives in media
    
    if len(drives) > 1: 
        print("No USB drives found. Make sure it is connected.")
        return 
    else:
        driveChoice = pypi.inputChoice(drives, prompt="Please select one of the drives: ",blank=True)
        print(f"Drive {driveChoice} is chosen.")
        return driveChoice.upper()

user_drive = findExternalDrive()

# if len(sys.argv) < 3:
#     print("Usage: python main.py [source_directory] [backup_directory]")
#     sys.exit(1)

#ask for which directory they want to back up

source_dir = input("Insert source directory path:(absolute path) ")
# source_dir = sys.argv[1]

#get directory that you want to back up to

backup_directory = input("Input backup directory path:(absolute path) ")
# backup_directory = sys.argv[2]

for item in os.listdir(source_dir):

    full_path = os.path.join(source_dir, item) #construct full path for checks
    if os.path.exists(full_path):

        if os.path.isdir(full_path): #checks if dir
            print(f'{item} is a directory')
            shutil.move(full_path, backup_directory + f'/{item}')

        elif os.path.isfile(full_path): #checks if file
            print(f'{item} is a file.')
            shutil.move(full_path, backup_directory + f'/{item}')
            
        else: 
            print(f'{item} is neither. {item} not moved.')
    else:
        print("Path does not exist.")

print("Move complete!")
