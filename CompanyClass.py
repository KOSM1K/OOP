from ProjectClass import Project
from PersonClass import Person
from printer import printCLR


class Company():
    def __init__(self, name: str, director: Person = None, workers: list[Person] = None,
                 projects: list[Project] = None, comments=None):

        self.setName(name)
        self.setDirector(director)
        self.setWorkers(workers)
        self.setProjects(projects)
        self.setComments(comments)

    def setName(self, name: str):
        self.name = name
        printCLR('gre', '[I]')
        print(' company name successfully set to %s' % self.name)

    def setDirector(self, director: Person):
        if director is not None:
            self.director = director
            printCLR('gre', '[I]')
            print(' director successfully set')
        else:
            self.director = None
            printCLR('yel', '[W]')
            print(' director is NOT set')

    def setWorkers(self, workers: list[Person]):
        if workers not in [None, []]:
            self.workers = workers
            printCLR('gre', '[I]')
            print('workers list successfully set')
        else:
            self.workers = []
            printCLR('yel', '[W]')
            print(' there are no workers in company')

    def setProjects(self, projects: list[Project]):
        if projects not in [None, []]:
            self.projects = projects
            printCLR('gre', '[I]')
            print(' projects list successfully set')
        else:
            self.projects = []
            printCLR('yel', '[W]')
            print(' there are no projects')

    def setComments(self, comments=None):
        if str(type(comments)) == "<class 'list'>":
            self.comments = comments
            printCLR('gre', '[I]')
            print(' successfully set comments as list')
        elif str(type(comments)) == "<class 'dict'>":
            self.comments = comments
            printCLR('gre', '[I]')
            print(' successfully set comments as dict')
        elif str(type(comments)) == "<class 'str'>":
            self.comments = comments
            printCLR('gre', '[I]')
            print(' successfully set comments as str')
        elif str(type(comments)) == "<class 'NoneType'>":
            self.comments = None
            printCLR('gre', '[I]')
            print(' comments are not set')
        else:
            self.comments = comments
            printCLR('gre', '[I]')
            print(' successfully set comments as ' + str(type(comments)))
