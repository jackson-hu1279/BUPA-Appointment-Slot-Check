import requests
import re
import random
import time
from bs4 import BeautifulSoup

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
    # print("Extracted HTML var:", available_dates)

    date_lst = re.findall(r'new Date\((.*?)\)', available_dates)
    if date_lst:
        print("Available Dates:")
        for date in date_lst:
            print(date)

        am_time_list, pm_time_list = extract_first_day_times(response.text)
        print("\nAvailable Times for", date_lst[0])
        print("\nMorning Times:")
        for am_time in am_time_list:
            print(am_time)
        print("\nAfternoon Times:")
        for pm_time in pm_time_list:
            print(pm_time)


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
    # print("Current Time:", time.strftime("%b %d %Y %H:%M:%S", time.localtime()))

    check_available_dates(custom_cookies, booking_url)
    time.sleep(random.randint(10, 30))