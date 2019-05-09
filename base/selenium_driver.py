# in Handy_wrappers we have a lot of utility methods to get the By type, find if element present, etc
# here we will paste the entire code from handy_wrappers.
# Here we will wrapp all the methods provided by selenium webdriver into our custom methods
# in order to use more efficiently in our framework, after all we can easy to use it, easy to understand
# and in future we can integrate a lot of things later in one place. ( exception handling, login in one place)
# it is a Framework approach
#we create this class to find elements
from traceback import print_stack

from selenium.webdriver.common.by import By


class SeleniumDriver():
    def __init__(self,driver):   # - we need driver to perform actions; if we need smt from oitside - we need __init__ method
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()

        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        else:
            print('This locator type is not supported')
        return False

    def getElement(self,locator,locatorType = 'id'):

        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print('Element is found')
        except:
            print('Element is not found')
        return element
    #we can create one more method


    def elementClick(self,locator, locatorType = 'id'):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            print('Click on element with locator'+locator + 'LocatorType: '+locatorType)
        except:
            print('Can not click on the element')
            print_stack()


    def is_element_present(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print('Elemnet is found')
                return True
            else:
                return False

        except:
            print('Element is not found')
            return False

        #OR

    def elementPresenceCheck(self,locator, byType):
        try:
            elementlist = self.driver.find_elements(byType, locator)
            if len(elementlist) > 0:
                print('Elemnet is found')
                return True
            else:
                return False

        except:
            print('Element is not found')
            return False



# after we created this class we can use it in using_wrappers_demo1





