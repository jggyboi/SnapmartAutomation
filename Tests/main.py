from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/CHEQWS172-USER/PycharmProjects/SnapmartAutomation/SnapmartAutomation/chromedriver.exe")

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://139.99.96.214:3000/#/")

#dismiss welcome banner and cookie message
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/app-welcome-banner/div/div[2]/button[2]').click()
driver.find_element_by_xpath('/html/body/div[1]/div/a').click()

#login
driver.find_element_by_id("navbarAccount").click()
driver.find_element_by_id("navbarLoginButton").click()
driver.find_element_by_id("email").send_keys("test@test.com")
driver.find_element_by_id("password").send_keys("abcd1234")
driver.find_element_by_id("loginButton").click()

#add item to cart
driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]/mat-grid-list/div/mat-grid-tile[8]/figure/mat-card/div[2]/button').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]').click()
time.sleep(2)

#checkout
driver.find_element_by_id("checkoutButton").click()
driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-select/div/app-address/mat-card/mat-table/mat-row[2]/mat-cell[1]').click()
driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-select/div/app-address/mat-card/button').click()
driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-delivery-method/mat-card/div[3]/mat-table/mat-row[1]/mat-cell[1]').click()
driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-delivery-method/mat-card/div[4]/button[2]').click()
driver.find_element_by_id("mat-radio-46").click()
driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-payment/mat-card/div/div[2]/button[2]').click()
driver.find_element_by_id("checkoutButton").click()
time.sleep(5)

#logout
driver.find_element_by_id("navbarAccount").click()
driver.find_element_by_id("navbarLogoutButton").click()

time.sleep(2)
driver.close()
driver.quit()
print("Test Completed")