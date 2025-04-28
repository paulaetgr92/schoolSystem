from flask import Blueprint, jsonify 

api_dp = Blueprint("api_dp", __name__)

@api_dp.route('/', methods=['GET'])
def api_root(): 
    return jsonify({"message": "API is running"}), 200