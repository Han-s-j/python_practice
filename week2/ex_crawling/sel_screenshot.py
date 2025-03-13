from selenium import webdriver
import time
import img_util

url = "https://www.apple.com/kr/iphone-16e/?afid=p238%7CpTCSbUlJ_mtid_209254jz40384&cid=wwa-kr-kwna-iphone-Brand-iPhone-Evergreen-"
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
driver.get_screenshot_as_file("appleIphone.png")
img_util.fullpage_screenshot(driver, 'full_appleIphone.png')
driver.close()
