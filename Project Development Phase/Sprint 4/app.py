from flask import Flask,redirect,url_for,request,render_template
from rainfall_prediction import prediction
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/auto-fill',methods=["POST"])
def auto_fill():
    form_data = request.form
    result = prediction(form_data['Location'])
    if result==1:
        return redirect(url_for('rainfall',location=form_data['Location']))
    else:
        return redirect(url_for('no_rainfall',location=form_data['Location']))
    

@app.route('/rain/<location>',methods=["GET"])
def rainfall(location):
    return render_template('rainfall.html',location=location)

@app.route('/no-rain/<location>',methods=["GET"])
def no_rainfall(location):
    return render_template('no_rainfall.html',location=location)


if __name__=="__main__":
    app.run(debug=True)

