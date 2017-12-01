from urllib.request import urlopen
import json
from collections import defaultdict

revAPI = ["http://store.steampowered.com/appreviews/",
            "?json=1&start_offset="]
def parse(fname):
    for l in urlopen(fname):
        yield json.loads(url.read().decode())
def getRev( appID, numB ):
    revs = []
    dets = dict()
    for i in range(numB):
        url = revAPI[0]+str(appID)+revAPI[1]+str(i*20)
        batch = json.loads(urlopen(url).read())
        revs.extend(batch['reviews'])
        if i == 0:
            dets = batch['query_summary']

    return (revs,dets)

appIds = [ int(x) for x in list(open('appIdsPopular')) ] 
reviews = dict()
for a in appIds:
    reviews[a] = getRev(a,50)

with open('steam.json', 'wb') as outfile:
    json.dump(reviews, outfile)
