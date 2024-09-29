
from selenium import webdriver
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC



def ano():
    driver = driver = webdriver.Chrome(ChromeDriverManager().install())
    wait=WebDriverWait(driver,10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    depart_from = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_city']")))
    # depart_from = wait.until(EC.element_to_be_clickable(By.ID,"BE_flight_origin_city"))
    depart_from.click()
    depart_from.send_keys("New Delhi")
    depart_from.send_keys(Keys.ENTER)

    going_to = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_arrival_city']")))
    going_to.click()
    going_to.send_keys("New")
    search_results = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
    print(len(search_results))
    for results in search_results:
        if "New Delhi (DEL)" in results.text:
            print(results.text)
            results.click()
            time.sleep(3)
            break

    time.sleep(2)
    origin=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
    time.sleep(2)
    origin.click()
    time.sleep(2)
    all_dates=driver.find_elements(By.XPATH,"//div[@id = 'monthWrapper']//tbody//td[@class !='inActiveTD']")
    for date in all_dates:
        if date.get_attribute("data-date") == "09/28/2024":
            date.click()
            time.sleep(3)
            break



ano()

# class Commands:
#
#     def c1(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://sqa.sporday.com/home")
#         time.sleep(3)
#         t= driver.find_element(By.LINK_TEXT,'Login').text
#         time.sleep(2)
#         print(t)
#         time.sleep(1)
#
#
#     def get_value(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://sqa.sporday.com/home")
#         time.sleep(2)
#         te=driver.find_element(By.XPATH,"//div[@class='c-iavrNG c-iavrNG-ibICGYT-css']//input[@placeholder='Search items here']").get_attribute("placeholder")
#         # driver.find_element(By.XPATH,"").is_enabled() ************for checking enabling ************
#         print(te)
#
#
#     def check_boxes_radiobutton(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://www.sugarcrm.com/au/request-demo/")
#         time.sleep(2)
#         driver.find_element(By.ID,"doi0").click()
#
#
#     def drop_down(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://www.salesforce.com/ap/form/signup/freetrial-sales/?d=topnav2-btn-ft")
#         drop=driver.find_element(By.NAME,"UserTitle")
#         dd=Select(drop)
#         dd.select_by_index(1)
#         time .sleep(3)
#         dd.select_by_visible_text("Sales Manager")
#         time.sleep(3)
#         dd.select_by_value("Customer_Service_Manager_AP")
#         time.sleep(3)
#         dd.deselect_by_value("Customer_Service_Manager_AP")
#         time.sleep(2)
#
#         # https: // sqa.sporday.com / auth / user - detail
#     def multi_select(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get(" https://sqa.sporday.com/auth/user-detail")
#         time.sleep(2)
#         driver.find_element(By.CLASS_NAME,"css-19bb58m").click()
#         time.sleep(2)
#         se=driver.find_element(By.CLASS_NAME,"css-1dyz3mf")
#         ds=Select(se)
#         ds.deselect_by_value(1)
#         time.sleep(2)
#
#
#     def auto_suggest(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://www.yatra.com/")
#         depart_from = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
#         depart_from.click()
#         time.sleep(2)
#         depart_from.send_keys("New Delhi")
#         time.sleep(2)
#         depart_from.send_keys(Keys.ENTER)
#         time.sleep(2)
#         going_to=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
#         going_to.send_keys("New")
#         time.sleep(2)
#         search_results= driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
#         print(len(search_results))
#         for search in search_results:
#             if "New York (NYC)" in search.text:
#                 search.click()
#                 time.sleep(4)
#                 break
#
#         # origin=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
#         # origin.click()
#
#
#     def screenshot_fnc(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://sqa.sporday.com/auth/login")
#         time.sleep(2)
#         Button_action = driver.find_element(By.XPATH, "//button[normalize-space()='Continue']")
#         Button_action.screenshot(".\\test.png")
#         Button_action.click()
#         time.sleep(2)
#         driver.get_screenshot_as_file("D:\sqa\pythonAutomation\error1.png")
#         driver.save_screenshot(".\\test1.png")
#
#
#
#     def multiple_window(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://www.yatra.com/")
#         driver.maximize_window()
#         parent=driver.current_window_handle
#         time.sleep(2)
#         driver.find_element(By.XPATH,"//a[@title='Student Flight Offer']//img[@class='conta iner large-banner']").click()
#         all_handles = driver.window_handles
#         print(all_handles)
#         for handle in all_handles:
#             if handle!=parent:
#                 driver.switch_to.window(handle)
#                 time.sleep(2)
#                 driver.find_element(By.XPATH,"//li[@class='blockDeal slick-slide slick-current slick-active']//span[@class='mt10 view-btn'][normalize-space()='View Details']").click()
#                 # driver.switch_to.window(handle=2)
#                 time.sleep(3)
#                 driver.close()
#                 break
#         driver.switch_to.window(parent)
#         time.sleep(2)
#
#
#
#     def testting_frames(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
#         driver.maximize_window()
#         driver.switch_to.frame(driver.find_element(By.XPATH,"//body/iframe[1]"))
#         time.sleep(2)
#         # driver.switch_to.frame(0)
#         # driver.find_element(By.XPATH,"//body/iframe[1]").
#         # frame name
#         driver.switch_to.frame("iframe")
#         # frame id
#         driver.switch_to.frame("iframe")
#         driver.find_element(By.XPATH,"//span[normalize-space()='Tutorials']")
#         time.sleep(2)
#         print("excutes")
#
#
#
#     def practise_alerts(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert3")
#         driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
#         time.sleep(2)
#         driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
#         time.sleep(2)
#         driver.switch_to.alert.dismiss()
#         time.sleep(2)
#
#
#     def mouse_hover(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://www.yatra.com/")
#         driver.maximize_window()
#         more_button=driver.find_element(By.XPATH,"//span[@class='more-arr']")
#         my_account = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
#         action=ActionChains(driver)
#         time.sleep(2)
#         action.move_to_element(my_account).perform()
#         # action.move_to_element(more_button).perform()
#         time.sleep(4)
#         driver.find_element(By.XPATH,"//a[@id='booking_engine_cabs']").click()
#         time.sleep(2)
#
#
#
#     def right_click(self):
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get("https://demo.guru99.com/test/simple_context_menu.html")
#         driver.maximize_window()
#         clicking=ActionChains(driver)
#         # ele1=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
#         # copi=driver.find_element(By.XPATH,"//span[normalize-space()='Copy']")
#         # clicking.context_click(ele1).perform()
#         # time.sleep(2)
#         # copi.click()
#         # time.sleep(2)
#
#
#
#         # double click
#         clicking = ActionChains(driver)
#         double_element =driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
#         clicking.double_click(double_element).perform()
#         time.sleep(2)
#         driver.switch_to.alert.dismiss()
#         time.sleep(2)
#         # driver.switch_to.window(driver.window_handles[])
#
#
#     # def sliders(self):
#     #     driver = webdriver.Chrome(ChromeDriverManager().install())
#     #     driver.get("https://demo.guru99.com/test/simple_context_menu.html")
#
#
#
#
# # create_object = Commands()
# # create_object.right_click()
# # create_object.mouse_hover()
# # create_object.practise_alerts()
# # create_object.multiple_window()
# # create_object.screenshot_fnc()
# # create_object.drop_down()
# # create_object.check_boxes()
# # create_object.get_value()


