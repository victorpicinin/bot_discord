import functions as lib

from selenium.webdriver.common.keys import Keys
lib.driver.get('https://discordapp.com/channels/276934481993269250/276934481993269250')

mages = len(lib.driver.find_elements_by_xpath("//*[contains(text(), '@Mage')]"))
lib.driver.find_element_by_xpath("//div[@aria-label='Conversar em #general']").send_keys('Resposta')
while True:
    if mages < len(lib.driver.find_elements_by_xpath("//*[contains(text(), '@Mage')]")):
        lib.driver.find_element_by_xpath("//div[@aria-label='Conversar em #general']").send_keys(Keys.RETURN)
        mages = len(lib.driver.find_elements_by_xpath("//*[contains(text(), '@Mage')]"))
        lib.driver.find_element_by_xpath("//div[@aria-label='Conversar em #general']").send_keys('Resposta')


