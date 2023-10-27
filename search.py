import re

def imgurl(str):
    str = str.replace("'", "")
    str = str.replace("[", "")
    str = str.replace("]", "")
    return str.replace("'", "")

def category_process(str):
    space = "'CDs & Vinyl',"
    s = str.replace(space,"")
    return s
