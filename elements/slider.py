from selenium.webdriver.common.by import By

import elements
from selenium.webdriver import ActionChains

from elements.element import Element
from managers.DriverManager import DriverManager


class Slider(Element):
    def __init__(self, by, locator, name):
        super().__init__(by, locator, name)

    def click_and_hold(self):
        actions = ActionChains(DriverManager.get_driver())
        actions.click_and_hold(DriverManager.get_driver().find_element(self.by, self.locator)).perform()

    def move_slider(self):
        actions = ActionChains(DriverManager.get_driver())
        actions.move_to_element(DriverManager.get_driver().find_element(self.by, self.locator)).perform()
