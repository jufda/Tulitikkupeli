"""
2022-02-15
Jufda
Tulitikkupeli

21 tulitikun peli
2 pelaajaa
poistavat vuorotellen 21 tulitikun kasasta 1-3 tikkua
viimeisen tikun poistaja häviää
Seuraavalla tavalla selviää voittaja:
            2-1=W
            3-2=W
            4-3=W
        5-x=L
    6-1-x=W
    7-2-x=W
    8-3-x=W
9--=L
10-1, 11-2, 12-3
13---=L
14-1, 15-2, 16-3
17----=L
18-1, 19-2, 20-3
21-----=L
"""


def bot(sticks_left):
    """Always wins the game if possible
    If losing in sight, removes 3 at a time
    Sees the light, accepts loss this time, and is still fine.

    param: int sticks_left, How many sticks are left in the game
    return: int sticks_to_remove, How many sticks the bot removes
    """

    # Loss in sight, avoid fright
    if sticks_left == 21 or sticks_left == 17 or sticks_left == 13 or sticks_left == 9 or sticks_left == 5:
        return 3
    # Game's won, hear the don
    elif sticks_left == 20 or sticks_left == 16 or sticks_left == 12 or sticks_left == 8 or sticks_left == 4:
        return 3
    # Game's won, loss gon'
    elif sticks_left == 19 or sticks_left == 15 or sticks_left == 11 or sticks_left == 7 or sticks_left == 3:
        return 2
    # With a single stick taken away, the battle gain
    elif sticks_left == 18 or sticks_left == 14 or sticks_left == 10 or sticks_left == 6 or sticks_left == 2:
        return 1
    # No choice left, it's the last theft.
    elif sticks_left == 1:
        return 1


def ai():
    """Versus AI"""
    while True:
        print("Do you want to play against artificial intelligence? \n ")
        print("Jos haluat, paina vain Enter \n")
        opponent = input("If not, against who do you want to play?  ")

        # Jos käyttäjä lyö tyhjää, lopetetaan kyseleminen.
        if opponent == "":
            opponent = "the_great_artificial_intelligence_stick_master_pro_2022"
            return opponent
        else:
            return opponent


def main():
    """Does the main thing.
    
    :p1_turn: boolean, kertoo onko Player 1 vuorossa
    :sticks_left: int, ilmaisee jäljellä olevan tikkujen lukumäärän
    :return: 0
    """
    # Pelin nimen julistus
    print("Game of sticks")
    print()
    player1 = input("What do you want to be called?  ")

    # Kysytään haluaako pelaaja tekoälyvastustajan
    player2 = ai()
    if player2 == "the_great_artificial_intelligence_stick_master_pro_2022":
        print("You play against Suuri ja Mahtava Tekoäly: Tikkumestari2022")
    else:
        print("You play against:", player2)

    # Aloitetaan peli antamalla vuoro Player 1:lle
    p1_turn = True
    # Asetetaan tikkujen lukumäärä
    sticks_left = 21
    # Kun tikkuja on jäljellä , pelataan
    while sticks_left in range(1, sticks_left+1):
        # Kun Player 1 vuoro koittaa
        while p1_turn:
            # Kysytään Player 1:ltä, montako tikkua hän haluaa poistaa
            p1_input = int(input(f"{player1} enter how many sticks to remove:  "))

            # Tarkistetaan valitseeko pelaaja poistaa sallitun määrän tikkuja
            if 1 <= p1_input <= 3:
                # Tallennetaan uusi tikkujen määrä poistamisen jälkeen
                sticks_left = sticks_left - p1_input
                # Jos tikut loppuvat, palataan
                if sticks_left <= 0:
                    break
                else:
                    # Kerrotaan kasaan jääneiden tikkujen määrä
                    print("There are", sticks_left, "sticks left")
                # Player 1 pelasi vuoronsa, vaihdetaan Player 2 vuoroon
                p1_turn = False
            else:
                # Muistutetaan pelin säännöistä, mikäli pelaaja yrittää ottaa kielletyn määrän tikkuja
                print("Must remove between 1-3 sticks!")
        # Kun Player 2 vuoro koittaa
        while not p1_turn:
            if player2 == "the_great_artificial_intelligence_stick_master_pro_2022":
                # Kutsutaan Suuri ja Mahtava Tekoäly: Tikkumestari2022 tekemään siirtonsa
                p2_input = bot(sticks_left)

                if 1 <= p2_input <= 3:
                    # Tallennetaan uusi tikkujen määrä poistamisen jälkeen
                    sticks_left = sticks_left - p2_input
                    # Jos tikut loppuvat, palataan
                    if sticks_left <= 0:
                        break
                    else:
                        print("Suuri ja Mahtava Tekoäly: Tikkumestari2022 poisti", p2_input, "tikkua.")
                        print("There are", sticks_left, "sticks left")
                    # Player 2 pelasi vuoronsa, vaihdetaan Player 1 vuoroon
                    p1_turn = True
                else:
                    # Muistutetaan pelin säännöistä, mikäli pelaaja yrittää ottaa kielletyn määrän tikkuja
                    print("Must remove between 1-3 sticks!")
            else:
                # Kysytään Player 2:ltä, montako tikkua hän haluaa poistaa
                p2_input = int(input(f"{player2} enter how many sticks to remove: "))

                if 1 <= p2_input <= 3:
                    # Tallennetaan uusi tikkujen määrä poistamisen jälkeen
                    sticks_left = sticks_left - p2_input
                    # Jos tikut loppuvat, palataan
                    if sticks_left <= 0:
                        break
                    else:
                        print("There are", sticks_left, "sticks left")
                    # Player 2 pelasi vuoronsa, vaihdetaan Player 1 vuoroon
                    p1_turn = True
                else:
                    # Muistutetaan pelin säännöistä, mikäli pelaaja yrittää ottaa kielletyn määrän tikkuja
                    print("Must remove between 1-3 sticks!")

    # Jos tikut loppuvat, julistetaan häviäjäksi viimeisen tikun ottanut
    if sticks_left <= 0:
        if p1_turn:
            print("Player 1 lost the game!")
        else:
            print("Player 2 lost the game!")


if __name__ == "__main__":
    main()
