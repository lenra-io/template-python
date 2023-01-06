def render(data, props) :
  return {
    "type": "flex",
    "direction": "vertical",
    "scroll": True,
    "spacing": 4,
    "crossAxisAlignment": "center",
    "children": [
      {
        "type": "view",
        "name": "menu",
      },
      {
        "type": "view",
        "name": "home"
      }
    ]
  }