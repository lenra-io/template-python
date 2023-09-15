def render(data, props) :
  return {
    "_type": "container",
    "decoration": {
      "color": 0xFFFFFFFF,
      "boxShadow": {
        "blurRadius": 8,
        "color": 0x1A000000,
        "offset": {
          "dx": 0,
          "dy": 1
        }
      },
    },
    "padding": {
      "top": 16,
      "bottom": 16,
      "left": 32,
      "right": 32,
    },
    "child": {
      "_type": "flex",
      "fillParent": True,
      "mainAxisAlignment": "spaceBetween",
      "crossAxisAlignment": "center",
      "padding": { "right": 32 },
      "children": [
        {
          "_type": "container",
          "constraints": {
            "minWidth": 32,
            "minHeight": 32,
            "maxWidth": 32,
            "maxHeight": 32,
          },
          "child": {
            "_type": "image",
            "src": "logo.png"
          },
        },
        {
          "_type": "flexible",
          "child": {
            "_type": "container",
            "child": {
              "_type": "text",
              "value": "Hello World",
              "textAlign": "center",
              "style": {
                "fontWeight": "bold",
                "fontSize": 24,
              },
            }
          }
        }
      ]
    },
  }