'''Astro Webservice App'''
from flask import Flask, request, jsonify
from flask_cors import CORS
from openastrochart.openAstroChart import openAstroChart

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    '''identify the service'''
    return 'Web Service for OpenAstro v1.1.57'

@app.route('/createchart/', methods=['GET', 'POST'])
def createchart() :
    '''wrapper to create chart'''
    oac   = request.json
    print ('createchart - creating openAstroChart')
    chart = openAstroChart ()
    print ('createchart - importing JSON string to openAstroChart')
    chart.setChartData (oac)
    print ('createchart - calc chart')
    chart.calc ()
    print ('createchart - convert chart back to JSON and return')
    chart_json = chart.getChartToJSON ()
    return jsonify(chart_json)

if __name__ == '__main__':
    app.run(debug=True)
