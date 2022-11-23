from PersonClass import Person
from printer import printCLR
import time


class Programmer(Person):
    def __init__(self, name=None, age=None, gender=None, comments=None, speedOfCoding=None, portfolio: dict = {}):
        super().__init__(name, age, gender, comments)

        self.job = 'Programmer'
        printCLR('gre', '[I]')
        print(" job successfully set as 'Programmer'")

        self.setSpeedOfCoding(speedOfCoding)
        self.setPortfolio(portfolio)

    def setSpeedOfCoding(self, speed):
        if str(type(speed)) in ["<class 'int'>", "<class 'float'>"]:
            self.speedOfCoding = speed
            printCLR('gre', '[I]')
            print(' speed of coding set to ' + str(self.speedOfCoding))

        elif str(type(speed)) == "<class 'str'>":
            self.speedOfCoding = float(speed)
            printCLR('gre', '[I]')
            print(' speed of coding set to ' + str(self.speedOfCoding))
        else:
            printCLR('yel', '[W]')
            print(" speed of coding is NOT set. you can NOT use function 'do some coding'."
                  " speed must be one of int, float, str")

    def setPortfolio(self, portfolio):
        self.portfolio = portfolio

    def addProjectToPortfolio(self, projectName: str, difficulty, projectComment=None):
        newProjectName = projectName
        cnt = 1
        while newProjectName in self.portfolio.keys():
            newProjectName = projectName + '(%s)' % str(cnt)
            cnt += 1

        if newProjectName != projectName:
            printCLR('gre', '[I]')
            print(" '%s' already exists. it will be added to portfolio with name '%s'" % (projectName, newProjectName))
        self.portfolio[newProjectName] = [difficulty, projectComment]

        return newProjectName

    def doSomeCoding(self, projectName: str, difficulty, projectComment=None):
        try:
            if str(type(difficulty)) in ["<class 'int'>", "<class 'float'>"]:
                for i in range(1, 101):
                    # printCLR('cya', '[P]')
                    # print(' doing some coding (%s)... ' % projectName + str(i) + '%', end='')
                    printCLR('cya', '[P] doing some coding (%s)... ' % projectName + str(i) + '%')
                    time.sleep(difficulty / self.speedOfCoding)
                    print('\r', end='')

                print('\r', end='')
                printCLR('gre', '[I]')
                print(' some coding is done.')
                return self.addProjectToPortfolio(projectName, difficulty, projectComment)
            else:
                raise ValueError('difficulty must be int or float')
        except:
            raise ValueError('speed is NOT set. set speed to use this function.')

    def getPortfolio(self):
        return self.portfolio

    def getProjectNames(self):
        return self.portfolio.keys()

    def getProjectInfo(self, name: str):
        return self.portfolio[name]

    def getProjectDifficulty(self, name: str):
        return self.portfolio[name][0]

    def getProjectComment(self, name: str):
        return self.portfolio[name][1]

    def getSpeedOfCoding(self):
        return self.speedOfCoding


# это классная важная штука но я подумал что ни в один из классов ее помещать нельзя
def fromPersonToProgrammer(per: Person, speedOfCoding=None, portfolio: dict = {}):
    pro = Programmer(per.getName(), per.getAge(), per.getGender(), per.getComments(), speedOfCoding, portfolio)
    printCLR('gre', '[I]')
    print(' successfully converted from %s to %s' % (str(type(per)), str(type(pro))))
    return pro


def Test():
    p = Programmer(name='Jared', gender=True, speedOfCoding=10000)
    p.doSomeCoding('something', 100, 'OOP 1st')
    p.doSomeCoding('someshow', 100, 'OOP 2nd')
    print(p.getPortfolio())
    print(p.getProjectInfo('something'))
    print(p.getProjectDifficulty('something'))
    print(p.getProjectComment('something'))
    joe = Person('joe', 5, True)
    joe = fromPersonToProgrammer(joe, speedOfCoding=200000)
    joe.doSomeCoding('someshow', 100, 'OOP 3nd')


if __name__ == '__main__':
    Test()
