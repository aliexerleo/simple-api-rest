from flask import Flask, request, jsonify
from src import query


app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add_movies():

    id = request.json['id']
    title = request.json['title']
    premiere = request.json['premiere']
    country = request.json['country']

    data = (id, title, premiere, country)
    new_movies = query.add_movies(data)
    print(new_movies)
    if new_movies != False:
        return jsonify({'message': 'new movies insert {0}'.format(title)})
    return jsonify({'message': 'Error in insert'})

@app.route('/list_movies', methods=['GET'])
def list_movies():
    all_movies = query.list_movies()

    return jsonify({'data': all_movies})


@app.route('/rename/<int:_id>', methods=['PUT'])
def rename_movies(_id):
    new_title = request.json['new_title']
    if _id and new_title:
        query.reanme_movies(_id, new_title)
        return jsonify({'message':'movie title was change to {0}'.format(new_title)})
    return jsonify({'message': 'Error in rename'})

@app.route('/remove/<int:_id>', methods=['DELETE'])
def remove_movies(_id):
    if _id:
        query.remove_movies(_id)
        return jsonify({'message': 'movie {0} was deleted'.format(_id)})
    return jsonify({'message': 'Error in remove'})

if __name__ == '__main__':
    app.run(debug=True)



