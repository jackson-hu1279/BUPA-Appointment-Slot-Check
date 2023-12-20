# Bupa Appointment Slot Check
This project includes simple Python scripts used to automatically check [Bupa appointment](https://www.bupa.com.au/bupamvs/appointments) slots that are currently available for booking by simulating the action to refresh the booking page. The script will keep fetching the available time slots for the clinic you selected with cookies stored in the browser. Any available appointments will be captured and showed in the terminal.

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

## Screenshots
### Expected Outputs

Target Web Page            |  Script Output
:-------------------------:|:-------------------------:
<img src="docs/imgs/sample%20result%20page.png" alt="Target Web Page" width="600" />  |  <img src="docs/imgs/sample%20output.png" alt="Script Output" width="200" /> 

### Other Possible Outputs
Multiple Dates             |  Limited Slots            |  No Available
:-------------------------:|:-------------------------:|:-------------------------:
<img src="docs/imgs/multiple dates.png" alt="Multiple Datese" width="200" />  |  <img src="docs/imgs/limited slots.png" alt="Limited Slots" width="200" /> |  <img src="docs/imgs/no available.png" alt="No Available" width="260" /> 

