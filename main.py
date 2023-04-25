import numpy as np 

from Q_learning import Q_learning

def main():
    q = Q_learning(0.2,4.3,132)
    print(q.get_max_value(5,5))

if __name__=="__main__":
    main()