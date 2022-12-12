def render(data, props) :
  return {
    "type": "flex",
    "direction": "vertical",
    "scroll": True,
    "spacing": 4,
    "crossAxisAlignment": "center",
    "children": [
      {
        "type": "widget",
        "name": "menu",
      },
      {
        "type": "widget",
        "name": "home"
      }
    ]
  }