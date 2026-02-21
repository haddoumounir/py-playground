class Person:
    def __init__(self) -> None:
        print("x1")
        """_summary_
        like that we have on c++ if you wanna use method without having
        the obj use decorator @static method
        """
    @staticmethod
    def bob():
        print("x2")


a = Person()

a.bob()

Person.bob()