# to import requests library & multiple exceptions libraries
import requests
from requests.exceptions import ChunkedEncodingError, RequestException

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()
        except ChunkedEncodingError as e:
            print(f"ChunkedEncodingError occurred: {e}")
            # Handle the error (e.g., retry the request, log the error, etc.)
        except RequestException as e:
            print(f"RequestException occurred: {e}")
            # Handle other types of request exceptions
        except Exception as e:
            print(f"An error occurred: {e}")
            # Handle any other exceptions

#Method to display country & currency
    def display_countries_and_currencies(self):
        for country in self.data:
            name = country['name']['common']
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                print(f"Country: {name}, Currency: {currency_info['name']}, Symbol: {currency_info['symbol']}")

# Method to display list of countries with dollar currency
    def display_countries_with_dollar(self):
        for country in self.data:
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                if 'dollar' in currency_info['name'].lower():
                    print(f"Country: {country['name']['common']}, Currency: {currency_info['name']}")

# Method to display list of countries with Euro currency
    def display_countries_with_euro(self):
        for country in self.data:
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                if currency_info['name'].lower() == 'euro':
                    print(f"Country: {country['name']['common']}, Currency: {currency_info['name']}")


# URL for REST Countries API
url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)

print("\nCountries and their currencies:")
country_data.display_countries_and_currencies()
    
print("\nCountries using Dollar:")
country_data.display_countries_with_dollar()
    
print("\nCountries using Euro:")
country_data.display_countries_with_euro()
