from printer import printCLR

class Person():
    def __init__(self, name=None, age=None, gender=None, comments=None):
        self.setName(name)
        self.setAge(age)
        self.setGender(gender)
        self.setComments(comments)

    def setName(self, name):
        if str(type(name)) == "<class 'str'>":
            self.name = name
            # print('[I] successfully set name to ' + self.name)
            printCLR('gre', '[I]')
            print(' successfully set name to ' + self.name)
        elif str(type(name)) == "<class 'list'>":
            self.name = name
            # print('[I] successfully set name to ' + str(self.name))
            printCLR('gre', '[I]')
            print(' successfully set name to ' + str(self.name))
        elif str(type(name)) == "<class 'NoneType'>":
            self.name = None
            # print('[W] name is NOT set')
            printCLR('yel', '[W]')
            print('name is NOT set')

    def setAge(self, age):
        if str(type(age)) in ["<class 'int'>", "<class 'float'>"]:
            if age >= 0:
                self.age = age
                # print('[I] age successfully set to ' + str(self.age))
                printCLR('gre', '[I]')
                print(' age successfully set to ' + str(self.age))
            else:
                raise ValueError('Age must be positive')
        elif str(type(age)) == "<class 'str'>":
            age_ = int(age)
            if age_ >= 0:
                self.age = age_
                # print('[I] age successfully set to ' + str(self.age))
                printCLR('gre', '[I]')
                print(' age successfully set to ' + str(self.age))
            else:
                raise ValueError('Age must be positive')
        elif str(type(age)) == "<class 'NoneType'>":
            self.age = None
            # print('[W] age is NOT set')
            printCLR('yel', '[W]')
            print(' age is NOT set')
        else:
            raise ValueError('Age type must be one of int, float, str')

    def setGender(self, gender):
        if str(type(gender)) == "<class 'str'>":
            if gender.lower() in ['male', 'female']:
                self.gender = gender.lower()
                # print('[I] gender successfully set to ' + self.gender.lower())
                printCLR('gre', '[I]')
                print(' gender successfully set to ' + self.gender.lower())
            else:
                raise ValueError('''gender must be 'male' or 'female' ''')
        elif str(type(gender)) == "<class 'bool'>":
            if gender:
                self.gender = 'male'
            else:
                self.gender = 'female'
            # print('[I] gender successfully set to ' + self.gender.lower())
            printCLR('gre', '[I]')
            print(' gender successfully set to ' + self.gender.lower())
        elif str(type(gender)) == "<class 'NoneType'>":
            self.gender = None
            # print('[W] gender is NOT set')
            printCLR('yel', '[W]')
            print(' gender is NOT set')
        else:
            raise ValueError('gender type must be \'str\' or \'bool\'')

    def setComments(self, comments):
        if str(type(comments)) == "<class 'list'>":
            self.comments = comments
            # print('[I] successfully set comments as list')
            printCLR('gre', '[I]')
            print(' successfully set comments as list')
        elif str(type(comments)) == "<class 'dict'>":
            self.comments = comments
            # print('[I] successfully set comments as dict')
            printCLR('gre', '[I]')
            print(' successfully set comments as dict')
        elif str(type(comments)) == "<class 'str'>":
            self.comments = comments
            # print('[I] successfully set comments as str')
            printCLR('gre', '[I]')
            print(' successfully set comments as str')
        elif str(type(comments)) == "<class 'NoneType'>":
            self.comments = None
            # print('[I] comments are NOT set')
            printCLR('gre', '[I]')
            print(' comments are not set')
        else:
            self.comments = comments
            # print('[I] successfully set comments as ' + str(type(comments)))
            printCLR('gre', '[I]')
            print(' successfully set comments as ' + str(type(comments)))

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getComments(self):
        return self.comments

    def clear(self):
        self.name = None
        self.age = None
        self.gender = None
        self.comments = None
        # print("[I] successfully cleared. All params set to 'None'")
        printCLR('gre', '[I]')
        print(" successfully cleared. All params set to 'None'")


def Test():
    p1 = Person()
    p2 = Person('Bob', 16, 'male', 'He is a programmer in future...')
    p2.clear()

if __name__ == '__main__':
    Test()