import os, shutil, sys, getpass, pyinputplus as pypi, json
from pathlib import Path

def findExternalDrive() -> str: #Used to find external drives for backup
    # TODO: show info of drive
    # TODO: make it cross platform (windows, linux, mac)
    drives = os.listdir(f"/media/{getpass.getuser()}")
    print("Drives in /media directory: ",  drives) # shows users drives in media
    
    if len(drives) < 1: 
        print(f"No USB drives found. Make sure they are connected. Found in /media/{getpass.getuser()}")
        sys.exit()
        return 
    else:
        driveChoice = pypi.inputMenu(drives, numbered=True, prompt="Please select one of the drives: \n",blank=True)
        print(f"Drive {driveChoice} is chosen. This is now your backup drive.")
        return driveChoice
    
def isDrivePluggedIn(backup_drive: str) -> bool:
    if os.path.exists(backup_drive):
        return True
    else:
        return False

# TODO: provide more secure input validation and error correcting

def copyDirs(backup_drive: str):
    source_dir = pypi.inputFilepath(prompt="Please enter the absolute path of the directory you want to backup" \
                                    "\nIf multiple directories, separate with a space:  ")
    # print(source_dir)
    dir_list =  source_dir.split(" ")

    backup_directory(backup_drive, dir_list)

    return dir_list


def backup_directory(backup_drive: str, dir_list: list):
    for directory in dir_list: #go through each dir that user inputted
        try:
            for item in os.listdir(directory):
                full_path = os.path.join(directory, item) #construct full path for checks
                if os.path.exists(full_path):
                    print(full_path)
                    if os.path.isdir(full_path): #checks if dir
                        print(f'{item} is a directory. Backup complete.')
                        print(full_path)
                        shutil.copytree(full_path, os.path.join(backup_drive, item), dirs_exist_ok=True)

                    elif os.path.isfile(full_path): #checks if file
                        print(f'{item} is a file. Backup complete.')
                        shutil.copy(full_path, os.path.join(backup_drive, item))
                        
                    else: 
                        print(f'{item} is not a file nor directory. {item} not moved.')
                else:
                    print("Path does not exist.")

        except FileExistsError:
            print("File already exists!")
            
            

        except FileNotFoundError:
            print("File does not exist or path is wrong!")
            
        except Exception as e:
            print(f"Error: {e}")

# TODO: set up these func to work with sys.args

def addDir(newDirs: list) -> None:
    drive, directories = getConfigJSON()
    home = Path.home()
    for dir in newDirs:
        dir = dir.lstrip("/") # gets rid of leftmost slash for concatenation
        full_path = home / dir

        if os.path.exists(full_path):
            print("Directory found!")
            print(full_path)
            directories.append(str(full_path))
            print("Added to backup_config.json!")
        else:
            print("Directory or path does not exist!")
            print(full_path)

    print(directories)

    # TODO: write to config file


def editDir():
    pass

def deleteDir(dirs: list) -> None:
    drive, directories = getConfigJSON()
    for del_dir in dirs:
        if del_dir in directories:
            directories.remove(del_dir)
            print(f"{del_dir} deleted!")
    
    # TODO: write removal to config

def help():
    pass

# TODO: fix path when made cross platform

def createJSON(backup_drive: str, dir_list: list):
    with open("backup_config.json", 'w') as f:
        config = {
            "backup_drive": f"/media/{getpass.getuser()}/{backup_drive}",
            "directories": dir_list
        }
        json.dump(config, f, indent=4)


def getConfigJSON() -> str | list:
    currDir = os.getcwd()
    configPath = os.path.join(currDir, "backup_config.json")
    if os.path.exists(configPath):
        print(f"Config located: {configPath}")
        with open(configPath, 'r') as f:
            data = json.load(f)
            return data['backup_drive'], data['directories']
    else:
        print("Something went very wrong.")
    
        
