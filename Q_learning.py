import numpy as np
from tqdm import tqdm
from api_wrapper import APIWrapper
import os
 
class Q_learning:
    def __init__(self, learning_rate, decay_rate, epsilon, width = 40, height = 40, 
                 reward_threshold = 800, save_threshold = 15,summary_threshold = 15, n_iterations = 15000, gridWorld_id = 0 ):
        self.lr = learning_rate
        self.weight_facter = 1 - learning_rate
        self.decay_rate = decay_rate
        self.epsilon = epsilon
        self.width = width
        self.height = height
        self.reward_threshold = reward_threshold
        self.save_threshold = save_threshold
        self.summary_threshold = summary_threshold
        self.n_iterations = n_iterations
        self.gridWorld_id = gridWorld_id

        self.api = APIWrapper()
        
        # self.gridWorld_id, curr_state = self.api.get_location()
        # if self.gridWorld_id == -1:
        #     self.api.enter_world(self.gridWorld_id)
        #     self.gridWorld_id, curr_state = self.api.get_location()

        while True:
            self.gridWorld_id, curr_state = self.api.get_location()

            if self.gridWorld_id != -1:
                break

            self.api.enter_world(self.gridWorld_id)
        
        print("Successfully entered to the grid world")

        self.x, self.y = int(curr_state["x"]), int(curr_state["y"])

        self.filename = "gridWorld_" + self.gridWorld_id + ".npy"        
        self.actions = ["North","South","West","East"]
        self.Q_table = self.get_table()

    def get_table(self):
        return np.load(self.filename) if os.path.exists(self.filename) else self.initialize_table()

    def _get_random_number(self):
        return np.random.uniform(low=-1, high=1)
    
    def initialize_table(self):
        return np.array([[{"North": self._get_random_number(), "South": self._get_random_number(), 
                            "West": self._get_random_number(), "East": self._get_random_number()} 
                            for _ in range(self.width)] for _ in range(self.height)])
    
    def save_table(self):
        np.save(self.filename,self.Q_table)

    def should_explore(self):
        return True if np.random.uniform(0, 1) < self.epsilon else False

    def get_max_value(self,x,y):
        return max(self.Q_table[x,y].values())
    
    def get_optimal_action(self,x,y):
        return max(self.Q_table[x][y], key = self.Q_table[x][y].get)

    def take_action(self):
        return np.random.choice(self.actions) if self.should_explore() else self.get_optimal_action(self.x, self.y) 

    def is_terminal(self,reward):
        return True if abs(reward) > self.reward_threshold else False
    
    def calculate_q_value(self,action,reward,max_q_value):
        return self.weight_facter * self.Q_table[self.x,self.y][action] +\
                self.lr * (reward + self.decay_rate * max_q_value)
    
    def train_agent(self, n_episodes):
        for _ in tqdm(range(n_episodes)):
            self.update_q_values()

    def update_q_values(self):
        for iter in range(self.number_of_iteration):

            reward, _, new_state = self.api.make_move()
            new_x, new_y =  int(new_state["x"]), int(new_state["y"])
            
            if self.is_terminal(reward):
                print("-----Agent is in terminal state-----")
                self.Q_table[self.x, self.y] = {action: reward for action in self.actions}
                self.summary_model(new_state, reward, new_x, new_y)
                return
            
            action = self.take_action()
            max_q_value_for_new_state = self.get_max_value(new_x, new_y)
            self.q_table[self.x, self.y][action] = self.calculate_q_value(action, reward, max_q_value_for_new_state)

            print("-----Q values successfully updated-----")
            
            if iter % self.save_threshold == 0:
                self.save_table()
                print("-----Q values successfully saved-----")

            if iter % self.summary_threshold == 0:
                self.summary_model(new_state, reward, new_x, new_y)
            
            self.x, self.y = new_x, new_y

    def summary_model(self, state, reward, x, y):
        print("State: ", state)
        print("Reward: ", reward)
        print("Coordinate X: ", x)
        print("Coordinate Y: ",y)



