from flask import Flask
from flask import render_template, url_for, redirect
from flask import request
import plotly.express as px
from plotly import plot

from wg_spliter.funktionen import mitbewohnerdaten_oeffnen, finanz_eintrag_speichern, \
    datenbank_finanzeintragdaten_oeffnen
from wg_spliter.funktionen import erfassen_speichern

app = Flask("wg_spliter")


@app.route("/")
def startseite():
    return render_template("index.html")


@app.route("/eintrag", methods=["GET", "POST"])
def finanz_eintrag():
    if request.method == "GET":
        mitbewohner = mitbewohnerdaten_oeffnen()
        mitbewohner = mitbewohner.keys()
        return render_template("finanz_eintrag.html", mitbewohner_gespeichert=mitbewohner)  # Verknüpfung zum html

    if request.method == "POST":
        nebenkosten = request.form.get('nebenkosten')
        wocheneinkauf = request.form.get('wocheneinkauf')
        kueche = request.form.get('kueche')
        bad = request.form.get('bad')
        divers = request.form.get('divers')
        betrag = float(
            request.form.get('betrag'))
        bezeichnung = request.form.get('bezeichnung')
        date_gekauft = request.form.get('date_gekauft')
        mitbewohner = request.form.getlist("mitbewohner")
        betrag_pro_person = betrag / len(mitbewohner)  # Betrag / anzahl Mitbewohner
        for person in mitbewohner:
            finanz_eintrag_speichern(
                nebenkosten,
                wocheneinkauf,
                kueche,
                bad,
                divers,
                bezeichnung,
                betrag_pro_person,
                date_gekauft,
                person
            )  # was ist falsch??
        return render_template("finanz_eintrag.html",
                               finanzen_gespeichert=finanz_eintrag_speichern)  # was gebe ich hier weiter?


@app.route("/uebersicht")
def uebersicht():
    # uebersicht.html wird generiert und die Variable finanzen_gespeichert werden mitgegeben
    finanzen_gespeichert = datenbank_finanzeintragdaten_oeffnen()
    if request.method == "GET":
        return render_template("uebersicht.html", seitentitel="uebersicht")
    if request.method == "POST":
        nebenkosten = request.form['nebenkosten']
        wocheneinkauf = request.form['wocheneinkauf']
        kueche = request.form['kueche']
        bad = request.form['bad']
        divers = request.form['divers']
        print(request.form.to_dict())
        ergebnis = finanzen_gespeichert(nebenkosten,wocheneinkauf,kueche,bad,divers)
    return render_template("uebersicht.html", ergebnis=ergebnis)


def grafik():
    mitbewohner = mitbewohnerdaten_oeffnen()
    schulden = {}
    for person in mitbewohner:
        if person["betrag_pro_person"] not in schulden:
            schulden[person["betrag_pro_person"]] = 1
        else:
            schulden[person["betrag_pro_person"]] += 1

    x = schulden.keys()
    y = schulden.values()
    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")
    if request.method == "GET":
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
        erfassen_speichern(notgood, geschlecht, erstellt, alter)
        return "yes es funktioniert dein Eintrag wurde hinzugefügt"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
