from opencage.geocoder import OpenCageGeocode, OpenCageGeocodeError
import logging
import time

def get_location(address):
    key = 'f84b15244f7146a88e7823674744588d'
    geocoder = OpenCageGeocode(key)

    try:
        if not address.strip():
            raise ValueError("The address provided is empty. Please enter a valid location.")

        result = geocoder.geocode(address)
        
        if result:
            for res in result:
                #print(res)
                if 'components' in res and 'country' in res['components']:
                    country = res['components']['country']

                    # See If location is in India
                    if country == 'India':
                        location = res['geometry']
                        #print(f"Latitude= {location['lat']} \nLongitude= {location['lng']}")
                        #print(location['lat'],location['lng'])

                        return location['lat'], location['lng']

            #print("Location found, but it is not in India.")
        else:
            logging.warning(f"No location found for the address: {address}")
            #print("Location not found.")

    except OpenCageGeocodeError as e:
        error_message = str(e)
        if "invalid API key" in error_message:
            logging.error("The API key is invalid. Please check and update it.")
            print("Error: The API key is invalid. Please check and update it.")
        elif "rate limit exceeded" in error_message:
            logging.warning("Rate limit exceeded. Waiting for a minute before retrying.")
            print("Rate limit exceeded. Please wait...")
            time.sleep(60)
            return get_location(address)
        elif "timeout" in error_message:
            logging.error("The request timed out. Please check your network connection and try again.")
            print("Error: The request timed out. Please check your network connection and try again.")
        else:
            logging.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")
    except ValueError as ve:
        logging.error(ve)
        print(ve)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

    return None,None

