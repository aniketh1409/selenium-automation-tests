from selenium.webdriver.common.by import By

def test_1_login_fields_present_and_fill(driver, base_url):
    driver.get(base_url)
    
    test1= driver.find_element(By.ID, "test-1-div")
    email = test1.find_element(By.ID, "inputEmail")
    password = test1.find_element(By.ID, "inputPassword")
    btn = test1.find_element(By.CSS_SELECTOR, "button[type='submit']")

    assert email.is_displayed()
    assert password.is_displayed()
    assert btn.is_displayed()
    email.send_keys("anikeths@ualberta.ca")
    password.send_keys("resolve2win")   