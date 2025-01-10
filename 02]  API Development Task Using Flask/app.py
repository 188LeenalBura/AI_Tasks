from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load movies data from a JSON file
def load_movies():
    with open('movies.json', 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    genre = data.get('genre', 'all')
    year = data.get('year', 'all')
    rating = data.get('rating', 'all')
    country = data.get('country', 'all')

    movies = load_movies()
    filtered_movies = []

    for movie in movies:
        if (genre == 'all' or movie['genre'] == genre) and \
           (year == 'all' or movie['year'] == year) and \
           (rating == 'all' or float(movie['rating']) >= float(rating)) and \
           (country == 'all' or movie['country'] == country):
            filtered_movies.append(movie)

    return jsonify(filtered_movies)

@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.json
    movie_title = data.get('movie_title')
    review = data.get('review')

    movies = load_movies()

    for movie in movies:
        if movie['title'] == movie_title:
            movie['reviews'].append(review)

    # Save updated movies to the file
    with open('movies.json', 'w') as file:
        json.dump(movies, file)

    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
