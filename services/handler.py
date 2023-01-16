import os
import json
from http.server import BaseHTTPRequestHandler

WIDGET_MAP = {
    "root": "root_widget",
    "home": "home_widget"
}

LISTENER_MAP = {
    "onEnvStart": "on_env_start",
    "onUserFirstJoin": "on_user_first_join",
    "onSessionStart": "on_session_start"
}

RESOURCE_TYPE = "resource"
LISTENER_TYPE = "listener"
WIDGET_TYPE = "widget"
MANIFEST_TYPE = "manifest"


class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        req_type = self.get_req_type()

        if req_type == RESOURCE_TYPE:
            self.handle_resource()
        elif req_type == LISTENER_TYPE:
            self.handle_listener()
        elif req_type == WIDGET_TYPE:
            self.handle_widget()
        elif req_type == MANIFEST_TYPE:
            self.handle_manifest()
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Middleware type unknown.")

    def get_req_type(self):
        """Determines the type of request based on the request body"""
        if self.command != "POST":
            return "none"
        elif self.headers.get("resource"):
            return RESOURCE_TYPE
        elif self.headers.get("listener"):
            return LISTENER_TYPE
        elif self.headers.get("widget"):
            return WIDGET_TYPE
        else:
            return MANIFEST_TYPE

    def handle_manifest(self):
        """Handles manifest requests"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        widgets = []
        for widget_key in WIDGET_MAP:
            widgets.append(WIDGET_MAP[widget_key])

        listeners = []
        for listener_key in LISTENER_MAP:
            listeners.append(LISTENER_MAP[listener_key])

        root_widget = WIDGET_MAP["root"]

        response = {
            "widgets": widgets,
            "listeners": listeners,
            "rootWidget": root_widget
        }

    def handle_widget(self):
        """Handles view requests"""
        widget_name = self.headers.get("view")
        widget_func = WIDGET_MAP.get(widget_name)

        if widget_func:
            data = self.headers.get("data")
            props = self.headers.get("props")
            context = self.headers.get("context")

            result = widget_func(data, props, context)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def handle_listener(self):
        """Handles listener requests"""
        listener_name = self.headers.get("listener")
        listener_func = LISTENER_MAP .get(listener_name)

        if listener_func:
            props = self.headers.get("props")
            event = self.headers.get("event")
            api = self.headers.get("api")

            result = listener_func(props, event, api)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def handle_resource(self):
        """Handles resource requests"""
        resources_path = "./resources/"

        resource = self.headers.get("resource")
        if resource.endswith((".jpeg", ".jpg", ".png", ".gif", ".webp", ".bmp", ".wbmp")):
            self.send_response(200)
            self.send_header("Content-type", "application/octet-stream")
            self.send_header("Content-Disposition", f'attachment; filename="{resource}"')
            self.end_headers()
            with open(f"{resources_path}/{resource}", "rb") as resource_file:
                self.wfile.write(resource_file.read())
        else:
            self.send_response(404)
            self.end_headers()