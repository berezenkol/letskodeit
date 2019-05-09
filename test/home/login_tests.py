import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from pages.home.login_page import LoginPage


class LoginTest(unittest.TestCase):
    @pytest.mark.run(order=2)                           # this way to mark the order of test run
    def test_validlogin(self):
        baseURL = 'https://letskodeit.teachable.com/'
        driver = webdriver.Chrome(executable_path=r'C:\Users\Liudmila\PycharmProjects\letskodeit\browsers_drivers\chromedriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login('test@email.com', 'abcabc')

        # my_courses = driver.find_element(By.LINK_TEXT,'My Courses')
        #
        # if my_courses is not None:
        #     print('Login successful')
        # else:
        #     print('Login failed')

        result = lp.verifyLoginSuccessful()
        # assert result == True
    @pytest.mark.run(order = 1)                       # this way to mark the order of test run
    def test_invalidlogin(self):
        baseURL = 'https://letskodeit.teachable.com/'
        driver = webdriver.Chrome(
            executable_path=r'C:\Users\Liudmila\PycharmProjects\letskodeit\browsers_drivers\chromedriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login('test@email.com','')

        lp.verifyLoginFailed()


if __name__ == '__main__':
    unittest.main()

# it is a normal python class at this moment
# we will convert it to unittest/pytest and then wil put under the framework POM