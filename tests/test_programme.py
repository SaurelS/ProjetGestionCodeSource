import unittest
from utils import extraire_temps_ping
from src.programme_principal import enregistrer_resultats

class TestAnalyseurReseau(unittest.TestCase):
    """Tests unitaires pour l'analyseur de réseau."""
    
    def test_extraire_temps_ping(self):
        """Teste l'extraction du temps de réponse d'une sortie de ping."""
        self.assertEqual(
            extraire_temps_ping(
                "64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=5.3 ms"
            ),
            5.3
        )
        self.assertIsNone(extraire_temps_ping("Request timed out"))
    
    def test_enregistrer_resultats(self):
        """Teste l'enregistrement des résultats dans un fichier CSV."""
        donnees_test = [
            ("192.168.1.1", "Active", 5.3),
            ("192.168.1.2", "Inactive", None)
        ]
        enregistrer_resultats("test_resultats.csv", donnees_test)
        with open("test_resultats.csv", "r") as fichier:
            lignes = fichier.readlines()
        self.assertEqual(lignes[1].strip(), "192.168.1.1,Active,5.3")
        self.assertEqual(lignes[2].strip(), "192.168.1.2,Inactive,")

if __name__ == "__main__":
    unittest.main()
