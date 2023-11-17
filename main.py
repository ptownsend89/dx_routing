import CreateScript
import flask
from flask import Flask, request, jsonify, redirect
import CreateScript as c
import RunScript as r


app = Flask(__name__)

#we have incoming json payload with 'dxvar' key set to route we want to take
#once we evaluate route run relevant function
#function will run/create a bash script which sets env vars and runs the correct program based on the dxvar route

#relevant json could be:
#dxvar (was/is - OPTION on normal dx calls)
#action - e.g. PAY or REFUND?
#paytype
#address1
#address2, etc.
#cardholdername
#email/phone
#logname
#environment - e.g. PRODUCTION / DEV


@app.route('/redirecting', methods=['POST'])
def redirect_call():
    try:
        find_json = {}
        form_req = {}
        form_req = dict(request.form)
        find_json = jsonify(form_req)
        dx_route = find_json.get_json().get('option')
        c = CreateScript.CreateScript()
        call_script = c.get_create_script(dx_route)
        if call_script != 'Script create fail':
            return call_script
    except Exception as e:
        return jsonify([{'Error': str(e)}])


if __name__ == '__main__':
    app.run(debug=True)