import os
import itertools
import re
import argparse
import random
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from pydub import AudioSegment
from pydub.playback import play

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# Check available dates from fetched HTML content
def check_available_dates(custom_cookies, booking_url):
    response = requests.get(url=booking_url, cookies=custom_cookies)
    try:
        available_dates = re.search(r'var gAvailDates = \[(.*)\];', response.text).group(1)
        date_lst = re.findall(r'new Date\((.*?)\)', available_dates)
        date_lst = [get_formatted_date(x) for x in date_lst]
    except:
        print(color.RED + "Failed to extract dates! Please ensure valid cookies are provided!" + color.END)
        exit(1)

    # Find available dates
    if date_lst:
        print("Available Dates:")
        for date in date_lst:
            print(date)

        # Extract time slots
        am_time_list, pm_time_list = extract_first_day_times(response.text)
        print("\nAvailable Time Slots For: " + color.BOLD + str(date_lst[0]) + color.END)

        # Print in two columns
        print('{:15s} {:s}'.format("Morning:", "Afternoon:"))
        for line in itertools.zip_longest(am_time_list, pm_time_list, fillvalue=' '):
            print('{:15s} {:s}'.format(line[0], line[1]))

        return date_lst

    # No available dates
    else:
        print("There are no available appointments at this time. \nPlease try another clinic or come back later.")

# Convert HTML date format to datetime.date format
def get_formatted_date(date):
    day = int(date.split(',')[2])
    month = int(date.split(',')[1])
    year = int(date.split(',')[0])

    current_month = month + 1
    if current_month < 10:
        current_month = '0' + str(current_month)

    date_str = f"{year}-{current_month}-{day}"
    formatted_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    return formatted_date

# Check if given date satisfies conditions
def date_condition_met(given_date, start_date, end_date=None):
    # All input dates are in datetime.date format

    # Check exact date match
    if not end_date:
        return given_date == start_date
    # Check if date falls in given period
    else:
        return start_date <= given_date <= end_date

# Extract time slots for the first available date
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

# Main loop to perform iterative checking
def main(target_start_date, target_end_date):
    booking_url = "https://bmvs.onlineappointmentscheduling.net.au/oasis/AppointmentTime.aspx"

    # Collect cookies from env vars
    custom_cookies = {}
    custom_cookies['.ASPXAUTH'] = os.environ.get('ASPXAUTH', None)
    custom_cookies['ASP.NET_SessionId'] = os.environ.get('ASPNET_SessionId', None)
    custom_cookies['AWSALB'] = os.environ.get('AWSALB', None)
    custom_cookies['AWSALBCORS'] = custom_cookies['AWSALB']
    custom_cookies['VisaBookingType'] = 'AU'

    try:
        assert None not in custom_cookies.values()
    except:
        print(color.RED + "Faild to read cookies from env vars!\n" \
              + "Please copy cookie value pairs into .env file and source it before use!" + color.END)
        exit(1)

    # Iterative checking
    while True:
        print("\n==================================\n")
        print("Current Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Fetch available dates
        available_date_lst = check_available_dates(custom_cookies, booking_url)
        
        # Check if found target date
        for available_date in available_date_lst:
            if date_condition_met(available_date, target_start_date, target_end_date):
                play(AudioSegment.from_mp3("alarm.mp3"))
                break
            
        time.sleep(random.randint(5, 20))


if __name__ == "__main__":
    # Parse optional arguments for start and end dates if given
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--target_start_date", help="Target start date", type=str)
    parser.add_argument("-e", "--target_end_date", help="Target end date", type=str)
    args = parser.parse_args()

    # Try to parse as datetime.date format
    # Get target date (range)
    target_start_date = target_end_date = None
    try:
        if args.target_start_date:
            target_start_date = datetime.strptime(args.target_start_date, '%Y-%m-%d').date()
        if args.target_end_date:
            target_end_date = datetime.strptime(args.target_end_date, '%Y-%m-%d').date()
    except:
        print(color.RED + "Failed to parse given dates, please give dates in the format of \"YYYY-MM-DD\" and try again!" + color.END)
        exit(1)

    # Execute main function
    main(target_start_date, target_end_date)