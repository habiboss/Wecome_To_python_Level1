from typing import type_check_only
import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metaData"]:
        print(theJSON["metaData"]["title"])

    count = theJSON["metaData"]["count"]
    print(str(count) + "events recorded")

    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("-------------------")

    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
            
    print("event that were felt")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"],
                "reported" + str(feltReports) + "times")
def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5"

    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getCode()))

    if (webUrl.getCode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Receivd error, cannot parse results")

if __name__ == "__main__":
    main()