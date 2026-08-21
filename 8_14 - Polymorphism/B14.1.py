class Duck:
    def speak(self):
        print(f"Cap cap")

class Robot:
    def speak(self):
        print(f"BEEP BOOP")


def make_it_speak(thing):
    thing.speak()


make_it_speak(Duck())
make_it_speak(Robot())