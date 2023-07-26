import requests
import datetime


API_KEY = "4b9a46c9d40e2910602d172ecbec17dc3"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather(date_str):
    try:
    
        date_object = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        
    except ValueError:
        print("invalid date format ")
        return
    
    unix_timestamp = int(date_object.timestamp())
   
    url = f"{BASE_URL}&dt={unix_timestamp}"

   
    response = requests.get(url)
    data = response.json()

    
    if data.get("cod")==200:
        temperature = data["main"]["temp"]
        print(f"Temperature on {date_str}: {temperature}°C")
    else:
        print("Error fetching")

def get_wind_speed_by_date(date_str):
    date_object = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    unix_timestamp = int(date_object.timestamp())

   
    url = f"{BASE_URL}?appid={API_KEY}&dt={unix_timestamp}"

   
    response = requests.get(url)
    data = response.json()

   
    temperature = data["main"]["temp"]
    print(f"Temperature on {date_str}: {temperature}°C")
    
def get_pressure_by_date(date_str):
    date_object = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    unix_timestamp = int(date_object.timestamp())

   
    url = f"{BASE_URL}?appid={API_KEY}&dt={unix_timestamp}"

   
    response = requests.get(url)
    data = response.json()

   
    temperature = data["main"]["temp"]
    print(f"Temperature on {date_str}: {temperature}°C")
    
    
def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date_str = input("Enter the date (YYYY-MM-DD): ")
            get_weather(date_str)
        elif choice == "2":
            date_str = input("Enter the date (YYYY-MM-DD): ")
            get_wind_speed_by_date(date_str)
        elif choice == "3":
            date_str = input("Enter the date (YYYY-MM-DD): ")
            get_pressure_by_date(date_str)
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
