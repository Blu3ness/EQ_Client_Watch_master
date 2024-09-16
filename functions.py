import time
import datetime
import subprocess
import psutil
import ctypes
import automation
import pygetwindow as gw
import os

blue_client = r'C:\Users\admin\Desktop\p99\P99\Launch Titanium.bat'
green_client = r'C:\Users\admin\Desktop\p99 - Copy\P99\Launch Titanium.bat'

def launch_blue():
    print('Launching Blue')


    bat_path = r"C:\Users\admin\Desktop\P99 - Copy\P99\Launch Titanium.bat"
    subprocess.Popen(bat_path, cwd=r"C:\Users\admin\Desktop\P99 - Copy\P99")

    time.sleep(6)
    title_change('Blue')
    move_window('Blue')

    print('Finding EULA Button...')
    automation.eula_button_finder()
    time.sleep(2)

    print('Logging In...')



def launch_green():
    print('Launching Green')


    bat_path = r"C:\Users\admin\Desktop\P99\P99\Launch Titanium.bat"
    subprocess.Popen(bat_path, cwd=r"C:\Users\admin\Desktop\P99\P99")

    time.sleep(6)
    title_change('Green')
    move_window('Green')

    print('Finding EULA Button...')
    automation.eula_button_finder()
    time.sleep(2)

    print('Logging In...')



def title_change(server):
    """Change the window title to the server name."""
    WM_SETTEXT = 0x000C
    hwnd = ctypes.windll.user32.FindWindowW(None, "Everquest")
    ctypes.windll.user32.SendMessageW(hwnd, WM_SETTEXT, 0, server)

def move_window(color):
    """Move the window to the specified position."""
    try:
        window = gw.getWindowsWithTitle(color)[0]
        time.sleep(0.5)
        window.moveTo(0, 0)
    except IndexError:
        print(f"Window with title '{color}' not found.")
    except Exception as e:
        print(f"Error moving window: {e}")

def kill_all():
    """Kill all instances of 'eqgame.exe'."""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() == 'eqgame.exe':
                print(f"Killing process {proc.info['name']} with PID {proc.info['pid']}")
                proc.terminate()  # or proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Error handling process: {e}")

def watch_log_file(file_path):
    """Watch the log file for a specific entry and restart clients if necessary."""
    print(file_path)
    target_entry = 'You are out of food and drink.'
    date_format = "%a %b %d %H:%M:%S %Y"
    print('Log Watch Called')
    last_entry_time = datetime.datetime.now()  # Initialize last entry time to the current time

    while True:
        try:
            with open(file_path, 'r', encoding='utf-8') as log_file:
                for line in log_file:
                    if target_entry in line:
                        timestamp_str = line.split(']')[0][1:].strip()
                        log_timestamp = datetime.datetime.strptime(timestamp_str, date_format)
                        last_entry_time = log_timestamp  # Update last entry time to the latest entry time
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin-1') as log_file:
                for line in log_file:
                    if target_entry in line:
                        timestamp_str = line.split(']')[0][1:].strip()
                        log_timestamp = datetime.datetime.strptime(timestamp_str, date_format)
                        last_entry_time = log_timestamp  # Update last entry time to the latest entry time

        # Check if the last entry is more than two minutes old
        time_difference = datetime.datetime.now() - last_entry_time
        if time_difference > datetime.timedelta(minutes=2):
            print('Food and drink warning found. Restarting clients.')
            kill_all()
            launch_blue()
            time.sleep(10)
            launch_green()
            time.sleep(200)
            print('Returning to Pulse')
            return
        time.sleep(2)


if __name__ == "__main__":
    log_file_path = r'path\to\log\file.txt'  # Replace with the actual path to your log file
    watch_log_file(log_file_path)
