from utils.ApiUtils import ApiUtils


class LegalRegistrationSteps:

    @staticmethod
    def register(user):
        user_json = user.to_json()
        response = ApiUtils.post("registration/legal", user_json)
        assert response.status_code == 201
        return response
