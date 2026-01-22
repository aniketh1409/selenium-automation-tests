from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_5_wait_then_click(driver, base_url):
    driver.get(base_url)

    test5 = driver.find_element(By.ID, "test-5-div")
    button_locator = (By.ID, "test5-button")
    alert_locator = (By.ID, "test5-alert")

    #since the time for the button to appear is randomized to be anywhere between 1000 to 10000ms (1 to 10s), we give a max wait of 12s
    btn = WebDriverWait(driver, 12).until(EC.visibility_of_element_located(button_locator)) 
    btn.click()

    #as for the alert, we can wait up to only 3s since the alert should appear basically almost immediately after button click.
    alert = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(alert_locator))
    assert "You clicked a button!" in alert.text

    btn2 = test5.find_element(*button_locator)
    assert btn2.is_enabled() is False
