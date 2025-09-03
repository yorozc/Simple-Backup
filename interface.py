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

# check if user has config file in same dir to check if it is their first time
CONFIG_BACKUP = "backup_config.json"
if os.path.exists(CONFIG_BACKUP):
    drive = main.getBackupDrive()
    print(drive)
    print("Config file found!")

else: # file doesn't exist, make user select drive and directories to backup
    # save all user info to config and make option for user to rewrite or edit config
    print("Config is required during first run.")
    print("====================================")
    backup_drive = main.findExternalDrive() #chooses drive to backup on
    print("====================================")
    dir_list = main.copyDirs(backup_drive)
    print("====================================")
    main.createJSON(backup_drive, dir_list)
    print("backup_config.json created!")