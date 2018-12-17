from robobrowser import RoboBrowser
import re
#browser = RoboBrowser(history=True, parser='html.parser')
BASE_URL = "https://badoo.com{}"
#for a in browser.find_all("a", {"rel":"profile-view"}):
#    print(a)

class BadooApi:

    def __init__(self):
        self.browser = RoboBrowser(history=True, parser='html.parser')
        self.browser.open(BASE_URL.format("/es/contactos/spain/zaragoza/zaragoza/"))

    def next_page(self):
        btns = self.browser.find_all(class_ =re.compile(r".*btn.*btn--xsm.*btn--transparent.*js-pages.*"))
        try:
            print(BASE_URL.format(btns[1]['href']))
            self.browser.open(BASE_URL.format(btns[1]['href']))
        except:
            print(BASE_URL.format(btns[0]['href']))
            self.browser.open(BASE_URL.format(btns[0]['href']))

    def extract_users(self):
        for a in self.browser.find_all("a", {"rel":"profile-view"}):
            print(a)

badoo_api = BadooApi()
badoo_api.next_page()
badoo_api.extract_users()
badoo_api.next_page()
badoo_api.extract_users()
badoo_api.next_page()
badoo_api.extract_users()
