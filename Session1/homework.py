from flask import Flask, redirect, render_template
app = Flask(__name__)


@app.route('/school')
def redirectt():
    return redirect("http://techkids.vn",code=302)

@app.route('/ex23')
def ex23():
    return render_template("index.html")

@app.route('/bmi')
def bmi():
    return render_template("bmi.html")

@app.route('/<txtMass>/<txtHeight>')
def bmians(txtMass,txtHeight):
    Height=int(txtHeight)/100
    BMI=int(txtMass)/(Height**2)
    return "Your BMI is"+str(BMI)

@app.route('/pex1')
def pex1():
    return render_template("pex1.html")

@app.route('/pex2')
def pex2():
    return render_template("pex2.html")

if __name__ == '__main__':
    app.run(debug=True)
