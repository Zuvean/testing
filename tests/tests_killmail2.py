from killmail2 import Killmail2
from tests.setup import Setup


class TestKillmail(Setup):

    def setUp(self):
        super().setUp()
        self.k00 = Killmail2(self.uk00)
        self.k30 = Killmail2(self.uk30)
        self.k70 = Killmail2(self.uk70)

    def test_id(self):
        self.assertEqual(71443648, self.k00.id, "Wrong id")
        self.assertEqual(71933840, self.k30.id, "wrong id")
        self.assertEqual(72012818, self.k70.id, "wrong id")

    def test_time(self):
        self.assertEqual("2018-07-24T17:56:14Z", self.k00.time, "wrong time")
        self.assertEqual("2018-08-18T11:39:49Z", self.k30.time, "wronge time")
        self.assertEqual("2018-08-22T10:41:01Z", self.k70.time, "wronge time")


class TestKillmailValue(TestKillmail):

    def test_total_value(self):
        self.assertEqual(7521431.46, self.k00.value_total, "Wrong ISK Amount")
        self.assertEqual(227289291.33, self.k30.value_total, "wrong isk amount")
        self.assertEqual(71262264.86, self.k70.value_total, "wrong isk amount")

    def test_fitted_value(self):
        self.assertEqual(2543013.41, self.k00.value_fitted, "Wrong ISK Amount")
        self.assertEqual(65084309.91, self.k30.value_fitted, "wrong isk amount")
        self.assertEqual(10593294.36, self.k70.value_fitted, "wrong isk amount")

    def test_ship_value(self):
        self.assertEqual(7521431.46 - 2543013.41, self.k00.value_ship, "Wrong ISK Amount")
        self.assertEqual(227289291.33 - 65084309.91, self.k30.value_ship, "wrong isk amount")
        self.assertEqual(71262264.86 - 10593294.36, self.k70.value_ship, "wrong isk amount")


class TestKillmailFinalBlow(TestKillmail):

    def test_final_blow_damage(self):
        self.assertEqual(4110, self.k00.final_blow_damage, "Wrong damage")
        self.assertEqual(778, self.k30.final_blow_damage, "wrong damage")
        self.assertEqual(1002, self.k70.final_blow_damage, "wrong damage")

    def test_final_blow_damage_percent(self):
        self.assertEqual(100, self.k00.final_blow_damage_percent, "Wrong percentage")
        self.assertEqual(45, self.k30.final_blow_damage_percent, "wrong percentage")
        self.assertEqual(48, self.k70.final_blow_damage_percent, "wrong percentage")

    def test_final_blow_ship_id(self):
        self.assertEqual(605, self.k00.final_blow_ship_id, "Wrong ship id")
        self.assertEqual(29990, self.k30.final_blow_ship_id, "wrong ship id")
        self.assertEqual(33470, self.k70.final_blow_ship_id, "wrong ship id")

    def test_final_blow_ship_name(self):
        self.assertEqual("Heron", self.k00.final_blow_ship_name, "Wrong Ship Name")
        self.assertEqual("Loki", self.k30.final_blow_ship_name, "wrong ship name")
        self.assertEqual("Stratios", self.k70.final_blow_ship_name, "wrong ship name")

    def test_final_blow_ship_group_id(self):
        self.assertEqual("25", self.k00.final_blow_ship_group_id, "Wrong Group id")
        self.assertEqual("963", self.k30.final_blow_ship_group_id, "wrong group id")
        self.assertEqual("26", self.k70.final_blow_ship_group_id, "Wrong Group id")

    def test_final_blow_ship_group_name(self):
        self.assertEqual("Frigate", self.k00.final_blow_ship_group_name, "Wrong group name")
        self.assertEqual("Strategic Cruiser", self.k30.final_blow_ship_group_name, "wrong group name")
        self.assertEqual("Cruiser", self.k70.final_blow_ship_group_name, "Wrong group name")


class TestKillmailGeographic(TestKillmail):

    def test_solar_system_id(self):
        self.assertEqual(30003681, self.k00.solar_system_id, "wrong id")
        self.assertEqual(30000142, self.k30.solar_system_id, "wrong id")
        self.assertEqual(31000153, self.k70.solar_system_id, "wrong id")

    def test_solar_system_name(self):
        self.assertEqual("DO6H-Q", self.k00.solar_system_name, "wrong name")
        self.assertEqual("Jita", self.k30.solar_system_name, "wrong name")
        self.assertEqual("J113820", self.k70.solar_system_name, "wrong name")

    def test_solar_system_security(self):
        self.assertEqual(-0.3, self.k00.solar_system_security, "wrong float")
        self.assertEqual(0.9, self.k30.solar_system_security, "wrong float")
        self.assertEqual(-1.0, self.k70.solar_system_security, "wrong float")

    def test_solar_system_class(self):
        self.assertEqual("nullsec", self.k00.solar_system_class, "wrong name")
        self.assertEqual("highsec", self.k30.solar_system_class, "wrong name")
        self.assertEqual("wormhole", self.k70.solar_system_class, "wrong name")

    def test_region_id(self):
        self.assertEqual(10000046, self.k00.region_id, "wrong id")
        self.assertEqual(10000002, self.k30.region_id, "wrong id")
        self.assertEqual(11000002, self.k70.region_id, "wrong id")

    def test_region_name(self):
        self.assertEqual("Fade", self.k00.region_name, "wrong name")
        self.assertEqual("The Forge", self.k30.region_name, "wrong name")
        self.assertEqual("A-R00002", self.k70.region_name, "wrong name")

    def test_constellation_id(self):
        self.assertEqual(20000536, self.k00.constellation_id, "wrong id")
        self.assertEqual(20000020, self.k30.constellation_id, "wrong id")
        self.assertEqual(21000002, self.k70.constellation_id, "wrong id")

    def test_constellation_name(self):
        self.assertEqual("XFLN-F", self.k00.constellation_name, "wrong name")
        self.assertEqual("Kimotoro", self.k30.constellation_name, "wrong name")
        self.assertEqual("A-C00002", self.k70.constellation_name, "wrong name")


class TestKillmailVictim(TestKillmail):

    def test_victim_damage_taken(self):
        self.assertEqual(4110, self.k00.victim_damage_taken, "wrong int")
        self.assertEqual(1737, self.k30.victim_damage_taken, "wrong int")
        self.assertEqual(2087, self.k70.victim_damage_taken, "wrong int")

    def test_victim_name_ids(self):
        self.assertEqual([99007362, 2114300996, 98531953], self.k00.victim_name_ids, "wrong ids")
        self.assertEqual([2113228085, 98446928, 99003581], self.k30.victim_name_ids, "wrong ids")

    def test_victim_names(self):
        self.assertEqual([{"category": "character", "id": 2114300996, "name": "Assassin Jx"},
                          {"category": "corporation", "id": 98531953, "name": "Rainbow Pegasus Squadron"},
                          {"category": "alliance", "id": 99007362, "name": "Ranger Regiment"}],
                         self.k00.victim_names, "wrong names")
        self.assertEqual([{"category": "character", "id": 2113228085, "name": "Omae Kumiko"},
                          {"category": "corporation", "id": 98446928, "name": "Setcreasea Pallida Corporation"},
                          {"category": "alliance", "id": 99003581, "name": "Fraternity."}],
                         self.k30.victim_names, "wrong names")
        self.assertEqual([{"category": "character", "id": 2112516399, "name": "Dmitry Ismagilov"},
                          {"category": "corporation", "id": 1000180, "name": "State Protectorate"}],
                         self.k70.victim_names, "wrong names")

    def test_victim_char_name(self):
        self.assertEqual("Assassin Jx", self.k00.victim_char_name, "wrong name")
        self.assertEqual("Omae Kumiko", self.k30.victim_char_name, "wrong name")
        self.assertEqual("Dmitry Ismagilov", self.k70.victim_char_name, "wrong name")

    def test_victim_corp_name(self):
        self.assertEqual("Rainbow Pegasus Squadron", self.k00.victim_corp_name, "wrong name")
        self.assertEqual("Setcreasea Pallida Corporation", self.k30.victim_corp_name, "wrong name")
        self.assertEqual("State Protectorate", self.k70.victim_corp_name, "wrong name")

    def test_victim_alliance_name(self):
        self.assertEqual("Ranger Regiment", self.k00.victim_alliance_name, "wrong name")
        self.assertEqual("Fraternity.", self.k30.victim_alliance_name, "wrong name")
        self.assertEqual("", self.k70.victim_alliance_name, "wrong name")

    def test_victim_ship_id(self):
        self.assertEqual(32878, self.k00.victim_ship_id, "wrong id")
        self.assertEqual(33468, self.k30.victim_ship_id, "wrong id")
        self.assertEqual(33468, self.k70.victim_ship_id, "wrong id")

    def test_victim_ship_name(self):
        self.assertEqual("Talwar", self.k00.victim_ship_name, "wrong name")
        self.assertEqual("Astero", self.k30.victim_ship_name, "wrong name")
        self.assertEqual("Astero", self.k70.victim_ship_name, "wrong name")

    def test_victim_ship_group_id(self):
        self.assertEqual(420, self.k00.victim_ship_group_id, "wrong id")
        self.assertEqual(25, self.k30.victim_ship_group_id, "wrong id")
        self.assertEqual(25, self.k70.victim_ship_group_id, "wrong id")

    def test_victim_ship_group_name(self):
        self.assertEqual("Destroyer", self.k00.victim_ship_group_name, "wrong name")
        self.assertEqual("Frigate", self.k30.victim_ship_group_name, "wrong name")
        self.assertEqual("Frigate", self.k70.victim_ship_group_name, "wrong name")


class TestKillmailAttacker(TestKillmail):

    def test_attacker_is_solo(self):
        self.assertEqual(True, self.k00.attacker_is_solo, "wrong bool")
        self.assertEqual(False, self.k30.attacker_is_solo, "wrong bool")
        self.assertEqual(False, self.k70.attacker_is_solo, "wrong bool")

    def test_attacker_is_npc(self):
        self.assertEqual(False, self.k00.attacker_is_npc, "wrong bool")
        self.assertEqual(False, self.k30.attacker_is_npc, "wrong bool")
        self.assertEqual(False, self.k70.attacker_is_npc, "wrong bool")

    def test_attacker_is_awox(self):
        self.assertEqual(False, self.k00.attacker_is_awox, "wrong  bool")
        self.assertEqual(False, self.k30.attacker_is_awox, "wrong  bool")
        self.assertEqual(False, self.k70.attacker_is_awox, "wrong  bool")

    def test_attacker_amount(self):
        self.assertEqual(1, self.k00.attacker_amount, "wrong int")
        self.assertEqual(2, self.k30.attacker_amount, "wrong int")
        self.assertEqual(2, self.k70.attacker_amount, "wrong int")

    def test_attacker_name_ids(self):
        pass

    def test_attacker_names(self):
        self.assertEqual([{"category": "character", "id": 992181402, "name": "Strife Senior"},
                          {"category": "corporation", "id": 1324429368, "name": "NED-Clan"},
                          {"category": "alliance", "id": 1354830081, "name": "Goonswarm Federation"}],
                         self.k00.attacker_names, "wrong names")
        self.assertEqual([{"category": "character", "id": 224182597, "name": "Shotgun Pimp"},
                          {"category": "corporation", "id": 818601383, "name": "The Reappropriation"},
                          {"category": "alliance", "id": 99005382, "name": "Jita Holding Inc."},
                          {"category": "character", "id": 91715917, "name": "Ailiece Ardua"},
                          {"category": "corporation", "id": 98567437, "name": "HC - georgieboys"}],
                         self.k30.attacker_names, "wrong names")
        self.assertEqual([{"category": "character", "id": 94830824, "name": "VorSunder Vampyra"},
                          {"category": "corporation", "id": 98539465, "name": "Voracious Vikings of Valor"},
                          {"category": "character", "id": 95074071, "name": "Jagreen Doshu"},
                          {"category": "corporation", "id": 98389109, "name": "Old Rotten Tomatoes"}],
                         self.k70.attacker_names, "wrong names")

    def test_attacker_char_names(self):
        self.assertEqual(";Strife Senior;", self.k00.attacker_char_names, "wrong name")
        self.assertEqual(";Shotgun Pimp;Ailiece Ardua;", self.k30.attacker_char_names, "wron name")
        self.assertEqual(";VorSunder Vampyra;Jagreen Doshu;", self.k70.attacker_char_names, "wron name")

    def test_attacker_corp_names(self):
        self.assertEqual(";NED-Clan;", self.k00.attacker_corp_names, "wrong name")
        self.assertEqual(";The Reappropriation;HC - georgieboys;", self.k30.attacker_corp_names, "wrong name")
        self.assertEqual(";Voracious Vikings of Valor;Old Rotten Tomatoes;", self.k70.attacker_corp_names, "wrong name")

    def test_attacker_alliance_names(self):
        self.assertEqual(";Goonswarm Federation;", self.k00.attacker_alliance_names, "wrong name")
        self.assertEqual(";Jita Holding Inc.;", self.k30.attacker_alliance_names, "wrong name")
        self.assertEqual("", self.k70.attacker_alliance_names, "wrong name")

    def test_attacker_ship_ids(self):
        self.assertEqual([605], self.k00.attacker_ship_id, "wrong ids")
        self.assertEqual([29990], self.k30.attacker_ship_id, "wrong ids")
        self.assertEqual([22456, 33470], self.k70.attacker_ship_id, "wrong ids")

    def test_attacker_ship_names(self):
        self.assertEqual(";Heron;", self.k00.attacker_ship_names, "wrong names")
        self.assertEqual(";Loki;", self.k30.attacker_ship_names, "wrong names")
        self.assertEqual(";Sabre;Stratios;", self.k70.attacker_ship_names, "wrong names")

    def test_attacker_ship_group_ids(self):
        self.assertEqual([25], self.k00.attacker_ship_group_ids, "wrong ids")
        self.assertEqual([963], self.k30.attacker_ship_group_ids, "wrong ids")
        self.assertEqual([541, 26], self.k70.attacker_ship_group_ids, "wrong ids")

    def test_attacker_ship_group_names(self):
        self.assertEqual(";Frigate;", self.k00.attacker_ship_group_names, "wrong names")
        self.assertEqual(";Strategic Cruiser;", self.k30.attacker_ship_group_names, "wrong names")
        self.assertEqual(";Interdictor;Cruiser;", self.k70.attacker_ship_group_names, "wrong names")
