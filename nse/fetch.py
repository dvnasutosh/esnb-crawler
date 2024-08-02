from dataclasses import asdict
from requests import get
from json import loads

from nse.extract.extract_suggestion_details import extract_suggestions


class Nse:
    def __init__(self) -> None:
        
        self.header = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9,en-IN;q=0.8",
            "cache-control": "max-age=0",
            "if-modified-since": "Sat, 29 Jun 2024 07:40:26 GMT",
            "if-none-match": "\"21ebc49bf7c9da1:0+gzip\"",
            "priority": "u=0, i",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",

            "Referrer-Policy": "strict-origin-when-cross-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        
        self.cookie=get('https://www.nseindia.com',headers=self.header).cookies

    
    def get_suggestions(self,keyword:str):
        req=get(f'https://www.nseindia.com/api/search/autocomplete?q={keyword}',headers=self.header,cookies=self.cookie)

        suggestions=extract_suggestions(loads(req.text))

        return suggestions

    def get_price(self,symbol:str,now:bool=True):
        pass

