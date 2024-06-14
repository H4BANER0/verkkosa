import requests as requests
import random
import json

url = "https://api.telegram.org/.................................../"

ohjeistus = ["Moro! Kirjoita 'Play' heittääksesi noppaa!", "Jaahas", "selvä"]
komennot = ["moi", "moro", " vai ", "/ohjeet", "play"]

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
                 'Sait ' + str(_1) +
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

# main funktio vastaukseen ja navigointiin
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "/ohjeet":
                send_message(get_chat_id(update),
                             ohjeiden_listaus())
            elif get_message_text(update).lower() == "play":
                throw_dice(update)
            elif " vai " in get_message_text(update).lower():
                this_or_that(update)

            update_id += 1

main()
