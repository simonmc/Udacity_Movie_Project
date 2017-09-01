import requests

OMDb_path = 'http://www.omdbapi.com/'
apikey = '73cd8d95'

class Movie():
    def __init__(self, title, poster):
        self.title = title
        self.poster = poster
        self.alldata = self.get_info
        self.plot = self.get_info('Plot')
        self.year = self.get_info('Year')
        self.rated = self.get_info('Rated')
        self.poster = self.get_info('Poster')
        
    def get_info(self, querytype):
        response = requests.get(OMDb_path, params = {'apikey':apikey, 't': self.title})
        self.alldata = response.json()
        
        if querytype == "":
            return {self.alldata}
        else:
            return self.alldata.get(querytype)
        
    