import services.apiService as apiService

def run(props, event, api):
    res = apiService.find(api, "counter", {
        "user": "@me"
    })

    counters = res.json()
    if (len(counters) == 0):
        apiService.createDoc(api, "counter", {
            "count": 0,
            "user": "@me"
        })