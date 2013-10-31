import urllib, json, time, datetime
url = "http://apify.heroku.com/api/olympics2012_medals.json"

while True:
    json_response = urllib.urlopen(url).read()
    medal_counts = json.loads(json_response)

    now = datetime.datetime.now()
    print "Updated at: " + str(datetime.time(now.hour, now.minute, now.second))

    _canada = False
    for medal in medal_counts:
        if( medal["country"] == "Canada" ):
            _canada = True
        print medal["country"] + " has " + medal["gold"] + " golds " + medal["silver"] + " silvers " + medal["bronze"] + " bronzes."
    time.sleep(2)
