'''print a chart'''
import json
from prettytable import PrettyTable
from openastrochart.openAstroVersion import OAS

def dec2deg (dd) :
    '''format days, minutes, seconds as degrees'''
    d = int (dd)
    # The minutes (m) are equal to the integer part of the decimal degrees (dd) minus integer degrees (d) times 60:
    m = int ((dd - d) * 60)
    # The seconds (s) are equal to the decimal degrees (dd) minus integer degrees (d) minus minutes (m) divided by 60 times 3600:
    s = int ((dd - d - m / 60) * 3600)
    return str (d) + 'd ' + str (m) + "' " + str (s) + '"'

def print_chart (data):
    '''print the chart'''
    chart = json.loads (data)
    print ("............ chart for ", chart['chartData']['name']," ............")
    print ("DOB (yyyy-mm-dd hh:mm:ss): ", chart['chartData']['datetime'])
    print ("local timezone: ", chart['chartData']['timezonestr'])
    print ("location: ", chart['chartData']['location'], " countrycode: ", chart['chartData']['countrycode'])
    print ("lattitude: ", chart['chartData']['latitude'], "longitude: ", chart['chartData']['longitude'], " altitude: ", chart['chartData']['altitude'])
    print ("\nplanets and planet signs")
    table = PrettyTable (["i", "planet","planet_sign #", "planet_sign", "planet_degree"])
    table.align["i"]    = "l"
    table.padding_width = 1
    for i, planet in enumerate (OAS.planets):
        table.add_row ([i, planet['label_short'],
                        chart['planets_sign'][i],
                        OAS.zodiac_short[chart['planets_sign'][i]], 
                        dec2deg(float (chart['planets_degree'][i]))])
    print (table)
