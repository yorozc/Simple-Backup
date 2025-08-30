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
if os.path.isfile(CONFIG_BACKUP):
    pass

else: # file doesn't exist, make user select drive and directories to backup
    print("Config is required during first run.")
    print("====================================")
    backup_drive = main.findExternalDrive() #chooses drive to backup on