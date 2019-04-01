# This demo requires schedule - https://pypi.org/project/schedule/ & time
# Import schedule, time & getpass
import schedule
import time
import getpass

# Import megalib
from megaLib import megalib

# Service UID
my_uid = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), getpass.getpass(), input('TFA (Leave black if not enabled): '))


def speed_change(header, uid, speed):
    print(megalib.update_vxc(header, uid, speed=speed).status_code)


# Define the schedule
# This example configures 1000Mbps between 23:50 & 04:00. 200Mbps at all other times.
schedule.every().monday.at('04:00').do(speed_change, auth.header, my_uid, 200)
schedule.every().monday.at('23:50').do(speed_change, auth.header, my_uid, 1000)
schedule.every().tuesday.at('04:00').do(speed_change, auth.header, my_uid, 200)
schedule.every().tuesday.at('23:50').do(speed_change, auth.header, my_uid, 1000)
schedule.every().wednesday.at('04:00').do(speed_change, auth.header, my_uid, 200)
schedule.every().wednesday.at('23:50').do(speed_change, auth.header, my_uid, 1000)
schedule.every().thursday.at('04:00').do(speed_change, auth.header, my_uid, 200)
schedule.every().thursday.at('23:50').do(speed_change, auth.header, my_uid, 1000)
schedule.every().friday.at('04:00').do(speed_change, auth.header, my_uid, 200)
schedule.every().friday.at('23:50').do(speed_change, auth.header, my_uid, 1000)
schedule.every().saturday.at('04:00').do(speed_change, auth.header, my_uid, 200)
schedule.every().saturday.at('23:50').do(speed_change, auth.header, my_uid, 1000)
schedule.every().sunday.at('04:00').do(speed_change, auth.header, my_uid, 200)
schedule.every().sunday.at('23:50').do(speed_change, auth.header, my_uid, 1000)

while True:
    schedule.run_pending()
    time.sleep(1)
