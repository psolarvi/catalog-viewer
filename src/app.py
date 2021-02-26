import json
import os
from flask import abort, Flask, jsonify
from markupsafe import escape

app = Flask(__name__)

DATA_FOLDER = escape(os.environ.get('DATA_FOLDER', 'data'))
ERROR_RESPONSE = int(os.environ.get('ERROR_RESPONSE', 404))

def sortByTimestamp(element):
  return element['timestamp']

@app.errorhandler(404)
def topicNotFound(error):
    return "Unable to find the specific category", 404

@app.route('/catalog/<string:category>')
def getElementsForCategory(category):
    try:
        with open('./%s/%s.json' % (DATA_FOLDER, escape(category))) as categoryFile:
            return jsonify(json.load(categoryFile))
        
    except IOError:
        abort(ERROR_RESPONSE)
