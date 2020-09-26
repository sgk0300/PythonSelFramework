from selenium.webdriver.common.by import By


class CheckoutPage():
    def __init__(self,driver):
        self.driver = driver
    add = (By.CLASS_NAME,"btn.btn-info")

    '''def ProductList(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def Product(self):
        return self.driver.find_element(*CheckoutPage.productname)'''

    def AddButton(self):
        return self.driver.find_element(*CheckoutPage.add)




