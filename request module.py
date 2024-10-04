import requests
API_KEY = 'f5b137b93cde54a1e2e02a634ac56334'  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

class WeatherApp:
    cities = ['Chennai', 'New York', 'london']
    def _init_(self):
        self.cities = []

    def get_weather(self, city):
        url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            print(f"\nWeather in {city}:")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Error: Unable to retrieve weather data for {city}. Status Code: {response.status_code}")

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
            print(f"Added {city} to the list.")
        else:
            print(f"{city} is already in the list.")

    def update_city(self, old_city, new_city):
        if old_city in self.cities:
            index = self.cities.index(old_city)
            self.cities[index] = new_city
            print(f"Updated {old_city} to {new_city}.")
        else:
            print(f"{old_city} not found in the list.")

    def delete_city(self, city):
        if city in self.cities:
            self.cities.remove(city)
            print(f"Deleted {city} from the list.")
        else:
            print(f"{city} not found in the list.")

    def display_weather(self):
        if not self.cities:
            print("No cities in the list.")
            return
        
        for city in self.cities:
            weather = self.get_weather(city)
            if weather:
                print(f"{weather['city']}: {weather['temperature']}°C, {weather['weather']}")
            else:
                print(f"Weather data for {city} not found.")

def main():
    app = WeatherApp()

    while True:
        print("\nOptions:")
        print("1. Add city")
        print("2. Update city")
        print("3. Delete city")
        print("4. Display weather")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            city = input("Enter city name to add: ")
            app.add_city(city)
        elif choice == '2':
            old_city = input("Enter the city name to update: ")
            new_city = input("Enter the new city name: ")
            app.update_city(old_city, new_city)
        elif choice == '3':
            city = input("Enter city name to delete: ")
            app.delete_city(city)
        elif choice == '4':
            app.display_weather()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()