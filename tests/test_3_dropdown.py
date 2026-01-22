from selenium.webdriver.common.by import By

def test_3_dropdown_select(driver, base_url):
    driver.get(base_url)
    test3 = driver.find_element(By.ID, "test-3-div")
    button = test3.find_element(By.ID, "dropdownMenuButton")

    assert button.text.strip() == "Option 1"

    button.click()
    option3 = test3.find_element(By.XPATH, ".//a[contains(@class,'dropdown-item') and normalize-space()='Option 3']")
    option3.click()
    assert button.text.strip() == "Option 3" #we update the button text on selection
