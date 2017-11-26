from flask import *
from .classifier import classifier

api = Blueprint('api', __name__)


@api.route('/api/v1/getClassification', methods=['GET'])
def classifyGig():
	print("I AM HERE")
	data = request.get_json()
	entry = data['post_entry']
	print("ENTRY:\t", entry)
	classification = classifier.predict([entry])
	print("CLASSIFICATION:\t", classification)
	return jsonify(str(classification), 200)
