def define_objective():
    print("Quel est votre objectif pour cette session ?")
    print("A) Identifier des fournisseurs")
    print("B) Concevoir des menus durables")
    print("C) Créer une offre alimentaire complète")
    objective = input("Veuillez entrer la lettre correspondant à votre objectif (ou combiner plusieurs objectifs en séparant par des virgules) : ")

    objectives = objective.split(',')
    chosen_objectives = []
    
    if "A" in objectives:
        chosen_objectives.append("Identifier des fournisseurs")
    if "B" in objectives:
        chosen_objectives.append("Concevoir des menus durables")
    if "C" in objectives:
        chosen_objectives.append("Créer une offre alimentaire complète")
    
    return chosen_objectives
