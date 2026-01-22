from selenium.webdriver.common.by import By

def get_cell_value(table_element, row, col):
    # row/col are 0-based within <tbody>
    rows = table_element.find_elements(By.CSS_SELECTOR, "tbody tr")
    cells = rows[row].find_elements(By.CSS_SELECTOR, "td")
    return cells[col].text.strip()

def test_6_table_cell(driver, base_url):
    driver.get(base_url)
    test6 = driver.find_element(By.ID, "test-6-div")
    table = test6.find_element(By.CSS_SELECTOR, "table")
    value = get_cell_value(table, 2, 2)
    assert value == "Ventosanzap"
