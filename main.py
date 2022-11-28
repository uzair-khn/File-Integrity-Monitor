import os
import hashlib
from tqdm.auto import tqdm
import time
from winotify import Notification, audio
import pyautogui
from tkinter import *

gui = []

def Monitor_files():
    file_path = input("\n\t\t\t\tEnter the path to the files : ")

    if os.path.exists(file_path):
        files_dict = os.listdir(file_path)
        for i in tqdm(range(100),
                      desc="\t\t\t\tChecking for baseline file…",
                      ascii=False, ncols=75):
            time.sleep(0.03)

        if 'file_baseline.txt' in files_dict:
            store_dict = {}
            with open(os.path.join(file_path, "file_baseline.txt"), 'r') as f:
                for line in f:
                    splitLine = line.split()
                    store_dict[splitLine[0]] = "".join(splitLine[1:])
            f.close()

            files_dict = os.listdir(file_path)
            check_dict = {}
            for file in files_dict:
                if file == 'file_baseline.txt':
                    pass
                else:
                    get_hash = Create_Hash(file_path, file)
                    j = os.path.join(file_path, file)
                    check_dict[j] = get_hash

            notif = Notification(app_id='Python Script',
                                 title='Monitoring Files',
                                 msg=file_path,
                                 duration='long',
                                 icon=r"C:\Users\admin\Desktop\Chamber_Of_Secrets\File_Integrity_Monitor\logo.png"
                                 )
            notif.set_audio(audio.Default, loop=False)
            notif.show()

            for i in tqdm(range(100),
                          desc="\t\t\t\tChecking files…",
                          ascii=False, ncols=75):
                time.sleep(0.08)

            # Checking if the files in the folder be added or if deleted to the folder

            for i in store_dict:
                try:
                    if store_dict[i] != check_dict[i]:
                        print("key error")
                except KeyError:
                    gui.append(i + ' is been deleted')
                    pyautogui.alert(i + " is been deleted!!!!!!!!!")

            for j in check_dict:
                if j not in store_dict:
                    gui.append(j + ' is been added')
                    pyautogui.alert(j + " is been added!!!!!!!!!")

        if 'data_baseline.txt' in files_dict:
            store_data_dict = {}
            with open(os.path.join(file_path, "data_baseline.txt"), 'r') as f:
                for line in f:
                    splitLine = line.split()
                    store_data_dict[splitLine[0]] = "".join(splitLine[1:])
            f.close()

            files_dict = os.listdir(file_path)
            check_data_dict = {}

            for file in files_dict:
                if file == 'data_baseline.txt':
                    continue
                elif file == 'file_baseline.txt':
                    continue
                else:
                    with open(os.path.join(file_path, file), 'r') as fpr:
                        data_dict = fpr.readlines()
                        get_data_hash = Create_Data_Hash(data_dict)
                        j = os.path.join(file_path, file)
                        check_data_dict[j] = get_data_hash
                fpr.close()

            for i in store_data_dict:
                try:
                    if store_data_dict[i] != check_data_dict[i]:
                        gui.append(i + " is been modified")
                        pyautogui.alert(i + " is been modified!!!!!!!!!")

                except KeyError:
                    gui.append(i + " is been modified")
                    pyautogui.alert(i + " is been modified!!!!!!!!!")

            getInterface(gui)

    else:
        print("\nFile does not exist\n")

def getInterface(data):
    data1 = "\n\n".join(map(str,data))
    top = Tk()
    top.title("File Integrity Monitor")
    top = Text(top, height=10, width=120)
    top.pack()
    top.insert(END, '\tSomeone again open the door to the chamber of secrets' + "\n\n")
    top.insert(END, data1)
    top.mainloop()


def Create_backup(file_path):
    backup_list = []
    files_dict = os.listdir(file_path)
    for file in files_dict:
        if file == 'baseline.txt':
            continue
        else:
            with open(os.path.join(file_path, file), 'r') as f:
                backup_list.append(f.read())


def Create_Hash(file_path, file):
    new_file = os.path.join(file_path, file)
    h = hashlib.sha3_512(new_file.encode()).hexdigest()
    return h


def Create_Data_Hash(data):
    data1 = " ".join(map(str, data))
    h = hashlib.sha3_512(data1.encode()).hexdigest()
    return h


def Create_Baselines():
    file_path = input("\n\t\t\t\tEnter the path to the files : ")

    if os.path.exists(file_path):

        Create_backup(file_path)

        files_dict = os.listdir(file_path)
        for file in files_dict:
            get_hash = Create_Hash(file_path, file)

            with open(os.path.join(file_path, file), 'r') as readf:
                data_dict = readf.readlines()
                get_data_hash = Create_Data_Hash(data_dict)
            readf.close()

            f = os.path.join(file_path, file)

            # save these hashes in a file_baseline.txt and data_baseline.txt
            with open(os.path.join(file_path, 'data_baseline.txt'), 'a') as fpd:
                fpd.write(f + " " + get_data_hash)
                fpd.write("\n")

            with open(os.path.join(file_path, 'file_baseline.txt'), 'a') as fp:
                fp.write(f + " " + get_hash)
                fp.write("\n")

        fpd.close()
        fp.close()

    else:
        print("Path does not exist")
    return


if __name__ == '__main__':
    print("\n\t Welcome to the File Integrity Monitoring \n")
    print("\t\t  A -  Setup a new baseline \n")  # need a reference point against which use to detect alterations
    print("\t\t  B -  Monitor files using saved baseline")
    select_option = input("\n\t\t\t\tSelect an option : ").upper()
    if select_option == 'A':
        Create_Baselines()
    elif select_option == 'B':
        Monitor_files()
