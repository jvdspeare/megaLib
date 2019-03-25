# This demo uses schedule - https://pypi.org/project/schedule/ & time
# Import schedule & time
import schedule
import time

# Import megalib
import megalib

# Service UID
my_uid = 'b80ed347-5716-463c-b628-e2be003b636e'

# Authenticate user credentials using the megalib.login function
auth = megalib.login(input('Username: '), input('Password: '), input('TFA (Leave black if not enabled): '))


def speed_change(header, uid, speed):
    print(megalib.update_vxc(header, uid, speed=speed).status_code)


# Define the schedule
schedule.every().monday.at('15:22').do(speed_change, auth.header, my_uid, 250)
schedule.every().monday.at('16:22').do(speed_change, auth.header, my_uid, 350)
schedule.every().monday.at('17:22').do(speed_change, auth.header, my_uid, 400)

while True:
    schedule.run_pending()
    time.sleep(1)
