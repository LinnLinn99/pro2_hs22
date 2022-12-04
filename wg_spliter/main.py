from flask import Flask
from flask import render_template, url_for, redirect
from flask import request
import plotly.express as px
import plotly

from wg_spliter.funktionen import mitbewohnerdaten_oeffnen

app = Flask("wg_spliter")


@app.route("/")
def startseite():
    todos = mitbewohnerdaten_oeffnen()
    # todos_html = todos.replace("\n", "<br>")
    # todo_liste = ["1,2", "3,4"]
    # neue_liste = []
    # for eintrag in todo_liste:
    #     print("eintrag:", eintrag)
    #     aufgabe, deadline = eintrag.split(",")
    #     neue_liste.append([aufgabe, deadline])
    #     print(neue_liste)
    return render_template("index.html")

@app.route("/eintrag", methods=["GET", "POST"])
def finanz_eintrag():
    if request.method == "GET":
        return render_template("finanz_eintrag.html")
        # Verknüpfung zum html

    if request.method == "POST":
        nebenkosten = request.form['nebenkosten']
        wocheneinkauf = request.form['wocheneinkauf']
        kueche = request.form['kueche']
        bad = request.form['bad']
        divers = request.form['divers']
        betrag = request.form['betrag']
        bezeichnung = request.form['bezeichnung']
        print(f"Request Form Nebenkosten: {nebenkosten}")
        print(f"Request Form Wocheneinkauf: {wocheneinkauf}")
        print(f"Request Form Küche: {kueche}")
        print(f"Request Form Bad: {bad }")
        print(f"Request Form Divers: {divers}")
        print(f"Request Form Betrag CHF: {betrag}")
        print(f"Request Form Bezeichnung: {bezeichnung}")
        finanz_eintrag_speichern(nebenkosten, wocheneinkauf, kueche, bad, divers, bezeichnung, betrag)
        return "yes es funktioniert, dein Eintrag wurde hinzugefügt"



@app.route("/uebersicht")
def uebersicht():
    return render_template("uebersicht.html")
def grafik():
    return render_template("uebersicht.html", barchart=div, seitentitel="Piechart")


@app.route("/archiv")
def archiv():
    return render_template("archiv.html")


@app.route("/mitglied", methods=["GET", "POST"])
def neuer_eintrag_mitglied():
    if request.method == "GET":
        return render_template("neuer_eintrag_mitglied.html")
    # Die Verknüpfung zum html

    if request.method == "POST":
        notgood = request.form['notgood']
        geschlecht = request.form['gender']
        erstellt = request.form['erstellt']
        alter = request.form['alter']
        print(f"Request Form Unverträglichkeit: {notgood}")
        print(f"Request Form Geschlecht: {geschlecht}")
        print(f"Request Form Erstellt am: {erstellt}")
        print(f"Request Form Alter: {alter}")
        erfassen_speichern(notgood, geschlecht, erstellt, alter)
        return "yes es funktioniert dein Eintrag wurde hinzugefügt"


if __name__ == "__main__":
    app.run(debug=True, port=5001)




