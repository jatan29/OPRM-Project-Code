import requests
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# -----------------------
# AMADEUS CREDENTIALS
# -----------------------
API_KEY = "hf7kpU1qz2eu2B9pRoDLCEEmxw0aKIQl"
API_SECRET = "FJM4mSGRB6GAP0Cn"

# -----------------------
# GOOGLE SHEETS CONFIG
# -----------------------
GOOGLE_CREDENTIALS_FILE = "credentials.json"  # Path to your Google service account JSON
GOOGLE_SHEET_NAME = "Flight Price Tracker"    # Name of your Google Sheet

# -----------------------
# FLIGHT ROUTES TO TRACK
# -----------------------
ROUTES = [
    {"origin": "BOM", "destination": "BLR", "date": "2026-03-22"},
    # Add more routes here:
    # {"origin": "DEL", "destination": "BLR", "date": "2026-03-17"},
]

# -----------------------
# GET AMADEUS ACCESS TOKEN
# -----------------------
def get_amadeus_token():
    auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    response = requests.post(auth_url, data={
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    })
    response.raise_for_status()
    print("✅ Amadeus login successful")
    return response.json()["access_token"]

# -----------------------
# FETCH FLIGHT OFFERS
# -----------------------
def fetch_flights(token, origin, destination, date):
    search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": date,
        "adults": 1,
        "max": 5  # Fetch top 5 offers per route
    }
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("data", [])

# -----------------------
# PARSE FLIGHT DATA
# -----------------------
def parse_flights(data, origin, destination):
    rows = []
    today = datetime.today().strftime("%Y-%m-%d")

    for offer in data:
        # Get airline code from the first itinerary's first segment
        itinerary = offer["itineraries"][0]
        first_segment = itinerary["segments"][0]

        airline_code = first_segment["carrierCode"]
        flight_number = f"{airline_code}{first_segment['number']}"
        departure_time = first_segment["departure"]["at"]  # ISO format
        departure_formatted = datetime.fromisoformat(departure_time).strftime("%Y-%m-%d %H:%M")
        price = offer["price"]["total"]
        currency = offer["price"]["currency"]
        route = f"{origin}-{destination}"

        rows.append([
            today,
            route,
            airline_code,
            flight_number,
            departure_formatted,
            f"{price} {currency}"
        ])

    return rows

# -----------------------
# CONNECT TO GOOGLE SHEETS
# -----------------------
def connect_google_sheets():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=scopes)
    client = gspread.authorize(creds)

    # Open or create the sheet
    try:
        sheet = client.open(GOOGLE_SHEET_NAME).sheet1
        print(f"✅ Opened existing sheet: '{GOOGLE_SHEET_NAME}'")
    except gspread.SpreadsheetNotFound:
        spreadsheet = client.create(GOOGLE_SHEET_NAME)
        sheet = spreadsheet.sheet1
        print(f"✅ Created new sheet: '{GOOGLE_SHEET_NAME}'")

    return sheet

# -----------------------
# ENSURE HEADERS EXIST
# -----------------------
def ensure_headers(sheet):
    headers = ["Date", "Route", "Airline", "Flight Number", "Departure", "Price"]
    existing = sheet.row_values(1)
    if existing != headers:
        sheet.insert_row(headers, 1)
        # Bold the header row
        sheet.format("A1:F1", {
            "textFormat": {"bold": True},
            "backgroundColor": {"red": 0.2, "green": 0.5, "blue": 0.8},
        })
        print("✅ Headers added to sheet")

# -----------------------
# APPEND ROWS TO SHEET
# -----------------------
def append_to_sheet(sheet, rows):
    sheet.append_rows(rows, value_input_option="USER_ENTERED")
    print(f"✅ Appended {len(rows)} row(s) to Google Sheet")

# -----------------------
# MAIN RUNNER
# -----------------------
def main():
    print("🚀 Starting Flight Price Tracker...")

    token = get_amadeus_token()
    sheet = connect_google_sheets()
    ensure_headers(sheet)

    all_rows = []
    for route in ROUTES:
        origin = route["origin"]
        destination = route["destination"]
        date = route["date"]

        print(f"🔍 Fetching flights: {origin} → {destination} on {date}")
        data = fetch_flights(token, origin, destination, date)

        if not data:
            print(f"⚠️  No flights found for {origin}-{destination}")
            continue

        rows = parse_flights(data, origin, destination)
        all_rows.extend(rows)
        print(f"   Found {len(rows)} flight(s)")

    if all_rows:
        append_to_sheet(sheet, all_rows)

    print("\n✅ Done! Flight prices updated in Google Sheets.")

if __name__ == "__main__":
    main()
