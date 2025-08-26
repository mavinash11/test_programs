from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
# This script uses Selenium to open a web browser and navigate to Google.

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

box = driver.find_element(By.XPATH, "//*[@id=\"comp\"]/div[2]/div[1]/div[2]/input")
# box.send_keys("Selenium Python")
box.send_keys("Selenium Python" + Keys.RETURN)
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id=\"topMainHeader\"]/div/a/div/img").click()

time.sleep(5)
parent_element = driver.find_element(By.CLASS_NAME, "headerMainList")
sub_elements = parent_element.find_elements(By.TAG_NAME, "li")
Found = False
# for element in sub_elements:
#     print(element.text)
#     if element.text == "Tutorials":
#         actions = ActionChains(driver)
#         actions.move_to_element(element).perform()
#         p_ele = driver.find_element(By.CLASS_NAME, "megaDropDown")
#         sub_items = p_ele.find_elements(By.TAG_NAME, "li")
#         for item in sub_items:
#             print(item.text)
#             if item.text == "Python":
#                 item.click()
#                 Found = True
#                 break
#         if Found:
#             break
print("*******List of main elements and sub elements*******")
l1 = {}
for element in sub_elements:
    print(f"Main element: {element.text}")
    x = element.text
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    p_ele = driver.find_element(By.CLASS_NAME, "megaDropDown")
    sub_items = p_ele.find_elements(By.TAG_NAME, "li")
    print("List of its sub elements:")
    l2 = []
    for item in sub_items:
        l2.append(item.text)
    print(l2)
    l1[x] = l2
time.sleep(4)

print(l1)


