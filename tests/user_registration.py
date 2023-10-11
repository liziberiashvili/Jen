from pages.user_registration_page import UserRegistrationPage
from steps.user_registration_steps import UserRegistrationSteps
from utils.UserDataBaseUtils import UserDataBaseUtils


class TestUserRegistration:
    def test_user_registration(self):
        steps = UserRegistrationSteps()
        users = UserDataBaseUtils.get_users()
        register_page = UserRegistrationPage()
        for i in users:
            steps.register(i)
            emails = (steps
                      .turn_element_list_into_string_list
                      (register_page.get_email_list()))
            assert i.email in emails
