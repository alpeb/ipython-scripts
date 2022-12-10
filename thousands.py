import numpy as np
import IPython

frm = get_ipython().display_formatter.formatters['text/plain']


def thousands(arg, p, cycle):
    p.text("{:,}".format(arg).replace(",","_"))

frm.for_type(int, thousands)
frm.for_type(float, thousands)

np.set_printoptions(formatter={'int_kind': lambda x: '{:,}'.format(x).replace(',', "_")})

np.set_printoptions(formatter={'float_kind': lambda x: '{:,}'.format(x).replace(',', "_")})

frm = get_ipython().display_formatter.formatters['text/plain']
frm.for_type(int, thousands)
frm.for_type(float, thousands)
