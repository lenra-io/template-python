def render(data, props) :
  return {
    "_type": "flex",
    "direction": "vertical",
    "scroll": True,
    "spacing": 4,
    "crossAxisAlignment": "center",
    "children": [
      {
        "_type": "view",
        "name": "menu",
      },
      {
        "_type": "view",
        "name": "home"
      }
    ]
  }