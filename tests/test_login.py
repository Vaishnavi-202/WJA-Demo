import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Login")
@allure.story("Valid user login")
@allure.title("Login succeeds with standard_user")
def test_login_success(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.title_text() == "Products"


@allure.feature("Login")
@allure.story("Invalid credentials")
@allure.title("Login fails with wrong password")
def test_login_invalid_password(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "wrong_password")

    assert "Username and password do not match" in login.get_error()
