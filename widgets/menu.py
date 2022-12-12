def render(data, props) :
  return {
    "type": "container",
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
      "top": 2,
      "bottom": 2,
      "left": 4,
      "right": 4,
    },
    "child": {
      "type": "flex",
      "fillParent": True,
      "mainAxisAlignment": "spaceBetween",
      "crossAxisAlignment": "center",
      "padding": { "right": 4 },
      "children": [
        {
          "type": "container",
          "constraints": {
            "minWidth": 32,
            "minHeight": 32,
            "maxWidth": 32,
            "maxHeight": 32,
          },
          "child": {
            "type": "image",
            "src": "logo.png"
          },
        },
        {
          "type": "flexible",
          "child": {
            "type": "container",
            "child": {
              "type": "text",
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