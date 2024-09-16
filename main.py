import functions
import time

cold_start = True
pulse = True
logs_blue = r'C:\Users\admin\Desktop\P99 - Copy\P99\Logs\eqlog_Zerotone_project1999.txt'
logs_green = r'C:\Users\admin\Desktop\P99\P99\Logs\eqlog_Airdiael_P1999Green.txt'

if cold_start == True: #Assuming clients are not running before script start, maybe from reboot.    print("Cold Start, launching clients.")
    functions.launch_blue()
    time.sleep(30)
    functions.launch_green()
    time.sleep(30)


while pulse:
    if cold_start == True:  #Giving clients time to start logging
        time.sleep(60)
    print("Pulse Started.")
    time.sleep(2)

    functions.watch_log_file(logs_blue)
    functions.watch_log_file(logs_green)

time.sleep(1)



