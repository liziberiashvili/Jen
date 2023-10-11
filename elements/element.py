from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from managers.DriverManager import DriverManager
from utils.LoggerUtils import LoggerUtils


class Element:

    def __init__(self, by=By.XPATH, locator=None, name=None):
        self.locator = locator
        self.name = name
        self.by = by

    def find_element(self):
        LoggerUtils.debug("Finding element by Locator: {}".format(self.locator))
        return DriverManager.get_driver().find_element(self.by, self.locator)

    def find_elements(self):
        return DriverManager.get_driver().find_elements(self.by, self.locator)

    def is_visible(self):
        return DriverManager.get_driver().find_element(self.by, self.locator).is_displayed()

    def is_exists(self):
        if len(DriverManager.get_driver().find_elements(self.by, self.locator)) > 0:
            return True
        else:
            return False

    def click(self):
        DriverManager.get_driver().find_element(self.by, self.locator).click()

    def get_text(self):
        return DriverManager.get_driver().find_element(self.by, self.locator).text

    def get_text_from_attribute(self, name):
        return DriverManager.get_driver().find_element(self.by, self.locator).get_attribute(name)

    def is_enabled(self):
        return DriverManager.get_driver().find_element(self.by, self.locator).is_enabled()

    def clear(self):
        DriverManager.get_driver().find_element(self.by, self.locator).clear()


    def multiple_click(self, count):
        for i in range(count):
            self.click()


    def move_to_element(self):
        ActionChains(DriverManager.get_driver()).move_to_element(self.find_element())







