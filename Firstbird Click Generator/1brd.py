from time import sleep
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless=new")
for i in range(0, 8000):
    print(i + 1)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://1brd.ly/8AJbB?st=63mubesipmts")
    sleep(5)
    driver.quit()
