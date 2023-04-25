from Q_learning import Q_learning
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-lr", "--learning_rate",dest="lr",
                        type=np.float32,help = "Learning rate for updating the Q values")
    
    parser.add_argument("-dr", "--decay_rate",dest="dr",
                    type=np.float32,help = "Decay rate for model")
    
    parser.add_argument("-e", "--epsilon",dest="epsilon",
                    type=np.float32,help = "Probability of the random action")
    
    
    args = parser.parse_args()
    
    learning_rate = args.lr
    decay_rate = args.dr
    epsilon = args.epsilon

    if learning_rate == None or decay_rate == None or epsilon == None:
        raise Exception("Please enter the values with proper flags\n\
                        For help message call the program with -h flag")

    grid_world_agent = Q_learning(learning_rate,decay_rate,epsilon,bool_proggressbar=True)
    grid_world_agent.train_agent(n_episodes = 3)

if __name__=="__main__":
    main()