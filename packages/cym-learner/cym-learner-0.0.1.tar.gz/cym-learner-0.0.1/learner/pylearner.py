
class PyLearner:
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        if self.verbose:
            print('PyLearner is initialized.')
            self.show()
    
    def show(self):
        print('Hello, I am PyLearner!')