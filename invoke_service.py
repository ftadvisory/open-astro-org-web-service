'''test the service'''
import sys
from openastromod import importfile
from util.get_chart import get_chart
from util.print_chart import print_chart


#CHART_HOST = 'https://open-astro-web-service-ilhgu4omwq-uk.a.run.app';
CHART_HOST = 'http://localhost:5050'
# import getopt

def main (argv) :
    '''main function'''
    # setup valid options for command line
    #unixOpt   = "f:"
    #gnuOpt    = ["file="]
    #try:
    #	arguments, values = getopt.getopt(sys.argv[1:], unixOpt, gnuOpt)
    #except getopt.error as err :
    #	# output error, and return with an error code
    #	print (str(err))
    #	print ('usage invokeService -f <input oac file name>')
    #	sys.exit(2)
    oac = {"name":"dan at yahoo",
           "datetime":"1990-3-15 15:00:00",
           "location":"queens, ny, usa",
           "latitude":"40.7135078",
           "longitude":"-73.8283132",
           "countrycode":"us",
           "timezone":"-5.0",
           "altitude":"0",
           "geonameid":"5368361",
           "timezonestr":"America/New_York"}
    match_data_from_json = get_chart(CHART_HOST, oac)
    print_chart(match_data_from_json)
    #filename = None
    src_file = './data/Joanne_Woodward.oac'
    # extract commmand line arguments  
    #for arg, val in arguments :
    #	if arg in ("-f", "--file") :
    #		filename = val
    oac = importfile.getOAC(src_file)
    match_data_from_file = get_chart (CHART_HOST, oac[0])
    if match_data_from_file is not None:
        print_chart(match_data_from_file)

if __name__ == '__main__':
    main(sys.argv[1:])
