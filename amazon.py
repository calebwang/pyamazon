import mechanize
from bs4 import BeautifulSoup

url = 'http://www.amazon.com'

class AmazonSession:

    def __init__(self):
        self.br = mechanize.Browser(factory = mechanize.RobustFactory())
        self.br.set_handle_robots(False)
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11')]

    def get_current_link(self):
        return br.find_link().base_url 

    def login(self, email, password):
        self.email = email
        self.password = password
        self.br.open(url)
        self.br.follow_link(text_regex='sign in')
        self.handle_login()

    def handle_login(self):
        self.br.select_form(nr=0)
        self.br['email'] = self.email
        self.br['password'] = self.password
        self.br.submit()
       
    def search(self, key):
        self.br.open(url)
        self.br.select_form(name='site-search')
        self.br['field-keywords'] = key 
        res = self.br.submit()
        page = res.read()
        soup = BeautifulSoup(page)
        results = []
        for result in soup.find_all('h3'):
            link = result.a
            if link:
                results = results + [(link.get_text(), link.get('href'))]
        return results 

    def goto_result(self, search_results, index):
        br.follow_link(search_results[index][1])

    def lucky(self, key):
        self.goto_result(self.search(key), 0)
        
    def turn_on_one_click(self):
        #link = self.br.find_link('oneClickSignInLinkID')
        link = self.br.find_link(text='Sign in')
        if link:
            self.br.follow_link(link)
            self.redirect()

    def redirect(self):
            link = self.br.find_link(url_regex = 'http://www.amazon.com/gp/redirect*', nr = 1)
            if link:
                self.br.follow_link(link)
            else:
                self.handle_login()
                self.redirect()

    
    def buy_current(self):
        """Call this if self.br is viewing a product"""  
        self.handle_buy(self.get_current_link())

    def handle_buy(self, link):
        if self.get_current_link != link:
            self.br.open(link)
        self.br.select_form(name='handleBuy')
        try:
            req = self.br.form.click(id='oneClickBuyButton')
        except:
            try:
                req = self.br.form.click(id='buyButton')
            except:
                print "Unknown error occured."
                return
        br.open(req)

