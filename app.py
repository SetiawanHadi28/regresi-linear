from flask import Flask, render_template, request
import joblib
import numpy as np

# Load model
model = joblib.load("regresi_sleep_stress.pkl")

# Init Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    message = None

    if request.method == "POST":
        try:
            # Ambil input dari form
            sleep_duration = float(request.form["sleep_duration"])

            # Validasi input sesuai range data
            if sleep_duration < 5.8 or sleep_duration > 8.5:
                message = "⚠️ Durasi tidur harus di antara 5.8 - 8.5 jam (sesuai data)."
            else:
                # Prediksi
                pred = model.predict(np.array([[sleep_duration]]))
                prediction = round(pred[0], 2)
        except:
            message = "⚠️ Input tidak valid!"

    return render_template("index.html", prediction=prediction, message=message)

if __name__ == "__main__":
    app.run(debug=True)
