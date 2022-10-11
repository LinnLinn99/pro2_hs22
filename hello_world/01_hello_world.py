from flask import Flask
from flask import render_template
import random

app = Flask("Hello World")


@app.route("/greet_all")
def greet_all():
    auswahl = ["Linda", "Fabian", "Michael", "Robin"]
    return render_template('hello_all.html', alle_namen=auswahl)

@app.route('/hello')
def hello_world():
    fruits = ["Bananen", "Äpfel", "Birnen", "Beeries"]
    ausgewaelte_fruits = random.choice(fruits)
    return render_template('fruits.html', name=ausgewaelte_fruits)


@app.route('/hallo')
@app.route('/hallo/<name>')
def hallo_welt(name="Welt"):
    return f'Hallo, {name}!'

@app.route('/add/<zahl_0>')
def add(zahl_0=0):
    return f'{int(zahl_0) +3}!'

zahl_1 = 5
zahl_2 = 10



if __name__ == "__main__":
    app.run(debug=True, port=5000)


