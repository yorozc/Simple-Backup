# cmd line interface
import main
import os

print("===========================================")
print("|                                         |")
print("|                                         |")
print("|                                         |")
print("|        Welcome to Simple Backup         |")
print("|                                         |")
print("|                                         |")
print("|                                         |")
print("===========================================")

# add options for user to add, edit, delete from config file
if os.path.exists(os.path.join(os.getcwd(), "backup_config.json")):
    print("Config file found!")
    drive, directories = main.getConfigJSON() #returns tuple(drive, directories)
    if main.isDrivePluggedIn(drive):
        print(f"Drive {drive} found!")
        main.backup_directory(drive, directories)
        print("Synced!")
    else:
        print(f"Drive {drive} is not plugged in or is not mounted properly!")

    # while loop that runs user options in terminal after sync?
    # ^ instead make it so user can control it using args

else: # file doesn't exist, make user select drive and directories to backup
    print("Config is required during first run.")
    print("====================================")
    backup_drive = main.findExternalDrive() #chooses drive to backup on
    print("====================================")
    dir_list = main.copyDirs(backup_drive) #setting up dirs to copy
    print("====================================")
    main.createJSON(backup_drive, dir_list) #creates config
    print("backup_config.json created!")