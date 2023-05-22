from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notification")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://www.indiatoday.in/crime')

for _ in range(13):
    try:
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div/div[2]/main/div/div[2]/span')))
        button.click()
        
    except (StaleElementReferenceException, TimeoutException):
        # If no notification appears or any other exception occurs, continue with the next click
        pass

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')
container = soup.find('div', {'class': 'story__grid'})
news_list = []

# Extract news titles
for h in container.findAll('a'):
    if h.has_attr('title'):
        new_title = h.text
        news_list.append(new_title)

#print(news_list)
