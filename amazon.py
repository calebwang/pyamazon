import mechanize
from bs4 import BeautifulSoup

class AmazonSession:

    def __init__(self):
        self.br = mechanize.Browser(factory = mechanize.RobustFactory())
        self.br.set_handle_robots(False)
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11')]
        self.base_url = 'http://www.amazon.com'

    def get_current_link(self):
        return br.find_link().base_url 

    def login(self, email, password):
        self.email = email
        self.password = password
        self.br.open(self.base_url)
        self.br.follow_link(text_regex='sign in')
        self._handle_login()

    def _handle_login(self):
        self.br.select_form(nr=0)
        self.br['email'] = self.email
        self.br['password'] = self.password
        self.br.submit()
       
    def search(self, key):
        """Searches, returns list of results. 
        Each result is a tuple of form (name, url)
        """
        self.br.open(self.base_url)
        self.br.select_form(name='site-search')
        self.br['field-keywords'] = key 
        res = self.br.submit()
        page = res.read()
        return self.parse_search(page)

    def parse_search(self, page):
        soup = BeautifulSoup(page)
        results = []
        for result in soup.find_all('h3'):
            link = result.a
            if link:
                href = link.get('href') 
                price = soup.find_all(attrs = {'href': href})[2].span.get_text().strip()
                results = results + [(link.get_text(), price, href)]
        return results

    def pretty_search(self, key):
        """Searches, prints pretty list of search results.
        Omits url when displaying results.
        """
        results = self.search(key)
        for key, entry in enumerate(results):
            print key + ', ' + entry[0] + ', ' + entry[1]
        return results

    def view_result(self, search_results, index):
        """Look at result from search result list"""
        br.follow_link(search_results[index][2])

    def lucky_search(self, key):
        """Immediately go to first result for search term"""
        self.view_result(self.search(key), 0)
        
    def _turn_on_one_click(self):
        """If one-click buying is off, turn it on"""
        #link = self.br.find_link('oneClickSignInLinkID') string is the id, iirc
        link = self.br.find_link(text='Sign in')
        if link:
            self.br.follow_link(link)
            self._redirect()

    def _redirect(self):
        """Handles redirects after turning on one-click"""
        link = self.br.find_link(url_regex = 'http://www.amazon.com/gp/_redirect*', nr = 1)
        if link:
            self.br.follow_link(link)
        else:
            self._handle_login()
            self._redirect()

    def get_price(self, url):    
        self.br.open(url)
        price = self.price_this() 
        return price 

    def price_this(self):
        """Gets price of item that session is currently looking at"""
        page = self.br.response().read()
        soup = BeautifulSoup(page)
        price = soup.find('b', attrs = {'class': 'priceLarge'})[0].get_text()
        return price

    def buy(self, url):
        """Buy item at url."""    
        self._handle_buy(url)

    def buy_this(self):
        """Call this if self.br is viewing a product"""  
        self._handle_buy(self.get_current_link())

    def _handle_buy(self, url):
        """Handles transactions"""
        if self.get_current_url != url:
            self.br.open(url)
        self._turn_on_one_click()
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

