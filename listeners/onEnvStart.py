import app_lib_python.utils.api as Api
import sys


def run(props, event, api:Api):
    res = api.DataApi.executeQuery(api, "counter", {
        "user": "global"
    })

    counters = res.json()

    if (len(counters)  == 0):
        api.DataApi.createDoc(api, "counter", {
            "count": 0,
            "user": "global"
        })