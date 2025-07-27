from flask import Flask, request, render_template
from datetime import datetime
import requests

app = Flask(__name__)

BACKEND_URL = 'http://127.0.0.1:9000'


@app.route('/')
def home():
    day_of_week = datetime.today().strftime("%A")
    currentTime = datetime.now().strftime("%H:%M:%S")
    print("this is current date and time (This is commit from new branch)")
    return render_template('index.html', day_of_week=day_of_week, currentTime=currentTime)


@app.route('/submit', methods=['POST'])
def submit():
    data = dict(request.form)

    requests.post(BACKEND_URL + '/submit', json=data)
    return 'Data submitted nicely'


@app.route('/get_data')
def get_data():
    respose = requests.get(BACKEND_URL + '/view')
    # print(respose.json)
    return respose.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
