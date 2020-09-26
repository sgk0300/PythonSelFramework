import pytest
from selenium import webdriver
global driver
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture(scope="class")
def setup(request):
    Browser_Name = request.config.getoption("--browser_name")
    if Browser_Name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif Browser_Name == "Firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif Browser_Name == "IE":
        driver = webdriver.Chrome(executable_path="C:\\IEDriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
