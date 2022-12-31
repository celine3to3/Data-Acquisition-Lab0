from bs4 import BeautifulSoup

class Parser:
    def __init__(self, data):
        self.data = data
        self.soup = BeautifulSoup(self.data.text, "html.parser")
        self.table = self.soup.find('table', {"class": 'wikitable sortable'})

    def format(self):
        self.soup.prettify()

    def parseTable(self):
        table_data = []
        wiki_table = self.table.find_all("td")
        for data in wiki_table:
            data.get('td')
            table_data.append(data.text)
        length = len(table_data)
        emissions_list = table_data[4:length:10]
        country_list = table_data[0:length:10]
        return emissions_list, country_list