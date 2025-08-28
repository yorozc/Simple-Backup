import os, shutil, sys, getpass, pyinputplus as pypi

# REMEMBER TO PUT IN README TO FORMAT TO NTFS DOES NO WORK IN exFAT
# save user info through JSON format or txt file? (find best soltuion to save user information)

def findExternalDrive(): #Used to find external drives for backup
    drives = os.listdir(f"/media/{getpass.getuser()}")
    print("Drives in /media directory: ",  drives) # shows users drives in media
    
    if len(drives) < 1: 
        print(f"No USB drives found. Make sure they are connected. Found in /media/{getpass.getuser()}")
        sys.exit()
        return 
    else:
        driveChoice = pypi.inputChoice(drives, prompt="Please select one of the drives: ",blank=True)
        print(f"Drive {driveChoice} is chosen.")
        return driveChoice.upper()

user_drive = findExternalDrive()

backup_drive = f"/media/{getpass.getuser()}/{user_drive}"

# prompt user for dir they want backed up and copy contents to drive

# add some input validation later
source_dir = pypi.inputFilepath(prompt="Please enter the absolute path of the directory: ")
print(source_dir)

for item in os.listdir(source_dir):

    full_path = os.path.join(source_dir, item) #construct full path for checks
    if os.path.exists(full_path):

        if os.path.isdir(full_path): #checks if dir
            print(f'{item} is a directory')
            shutil.copytree(full_path, backup_drive + f'/{item}')

        elif os.path.isfile(full_path): #checks if file
            print(f'{item} is a file.')
            shutil.copy(full_path, backup_drive + f'/{item}')
            
        else: 
            print(f'{item} is neither. {item} not moved.')
    else:
        print("Path does not exist.")

#after prompting user to choose drive, prompt user to select 
#directories that you want to back up
