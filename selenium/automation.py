from selenium import webdriver
chrome_browser = webdriver.Chrome('chromedriver')
# print (chrome_browser)
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
print('Selenium Easy Demo' in chrome_browser.title)
assert 'Selenium Easy Demo' in chrome_browser.title
# assert 'Selenium Easy Demo' in chrome_browser.body
button = chrome_browser.find_element_by_class_name('btn-default')
print(button.get_attribute('innerHTML'))
assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('HI There!!')

button.click()

output_message= chrome_browser.find_element_by_id('display')
assert 'HI There!!'
assert 'HI There!!' in chrome_browser.output_message
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
chrome_browser.close()
chrome_browser.close()
chrome_browser.quit()