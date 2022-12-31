# Celine Phan
# CIS41B
# Lab0 - Data Acquisition

from bs4 import BeautifulSoup
from collections import defaultdict
import requests

import FileStream
import Parser
import Database
import Output


def default():
    return "N/A"


def main():
    # request html file from web
    fs = FileStream.FileStream('https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions')
    data = fs.retrieve_data()

    # parse html and format the soup
    p = Parser.Parser(data)
    p.format()

    # create lists for country and emissions column
    lists = p.parseTable()
    emissionsList = lists[0]
    countryList = lists[1]

    # create dict and load lists into dict
    countryEmissions = defaultdict(default)
    dataDict = Database.Database(countryEmissions)
    dataDict.load_dict(countryList, emissionsList)

    # output dict to screen
    printer = Output.Output(dataDict)
    printer.displayDict()


main()
