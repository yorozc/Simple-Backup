import os, shutil, sys, getpass, pyinputplus as pypi, pathlib, json

# REMEMBER TO PUT IN README TO FORMAT TO NTFS DOES NO WORK IN exFAT

def findExternalDrive(): #Used to find external drives for backup
    #try to show info of drive
    drives = os.listdir(f"/media/{getpass.getuser()}")
    print("Drives in /media directory: ",  drives) # shows users drives in media
    
    if len(drives) < 1: 
        print(f"No USB drives found. Make sure they are connected. Found in /media/{getpass.getuser()}")
        sys.exit()
        return 
    else:
        driveChoice = pypi.inputMenu(drives, numbered=True, prompt="Please select one of the drives: \n",blank=True)
        print(f"Drive {driveChoice} is chosen. This is now your backup drive.")
        return driveChoice.upper()



# add some input validation later

def copyDirs(backup_drive: str):
    backup_drive = f"/media/{getpass.getuser()}/{backup_drive}"
    source_dir = pypi.inputFilepath(prompt="Please enter the absolute path of the directory you want to backup" \
                                    "\nIf multiple directories, separate with a space:  ")
    # print(source_dir)
    dir_list =  source_dir.split(" ")

    for directory in dir_list: #go through each dir that user inputted
        for item in os.listdir(directory):
            full_path = os.path.join(directory, item) #construct full path for checks
            print(full_path)
            try:
                if os.path.exists(full_path):
                    if os.path.isdir(full_path): #checks if dir
                        print(f'{item} is a directory. Backup complete.')
                        shutil.copytree(full_path, backup_drive + f'/{item}')

                    elif os.path.isfile(full_path): #checks if file
                        print(f'{item} is a file. Backup complete.')
                        shutil.copy(full_path, backup_drive + f'/{item}')
                        
                    else: 
                        print(f'{item} is not a file nor directory. {item} not moved.')
                else:
                    print("Path does not exist.")

            except FileExistsError:
                print("Directory/file already exists!")
                continue
            
def checkForJSON(backup_drive):
    pass

def createJSON(backup_drive, directories):
    with open("backup_config.json", 'w') as f:
        config = {
            "backup_drive": backup_drive,
            "directories": []
        }
        json.dump(config, f, indent=4)

        
