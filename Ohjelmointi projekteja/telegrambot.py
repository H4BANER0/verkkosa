
import requests as requests
import random
import json


url = "https://api.telegram.org/..................................../"

ohjeistus = ["Moro! Kirjoita 'Play' heittääksesi noppaa!", 
"Lisätäksesi siipiä tilastoosi kirjoita siipien määrä kokonaislukuna /siipi esim. 20 /siipi",
 "selvä"]
komennot = ["moi", "moro", " vai ", "/ohjeet", "/play", "/siipi", "/siipistats"]

class Person:
    def __init__(self, name, wings):
        self.__name = name
        self.__wings = int(wings)

    def get_name(self):
        return f"{self.__name}"

    def get_wings(self):
        return int(self.__wings)

    def add_wings(self, wings, update):
        new_mount = self.get_wings() + wings     
        send_message(get_chat_id(update), 
        f"Henkilöllä {self.get_name()} on nyt {new_mount} siipeä!")
        self.__wings = new_mount

# luodaan chat id löytävä functio
def get_chat_id(update):
    chat_id = update["message"]["chat"]["id"]
    return chat_id

# funktio viestin tekstin hakemiseen
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# funktio viimeisimmän updaten hakemiseen
def last_update(req):
    response = requests.get(req + "getUpdates").json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates] # viimeisin viestin päivitys


# funktio joka lähettää viestin käyttäjälle
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response

def get_username(update):
    username = update["message"]["chat"]["username"]
    return username



# ohjeistuksen tulostus
def ohjeiden_listaus():
    ohjeet = ""
    for i in ohjeistus:
        ohjeet += i + '\n'
    return ohjeet

#funktio arpoo noppien luvuista
def throw_dice(update):
    _1 = random.randint(1, 6)
    _2 = random.randint(1, 6)
    send_message(get_chat_id(update),
                 str(get_username) + ' sai ' + str(_1) +
                 ' ja ' +
                 str(_2) +
                 '!\n Tulos on ' +
                 str(_1 + _2 ) + '!')

# funktio arpoo jomman kumman vastauksen kahdesta
def this_or_that(update):
    teksti = get_message_text(update).lower()
    teksti = teksti.split("vai")
    arpa = random.randint(1, 2)
    send_message(get_chat_id(update), str(teksti[arpa - 1]))

# Kukaan ei syö yli 30 siipeä kerralla jotan tämä funktio toimii rajoittimena sitä varten
def too_many_wings_check(update, data):
    teksti = get_message_text(update).lower()
    teksti = teksti.split(" ")
    wings = int(teksti[0])
    if wings > 31:
            send_message(get_chat_id(update), "Niin varmaan!")
            return False
    return True

#printtaa data kirjaston arvot siipilistaus.txt tiedostoon
def print_data_to_file(update,data):
    file = open("siipilistaus.txt", "w") 
    for value in data:         
        file.write(f"{value};{data[value].get_wings()}\n")     
    file.close()

# Siipistatistiikan tallennus käyttäjänimen mukaan
def save_data(update, data):
    teksti = get_message_text(update).lower()
    teksti = teksti.split(" ")
    wings = int(teksti[0])
    username = get_username(update)

    if username not in data:
        data[username] = Person(username,wings)
        data[username].add_wings(wings, update)
        
    else:
        data[username].add_wings(wings, update)
        
    print_data_to_file(update,data)     

#siipi listan tarkistaminen
def read_file(data):
    file = open("siipilistaus.txt", "r")
    tiedosto = file.readlines()
    file.close()
    for line in tiedosto:
        lista = line.strip().split(";")
        username = lista[0]
        wings = int(lista[1])
        data[username] = Person(username, wings)
    return data

# siipistatistiikan tulostus telegram chättiin
def list_values(update,data):
    for value in data:
        send_message(get_chat_id(update),f"{value} : {data[value].get_wings()}")

# main funktio vastaukseen ja navigointiin
def main():
    update_id = last_update(url)["update_id"]

    data = {}
    read_file(data)
    while True:
        update = last_update(url)
        komento = get_message_text(update).lower()
        if update_id == update["update_id"]:
            if komento == "/ohjeet":
                send_message(get_chat_id(update),
                             ohjeiden_listaus())
            elif komento == "/play":
                throw_dice(update)
            elif " vai " in komento:
                this_or_that(update)
            elif " /siipi" in komento:
                if too_many_wings_check(update,data) == False:
                    continue
                else:
                    save_data(update,data)
            elif "/siipistats" in komento:
                list_values(update,data)
                
                              
            update_id += 1

main()
