# app.py
from flask import Flask, render_template, redirect, url_for
from Crew_module import Crews

app = Flask(__name__)

# Initialize the list of crews
crews = [
    Crews("Street Kings", 10, True, "1st Place"),
    Crews("Urban Beats", 8, False, "3rd Place"),
    Crews("Rhythm Masters", 12, True, "2nd Place")
]

@app.route('/')
def index():
    # Convert the list of Crews to a list of dictionaries for easy rendering
    crew_info = [crew.display() for crew in crews]
    return render_template('index.html', crews=crew_info)

@app.route('/remove_crew/<int:index>')
def remove_crew(index):
    # Remove the crew that has already performed from the list
    if crews[index].performing:
        del crews[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
