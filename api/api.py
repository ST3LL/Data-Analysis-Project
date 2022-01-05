from flask import Flask, render_template, request
from params import *


app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET', 'POST'])
def home_app():
    return render_template('home.html',
                           dataset=['blocks_classification', 'seoul_bike'])


@app.route("/prediction/", methods=['POST', 'GET'])
def prediction_by_models():
    if request.method == 'POST':
        data = request.form.get('dataset_selected')
        # just the seoul_bike has been implemented here
        if data == 'seoul_bike':
            f1 = float(request.args.get('temperature'))
            f2 = int(request.args.get('hour'))
            f3 = int(request.args.get('seasons'))
            f4 = float(request.args.get('solar_radiation'))
            f5 = int(request.args.get('visibility'))
            f6 = int(request.args.get('month'))
            f7 = float(request.args.get('wind_speed'))
            f8 = int(request.args.get('business_day'))
            # l_significant_features = [f1, f2, f3, f4, f5, f6, f7, f8]
            # prediction = model.predic(l_significant_features)

        return render_template('prediction.html',
                               description=desc_seoul_bike,
                               predict='--> The prediction should be here! <--')


if __name__ == '__main__':
    app.run()
