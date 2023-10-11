from pages.user_registration_page import UserRegistrationPage


class UserRegistrationSteps:
    def register(self, user):
        user_registration_page = UserRegistrationPage()
        user_registration_page.click_add()
        user_registration_page.fill_first_name(firstname=user.firstname)
        user_registration_page.fill_last_name(lastname=user.lastname)
        user_registration_page.fill_age(age=user.age)
        user_registration_page.fill_email(email=user.email)
        user_registration_page.fill_salary(salary=user.salary)
        user_registration_page.fill_department(department=user.department)
        user_registration_page.click_submit()

    def turn_element_list_into_string_list(self, elements):
        strings = []
        for i in elements:
            strings.append(i.text)
        return strings
