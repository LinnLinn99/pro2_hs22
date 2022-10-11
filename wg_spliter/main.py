from flask import Flask
from flask import render_template
from flask import request

from todoloo.datenbank import abspeichern, auslesen

app = Flask("wg_spliter")


@app.route("/")
def start():
    todos = auslesen()
    todos_html = todos.replace("\n", "<br>")
    todo_liste = todos.split("\n")
    neue_liste = []
    for eintrag in todo_liste:
        aufgabe, deadline = eintrag.split(",")
        neue_liste.append([aufgabe, deadline])
        print(neue_liste)
    return render_template("index.html", liste=neue_liste)



@app.route("/add", methods=["GET", "POST"])
def add_new_todo():
    if request.method == "GET":
        return render_template("startseite_form.html")
    # Die Verknüpfung zum html

    if request.method == "POST":
        aufgabe = request.form['aufgabe']
        deadline = request.form['deadline']
        print(f"Request Form Aufgabe: {aufgabe}")
        print(f"Request Form Deadline: {deadline}")
        abspeichern(aufgabe, deadline)
        return "yes funktioniert"


if __name__ == "__main__":
    app.run(debug=True, port=5001)




