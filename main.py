import time
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://portal.compliancehcm.com.br/apex/f?p=187:LOGIN')
wait = WebDriverWait(driver, 10)

load_dotenv()

user = os.getenv('P101_USERNAME')
password = os.getenv('P101_PASSWORD')

user_input = wait.until(EC.visibility_of_element_located((By.ID, 'P101_USERNAME')))
password_input = wait.until(EC.visibility_of_element_located((By.ID, 'P101_PASSWORD')))
submit_button = wait.until(EC.visibility_of_element_located((By.ID, 'P101_LOGIN')))

user_input.send_keys(user)
password_input.send_keys(password)
submit_button.click()

point_button = wait.until(EC.visibility_of_element_located((By.ID, 'B491409282691032647')))
point_button.click()

iframe = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'iframe')))
driver.switch_to.frame(iframe)

point_confirm_button = wait.until(EC.visibility_of_element_located((By.ID, 'B491409745545032651')))
#point_confirm_button.click()

time.sleep(10)
driver.quit()
