from selenium import webdriver
import unittest
class Test(unittest.TestCase): 
    browser=webdriver.Firefox(executable_path=r'./geckodriver.exe') #for linux webdriver.Firefox('driver')
    def test1(self):
        self.browser.maximize_window()
        self.browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
        assert 'Selenium Easy Demo' in self.browser.title
        a=self.browser.find_element_by_class_name('btn-default')
        print(a.get_attribute("innerHTML"))
        assert 'Show Message' in self.browser.page_source
        message=self.browser.find_element_by_id("user-message")
        btn=self.browser.find_element_by_class_name("btn-default")
        text=self.browser.find_element_by_id("display")
        css_select=self.browser.find_element_by_css_selector("#get-input > .btn")
        print(css_select)
        message.clear()
        a='I AM JOD'
        message.send_keys(a)
        btn.click()
        assert  'I AM JOD' in text.get_attribute('innerHTML')
        #self.browser.close() close current window
        self.browser.quit() # close all sessions 
        #call twice if it doesnt work
    def formcheck(self):
        print('hey')
        assert 'Show Message' in self.browser.page_source
        message=self.browser.find_element_by_id("user-message")
        message.clear()
        message.send_keys('I AM JOD')
if(__name__=="__main__"):
    unittest.main()
