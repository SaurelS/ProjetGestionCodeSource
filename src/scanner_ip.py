import argparse
import asyncio
import csv
import ipaddress
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor
from utils import extraire_temps_ping  # Importation de la fonction déplacée

def tester_ip(adresse_ip: str) -> tuple[str, bool, float]:
    """
    Envoie une requête ping à une adresse IP et retourne son statut
    et son temps de réponse.
    
    Args:
        adresse_ip (str): L'adresse IP à tester.
    
    Returns:
        tuple[str, bool, float]: Un tuple contenant l'adresse IP,
        son statut (True si active, False sinon), et le temps de réponse en ms.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        resultat = subprocess.run(
            ["ping", param, "1", "-w", "1000", adresse_ip],
            capture_output=True,
            text=True,
            check=True
        )
        return adresse_ip, True, extraire_temps_ping(resultat.stdout)
    except subprocess.CalledProcessError:
        return adresse_ip, False, None

async def analyser_reseau(plage_ip: str, fichier_sortie: str):
    """
    Analyse une plage d'adresses IP de manière asynchrone.
    
    Args:
        plage_ip (str): La plage d'IP à analyser (format CIDR).
        fichier_sortie (str): Nom du fichier où enregistrer les résultats.
    """
    reseau = ipaddress.ip_network(plage_ip, strict=False)
    ips_actives = []
    
    with ThreadPoolExecutor(max_workers=10) as executant:  # Limitation du nombre de threads
        loop = asyncio.get_event_loop()
        taches = [
            loop.run_in_executor(executant, tester_ip, str(ip))
            for ip in reseau.hosts()
        ]
        resultats = await asyncio.gather(*taches)
    
    for ip, est_active, temps_reponse in resultats:
        statut = "Active" if est_active else "Inactive"
        ips_actives.append((ip, statut, temps_reponse))
        print(
            f"{ip} {statut} (Ping: {temps_reponse} ms)"
            if est_active else f"{ip} {statut}"
        )
    enregistrer_resultats(fichier_sortie, ips_actives)

def enregistrer_resultats(nom_fichier: str, resultats: list):
    """
    Enregistre les résultats de l'analyse dans un fichier CSV.
    
    Args:
        nom_fichier (str): Le nom du fichier où enregistrer les résultats.
        resultats (list): Liste des résultats sous forme de tuples.
    """
    with open(nom_fichier, mode="w", newline="") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(["IP", "Statut", "Ping (ms)"])
        ecrivain.writerows(resultats)
    print(f"Résultats enregistrés dans {nom_fichier}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyseur de réseau : Détection des IP actives et inactives."
    )
    parser.add_argument(
        "--plage", type=str, required=True,
        help="Plage IP à analyser (ex: 192.168.1.0/24)"
    )
    parser.add_argument(
        "--sortie", type=str, default="resultats.csv",
        help="Fichier de sortie des résultats"
    )
    args = parser.parse_args()
    asyncio.run(analyser_reseau(args.plage, args.sortie))