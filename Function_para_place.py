import spacy
import requests

nlp = spacy.load('en_core_web_sm')

API_KEY = 'f84b15244f7146a88e7823674744588d'

def get_place_info(place_name):
    
    url = f"https://api.opencagedata.com/geocode/v1/json?q={place_name}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]
    return None

def extract_most_relevant_place(paragraph):
    paragraph=paragraph.title()
    doc = nlp(paragraph)
    #print(doc)

    places=doc.ents
    #print(token,token.idx)
    print(places)

    if not places:
        return None

    most_relevant_place = None
    lowest_priority = float('inf')

    
    for place in places:
        place = place.text.strip()
        place_info = get_place_info(place)

        if place_info:

            types = place_info['components']
            #print(place)
            #print(types)
            if 'neighbourhood' in types:
                priority = 1
            elif 'state_district' in types:
                priority = 2
            elif 'city' in types:
                priority = 3
            elif 'state' in types:
                priority = 4
            elif 'country' in types:
                priority = 5
            else:
                priority = float('inf')


            if priority < lowest_priority:
                lowest_priority = priority
                most_relevant_place = place

    return most_relevant_place


