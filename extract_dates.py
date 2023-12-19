import requests
import re
import random
import time

custom_cookies = {}
custom_cookies['.ASPXAUTH'] = ''
custom_cookies['ASP.NET_SessionId'] = ''
custom_cookies['AWSALB'] = ''
custom_cookies['AWSALBCORS'] = ''
custom_cookies['VisaBookingType'] = ''
custom_cookies['lpTestCookie1702961817385'] = ''


booking_url = "https://bmvs.onlineappointmentscheduling.net.au/oasis/AppointmentTime.aspx"

def check_available_dates(custom_cookies, booking_url):
    response = requests.get(url=booking_url, cookies=custom_cookies)

    available_dates = re.search(r'var gAvailDates = \[(.*)\];', response.text).group(1)
    print("Extracted HTML var:", available_dates)

    date_lst = re.findall(r'new Date\((.*?)\)', available_dates)
    if date_lst:
        print("\nAvailable Dates:")
        for date in date_lst:
            print(date)


while True:
    print("\n==================================\n")
    print("Current Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # print("Current Time:", time.strftime("%b %d %Y %H:%M:%S", time.localtime()))

    
    time.sleep(random.randint(3, 6))