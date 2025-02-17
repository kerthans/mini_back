from flask import jsonify, request
from . import api_v1

@api_v1.route('/site-borrow', methods=['GET'])
def get_site_bookings():
    return jsonify({"message": "Get all site bookings"})

@api_v1.route('/site-borrow', methods=['POST'])
def book_site():
    data = request.get_json()
    return jsonify({"message": "Book site", "data": data}), 201

@api_v1.route('/site-borrow/<int:booking_id>', methods=['DELETE'])
def cancel_booking(booking_id):
    return jsonify({"message": f"Cancel booking {booking_id}"}), 204

@api_v1.route('/site-borrow/available', methods=['GET'])
def get_available_sites():
    return jsonify({"message": "Get available sites"})
