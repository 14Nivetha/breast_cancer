from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np




app = Flask(__name__)

knn = pickle.load(open('model/model.pkl','rb'))

@app.route("/")
def index():
    # locations = sorted(data['details'].unique())
    return render_template('index.html')

@app.route('/classify', methods = ['POST'])
def classify():
    radius_mean = float(request.form.get('radius_mean'))
    perimeter_mean = float(request.form.get('perimeter_mean')) 
    area_mean = float(request.form.get('area_mean'))
    compactness_mean = float(request.form.get('compactness_mean'))
    concave_points_mean = float(request.form.get('concave_points_mean'))
    radius_se = float(request.form.get('radius_se'))
    perimeter_se = float(request.form.get('perimeter_se'))
    area_se = float(request.form.get('area_se'))
    compactness_se= float(request.form.get('compactness_se'))
    concave_points_se= float(request.form.get('concave_points_se'))
    radius_worst= float(request.form.get('radius_worst'))
    perimeter_worst= float(request.form.get('perimeter_worst'))  
    concave_points_worst= float(request.form.get('concave_points_worst'))
    texture_worst= float(request.form.get('texture_worst'))
    area_worst= float(request.form.get('area_worst'))
    concavity_worst=float(request.form.get('concavity_worst'))
    concave_points_worst= float(request.form.get('concave_points_worst'))
    

    sc = StandardScaler()
    inp = [float(x) for x in request.form.values()]
    inp = [np.array(inp)]
    minp = sc.fit_transform(inp)
    res = knn.predict(minp)

   
    return render_template('index.html',  cl_out="It seems to be {}".format("Malignant" if res[0]==1 else "Benign"))



if __name__ == '__main__':
    app.run(debug = True)
