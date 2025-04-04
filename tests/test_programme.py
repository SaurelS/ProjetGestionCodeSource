"""Tests unitaires pour le module scanner_ip."""

import sys
import os
import unittest
from unittest.mock import patch
import asyncio

# Ajouter le répertoire src à sys.path pour résoudre le problème d'import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

# Importation des modules à tester
from scanner_ip import (
    extraire_temps_ping,
    enregistrer_resultats,
    analyser_reseau
)


class TestAnalyseurReseau(unittest.TestCase):
    """Tests unitaires pour l'analyseur de réseau."""

    def test_extraire_temps_ping(self):
        """Teste l'extraction du temps de réponse d'une sortie de ping.

        Cette fonction vérifie si le temps de réponse est correctement extrait
        d'une sortie de commande `ping` et si elle retourne `None` pour des
        erreurs telles que "Request timed out".
        """
        sortie = "64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=5.3 ms"
        self.assertEqual(extraire_temps_ping(sortie), 5.3)
        self.assertIsNone(extraire_temps_ping("Request timed out"))

    def test_enregistrer_resultats(self):
        """Teste l'enregistrement des résultats dans un fichier CSV.

        Cette fonction vérifie si les résultats des tests de ping sont
        correctement enregistrés dans un fichier CSV et si le fichier est
        correctement formaté.
        """
        donnees_test = [
            ("192.168.1.1", "Active", 5.3),
            ("192.168.1.2", "Inactive", None)
        ]
        fichier_test = "test_resultats.csv"
        enregistrer_resultats(fichier_test, donnees_test)

        with open(fichier_test, "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()

        self.assertEqual(lignes[1].strip(), "192.168.1.1,Active,5.3")
        self.assertEqual(lignes[2].strip(), "192.168.1.2,Inactive,")

        os.remove(fichier_test)

    @patch("scanner_ip.tester_ip")
    def test_analyser_reseau(self, mock_tester_ip):
        """Teste l'analyse réseau avec mock des tests IP.

        Cette fonction vérifie si l'analyse réseau fonctionne comme prévu en
        simulant des réponses actives pour les adresses IP dans un sous-réseau.
        Elle s'assure que les résultats sont enregistrés dans un fichier CSV.
        """
        mock_tester_ip.side_effect = lambda ip: (ip, True, 2.5)
        fichier_test = "test_analyse.csv"

        async def run_test():
            await analyser_reseau("192.168.0.0/30", fichier_test)

        asyncio.run(run_test())

        with open(fichier_test, "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()

        self.assertEqual(lignes[0].strip(), "IP,Statut,Ping (ms)")
        self.assertIn("192.168.0.1,Active,2.5", lignes[1])
        self.assertIn("192.168.0.2,Active,2.5", lignes[2])

        os.remove(fichier_test)


if __name__ == "__main__":
    unittest.main()

