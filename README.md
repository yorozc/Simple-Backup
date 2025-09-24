# Simple-Backup
A simple python script that was created to automatically backup files to my usb sticks.

## Usage during configuration
- Running the application for the first time will prompt the user to select the external drive they want to connect to and to type in the directories they want to copy (Abs path)
    - Will make a config file holding these two
    - Do not move or delete config file from where the application is stored

## Usage after configuration
- Add cmd
    - python3 [name.py] add [list of dirs... "/home/usr/tst1" "/home/usr/tst2/tut"]
    - Type space between each directory you want to add