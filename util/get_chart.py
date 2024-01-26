'''get the chart'''
import json
import requests

def get_chart(chart_host, oac):
    '''get chart from oac (in json format)'''
    chart_url = chart_host + '/createchart/'
    print ('creating chart at URL:', chart_url, '\noac: ', json.dumps (oac))
    try:
        res   = requests.post (chart_url, json=oac)
        res.raise_for_status ()
        data  = res.json ()
        chart = json.loads (data)
        return data
    except requests.exceptions.RequestException as err:
        print ("a request exception error: Something Else",err)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:", errh.response.text)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc.response.text)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt.response.text)
    return None