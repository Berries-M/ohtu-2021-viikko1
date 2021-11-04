import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ota_kaikki_oikein(self):
        self.varasto.lisaa_varastoon(6)

        saatu_maara = self.varasto.ota_varastosta(9)

        # Pitäisi ottaa kaikki, mitä varastossa on.
        self.assertAlmostEqual(saatu_maara, 6)

    def test_ota_kaikki_varasto_tyhja(self):
        self.varasto.lisaa_varastoon(6)

        saatu_maara = self.varasto.ota_varastosta(9)

        # Varaston pitäsi olla tyhjä, kun otetaan kaikki.
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def	test_ota_varastosta_negatiivinen(self):
        self.varasto.lisaa_varastoon(8)
        
        saatu_maara = self.varasto.ota_varastosta(-10)
   	
        # Varaston saldon ei pitäisi muuttua
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_negatiivista_saldoa(self):
        self.varasto.lisaa_varastoon(-10)

        # Varastoon ei negatiivista saldoa
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(15)

        # Varastoon mahtuu vain 10, loput katoaa
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_sopivasti(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(2)

        # Lisäys lasketaan oikein
        self.assertAlmostEqual(self.varasto.saldo, 7)

    def test_init_negatiivinen_varasto(self2):
        self2.varasto = Varasto(-10)
      
        # Yritetään luoda Varastoa, joka negatiivinen.
        self2.assertAlmostEqual(self2.varasto.tilavuus, 0)

    def test_init_negatiivinen_varastouuuuuu(self3):
        self3.varasto = Varasto(10, -8)

        # Yritetään luoda varastoa, jonka alkusaldo negatiivinen
        self3.assertAlmostEqual(self3.varasto.saldo, 0)

    def test_varasto_merkkijonona_oikein(self):
        self.varasto.lisaa_varastoon(5)
        
        # Varasto Stringinä tuoimii oikein
        self.assertAlmostEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")

