
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes//(365*24*60*60)
    reste= secondes%(365*24*60*60)
    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines =reste//(7*24*60*60)
    reste= reste%(7*24*60*60)

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = reste//(24*60*60)
    reste = reste%(24*60*60)

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = reste//(60*60)
    reste = reste%(60*60)

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes =reste//60
    reste=reste%60

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = reste

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(f"{annees} années ,{semaines} semaines ,{jours} jours ,{heures} heures , {minutes} minutes ,{secondes} secondes")

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
