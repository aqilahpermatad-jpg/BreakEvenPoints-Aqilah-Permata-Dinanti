from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    hasil_bep = None
    if request.method == "POST":
        try:
            # Biaya Tetap (Fixed Cost) - cth: sewa gedung, gaji tetap
            fc = float(request.form.get("fixed_cost", 0))
            # Harga Jual per Unit (Price)
            p = float(request.form.get("price", 0))
            # Biaya Variabel per Unit (Variable Cost) - cth: bahan baku
            vc = float(request.form.get("variable_cost", 0))

            if p <= vc:
                hasil_bep = "error_price"
            else:
                # Rumus BEP Unit = FC / (P - VC)
                bep_unit = fc / (p - vc)
                # Rumus BEP Rupiah = BEP Unit * P
                bep_rupiah = bep_unit * p
                # Margin Kontribusi
                margin = p - vc

                hasil_bep = {
                    "unit": bep_unit,
                    "rupiah": bep_rupiah,
                    "margin": margin,
                    "fc": fc
                }
        except:
            hasil_bep = "error_input"

    return render_template("bep.html", hasil=hasil_bep)

if __name__ == "__main__":
    app.run(debug=True)