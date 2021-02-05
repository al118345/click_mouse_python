from selenium import webdriver

option = webdriver.ChromeOptions()
option.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'

option.add_argument("--incognito")

driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=option)
driver.get("https://www.google.com")