from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    
    if request.method == "POST":
        
        clf = pickle.load(open("model.pkl", 'rb'))
        
        X1 = request.form.get("X1")
        X2 = request.form.get("X2")
        X3 = request.form.get("X3")
        X4 = request.form.get("X4")
        X6 = request.form.get("X6")
        X7 = request.form.get("X7")
        CASINO = request.form.get("CASINO")
        AUCHAN = request.form.get("AUCHAN")
        CARREFOUR = request.form.get("CARREFOUR")
        LECLERC = request.form.get("LECLERC")
        GEANT = request.form.get("GEANT")
        INTERMARCHE = request.form.get("INTERMARCHE")
        CORA = request.form.get("CORA")
        CARREFOUR_MARKET = request.form.get("CARREFOUR MARKET")
        SUPER_U = request.form.get("SUPER U")
        SIMPLY_MARKET = request.form.get("SIMPLY MARKET")
        MONOPRIX = request.form.get("MONOPRIX")
        MATCH = request.form.get("MATCH")
        MARCHE_U = request.form.get("MARCHE U")
        HYPER_U = request.form.get("HYPER U")
        PRISUNIC = request.form.get("PRISUNIC")
        ECOMARCHE = request.form.get("ECOMARCHE")
        FRANPRIX = request.form.get("FRANPRIX")
        OTHERS = request.form.get("OTHERS")
        SHOPI = request.form.get("SHOPI")

        X = pd.DataFrame([[X1, X2, X3, X4, X6, X7, CASINO, AUCHAN, CARREFOUR, LECLERC, GEANT, INTERMARCHE, CORA, CARREFOUR_MARKET, SUPER_U, SIMPLY_MARKET, MONOPRIX, MATCH, MARCHE_U, HYPER_U, PRISUNIC, ECOMARCHE, FRANPRIX, OTHERS, SHOPI]], 
        columns = ['X1', 'X2', 'X3', 'X4', 'X6', 'X7', 'AUCHAN', 'CARREFOUR', 'CARREFOUR MARKET', 'CASINO', 'CORA', 'ECOMARCHE', 'FRANPRIX', 'GEANT', 'HYPER U', 'INTERMARCHE', 'LECLERC', 'MARCHE U', 'MATCH', 'MONOPRIX', 'OTHERS', 'PRISUNIC', 'SHOPI', 'SIMPLY MARKET', 'SUPER U'])

        if clf.predict(X)[0] == 1 : 
            prediction = "Display"
        else : 
            prediction = "Not Display"
        
    else:
        prediction = ""
        
    return render_template("index.html", output = prediction)

if __name__ == '__main__':
    app.run(debug = True)