import services.apiService as apiService

def run(props, event, api):
    res = apiService.executeQuery(api, "counter", {
        "user": "global"
    })

    counters = res.data
    if (counters.length == 0):
        apiService.createDoc(api, "counter", {
            "count": 0,
            "user": "global"
        })