from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib3
import shutil

download_dir = "../pdf_scraper/" 
options = webdriver.FirefoxOptions()
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0")
DRIVER_PATH = '../pdf_scraper/geckodriver-v0.27.0-win64/geckodriver.exe'
download_dir = '../pdf_scraper'

driver = webdriver.Firefox(profile,executable_path=DRIVER_PATH) 
driver.get('https://www.candriam.lu/fr/professional/details-de-fonds/LU1829309977/')

action = ActionChains(driver) 
time.sleep(6)

accept_button = driver.find_element_by_xpath('//body[@class="funds-details modal-open isdesktop"]/div[@id="checkUserStatut"]/div[@class="modal-dialog"]/div[@class="modal-content"]/form/div[@class="btn-wrapper"]/button[@id="disclaimer-bt-success"]')
action.click(accept_button).perform()

time.sleep(6)

driver.execute_script("window.scrollTo(0, 3100);")
link_to_pdf = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[8]/div[2]/div/div[2]/div[3]/ul/li/a').get_attribute('href')
#wget.download(link_to_pdf.get_attribute('href'))

http = urllib3.PoolManager(10, headers=user_agent)

with http.request('GET', link_to_pdf, preload_content=False) as r, open('../pdf_scraper/Reporting (EN, Classe dactions I).pdf', 'wb') as out_file:       
    shutil.copyfileobj(r, out_file)

time.sleep(6)
