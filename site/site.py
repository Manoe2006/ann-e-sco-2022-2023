from flask import Flask, render_template, request, redirect, url_for
import os
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and file.filename.endswith('.csv'):
        filename = 'points.csv'
        file.save(os.path.join('uploads', filename))
        # Appelez les fonctions de votre programme ici
        # nuagedepts()
        # polygone()
        return redirect(url_for('results'))
    else:
        return "Erreur: Veuillez télécharger un fichier CSV."

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
