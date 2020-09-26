import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#@pytest.mark.usefixtures("setup")
from pajeObjects.CheckoutPage import CheckoutPage
from pajeObjects.HomePage import HomePage
from utilities.BaseClass import Baseclass


class Teste2e(Baseclass):
    def test_e2e(self):
        homePage= HomePage(self.driver)
        checkoutPage=homePage.ShopItems()
        #checkoutPage=CheckoutPage(self.driver)
        #ProdList=checkoutPage.ProductList()
        #checkoutPage.Product()
        checkoutPage.AddButton().click()

        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
       # for prod in ProdList:
            #if product.find_element_by_xpath("div/h4/a").text == "Blackberry":
               # product.find_element_by_xpath("div/button").click()
           # if prod.checkoutPage.Product().text=="Blackberry":
            #    prod.checkoutPage.AddButton().click()




        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element_by_xpath("//button[contains(@class,'success')]").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.VerifyLinkText("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_css_selector(".checkbox.checkbox-primary").click()
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        assert "Success" in self.driver.find_element_by_css_selector("div[class*='alert-success']").text

        self.driver.get_screenshot_as_file("Screenshot.png")