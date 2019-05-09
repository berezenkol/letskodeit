from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

#each page class should inherit from selenium_driver and put in () SeleniumDriver
#after inheritance we create super(LoginPage,self).__init__(driver) under def __inti__
class LoginPage(SeleniumDriver):
    def __init__(self,driver):   # we are putting driver because all our actions from the test will be moved to page class(driver instance is coming from the test)
        super(LoginPage,self).__init__(driver)
        self.driver = driver

    # 1. We create the Locators used at this page in one place

    # Locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'

    # 2. We define separate method for each Locator in order to expose the Locators into webelements,
    #after that thsese webelements might be utilized in any number of methods

    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)
    def getEmailField(self):
        return self.driver.find_element_by_id(self._email_field)
    def getPasswordField(self):
        return self.driver.find_element_by_id(self._password_field)
    def getLoginButton(self):
        return self.driver.find_element(By.NAME, self._login_button)

    # 3. We will create methods for actions which are to be performed on the elements

    def clickLoginLink(self):
        self.getLoginLink().click()
    def enterEmail(self,username):
        self.getEmailField().send_keys(username)
    def enterPassword(self,password):
        self.getPasswordField().send_keys(password)
    def clickLoginButton(self):
        self.getLoginButton().click()


    # 0. Define the login code

    def login(self,username = '',password = ''):     # username = '',password = '' -this way we make these arguments as optional, by default - empty

        # After steps 1-3 are performed, the below code is gonna be optimised

        # login_link = self.driver.find_element(By.LINK_TEXT, 'Login')
        # login_link.click()
        self.clickLoginLink()
        # email_field = self.driver.find_element_by_id('user_email')
        # email_field.send_keys(username)
        self.enterEmail(username)
        # password_field = self.driver.find_element_by_id('user_password')
        # password_field.send_keys(password)
        self.enterPassword(password)
        # login_button = self.driver.find_element(By.NAME, 'commit')
        # login_button.click()
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.is_element_present('//input[@id = "search-courses"]',byType= 'xpath')
        return result

    def verifyLoginFailed(self):
        error_result = self.is_element_present('//div[@class ="alert alert-danger"]',byType= 'xpath')
        return error_result


    #It is not the best way
        # my_courses = self.driver.find_element(By.XPATH, '//input[@id = "search-courses"]')
        #
        # if my_courses is not None:
        #     print('Login successful')
        # else:
        #     print('Login failed')
