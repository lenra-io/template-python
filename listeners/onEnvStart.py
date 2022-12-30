import services.apiService as apiService
import sys


def run(props, event, api):
    res = apiService.executeQuery(api, "counter", {
        "user": "global"
    })

    counters = res.json()

    if (len(counters)  == 0):
        print("passsssssssssssssss", file=sys.stderr)

        apiService.createDoc(api, "counter", {
            "count": 0,
            "user": "global"
        })