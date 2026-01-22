from selenium.webdriver.common.by import By

def test_2_listgroup_values(driver, base_url):
    driver.get(base_url)

    test2 = driver.find_element(By.ID, "test-2-div")
    items = test2.find_elements(By.CSS_SELECTOR, "ul.list-group > li.list-group-item")

    assert len(items) == 3

    item_2 = items[1]
    #text should includes both label + badge, so we grab label node + badge node separately
    #label_text = item_2.contents = item_2.text #fallback in case DOM doesnt have distinct child nodes #edit: better to just remove badge text from full text
    badge = item_2.find_element(By.CSS_SELECTOR, "span.badge") #gets badge element

    #better: get the label part by removing badge text
    full = item_2.text.strip()
    badge_text = badge.text.strip()
    label_only = full.replace(badge_text, "").strip()

    assert label_only == "List Item 2"
    assert badge_text == "6"
