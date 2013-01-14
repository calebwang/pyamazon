from mechanize import Browser
import cookielib
import selenium

class AmazonSession:
    url = 'http://www.amazon.com'

    def __init__(self):
        self.br = Browser(factory = mechanize.RobustFactory())
        self.br.set_handle_robots(False)
        self.cj = cookielib.LWPCookieJar()
        self.br.set_cookiejar(self.cj)
        self.ff = selenium.webdriver.Firefox()

    def login_mechanize(self, email, password):
        self.br.open(url)
        self.br.follow_link(text_regex='sign in')
        br.select_form(nr=0)
        br['email'] = email
        br['create'] = '0'
        br['password'] = password

    def login_selenium_ff(self, email, password):
        driver = self.ff
        driver.get(login_url) 
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_name('signIn').submit()
        
