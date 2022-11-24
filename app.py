from flask import Flask
import json
import os
from flask import json
# from agentpy_IntersectioSimulation.ipynb import *
app = Flask(__name__)


@app.route("/", methods=['GET'])
def simulationJson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = SITE_ROOT + "/positions.json"

    data = json.load(open(json_url))
    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )

    return response


if __name__ == '__main__':
    app.run()
