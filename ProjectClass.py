class Project():
    def __init__(self, projectName: str, projectDifficulty: (int, float), currentStatus: (int, float) = 0,
                 doneBy: list = {}, comments: (list, str) = None):

        self.name = projectName
        self.setDifficulty(projectDifficulty)
        self.comments = comments

    def setDifficulty(self, difficulty: (int, float)):
        if difficulty > 0:
            self.difficulty = difficulty
            print("\033[32m{}\033[0m".format('[I]'), 'project difficulty successfully set to %s' % self.difficulty)
        else:
            raise ValueError('project difficulty must be positive')

    def setStatus(self, status: (int, float)):
        if status <= 0:
            self.status = 0
        elif 0 < status < 1:
            self.status = status
        else:
            self.status = 1


if __name__ == '__main__':
    p = Project('smth', 5.1)
