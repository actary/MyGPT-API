def collect_metadata():
    location = input("Quel est l'emplacement de votre événement ou restaurant ? ")
    budget = float(input("Quel est le panier moyen des participants/clients ? (en euros) "))
    ambiance = input("Quel type d'ambiance culinaire souhaitez-vous ? (luxueuse, conviviale, bon rapport qualité-prix) ")
    restrictions = input("Avez-vous des restrictions alimentaires spécifiques ? (végétarien, sans gluten, etc.) ")
    size = input("Quel est le nombre de repas à prévoir et la durée de l'événement ? ")
    
    return {
        "location": location,
        "budget": budget,
        "ambiance": ambiance,
        "restrictions": restrictions,
        "size": size
    }
