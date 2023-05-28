import requests
import os

url = "https://www.torrentleech.me/torrents/browse/list/facets/tags%3AFREELEECH/added/-1%20day/orderby/completed/order/desc"

headers = {'cookie': 'xxxxxxxxxxxxxxx'}

response = requests.request("GET", url, headers=headers, data={}).json()

for torrent in response_json["torrentList"]:
    fid = torrent["fid"]
    filename = torrent["filename"]
    seeders = torrent['seeders']
    leechers = torrent['leechers']
    if leechers*10 > seeders:
        print(f"p: {leechers} s: {seeders}")
        response = requests.request("GET", f"https://www.torrentleech.me/download/{fid}/{filename}", headers=headers, data={})
        with open(f"/tmp/{filename}", 'wb') as f:
            f.write(response.content)
        os.system(f"transmission-remote -a /tmp/{filename}")
