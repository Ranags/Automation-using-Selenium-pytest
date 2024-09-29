from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())


def test_scoll():
    driver.get("https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world/")
    driver.maximize_window()
    # driver.execute_script("window.scrollBy(0,500)")
    # flag=driver.find_element(By.XPATH,"//a[normalize-space()='Iceland']")
    # driver.execute_script("arguments[0].scrollIntoView();",flag)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    # driver.close()


