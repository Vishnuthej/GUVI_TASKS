import requests

class BreweryData:

    def __init__(self):
        self.url = "https://api.openbrewerydb.org/breweries"
        self.states = ['Alaska', 'Maine', 'New York']
        # list of required states 

    # Method to fetch the data of breweries by state
    def fetch_breweries_by_state(self, state):
        response = requests.get(f"{self.url}?by_state={state}")
        return response.json()
    # Method to list out the no.of breweries by each state
    def list_breweries(self):
        for state in self.states:
            breweries = self.fetch_breweries_by_state(state)
            print(f"Breweries in {state}:")
            for brewery in breweries:
                print(f"  - {brewery['name']}")
            print(f"Total breweries in {state}: {len(breweries)}\n")

    def count_brewery_types_by_city(self):
        for state in self.states:
            breweries = self.fetch_breweries_by_state(state)
            #Each brewery is represented as a dictionary with keys like city and brewery_type.
            city_brewery_types = {}
        
            for brewery in breweries:
                city = brewery['city']
                brewery_type = brewery['brewery_type']
                if city not in city_brewery_types:
                    city_brewery_types[city] = set()
                    # Sets containing unique brewery types

                city_brewery_types[city].add(brewery_type)
                #will store the set of brewery types for each city in the state.
            print(f"Brewery types by city in {state}:")
            
            for city, brewery_types in city_brewery_types.items():
                print(f"  - {city}: {len(brewery_types)} types")

    def count_breweries_with_websites(self):
        for state in self.states:
            breweries = self.fetch_breweries_by_state(state)
            count_with_website = sum(1 for brewery in breweries if brewery['website_url'])
            print(f"Breweries with websites in {state}: {count_with_website}")

# Fetch and display brewery data
brewery_data = BreweryData()

print("Listing breweries in selected states:")
brewery_data.list_breweries()

print("\nCounting brewery types by city:")
brewery_data.count_brewery_types_by_city()

print("\nCounting breweries with websites:")
brewery_data.count_breweries_with_websites()
