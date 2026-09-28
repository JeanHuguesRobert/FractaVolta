from .model import Producer, Station, Buffer

# Corsican Hubs & Fast-Charging Stations (Urban demand centers)
STATIONS = [
    Station("S_BIA", "Bastia", 9.4509, 42.6973, 2800, 0.65),
    Station("S_AJA", "Ajaccio", 8.7386, 41.9192, 2500, 0.65),
    Station("S_CRT", "Corte", 9.1490, 42.3094, 1500, 0.55),
    Station("S_PV", "Plaine Orientale", 9.2795, 41.5910, 1800, 0.75),
]

# Fixed Hub (Centralized scenario: single central buffer at Corte)
FIXED_HUB = Buffer("H0", "Hub Central Corte", 9.1490, 42.3094, 3000)

# Mobile Buffers (Distributed regional containers near production clusters)
MOBILE_BUFFERS = {
    "Bastia": Buffer("B_BIA", "Bastia", 9.4400, 42.5200, 3000),             # Casamozza
    "Ajaccio": Buffer("B_AJA", "Ajaccio", 8.7700, 41.9600, 3000),           # Mezzavia
    "Corte": Buffer("B_CRT", "Corte", 9.1490, 42.3094, 3000),               # Corte
    "Plaine Orientale": Buffer("B_PO", "Plaine Orientale", 9.5100, 42.1100, 3000),  # Cateraggio / Aléria
}

# 12 representative Corsican solar production nodes across the 4 clusters
PRODUCERS = [
    # Bastia cluster
    Producer("P01_Casalta", "Bastia", 9.4200, 42.4200, 420, 0.085, 0.100),
    Producer("P02_Borgo", "Bastia", 9.4300, 42.5500, 260, 0.090, 0.100),
    Producer("P03_Pieve", "Bastia", 9.2900, 42.5800, 310, 0.075, 0.100),
    # Corte cluster
    Producer("P04_Corte", "Corte", 9.1500, 42.3100, 520, 0.092, 0.100),
    Producer("P05_Venaco", "Corte", 9.1700, 42.2300, 340, 0.080, 0.100),
    Producer("P06_PonteLeccia", "Corte", 9.2100, 42.4600, 280, 0.088, 0.100),
    # Plaine Orientale cluster
    Producer("P07_Tallone", "Plaine Orientale", 9.4800, 42.2300, 600, 0.090, 0.100),
    Producer("P08_Aleria", "Plaine Orientale", 9.5100, 42.1100, 450, 0.095, 0.105),
    Producer("P09_Ventiseri", "Plaine Orientale", 9.4000, 41.9300, 360, 0.082, 0.100),
    # Ajaccio cluster
    Producer("P10_Afa", "Ajaccio", 8.8000, 41.9800, 300, 0.080, 0.100),
    Producer("P11_Bastelicaccia", "Ajaccio", 8.8200, 41.9300, 380, 0.090, 0.105),
    Producer("P12_Peri", "Ajaccio", 8.8600, 42.0100, 260, 0.075, 0.095),
]

# Road Corridors (lon, lat) along primary Corsican routes
CORRIDOR_T20 = [
    (8.7386, 41.9192),  # Ajaccio centre
    (8.7700, 41.9600),  # Mezzavia
    (8.9100, 42.0200),  # Tavera
    (8.9800, 42.0800),  # Bocognano
    (9.1100, 42.1200),  # Col de Vizzavona
    (9.1700, 42.1700),  # Vivario
    (9.1700, 42.2300),  # Venaco
    (9.1490, 42.3094),  # Corte
    (9.1600, 42.3600),  # Soveria
    (9.2100, 42.4600),  # Ponte-Leccia
    (9.4400, 42.5200),  # Casamozza
    (9.4300, 42.6300),  # Biguglia
    (9.4509, 42.6973),  # Bastia centre
]

CORRIDOR_T10 = [
    (9.4400, 42.5200),  # Casamozza (jonction T20/T10)
    (9.5000, 42.4500),  # Folelli
    (9.5300, 42.3700),  # Moriani-Plage
    (9.5400, 42.2600),  # Cervione
    (9.5100, 42.1100),  # Aléria / Cateraggio
    (9.4100, 42.0200),  # Ghisonaccia
    (9.4000, 41.8600),  # Solenzara
    (9.3500, 41.7000),  # Sainte-Lucie-de-Porto-Vecchio
    (9.2795, 41.5910),  # Porto-Vecchio centre
]

CORRIDOR_T50 = [
    (9.1490, 42.3094),  # Corte centre
    (9.2300, 42.2800),  # Favalello
    (9.2800, 42.2600),  # Erbajolo
    (9.3900, 42.1800),  # Antisanti bas
    (9.5100, 42.1100),  # Cateraggio / Aléria (jonction T10)
]

CORRIDORS = {
    "T20 (Ajaccio–Corte–Bastia)": CORRIDOR_T20,
    "T10 (Bastia–Aléria–Porto-Vecchio)": CORRIDOR_T10,
    "T50 (Corte–Aléria)": CORRIDOR_T50,
}
