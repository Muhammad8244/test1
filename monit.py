import os
import time
import subprocess
import requests

def monitor_and_open(file_path, csv_file, url):
    # Monitor the link.bat file for access events
    last_access_time = os.path.getatime(file_path)
    print(f"Monitoring {file_path} for access events...")

    while True:
        try:
            current_access_time = os.path.getatime(file_path)
            # Check if the access time has changed
            if current_access_time != last_access_time:
                print(f"The file {file_path} was accessed at {time.ctime(current_access_time)}.")
                last_access_time = current_access_time

                # Open the CSV file in the default application
                open_csv(csv_file)

                # Make an HTTP GET request to the URL and print status code
                make_request(url)

            time.sleep(1)  # Check every second

        except KeyboardInterrupt:
            print("Stopped monitoring.")
            break

def open_csv(csv_file):
    try:
        if os.name == 'nt':  # Windows
            os.startfile(csv_file)
        elif os.name == 'posix':  # macOS and Linux
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, csv_file])
        print(f"Opened CSV file: {csv_file}")
    except Exception as e:
        print(f"Failed to open CSV file: {e}")

def make_request(url):
    try:
        response = requests.get(url)
        print(f"Response Status Code: {response.status_code}")
        # Uncomment the next line to print the response content
        # print(response.text)
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")

# Define file paths and URL
bat_file = r"C:\Users\PMLS\Desktop\link.bat"
csv_file = r"C:\Users\PMLS\Downloads\combined_file2.csv"
url = r"https://www.google.com"

# Start monitoring and handling file access
monitor_and_open(bat_file, csv_file, url)
