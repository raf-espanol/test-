import unittest
from selenium import webdriver

'''
  this shows how to use class to create a test using unittest()
  then invoke web page, use various api calls in selenium
  
  Note: website displays a dialog you must press 'no thanks'
       to NOT get assert exception.
     code example from www.seleniumeasy.com/python/selenium-webdriver-unittest-example

'''


class InputFormsCheck(unittest.TestCase):

    #Opening browser.
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome(r'C:\Users\pc\Downloads\chromedriver.exe')

    #Testing Single Input Field.    
    def test_singleInputField(self):
        pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
        driver=self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        #Finding "Single input form" input text field by id. And sending keys(entering data) in it.
        eleUserMessage = driver.find_element_by_id("user-message")
        eleUserMessage.clear()
        eleUserMessage.send_keys("Test Python")

        #Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
        eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
        eleShowMsgBtn.click()

        #Checking whether the input text and output text are same using assertion.
        eleYourMsg=driver.find_element_by_id("display")
        assert "Test Python" in eleYourMsg.text
 
    # Closing the browser.
    def tearDown(self):
        self.driver.close()

#if this file is imported from another module then 'name' will be set as main
if __name__ == "__main__":
    unittest.main()
