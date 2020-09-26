import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from utilities.BaseClass import Baseclass


class TestHomePage(Baseclass):
    def test_FormSubmission(self,getData):


        # driver.find_element_by_name("name").send_keys("Sanjog")
        self.driver.find_element_by_css_selector("input[name='name']").send_keys(getData[0])
        self.driver.find_element_by_name("email").send_keys(getData[1])
        self.driver.find_element_by_id("exampleCheck1").click()
        dropdown = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        dropdown.select_by_visible_text(getData[2])
        dropdown.select_by_index(0)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        msg = (self.driver.find_element_by_class_name("alert.alert-success.alert-dismissible").text)
        assert "success" in msg
        self.driver.refresh()

    @pytest.fixture(params=[("Sanjog","Kulkarni","Male"),("Ash","Kulkarni","Female")])
    def getData(self,request):
        return request.param

