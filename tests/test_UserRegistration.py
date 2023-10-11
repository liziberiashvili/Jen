import time

from faker import Faker

from data.models.User import User
from managers.DriverManager import DriverManager
from steps.LegalRegistrationSteps import LegalRegistrationSteps
from utils.RandomUtils import RandomUtils


class TestUserRegistration:

    def test_user_registration(self):
        fake = Faker()
        password = RandomUtils.password()
        user = User(
            legal_form=fake.name(),
            name=fake.name(),
            id_number=RandomUtils.integer(11),
            chief=fake.name(),
            contact_person=fake.name(),
            phone_number="+995598113344",
            email=fake.email(),
            address=fake.name(),
            password=password,
            repeat_password=password,
        )
        response = LegalRegistrationSteps.register(user)
        DriverManager.get_driver().get("https://mailtrap.io/inboxes")
        DriverManager.get_driver().add_cookie({
                                                  "remember_user_token": "eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hOall3T0RFNFhTd2lKREpoSkRFd0pFeDFOM1IxVkVGR2FtaFhiR280UzBobE1GRTRZeTRpTENJeE5qa3hNVFkwTVRJd0xqWTJNalV4TlRZaVhRPT0iLCJleHAiOiIyMDIzLTA4LTE4VDE1OjQ4OjQwLjY2MloiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--d304e46b7172e0728407a613092046255e3ffa2b",
                                                  "_mailtrap_session": "15242a99deab64a2ede89351b609f991"})
        time.sleep(4)
