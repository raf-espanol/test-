from selenium import webdriver
from selenium.webdriver.common.keys import Keys



user = ""
pwd = ""
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://10.1.218.16")
assert "Lilee Systems" in driver.title
#elem = driver.find_element_by_id("usingSystem")
#elem.send_keys(user)
#elem = driver.find_element_by_id("pass")
#elem.send_keys(Keys.RETURN)

#look for the "	Using LileeOS CLI User Account " checkbox

#sites = driver.find_element_by_partial_link_text('sites')
id = driver.find_element_by_id("login").find_element_by_name('system').click()

print id



driver.close()


