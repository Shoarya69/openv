from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# firefox binary path (update if needed)
FIREFOX_PATH = "/snap/firefox/current/usr/lib/firefox/firefox"  # ya "/snap/bin/firefox" if you installed from Snap
GECKODRIVER_PATH = "/usr/local/bin/geckodriver"

options = Options()
options.add_argument("--headless")
options.binary_location = FIREFOX_PATH

service = Service(GECKODRIVER_PATH)
driver = webdriver.Firefox(service=service, options=options)


def flash():
    driver.get("http://admin:admin@192.168.31.244:8080")

    element = driver.find_element(By.ID, "flashbtn")
    element.click()
    driver.quit()
