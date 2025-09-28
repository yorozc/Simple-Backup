# Simple-Backup
A simple python script that was created to automatically backup files to my usb sticks.

## Usage during configuration
- Running the application for the first time will prompt the user to select the external drive they want to connect to and to type in the directories they want to copy (Abs path)
    - Will make a config file holding these two
    - Do not move or delete config file from where the application is stored

## Usage after configuration
- add
    - python3 [name.py] add [directories... "/home/usr/tst1" "/home/usr/tst2/tut"]
    - Adds directories to config
- delete
    - python3 [name.py] delete [directories... "/home/usr/tst1" "/home/usr/tst2/tut"]
    - Deletes directories from config
- sync
    - python3 [name.py] sync
    - Backs up all directories and files from the directories inputted into selected drive
- help
    - displays uses of commands