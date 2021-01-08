# Phone is the parent or super class
class Phone:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __str__(self):
        return "{}, {}".format(self.number, self.color)

    def call(self, other_num):
        print(f"calling: {other_num}")

# Android is a sub class of Phone
class Android(Phone):
    def __init__(self, number, color):
        super().__init__(number, color)
        self.passcode = None

    def __str__(self):
        return f"this is an Android phone at {self.number}"

    def set_passcode(self, passcode):
        self.passcode = passcode

    def get_my_number(self):
        print(self.number)

class IPhone( Android):
    def __init__(self, number, color):
        super().__init__(number, color)
        self.face_id = None

    def __str__(self):
        return f"this is an iPhone at {self.number}"

    def set_face_id(self):
        self.face_id = True


android_phone = Android('123-456-7890', 'red')
android_phone.get_my_number()
android_phone.call('098-765-4321')

iphone_phone = Android('123-456-7890', 'rose gold')
iphone_phone.get_my_number()
iphone_phone.call('098-765-4321')
