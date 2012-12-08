from mechanize import Browser
import cookielib
import selenium

class AmazonSession:
    login_url = 'https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dgno_signin'

    def __init__(self):
        self.br = Browser(factory = mechanize.RobustFactory())
        self.br.set_handle_robots(False)
        self.cj = cookielib.LWPCookieJar()
        self.br.set_cookiejar(self.cj)
        self.ff = selenium.webdriver.Firefox()

    def login_mechanize(self, email, password):
        self.br.open(login_url)
        br.select_form(nr=0)
        br['email'] = email
        br['password'] = password

    def login_selenium_ff(self, email, password):
        driver = self.ff
        driver.get(login_url) 
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_name('signIn').submit()
        
