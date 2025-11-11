import os
import json
import requests

logo = r"""
/  |                          /  |                  /      |/       \ 
$$ |        ______    ______  $$ |   __             $$$$$$/ $$$$$$$  |
$$ |       /      \  /      \ $$ |  /  |              $$ |  $$ |__$$ |
$$ |      /$$$$$$  |/$$$$$$  |$$ |_/$$/               $$ |  $$    $$/ 
$$ |      $$ |  $$ |$$ |  $$ |$$   $$<                $$ |  $$$$$$$/  
$$ |_____ $$ \__$$ |$$ \__$$ |$$$$$$  \              _$$ |_ $$ |      
$$       |$$    $$/ $$    $$/ $$ | $$  |            / $$   |$$ |      
$$$$$$$$/  $$$$$$/   $$$$$$/  $$/   $$/             $$$$$$/ $$/       
"""

print(logo)

# Czyszczenie ekranu w zależności od systemu
if os.name == "nt":
    os.system("cls")


# Pobranie IP od użytkownika
ip = input("Podaj IP: ")

# Wysłanie zapytania do API
r = requests.get(f"http://ip-api.com/json/{ip}")
data = r.json()

# Wyświetlenie wyników
print("\n=== Anserw ===\n")
print(f"Status: {data.get('status', 'No data')}")
print(f"Country: {data.get('country', 'No data')}")
print(f"Country code: {data.get('countryCode', 'No data')}")
print(f"Region: {data.get('region', 'No data')}")
print(f"RegionName: {data.get('regionName', 'No data')}")
print(f"City: {data.get('city', 'No data')}")
print(f"ISP: {data.get('isp', 'No data')}")
print(f"Timezone: {data.get('timezone', 'No data')}")
print(f"Lat: {data.get('lat', 'No data')}")
print(f"Lon: {data.get('lat', 'No data')}")
print(f"Org: {data.get('org', 'No data')}")
print(f"As: {data.get('as', 'No data')}")

