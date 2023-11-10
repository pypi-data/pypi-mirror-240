import numpy as np

class PyLearner:
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        if self.verbose:
            print('PyLearner is initialized.')
            self.show()
        else:
            self.show_rand()
    
    def show(self):
        print('Hello, I am PyLearner!')
    
    def show_rand(self):
        print('Hello, I am random PyLearner #', np.random.rand())