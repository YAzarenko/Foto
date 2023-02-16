from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Get a list of all the files in the static folder
    static_folder = os.path.join(app.root_path, 'static')
    files = os.listdir(static_folder)

    # Filter the list to only include jpg files
    jpg_files = [f for f in files if f.endswith('.jpg')]

    # Choose a random jpg file
    random_file = random.choice(jpg_files)

    # Serve the index.html file, passing in the path to the randomly selected jpg
    return render_template('index.html', image_path=os.path.join('/static', random_file))

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    app.run()