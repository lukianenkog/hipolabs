import sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)

URL = 'https://www.google.com.tr/'

driver.get(URL)

try:
    assert driver.current_url == URL
except AssertionError:
    print(f"couldn't open {URL}")
    driver.quit()
    sys.exit()

try:
    search_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
    search_field.send_keys('Hipo Labs')
    search_field.submit()

    link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://hipolabs.com/"]')))
    link.click()

    team_menu_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/team/"]')))
    team_menu_link.click()

    driver.execute_script("document.querySelector('#pageTeamApplynowButton').scrollIntoView()")

    apply_now_button = wait.until(EC.element_to_be_clickable((By.ID, 'pageTeamApplynowButton')))
    apply_now_button.click()

    apply_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'APPLY NOW')))
    driver.execute_script("arguments[0].scrollIntoView();", apply_button)
    driver.save_screenshot("screenshot.png")

except NoSuchElementException as e:
    print(f'couldn\'t find {str(e)}')
    driver.quit()
    sys.exit()

driver.quit()
