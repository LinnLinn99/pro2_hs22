from flask import Flask
from flask import render_template
from flask import request

import plotly.express as px
from plotly.offline import plot

from todoloo.datenbank import abspeichern, auslesen, todos_laden

app = Flask("todoloo")


@app.route("/")
def start():
    todos = todos_laden()
    return render_template("index.html", liste=todos, seitentitel="start")



@app.route("/add", methods=["GET", "POST"])
def add_new_todo():
    if request.method == "GET":
        return render_template("todo_form.html", seitentitel="start")
    # Die Verknüpfung zum html

    if request.method == "POST":
        aufgabe = request.form['aufgabe']
        deadline = request.form['deadline']
        print(f"Request Form Aufgabe: {aufgabe}")
        print(f"Request Form Deadline: {deadline}")
        abspeichern(aufgabe, deadline)
        return "yes funktioniert"

@app.route("/viz")
def grafik():
    todos = todos_laden()
    deadlines ={}
    for todo in todos:
        if todo[1] not in deadlines:
            deadlines[todo[1]] = 1
        else:
            deadlines[todo[1]] += 1

    x = deadlines.keys()
    y = deadlines.values()
    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")

    return render_template("viz.html", barchart=div, seitentitel="Piechart")



if __name__ == "__main__":
    app.run(debug=True, port=5001)


