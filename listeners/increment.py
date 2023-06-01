import lenra_app_lib.utils.api as Api

def run(props, event, api:Api):
    res = api.DataApi.getDoc(api, "counter", props["id"])
    counter = res.json()
    counter["count"] += 1
    api.DataApi.updateDoc(api, "counter", counter)
    return {}