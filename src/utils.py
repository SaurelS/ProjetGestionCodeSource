def extraire_temps_ping(sortie: str) -> float:
    """
    Extrait le temps de réponse du ping à partir de la sortie de la commande.
    
    Args:
        sortie (str): La sortie de la commande ping.
    
    Returns:
        float: Le temps de réponse en millisecondes, ou None si non trouvé.
    """
    for ligne in sortie.split("\n"):
        if "time=" in ligne:
            try:
                return float(ligne.split("time=")[1].split()[0].replace("ms", ""))
            except ValueError:
                return None
    return None
