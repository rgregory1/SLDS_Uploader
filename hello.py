import platform

if platform.system() == "Darwin":
    print("mac")
else:
    print("nada")

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)

print("Success")
