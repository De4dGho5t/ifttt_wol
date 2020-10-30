from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import send_wol as sw

app = Flask(__name__)
api = Api(app)

devices = { "pc": {"mac_address": "40:8D:5C:10:7D:EF"},
            "nas": {"mac_address": "24:5E:BE:2F:FE:44"} }


device_args = reqparse.RequestParser()
device_args.add_argument("device_name", type=str, help="Name of the device is required", required=True)
device_args.add_argument("operation", type=str, help="Name of the operation is required", required=True)


def abort_if_device_not_exists(device_name):
    if device_name not in devices:
        abort(404, message="Device not found.")

class wol(Resource):
    def post(self):
        args = device_args.parse_args()
        abort_if_device_not_exists(args['device_name'])

        if args['operation'] == "up":
            sw.send_packet(devices[args['device_name']]['mac_address'])
        else:
            abort(501, message="Operation not implemented.")

        return [args['device_name'],args['operation'],devices[args['device_name']]['mac_address']]

api.add_resource(wol, "/wol")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)