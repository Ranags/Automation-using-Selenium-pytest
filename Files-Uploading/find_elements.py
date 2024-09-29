from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriver


class TestCases:

    # def t1(self):

        # driver.get("https://sqa.sporday.com/auth/login")
        # time.sleep(3)
        # driver.find_element(By.TAG_NAME,"input").send_keys("sporday-admin@yopmail.com")
        # driver.find_element(By.NAME,"password").send_keys("Abc1234#")
        # # driver.find_element(By.NAME)
        # time.sleep(2)


    # def link_text(self):
    #     driver = webdriver.Chrome(ChromeDriverManager().install())
    #     driver.get("https://sqa.sporday.com/auth/login")
    #     time.sleep(2)
    #     driver.find_element(By.TAG_NAME,"Are you a Trainer?").click()
    #     time.sleep(2)


    def find_elements(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://sqa.sporday.com/home")
        wait=WebDriverWait(driver,20)
        wait.until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]")))

        time.sleep(5)
        e=driver.find_elements(By.CLASS_NAME,"c-ikgNFp")
        for i in e:
            print(i.text)
        time.sleep(1)
        if i.text=='Boxing':
            i.text.click()
        wait2 = WebDriverWait(driver,10)













create_object = TestCases()
create_object.find_elements()
#
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver.get("https://www.google.com/")
# driver.
# driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("Hello")

