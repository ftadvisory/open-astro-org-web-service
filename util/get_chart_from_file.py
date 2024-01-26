from util.get_chart import get_chart
from openastromod import importfile

def get_chart_from_file (host_name, filename) :
    '''get the chart using the OAC data in 'filename'''
    oac      = importfile.getOAC(filename)
    return get_chart(host_name, oac)
