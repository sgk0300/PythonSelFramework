from selenium.webdriver.common.by import By

from pajeObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self,driver):
        self.driver=driver
    shop = (By.LINK_TEXT, "Shop")

    def ShopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
