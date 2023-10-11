

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from managers.DriverManager import DriverManager


class DriverUtils:

    @staticmethod
    def find_element(xpath):
        return DriverManager.get_driver().find_element(By.XPATH, xpath)

    @staticmethod
    def wait_for_element_enable(element):
        WebDriverWait(DriverManager.get_driver(), timeout=15) \
            .until(expected_conditions.element_to_be_clickable(element))

    @staticmethod
    def wait_for_changes(locator, attribute, text):
        WebDriverWait(DriverManager.get_driver(), timeout=60, poll_frequency=0.1) \
            .until(expected_conditions.text_to_be_present_in_element_attribute(locator, attribute, text))

    @staticmethod
    def wait_for_visible(locator):
        WebDriverWait(DriverManager.get_driver(), timeout=15) \
            .until(expected_conditions.visibility_of_element_located(locator))

    @staticmethod
    def wait_for_alert_visible():
        WebDriverWait(DriverManager.get_driver(), timeout=10).until(expected_conditions.alert_is_present())

    @staticmethod
    def wait_for_clickable(element):
        (WebDriverWait(DriverManager.get_driver(), timeout=10)
         .until(expected_conditions.element_to_be_clickable(element)))



