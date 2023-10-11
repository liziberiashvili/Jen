from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from elements.input import Input
from utils.DriverUtils import DriverUtils


class BooksPageLogin:
    __user_name = Input(By.XPATH, "//input[@id='userName']", "username")
    __password = Input(By.XPATH, "//input[@id='password']", "password")
    __login_button = Button(By.XPATH, "//button[@id='login']", "login button")
    __registered_user = Element(By.XPATH, "//label[@id='userName-value']", "daregistrirebuli useri")
    __log_out = Button(By.XPATH, "//div[@class='text-right col-md-5 col-sm-12']//button[@id='submit']", "log out")
    __profile_page = Element(By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-3']", "profile")
    __book_title = Element(By.XPATH, "//span[@class='mr-2']", "title books")

    def fill_user_name(self, value):
        self.__user_name.send_text(value)

    def fill_password(self, value):
        self.__password.send_text(value)

    def click_button_login(self):
        DriverUtils.wait_for_clickable(self.__login_button.find_element())
        self.__login_button.move_to_element()
        self.__login_button.click()

    def is_user_name_visible(self):
        locator = By.XPATH, self.__registered_user.locator
        DriverUtils.wait_for_visible(locator)
        return self.__registered_user.is_visible()

    def log_out_button(self):
        self.__log_out.click()

    def profile_page(self):
        self.__profile_page.click()

    def get_book_title(self):
        return self.__book_title.get_text()

