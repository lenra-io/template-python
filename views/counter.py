def render(data, counter) :
  return {
    "type": "flex",
    "spacing": 2,
    "mainAxisAlignment": "spaceEvenly",
    "crossAxisAlignment": "center",
    "children": [
      {
        "type": "text",
        "value": counter["text"] +": "+ str(data[0]["count"])
      },
      {
        "type": "button",
        "text": "+",
        "onPressed": {
          "action": "increment",
          "props": {
            "id": data[0]["_id"],
          }
        }
      }
    ]
  }