class Application:

    action_list = {
        1: "Create Account",
        2: "Delete Account[not implemented yet]",
        3: "Exit"
    }

    @classmethod
    def print_actions(cls):
        print("\n===========================MENU===========================\n")
        for action in cls.action_list:
            print(str(action) + "\t" + cls.action_list[action])

        print("\n========================END MENU==========================\n")

    @classmethod
    def perform(self, action):
        print(Application.action_list.get(action))
