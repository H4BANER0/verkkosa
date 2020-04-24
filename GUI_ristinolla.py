"""
Yksinkertainen ristinolla peli jonka suunnittelin ohjelmoinnin kurssilleni
"""

from tkinter import *

class Ristinolla:
    """
    Ristinolla-olio
    """
    def __init__(self):
        """
        init metodi avaa käyttöliittymän ikkunan, ikkunalle otsikon, juoron ja
        pelilaudan jota tarvitaan pelin voittajan testauksessa.
        pelistä voi POISTUA VAIN "POISTU" napilla tai raksilla ylä oikeasta
        kulmasta.
        Nappeja painellessa mennään eri metodiin jatkamaan toimintoa.
        """
        self.__pääikkuna = Tk()
        self.__pääikkuna.title("Ristinolla")
        self.__pääikkuna.option_add("*Font", "Arial 24")
        self.__turn = 0
        self.__pelilauta = [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " ",
        ]
        Label(self.__pääikkuna,
              text=f"Tervetuloa pelaamaan! X aloittaa").grid(
            row=4, columnspan=5, sticky=E + W)

        self.__napit_text = []
        for i in range(9):
            self.__napit_text.append(StringVar())

        self.__napit = []
        for i in range(9):
            self.__napit.append(Button(self.__pääikkuna,
                                       textvariable=self.__napit_text[i],
                                       command=lambda ind=i: self.nappia_painettu(ind)))

            self.__napit_text[i].set(" ")

        for i in range(9):
            self.__napit[i].grid(row=i//3, column=i % 3, ipadx=60, ipady=60)

        self.__lopetusnappi = Button(self.__pääikkuna, text="Poistu",
                                     font=("Arial", 24), bg="red",
                                     command=self.quit).grid(row=6,
                                                             columnspan=3)

        self.__pääikkuna.mainloop()

    def nappia_painettu(self, indeksi):
        """
        metodi asettaa X tai O pelilaudalle ja syöttää
        graafiseen käyttöliittymään = GKL uudet kuvat eli X tai O
        lisäksi se poistaa painetun napin käytöstä.
        Voittaja tulostuu GKL:mään
        jos peli jatkuu 9. vuoroon asti niin peli päättyy ja julistetaan
        tasapeli. Myös seuraavan pelaajan vuoro kerrotaan.

        :param indeksi: indeksi Väliltä 0-8 joka kertoo painetun napin indeksin
        jotta saadaan oikeaan kohtaan oikea merkki
        """
        Label(self.__pääikkuna,
              text=f"Pelaajan {checker(self.__turn+1)} vuoro!").grid(
            row=4, columnspan=5, sticky=E + W)
        self.__pelilauta[indeksi] = checker(self.__turn)
        self.__napit_text[indeksi].set(checker(self.__turn))
        self.__napit[indeksi].config(state=DISABLED)
        self.__turn += 1

        winner = voitto(self.__pelilauta)
        if winner == "X" or winner == "O":
            Label(self.__pääikkuna, text=f"Voittaja on {winner}! Kiitos pelistä").grid(
                row=4, columnspan=5, sticky=E+W)

        elif self.__turn == 9:
            Label(self.__pääikkuna, text="Tasapeli!").grid(
                row=4, columnspan=5, sticky=E + W)


    def quit(self):
        """
        Tuhoaa pääikkunan eli ohjelman suoritus loppuu.
        """
        self.__pääikkuna.destroy()

def voitto(pelilauta):
    """
    Funktio testaa voitokkaat tapaukset
    :param pelilauta: antaa listan arvoja
    :return: X tai O
    """
    for k in range(3):
        i = k * 3
        if pelilauta[i+0] == pelilauta[i+1] == pelilauta[i+2] != " ":
            return pelilauta[i]
        if pelilauta[k+0] == pelilauta[k+3] == pelilauta[k+6] != " ":
            return pelilauta[k]

    if pelilauta[0] == pelilauta[4] == pelilauta[8] != " " or\
            pelilauta[2] == pelilauta[4] == pelilauta[6] != " ":
        return pelilauta[4]
    return False

def checker(turns):
    """
    tarkistaa onko X vai O vuoro
    :param turns:
    :return: Merkki joka on X tai O
    """
    while turns < 9:

        # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        return mark

def main():
    """
    pääfunktio joka vain aloittaa graafisen käyttöliittymä pelin
    :return:
    """

    Ristinolla()


main()