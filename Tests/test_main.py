from selenium import webdriver
import pytest
import time

class TestSnapmartAutomation():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/CHEQWS172-USER/PycharmProjects/SnapmartAutomation/SnapmartAutomation/chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        time.sleep(2)
        self.driver.close()
        self.driver.quit()

    def test_checkout(self, setup):
        self.driver.get("http://139.99.96.214:3000/#/")

        # dismiss welcome banner and cookie message
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/app-welcome-banner/div/div[2]/button[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/a').click()

        # login
        self.driver.find_element_by_id("navbarAccount").click()
        self.driver.find_element_by_id("navbarLoginButton").click()
        self.driver.find_element_by_id("email").send_keys("test@test.com")
        self.driver.find_element_by_id("password").send_keys("abcd1234")
        self.driver.find_element_by_id("loginButton").click()

        # add item to cart
        self.driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]/mat-grid-list/div/mat-grid-tile[8]/figure/mat-card/div[2]/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]').click()
        time.sleep(3)

        # checkout
        self.driver.find_element_by_id("checkoutButton").click()
        self.driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-select/div/app-address/mat-card/mat-table/mat-row[2]/mat-cell[1]').click()
        self.driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-address-select/div/app-address/mat-card/button').click()
        self.driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-delivery-method/mat-card/div[3]/mat-table/mat-row[1]/mat-cell[1]').click()
        self.driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-delivery-method/mat-card/div[4]/button[2]').click()
        self.driver.find_element_by_id("mat-radio-46").click()
        self.driver.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-payment/mat-card/div/div[2]/button[2]').click()
        self.driver.find_element_by_id("checkoutButton").click()
        assert self.driver.find_element_by_class_name("confirmation").text
        time.sleep(5)

        # logout
        self.driver.find_element_by_id("navbarAccount").click()
        self.driver.find_element_by_id("navbarLogoutButton").click()