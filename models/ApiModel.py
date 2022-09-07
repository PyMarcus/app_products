from controllers.ApiController import ApiController


class ApiModel:
    def __init__(self) -> None:
        pass

    def signIn(self, values) -> bool:
        """
        sign in a user into database
        :return: None
        """
        api = ApiController(values)
        return api.postSignIn()
