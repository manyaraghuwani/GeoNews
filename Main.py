from Function_para_place import extract_most_relevant_place
from Function_place_latlon import get_location
from DB import insert_cluster

def main():
    
    paragraph = "I live in ahmedabad"
    place_name = extract_most_relevant_place(paragraph)
    if place_name:
        address=place_name
        print(address)
        lat,lon=get_location(address)
        if lat is not None and lon is not None:
            print(lat,lon)
            insert_cluster(address, lat, lon)
        else:
            print("Location not found or not in India.")


    else:
        print("no")
        
    
    
    
    

if __name__ == "__main__":
    main()
