import app_lib_python.utils.api as Api

def run(props, event, api):
    res = api.DataApi.executeQuery(api, "counter", {
        "user": "@me"
    })

    counters = res.json()
    if (len(counters) == 0):
        api.DataApi.createDoc(api, "counter", {
            "count": 0,
            "user": "@me"
        })