import services.apiService as apiService
import sys


def run(props, event, api):
    res = apiService.find(api, "counter", {
        "user": "global"
    })

    counters = res.json()

    if (len(counters)  == 0):
        apiService.createDoc(api, "counter", {
            "count": 0,
            "user": "global"
        })