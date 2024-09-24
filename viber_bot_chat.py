import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pyautogui
import time
import sys
import io
import pyperclip

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]


creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\path->\\secret_key\Valued-rigging-423011-p9-19d5f63df9b7.json", scopes=scopes)

file = gspread.authorize(creds)
Workbook = file.open("Viber_Automation")
sheet3 = Workbook.get_worksheet(2)  # Get the third sheet (index starts at 0)
print("Data from google-sheet are recorded!!")
data = sheet3.get_all_records()

# Send data to Viber
print("Viber automation process by controlling screen are started!")

# Open Viber
pyautogui.press('winleft')  # Open the Start menu
pyautogui.typewrite('viber')  # Type 'viber' in the search box
pyautogui.press('enter')  # Open Viber
time.sleep(5)  # Wait for Viber to open
message_input_coords = (1359, 934)

# Ensure UTF-8 encoding for console output
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', errors='replace')

i = 1
for row in data:
    i += 1
    message = f"Dear:{row['Dear']}\t\t SenderName: {row['name']},\t\t Report: {row['report']}  \t\t Description: {row['Description']}   \t\t Impact: {row['Impact']}   \t\t Cause: {row['Cause']}  \t\t Action: {row['Action']}  \t\t Start time: {row['Starttime']}  \t\t End time: {row['Endtime']}  \t\t Total time: {row['Totaltime']}"
    print(message)
    print(f"\n Looping {i} \n")

    # Copy the message to the clipboard
    pyperclip.copy(message)

    # Click on the message input field
    pyautogui.click(message_input_coords)

    # Paste the message from the clipboard
    pyautogui.hotkey('ctrl', 'v')

    # Send the message
    pyautogui.press('enter')  # Press Enter to send the message