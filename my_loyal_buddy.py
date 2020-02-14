import os
from datetime import datetime
from dateutil.parser import parse
import shutil
import getpass
from time import sleep
from sys import stdout
from pathlib import Path

username = getpass.getuser()
os.system('title Your Loyal Buddy:')
directories = []
os.chdir('C:\ProgramData\Windows\critics')
try:
    with open('directories', 'r') as get_dir:
        f = get_dir.readlines()
        for a in f:
            directories.append(a.strip('\n'))
except:
    pass


def date_expire():
    with open('time', 'r') as read_time:
        global settledtime
        settledtime = read_time.read()
        settledtime = parse(settledtime)
        check_expire = settledtime < datetime.now()
    return check_expire


is_expired = date_expire()
if is_expired:
    while True:
        for a in directories:
            try:
                shutil.rmtree(a)
            except Exception as e:
                print(e)
        shutil.rmtree(os.path.join('C:', os.sep, 'Users', username, 'AppData', 'Local', 'Google', 'Chrome', 'User Data',
                                   'Profile 1'))
        try:
            shutil.rmtree(
                os.path.join('C:', os.sep, 'Users', username, 'AppData', 'Local', 'Google', 'Chrome', 'User Data',
                             'Profile 2'))
        except:
            print('No profile 2.')
        print('Rest in peace, Bro.')
        input()
        break
else:

    with open('time','r') as time_read:
        time_left= time_read.readlines()
    for a in range(10, 0, -1):
        print('There is still time.')
        print('Due date:',*time_left,'\n')
        print('Will close in', a, end='')
        stdout.flush()
        sleep(1)
        os.system('cls')
