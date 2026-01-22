from selenium.webdriver.common.by import By

def test_4_button_enabled_disabled(driver, base_url):
    driver.get(base_url)
    test4 = driver.find_element(By.ID, "test-4-div")
    buttons = test4.find_elements(By.TAG_NAME, "button")
    assert buttons[0].is_enabled() is True
    assert buttons[1].is_enabled() is False
