import os
import itertools
import re
import random
import time
import requests
from bs4 import BeautifulSoup

custom_cookies = {}
custom_cookies['.ASPXAUTH'] = os.environ.get('ASPXAUTH', None)
custom_cookies['ASP.NET_SessionId'] = os.environ.get('ASPNET_SessionId', None)
custom_cookies['AWSALB'] = os.environ.get('AWSALB', None)
custom_cookies['AWSALBCORS'] = os.environ.get('AWSALBCORS', None)
custom_cookies['VisaBookingType'] = os.environ.get('VisaBookingType', None)
custom_cookies['lpTestCookie1702961817385'] = os.environ.get('lpTestCookie1702961817385', None)


booking_url = "https://bmvs.onlineappointmentscheduling.net.au/oasis/AppointmentTime.aspx"

def check_available_dates(custom_cookies, booking_url):
    response = requests.get(url=booking_url, cookies=custom_cookies)

    available_dates = re.search(r'var gAvailDates = \[(.*)\];', response.text).group(1)
    date_lst = re.findall(r'new Date\((.*?)\)', available_dates)
    date_lst = [get_formatted_date(x) for x in date_lst]

    if date_lst:
        print("Available Dates:")
        for date in date_lst:
            print(date)

        # Extract time slots
        am_time_list, pm_time_list = extract_first_day_times(response.text)
        print("\nAvailable Time Slots for:", date_lst[0])

        # Print in two columns
        print('{:15s} {:s}'.format("Morning:", "Afternoon:"))
        for line in itertools.zip_longest(am_time_list, pm_time_list, fillvalue=' '):
            print('{:15s} {:s}'.format(line[0], line[1]))

def get_formatted_date(date):
    day = int(date.split(',')[2])
    month = int(date.split(',')[1])
    year = int(date.split(',')[0])

    current_month = month + 1
    if current_month < 10:
        current_month = '0' + str(current_month)
    date_str = f"{year}-{current_month}-{day}"
    return date_str


def extract_first_day_times(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    time_section = ['am', 'pm']
    am_time_list = []
    pm_time_list = []

    for time_sec in time_section:
        time_list_div = soup.find('div', {"class": time_sec + "-list"})
        time_list_div_children = time_list_div.findChildren("label" , recursive=False)
    
        for child in time_list_div_children:
            # Store morning times
            if time_sec == 'am':
                am_time_list.append(child.string)
            # Store afternoon times
            else:
                pm_time_list.append(child.string)

    return am_time_list, pm_time_list

while True:
    print("\n==================================\n")
    print("Current Time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    check_available_dates(custom_cookies, booking_url)
    time.sleep(random.randint(10, 30))