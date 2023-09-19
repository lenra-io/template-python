import services.apiService as apiService

def run(props, event, api):
    apiService.updateMany(api, "counter", { '_id': props["id"] }, { '$inc': { 'count': 1 } })
    return {}