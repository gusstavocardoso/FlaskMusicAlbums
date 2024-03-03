from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from api import albums

albums_bp = Blueprint('albums', __name__)

albums = []

last_id = 0


@albums_bp.route('/albums', methods=['GET'])
def get_albums():
    return jsonify(albums), 200


@albums_bp.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    for album in albums:
        if album['id'] == id:
            return jsonify(album), 200
    return jsonify({'message': 'Album not found!'}), 404


@albums_bp.route('/albums', methods=['POST'])
@jwt_required()
def add_album():
    global last_id

    data = request.get_json()
    global last_id
    album = {
        'id': last_id,
        'banda': data['banda'],
        'album': data['album'],
        'ano': data['ano'],
        'integrantes': data['integrantes']
    }
    albums.append(album)
    last_id += 1
    return jsonify({'message': 'Album added successfully!', 'id': album['id']}), 201


@albums_bp.route('/albums/<int:id>', methods=['PUT'])
@jwt_required()
def update_album(id):
    for i, album in enumerate(albums):
        if album['id'] == id:
            data = request.get_json()
            albums[i] = {
                'id': id,
                'banda': data['banda'],
                'album': data['album'],
                'ano': data['ano'],
                'integrantes': data['integrantes']
            }
            return jsonify({'message': 'Album updated successfully!'}), 200
    return jsonify({'message': 'Album not found!'}), 404


@albums_bp.route('/albums/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_album(id):
    for i, album in enumerate(albums):
        if album['id'] == id:
            del albums[i]
            return jsonify({'message': 'Album deleted successfully!'}), 200
    return jsonify({'message': 'Album not found!'}), 404
