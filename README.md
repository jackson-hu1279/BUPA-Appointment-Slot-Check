# Bupa Appointment Slot Check
This project includes simple Python scripts used to automatically check [Bupa appointment](https://www.bupa.com.au/bupamvs/appointments) slots that are currently available for booking by simulating the action to refresh the booking page. The script will keep fetching the available time slots for the clinic you selected with cookies stored in the browser. Any available appointments will be captured and showed in the terminal. If you set up the [date filter](#activate-notify-alarm), an alarm will notify you when target date(s) which satisfy your conditions has/have been found.

<p align="center">
    <img src="docs/imgs/booking page.png" alt="Bupa Booking Page" width="600" />
    <br>Bupa Booking Page</br>
</p>

## How to Run
1. Have a working Python environment.
2. Install `ffmpeg` and required packages in `requirements.txt`
3. Try to make a new appointment on [Bupa](https://bmvs.onlineappointmentscheduling.net.au/oasis/) in your browser
4. Check cookies saved for the domain `bmvs.onlineappointmentscheduling.net.au`
5. Save the cookies as key-value pairs into a `.env` file under the directory.
6. Execute the script with Python - `python extract_datetime.py`
7. The script will keep fetching the available time slots for your appointment
8. The notify alarm will be triggered if [desired date](#activate-notify-alarm) given was found.

## Activate Notify Alarm
### Set Date Filter
You can also set up a notify alarm if you only want to monitor available bookings for a specific date or within a date range. Simply add optional arguments for `start_date` and `end_date` with `-s` and `-e` flags respectively.
```shell
# Check available dates only
python extract_datetime.py

# Monitor a single date
python extract_datetime.py -s 2024-01-28

# Monitor a date range
python extract_datetime.py -s 2024-01-28 -e 2024-02-05
```
- For a single date: 
    - Set only the `start_date`
    - **Or** set both dates to be the same
- For a date range:
    - Set both `start_date` and `end_date`

## Error Messages
1. Failed to read cookies.
    - Error message:
    ```
    Faild to read cookies from env vars!
    Please copy cookie value pairs into .env file and source it before use!
    ```
    - Solution:
    Check cookie value pairs are correctly saved in `.env` file and activated by `source .env`
2. Failed to parse dates.
    - Error message:
    ```
    Failed to parse given dates, please give dates in the format of "YYYY-MM-DD" and try again!
    ```
    - Solution:
    Use correct date format when give optional arguments, check [examples](#set-date-filter) above.
3. Failed to extract dates.
    - Error message:
    ```
    Failed to extract dates! Please ensure valid cookies are provided!
    ```
    - Solution:
    Your session may be expired, please get new cookies and try again.

## Screenshots
### Expected Outputs

Target Web Page            |  Script Output
:-------------------------:|:-------------------------:
<img src="docs/imgs/sample%20result%20page.png" alt="Target Web Page" width="600" />  |  <img src="docs/imgs/sample%20output.png" alt="Script Output" width="200" /> 

### Other Possible Outputs
Multiple Dates             |  Limited Slots            |  No Available
:-------------------------:|:-------------------------:|:-------------------------:
<img src="docs/imgs/multiple dates.png" alt="Multiple Datese" width="200" />  |  <img src="docs/imgs/limited slots.png" alt="Limited Slots" width="200" /> |  <img src="docs/imgs/no available.png" alt="No Available" width="260" /> 

### Case Demo
- Date filter set to:
    - `start_date`: `"2024-01-05"`
    - `end_date`: `"2024-01-08"`
- Alarm triggered when `"2024-01-05"` was found in available dates:

<p align="center">
    <img src="docs/imgs/case demo.png" alt="Case Demo" width="310" />
    <br>Alarm Triggered</br>
</p>