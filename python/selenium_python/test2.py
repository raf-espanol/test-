from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



user = ""
pwd = ""
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
#driver.get("http://google.com")
#assert "google" in driver.title
#sites = driver.find_element_by_partial_link_text('sites')
#id = driver.find_element_by_id("login").find_element_by_name('system').click()

#print id



#driver.close()


#driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
