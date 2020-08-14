import requests
from dotenv import load_dotenv
import os

def get_offers_id():
    url = 'http://api.cpanomer1.affise.com/3.0/offers'
    headers = {
        "API-Key": TOKEN
    }
    response = requests.get(url, headers=headers)
    offers = response.json()
    id_list = []
    for offer in offers["offers"]:
        id_list.append(offer["id"])
    return id_list

def get_offer_by_id(id):
    url = 'http://api.cpanomer1.affise.com/3.0/offer/' + str(id)
    headers = {
        "API-Key": TOKEN
    }
    response = requests.get(url, headers=headers)
    offer = response.json()
    offer = offer["offer"]
    payments = offer["payments"]
    countries = payments[0]["countries"]
    output.write(f"In offer №{id} avaliable countries: {countries} \n")

def get_conversion(id, id_list):
    url = "http://api.cpanomer1.affise.com/3.0/stats/convertionbyid"
    params = {
        "id" : id
    }
    headers = {
        "API-Key" : TOKEN
    }
    response = requests.get(url, params=params, headers=headers)
    conversion = response.json()
    conversion = conversion["conversion"]
    conversion_offer = conversion["offer"]
    id = conversion_offer["id"]
    if id in id_list:
        print(conversion["clickid"])


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    offers_id_list = get_offers_id()
    output = open('offers.txt', 'w')
    for id in offers_id_list:
        get_offer_by_id(id)
    output.close()
    get_conversion("5bd00d73901fcf20008b4574", offers_id_list)