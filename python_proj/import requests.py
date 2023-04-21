import requests


app_id = 730  # L'ID de l'application pour CS:GO
search_query = "case+hardened"  # Laissez vide pour obtenir tous les articles, ou spécifiez une requête pour filtrer les résultats
start = 0  # L'index de départ pour les résultats de la recherche
count = 20  # Le nombre de résultats à récupérer

url = f"https://steamcommunity.com/market/search/render/?query={search_query}&appid={app_id}&start={start}&count={count}&norender=1&sort_column=date&sort_dir=desc"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if data["success"]:
        print(f"Total des articles trouvés : {data['total_count']}")
        print("Derniers articles répertoriés :")

        for item in data["results"]:
            # Vérifiez si l'article a été vendu instantanément ou non
            if "sell_price" in item and item["sell_price"] == 0:
                continue

            print(f"- {item['name']} (ID du marché : {item['hash_name']} (prix : {item['sale_price_text']}))")
    else:
        print("Échec de la récupération des résultats de recherche.")
else:
    print(f"Échec de l'accès à l'API, code d'état : {response.status_code}")
listing_id = item.get("listingid")
asset_id = item.get("assetid")
class_id = item.get("classid")

# Construire l'URL du marché pour cet élément
market_url = f"https://steamcommunity.com/market/listings/{app_id}/{asset_id}-{listing_id}"
print (market_url)