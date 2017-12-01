revAPI = ["http://store.steampowered.com/appreviews/",
            "?json=1&start_offset="]
getRev( appID, numB ):
    for i in range(numB):
        revAPI[0]+str(appID)+revAPI[1]+str(i*20)

get



