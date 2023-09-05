#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getopt, sys
import requests
import json
import openastromod.importfile as importfile
from openastrochart.openAstroVersion import OAS
from prettytable import PrettyTable

def dec2deg (dd) :
	d = int (dd)
	# The minutes (m) are equal to the integer part of the decimal degrees (dd) minus integer degrees (d) times 60:
	m = int ((dd - d) * 60)
	# The seconds (s) are equal to the decimal degrees (dd) minus integer degrees (d) minus minutes (m) divided by 60 times 3600:
	s = int ((dd - d - m / 60) * 3600)
	return str (d) + 'd ' + str (m) + "' " + str (s) + '"'



chartHost = 'https://open-astro-web-service-ilhgu4omwq-uk.a.run.app';
#chartHost = 'http://localhost:5000'

def printChartFromDictionary (chart) :
	print ("............ chart for ", chart['chartData']['name']," ............")
	print ("DOB (yyyy-mm-dd hh:mm:ss): ", chart['chartData']['datetime'])
	print ("local timezone: ", chart['chartData']['timezonestr'])
	print ("location: ", chart['chartData']['location'], " countrycode: ", chart['chartData']['countrycode'])
	print ("lattitude: ", chart['chartData']['latitude'], "longitude: ", chart['chartData']['longitude'], " altitude: ", chart['chartData']['altitude'])
	print ("\nplanets and planet signs")
	table = PrettyTable (["i", "planet","planet_sign #", "planet_sign", "planet_degree"])
	table.align["i"]    = "l"
	table.padding_width = 1 
	for i in range (len (OAS.planets)) :
		table.add_row ([i, OAS.planets[i]['label_short'],
						chart['planets_sign'][i], 
						OAS.zodiac_short[chart['planets_sign'][i]], 
						dec2deg(float (chart['planets_degree'][i]))])
	print (table)
	return

# get the chart using the OAC data in 'filename'
def getChart (filename) :
	oac      = importfile.getOAC(filename)
	chartURL = chartHost + '/createchart/'
	print ('creating chart at URL:', chartURL, '\noac: ', json.dumps (oac[0]))
	data = None
	try:
		res   = requests.post (chartURL, json=oac[0])
		res.raise_for_status ()
		data  = res.json ()
		chart = json.loads (data)
		printChartFromDictionary (chart)
	except requests.exceptions.RequestException as err:
		print ("OOps: Something Else",err)
	except requests.exceptions.HTTPError as errh:
		print ("Http Error:", errh.response.text)
	except requests.exceptions.ConnectionError as errc:
		print ("Error Connecting:", errc.response.text)
	except requests.exceptions.Timeout as errt:
		print ("Timeout Error:",errt.response.text)
	return data

def getChartUsingJSON () :
	oac = {"name":"dan at yahoo",
		   "datetime":"1960-12-26 15:00:00",
		   "location":"queens, ny, usa",
		   "latitude":"40.7135078",
		   "longitude":"-73.8283132",
		   "countrycode":"us",
		   "timezone":"-5",
		   "altitude":0,
		   "geonameid":5368361,
		   "timezonestr":"America/New_York"};
	
	chartURL = chartHost + '/createchart/'
	print ('creating chart at URL:', chartURL, '\noac: ', json.dumps (oac))
	data = None
	try:
		res   = requests.post (chartURL, json=oac)
		res.raise_for_status ()
		data  = res.json ()
		chart = json.loads (data)
		printChartFromDictionary (chart)
	except requests.exceptions.RequestException as err:
		print ("OOps: Something Else",err)
	except requests.exceptions.HTTPError as errh:
		print ("Http Error:", errh.response.text)
	except requests.exceptions.ConnectionError as errc:
		print ("Error Connecting:", errc.response.text)
	except requests.exceptions.Timeout as errt:
		print ("Timeout Error:",errt.response.text)
	return data

def main (argv) :
	# setup valid options for command line
	unixOpt   = "f:"
	gnuOpt    = ["file="]
	#try:
	#	arguments, values = getopt.getopt(sys.argv[1:], unixOpt, gnuOpt)
	#except getopt.error as err :
	#	# output error, and return with an error code
	#	print (str(err))
	#	print ('usage invokeService -f <input oac file name>')
	#	sys.exit(2)

	#filename = None
	
	match_data = {}

	src_file   = './test/Joanne_Woodward.oac'
	# extract commmand line arguments
	
	#for arg, val in arguments :
	#	if arg in ("-f", "--file") :
	#		filename = val

	match_data['src'] = getChart (src_file)
	match_data['src'] = getChartUsingJSON ()

if __name__ == '__main__':
	main(sys.argv[1:])
