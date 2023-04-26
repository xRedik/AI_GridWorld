from Q_learning import Q_learning
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--alpha",dest="alpha",
                        type=np.float32,help = "Learning rate for updating the Q values")
    
    parser.add_argument("-g", "--gamme",dest="gamma",
                    type=np.float32,help = "Discount factor for model")
    
    parser.add_argument("-e", "--epsilon",dest="epsilon",
                    type=np.float32,help = "Probability of the random action")
    
    
    args = parser.parse_args()
    
    alpha = args.alpha
    gamma = args.gamma
    epsilon = args.epsilon

    if alpha == None or gamma == None or epsilon == None:
        raise Exception("Please enter the values with proper flags\n\
                        For help message call the program with -h flag")

    grid_world_agent = Q_learning(alpha, gamma, epsilon,bool_proggressbar=True,gridWorld_id=0)
    grid_world_agent.train_agent(n_episodes = 1)

if __name__=="__main__":
    main()