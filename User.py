
from dataclasses import dataclass


@dataclass
class User:
    """
    A class representing a user.

    Attributes:
        name (str): The name of the user.
        email (str): The email of the user.
        dl_number (int): The driver's license number of the user.
    """

    name: str
    email: str
    dl_number: int

    def __post_init__(self):
        # TODO data validation
        # TODO post processing
        pass

# class User:
#     def __init__(self, name, email, dl_number):
#         self.name = name
#         self.email = email
#         self.dl_number = dl_number


def main():
    users = [
        User("jane", "jane@gmail.com", 12345),
        User("john", "john@gmail.com", 54321),
        User("Jack", "jack@ec.rr.com", 12346),
    ]

    for user in users:
        print(user)


if __name__ == "__main__":
    main()
