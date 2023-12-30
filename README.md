# Bupa Appointment Slot Check
This project includes simple Python scripts used to automatically check [Bupa appointment](https://www.bupa.com.au/bupamvs/appointments) slots that are currently available for booking by simulating the action to refresh the booking page. The script will keep fetching the available time slots for the clinic you selected with cookies stored in the browser. Any available appointments will be captured and showed in the terminal. If you set up the date filter, an alarm will notify you when target date(s) which satisfy your conditions has/have been found.

<p align="center">
    <img src="docs/imgs/booking page.png" alt="Bupa Booking Page" width="600" />
    <br>Bupa Booking Page</br>
</p>

## How to Run
1. Have a working Python environment
2. Try to make a new appointment on [Bupa](https://bmvs.onlineappointmentscheduling.net.au/oasis/) in your browser
3. Check cookies saved for the domain `bmvs.onlineappointmentscheduling.net.au`
4. Save the cookies as key-value pairs the `.env` file under the directory
5. Enter Docker containers and direct to project folder
6. Execute the script with Python - `python extract_datetime.py`
7. The script will keep fetching the available time slots for your appointment until killed with `Ctrl + C`

## Activate Notify Alarm
### Set Date Filter
You can also set up a notify alarm if you only want to monitor available bookings for a specific date or within a date range. Simply set your desirable dates in `extract_datetime.py` like the following:
```python
# Target date (period)
target_start_date = "2024-02-08"
target_end_date = "2024-03-02"
```
- For a date range:
    - Set both `target_start_date` and `target_end_date`
- For a single date: 
    - Set only the `target_start_date` and leave the `target_end_date` as `None`
    - *Or* set both dates to be the same

## Screenshots
### Expected Outputs

Target Web Page            |  Script Output
:-------------------------:|:-------------------------:
<img src="docs/imgs/sample%20result%20page.png" alt="Target Web Page" width="600" />  |  <img src="docs/imgs/sample%20output.png" alt="Script Output" width="200" /> 

### Other Possible Outputs
Multiple Dates             |  Limited Slots            |  No Available
:-------------------------:|:-------------------------:|:-------------------------:
<img src="docs/imgs/multiple dates.png" alt="Multiple Datese" width="200" />  |  <img src="docs/imgs/limited slots.png" alt="Limited Slots" width="200" /> |  <img src="docs/imgs/no available.png" alt="No Available" width="260" /> 

