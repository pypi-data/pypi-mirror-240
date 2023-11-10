
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

class Delegator:

    def __init__(self, on_view, on_add, on_update, on_delete, on_get_field_data, application_token):
        self.app = Flask(__name__)
        CORS(self.app)
        self.app.add_url_rule('/', view_func=self.index, methods=['POST'])
        self.on_view = on_view
        self.on_add = on_add
        self.on_update = on_update
        self.on_delete = on_delete
        self.on_get_field_data = on_get_field_data
        self.application_token = application_token


    @cross_origin()
    def index(self):

        request_data = request.get_json()

        if 'application_token' in request_data:

            if self.application_token == request_data['application_token']:

                command = request_data['command']

                if command == 'get_field_data':

                    data, res_code = self.on_get_field_data(request_data)

                elif command == 'add_module_row':

                    data, res_code = self.on_add(request_data)

                elif command == 'update_module_row':

                    data, res_code = self.on_update(request_data)

                elif command == 'delete_module_row':

                    data, res_code = self.on_delete(request_data)

                elif command == 'get_module_row':

                    data, res_code = self.on_view(request_data)

                else:

                    ##UNKNOWN COMMAND##

                    pass
            
            else:

                raise Exception('Unknown application_token')

        
        return jsonify(data), res_code
    

    def start(self):
        self.app.run(threaded=True)
