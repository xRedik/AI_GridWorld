import numpy as np
import os

class Q_learning:
    def __init__(self, lr, decay_rate, epsilon, width = 40, height = 40):
        self.lr = lr
        self.decay_rate = decay_rate
        self.epsilon = epsilon
        self.width = width
        self.height = height

        #will be created after postman
        self.gridWorld_id = None
        self.x = None
        self.y = None

        self.filename = "gridWorld_" + self.gridWorld_id + ".npy"
        
        self.actions = ["North","South","West","East"]
        self.Q_table = self.get_table()

    def should_explore(self):
        return True if np.random.uniform(0, 1) < self.epsilon else False

    def get_table(self):

        if os.path.exists(self.filename):
            return np.load(self.filename)

        return self.initialize_table()

    def initialize_table(self):
        return np.array([[{"North": 0, "South": 0, 
                            "West": 0, "East": 0} for i in range(self.width)] for j in range(self.height)])
    
    def save_table(self):
        np.save(self.filename,self.Q_table)



