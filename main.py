# def reset fonksiyonu yazıyordum
import os
from time import sleep
from datetime import datetime,timedelta
from datetime import datetime,timedelta
from dateutil.parser import parse
from colorama import Style, Fore,init
import sys
import getpass
import shutil


os.system('title Safe Death')
first_dir = os.getcwd() #this will be necessary later.
init()
green = Style.BRIGHT + Fore.GREEN
blue = Style.BRIGHT + Fore.BLUE
red = Style.BRIGHT + Fore.RED
magenta = Style.BRIGHT + Fore.MAGENTA
yellow = Style.BRIGHT+Fore.YELLOW
default = Style.RESET_ALL
username = getpass.getuser()

#my_loyal_buddy script required to be executed automatically when the pc is started.
auto_file_target= os.path.join('C:', os.sep, 'Users', username, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu',
                             'Programs','Startup')
auto_file_source = 'my_loyal_buddy.py'
auto_file_on_target =os.path.join('C:', os.sep, 'Users', username, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu',
                             'Programs','Startup','my_loyal_buddy.py')

try:
    with open('my_loyal_buddy.py','r') as f:
        f.read()
        print('Setting executer... ')
        shutil.copy(auto_file_source,auto_file_target)
        print(red)
        input('You can now delete my_loyal_buddy.py file.(Don\'t run it.)\nPress any key to continue.')
        print(green)
        os.system('cls')
except FileNotFoundError:
    try:
        with open(auto_file_on_target,'r') as f:
            f.read()
            print('Executer is ready.')
    except:
        print(red,'This program requires my_loyal_buddy_py script for first time running.')
        print(f'Put the script in the same directory with this program.\nIf you have the script, rename it correctly.\nTo get the script, mail to me:{magenta} aslanhassan98@gmail.com{default}')
        input('press any key to exit')
        quit()


codex = {
        "\n": "\n",
        "\t": "\t", "1": "q", "x": "b", "£": "p", "s": "u", "Ò": "{", "ñ": "Ÿ", "ï": "M", "K": "ç", ">": "È", "F": "!",
        ".": "Ç", "9": "ş", "4": "^", "Â": "Ó", "è": "~", "B": "ì", ",": "n", "e": "Z", "8": "5", "¾": "}", "P": "Ã",
        "d": "Î", "î": "m", "g": "#", "j": "õ", "+": "2", "ä": "r", "ã": "N",
        "ý": "û", "ı": "Ü", "ÿ": "3", "V": "U", "T": "ô", "a": "k", "o": "i",
        "Û": "Ô", "Ñ": "c", "W": "O", "Á": "ú", "ß": "Ý", "â": "Ì", "(": "D",
        "E": "R", "É": "]", "H": "Í", "G": "Y", ")": "ù", "I": "f", "'": "v",
        "X": "y", "<": "ê", "À": "w", "Ê": " ", "ö": "[", "Ú": "ğ", "½": "t",
        "Q": "ó", "_": "L", "&": "ü", "=": ";", "å": "0", "ò": "İ", "Ù": "á",
        "l": "Ğ", "7": "—", "%": "$", "ë": "Õ", "J": "A", "Ş": "?", "z": "/", "6": "h", "S": "à", "é": "C", "-": "í",
        ":": "Ö",
        "@": '"',
        "q": "1", "b": "x", "p": "£", "u": "s", "{": "Ò", "Ÿ": "ñ", "M": "ï", "ç": "K", "È": ">", "!": "F",
        "Ç": ".", "ş": "9", "^": "4", "Ó": "Â", "~": "è", "ì": "B", "n": ",", "Z": "e", "5": "8", "}": "¾", "Ã": "P",
        "Î": "d", "m": "î", "#": "g", "õ": "j", "2": "+", "r": "ä", "N": "ã",
        "û": "ý", "Ü": "ı", "3": "ÿ", "U": "V", "ô": "T", "k": "a", "i": "o",
        "Ô": "Û", "c": "Ñ", "O": "W", "ú": "Á", "Ý": "ß", "Ì": "â", "D": "(",
        "R": "E", "]": "É", "Í": "H", "Y": "G", "ù": ")", "f": "I", "v": "'",
        "y": "X", "ê": "<", "w": "À", " ": "Ê", "[": "ö", "ğ": "Ú", "t": "½",
        "ó": "Q", "L": "_", "ü": "&", ";": "=", "0": "å", "İ": "ò", "á": "Ù",
        "Ğ": "l", "—": "7", "$": "%", "Õ": "ë", "A": "J", "?": "Ş", "/": "z", "h": "6", "à": "S", "C": "é", "í": "-",
        '"': '@', "Ö": ":"
    }
key_list = list(codex.keys())
val_list = list(codex.values())

def logo():
    print(f'''{blue}
####################################################################################################################
{red}<><><><><><><><><><><><>                 {magenta} r/hasanaslan{red}                                      <><><><><><><><><><><><>
<><><><><><><><><><><><>         {magenta}         aslanhassan98@gmail.com {red}                          <><><><><><><><><><><><>
<><><><><><><><><><><><>                {magenta}  instagram: hasanaslan7  {red}                          <><><><><><><><><><><><>
<><><><><><><><><><><><>                  {magenta}twitter: gepettolyon         {red}                     <><><><><><><><><><><><>{blue}
####################################################################################################################
    ''')


directories=[] # this will store the directories user entered.
clear = lambda:os.system('cls')
log_dir  = 'C:\ProgramData\Windows\critics'

if not os.path.exists(log_dir):
    os.chdir('C:\ProgramData')
    if os.path.exists('Windows'):
        os.chdir('C:\ProgramData\Windows')
        os.mkdir('critics')
        os.chdir('C:\ProgramData\Windows\critics')
    else:
        os.mkdir('Windows')
        os.chdir('C:\ProgramData\Windows')
        os.mkdir('critics')
        os.chdir('C:\ProgramData\Windows\critics')
os.chdir(log_dir)
def set_time_and_save():
    while True:
        try:
            print(green)
            clear()
            user_hours=int(input('Set hours: '))
            time_to_go = datetime.now() + timedelta(hours=user_hours)
            print(red)
            clear()
            for a in (f'Cleaning will begin at :{time_to_go}'):
                print(a,end='')
                sys.stdout.flush()
                sleep(0.1)
            input()
            break
        except:
            print('You need to enter numbers!')
            input('\nPress enter to continue.')
            clear()
            continue
    with open('time','w') as f:
         f.write(str(time_to_go))

def date_expire():
    with open('time','r') as read_time:
        global settledtime
        settledtime = read_time.read()
        settledtime = parse(settledtime)
        check_expire = settledtime<datetime.now()
    return check_expire



def password_call():
    log_entries = 0
    while True:
        logo()
        output = ''
        if not os.path.exists('C:\ProgramData\Windows\critics\config'):
            return password_create()
        if os.path.exists('C:\ProgramData\Windows\critics\config'):
            sleep(1)
            os.system('cls')
            logo()
            print(magenta,'------------------------------------------------------------------------------------------------',red)
            print('Password Verification',default)
            check_pass = input('Enter your pass: ')
            with open('config') as t:
                readpass = t.read()
                for b in readpass:
                    output+=key_list[val_list.index(b)]
                if output ==check_pass:
                    print('Welcome.')
                    t.close()
                    return menu()
                else:
                    print(red)
                    input('Wrong password.')
                    print(default)
                    log_entries+=1
                    clear()
        if log_entries==3:
            os.system('rundll32.exe user32.dll, LockWorkStation')# Locks the PC after 3 failed login attempt.
            quit()
        elif not os.path.exists('C:\ProgramData\Windows\critics\config'):
            return password_create()


def password_create():
    while True:
        os.system('cls')
        logo()
        print(magenta,'------------------------------------------------------------------------------------------')
        print(magenta,
              '------------------------------------------------------------------------------------------', green)
        print(green)
        password =input('Enter a password: ')
        if len(password)<4:
            print(red,'You need to use at least 4 characters!',default)
            input('\nPress enter to continue.')
            clear()
            continue
        password2 = input('Enter again: ')
        if password!=password2:
            print(red,'\tPasswords does not match!',default)
            input('\nPress enter to continue.')
            clear()
            continue
        print('\tcongratulations. Your password is set.')
        input('\nPress enter to continue.')
        output = ''
        for a in password:
            output+=codex.get(a)
        password=output
        with open('config','w') as f:
            f.write(password)
            f.close()
            break
    return menu()
def hide_files():
    os.chdir('C:\ProgramData')
    os.system('attrib +h +s Windows')
    os.system('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v Hidden /t REG_DWORD /d 0 /f')
    os.system('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowSuperHidden /t REG_DWORD /d 0 /f')
    os.chdir(log_dir)
    os.system('attrib +h +s directories')
    os.system('attrib +h +s time')
    os.chdir('C:\ProgramData\Windows\critics')

def hide_user_files():
    os.chdir(log_dir)
    try:
        with open('directories','r') as dir23:
            textdir23= dir23.readlines()
            for a in textdir23:
                os.system(f'attrib +h +s {a}')
                clear()
        input('Process done!')
    except:
        print(red,'I couldnt open',default)



def unhide_user_files():
    os.chdir(log_dir)
    try:
        with open('directories','r') as dir23:
            textdir23= dir23.readlines()
            for a in textdir23:
                os.system(f'attrib -h -s {a}')
                clear()
        input('Process done!')
    except:
        print(red,'I couldnt open',default)






def set_directories():
    while True:
        clear()
        print(red,'\t\tCurrent directories:',green)
        for a in directories:
            print(a)
        print(yellow,'\n\tEnter the directories you want to add.Type "q" to exit.')
        print('\n\tExample: C:\Program Files\Myfiles',green)
        add_directory = input(' ')
        if add_directory in directories:
            print(red,'\nAlready added.',green)
            input('Press to continue...')
            clear()
            continue
        if add_directory=='q':
            break
        if os.path.exists(add_directory):
            directories.append(add_directory)
            print('Added')
            try:
                with open('directories','r') as dir_read:
                    f=dir_read()
                    break
            except:
                with open('directories','a') as dir_write:
                    dir_write.write(f'{add_directory}\n')
                sleep(2)
        else:
            print(red,'No such directory!',green)
            input('Press to continue.')
            clear()
            continue

def deselect_directories():
    while True:
        clear()
        print(green,'\tDirectories:',yellow)
        for a in directories:
            print(a)
        print(green)
        remove_input = input('Select the directory you want to remove :\n>>')
        if remove_input=='q':
            with open('directories', 'w+') as dir_write:
                for a in directories:
                    dir_write.write(f'{a}\n')
            break
        if remove_input not in directories:
            print(red,'That directory is not in my list.',green)
            input('Press to continue...')
            clear()
            continue
        directories.remove(remove_input)
        print('removed')
        input('Press to continue...')
        clear()


def reset():
    os.remove(auto_file_on_target)
    try:
        os.remove(os.path.join("C:\\", "ProgramData", "Windows", 'critics', 'time'))
    except:
        pass
    try:
        os.remove(os.path.join("C:\\", "ProgramData", "Windows", 'critics', 'config'))
    except:
        pass
    try:
        os.remove(os.path.join("C:\\", "ProgramData", "Windows", 'critics', 'directories'))
    except:
        pass
    input('EVERYTHING IS CLEANED!')
    quit()



def menu():
    print(green)
    clear()
    while True:
        print(yellow)
        clear()
        print('''
##################################################################################################################     
|                                Type '1' to select files/directories.                                           |
|                                Type '2' to set time.                                                           |      
|                                Type '3' to reset program settings.                                             |
|                                Type '4' to deselect files/directories.                                         |
|                                Type '5' to hide files/directories.                                             |
|                                Type '6' to unhide files/directories.                                           |
|                                Type '7' to see me and guide.                                                   |
|                                Type 'q'  to exit                                                               |
##################################################################################################################
                      ''')
        print(green,'Select an operation',default)
        menu_select = input('>>>>>>')
        if menu_select=='1':
            set_directories()
        elif menu_select=='2':
            set_time_and_save()
        elif menu_select=='3':
            os.system('cls')
            return reset()
        elif menu_select=='4':
            deselect_directories()
        elif menu_select=='5':
            hide_user_files()
        elif menu_select=='6':
            unhide_user_files()
        elif menu_select=='7':
            os.system('cls')
            logo()
            print(f'''{red}
            This basic app is made for pick up after you if you are dead.
            If you don't set the time to the future, all of the directories you added and 
            your Google Chrome local history will be deleted.
            If you don't want to delete any file, do not add any directory.Set the time and leave.
            This will only delete your chrome history and it is safe.When the computer opened,
            it checks if the time you set is came or not. If came, bomm. If not, nothing will happen.
            If you added directories, you can hide them.
            If you are new, set the time from the menu by typing '2'.
            Time is calculated by hours.(Type '24' on the time setting section for 1 day.)
            The program will show you your cleaning process starting time on every startup.
            For better performance, do not force program to stop.Just press 'q'
            ''')
            input('\nPress enter key to return menu.')
            os.system('cls')
            continue
        elif menu_select=='q':
            quit()

        else:
            print(red,'Invalid option!',default)
            input('\nPress enter to continue.')
            clear()
try:
    with open('directories','r') as directory_read:
        ff = directory_read.readlines()
        for a in ff:
            if a not in directories:
                directories.append(a.strip('\n'))
except:
    pass
password_call()
hide_files()
