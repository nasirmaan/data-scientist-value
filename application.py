from flask import Flask, render_template, request
import requests
import json

application = Flask(__name__)

@application.route('/')
@application.route('/index')
def home():
    #counting the quantity of objects on S3 bucket
    url = 'https://hvscyggpte.execute-api.us-west-2.amazonaws.com/default/OSI_LTD_MODEL'
    r = requests.get(url).json()

    return render_template('index.html')


@application.route('/score', methods=['POST', 'GET'])
def score():
    if request.method == 'POST':
        # get result from form and treat it
        input_json = request.form

        print(input_json)

        # create header and url
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = 'https://hvscyggpte.execute-api.us-west-2.amazonaws.com/default/OSI_LTD_MODEL'

        # make POST request and load response
        r = requests.post(url, params=input_json, headers=header).json()
        #print(r)
        #result = json.loads(r)

        # render the html template sending the variables
        return render_template("score.html", score=r['score'], proba=0.9)


if __name__ == '__main__':
    application.run(debug=True)





