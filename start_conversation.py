def start_conversation():
    print("Bienvenue ! Pour mieux vous accompagner, pourriez-vous me dire dans quel secteur vous évoluez ?")
    print("1. Organisateur d'événements")
    print("2. Restaurateur")
    print("3. Autre secteur")
    sector = input("Veuillez entrer le numéro correspondant à votre secteur : ")

    if sector == "1":
        return "evenementiel"
    elif sector == "2":
        return "restauration"
    else:
        return "autre"
