from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import send_wol as sw

app = Flask(__name__)
api = Api(app)

devices = { "pc": {"mac_address": "24:5E:BE:2F:FE:44"},
            "nas": {"mac_address": "40:8D:5C:10:7D:EF"} }

operations = { "up": {"device": "up"},
               "down": {"device": "down"} }


def abort_if_device_not_exists(device_name):
    if device_name not in devices:
        abort(404, message="Device not found.")

def abort_if_operation_not_exists(operation_name):
    if operation_name not in operations:
        abort(404, message="Operation not found.")

class wol(Resource):
    def post(self, device_name, operation_name):
        abort_if_device_not_exists(device_name)
        abort_if_operation_not_exists(operation_name)

        if operation_name == "up":
            sw.send_packet(devices[device_name]['mac_address'])
        elif operation_name == "down":
            abort(501, message="Operation not implemented.")

        return operations[operation_name]

api.add_resource(wol, "/wol/<string:device_name>/<string:operation_name>")

if __name__ == "__main__":
    app.run(debug=False)