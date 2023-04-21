import requests

app_id = 730  # ID de l'application pour CS:GO
listing_url = f"https://steamcommunity.com/market/recent?country=FR&language=french&currency=3&appid={app_id}"

response = requests.get(listing_url)

if response.status_code == 200:
    data = response.text

    # Recherchez le début de la section contenant les articles les plus récents listés
    start_index = data.find("market_recent_listing_table")
    if start_index != -1:
        start_index = data.find("<tbody>", start_index)
        end_index = data.find("</tbody>", start_index)

        # Récupérez les données de la section
        section_data = data[start_index:end_index]

        # Analysez les données pour extraire les articles les plus récents listés
        article_start_index = section_data.find("<tr>")
        while article_start_index != -1:
            article_end_index = section_data.find("</tr>", article_start_index)
            article_data = section_data[article_start_index:article_end_index]

            # Extrayez le nom et le prix de l'article
            name_start_index = article_data.find("market_listing_item_name")
            name_end_index = article_data.find("</span>", name_start_index)
            name = article_data[name_start_index:name_end_index].split(">")[-1].strip()

            price_start_index = article_data.find("market_listing_price_with_fee")
            price_end_index = article_data.find("</span>", price_start_index)
            price = article_data[price_start_index:price_end_index].split(">")[-1].strip()

            # Affichez le nom et le prix de l'article
            print(f"{name} - {price}")

            # Trouvez le début de l'article suivant
            article_start_index = section_data.find("<tr>", article_end_index)

    else:
        print("Échec de la récupération des informations sur le marché.")
else:
    print(f"Échec de l'accès à l'API, code d'état : {response.status_code}")
