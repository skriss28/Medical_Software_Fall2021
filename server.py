from flask import Flask, request, jsonify
from Blood_Calculator import HDL_Analysis

app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def server_status():
    return "Server is on"


@app.route("/info", methods=["GET"])
def info():
    my_output = "This server is for BME 547"
    return my_output


@app.route("/hdl/<HDL_Value>", methods=["POST"])
def hdl_analysis_server(HDL_Value):
    """
    Input should look like {"hdl": 50, "patient_id": 200}

    :return:
    """
    # in_data = request.get_json()
    # hdl_value = in_data["hdl"]
    hdl_value = int(HDL_Value)
    print("The hdl_value is {}".format(hdl_value))
    answer = HDL_Analysis(hdl_value)
    return jsonify(answer), 201


@app.route("/say_hello/<input_name>", methods=["GET"])
def say_hello(input_name):
    return "Hello, {}".format(input_name)


if __name__ == '__main__':
    app.run()
