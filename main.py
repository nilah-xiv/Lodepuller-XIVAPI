import requests
import json

# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

LODESTONE_ID = config.get("lodestone_id")
BASE_URL = f"https://xivapi.com/character/{LODESTONE_ID}?data=ClassJobs"


# Fetch character data
def fetch_character_data():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Parse and display job levels
def display_job_levels(character_data):
    try:
        classes = character_data['Character']['ClassJobs']
        print("\n--- Current Job Levels ---")
        for job in classes:
            print(f"{job['UnlockedState']['Name']}: Level {job['Level']}")
    except KeyError as e:
        print(f"Failed to parse character data: {e}")

# Main execution
if __name__ == '__main__':
    data = fetch_character_data()
    if data:
        display_job_levels(data)

# Sample config.json content:
# {
#     "lodestone_id": "1234567"
# }
