from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from elements.input import Input
from utils.LoggerUtils import LoggerUtils


class UserRegistrationPage:
    __add_button = Button(By.XPATH, "//button[@id='addNewRecordButton']", "add_button")
    __first_name_field = Input(By.XPATH, "//input[@id='firstName']", "first_name")
    __last_name_field = Input(By.XPATH, "//input[@id='lastName']", "last_name")
    __email_field = Input(By.XPATH, "//input[@id='userEmail']", "email")
    __age_field = Input(By.XPATH, "//input[@id='age']", "age")
    __salary_field = Input(By.XPATH, "//input[@id='salary']", "salary")
    __department_field = Input(By.XPATH, "//input[@id='department']", "department")
    __submit_button = Button(By.XPATH, "//button[@id='submit']", "submit_button")
    __email_data = Element(By.XPATH, "//div[@class='rt-td' and string-length(text()) > 0][4]", "email_data")

    def click_add(self):
        LoggerUtils.info("Clicking on {}".format(self.__add_button.name))
        self.__add_button.click()

    def fill_first_name(self, firstname):
        self.__first_name_field.send_text(firstname)

    def fill_last_name(self, lastname):
        self.__last_name_field.send_text(lastname)

    def fill_age(self, age):
        self.__age_field.send_text(age)

    def fill_email(self, email):
        self.__email_field.send_text(email)

    def fill_salary(self, salary):
        self.__salary_field.send_text(salary)

    def fill_department(self, department):
        self.__department_field.send_text(department)

    def click_submit(self):
        self.__submit_button.click()

    def get_email_list(self):
        return self.__email_data.find_elements()

