"""Takes degrees minutes seconds coordinates and returns them in decimal degrees

"""
import pyperclip
def dms_to_dd(d, m, s):
    dd = d + float(m)/60 + float(s)/3600
    return dd