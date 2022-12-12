def run(props, event, api):
    res = apiService.getDoc(api, "counter", props.id)
    counter = res.data
    counter.count += 1
    apiService.updateDoc(api, "counter", counter)
    return {}