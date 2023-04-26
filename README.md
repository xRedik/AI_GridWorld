# AI GridWorld

The program was written with the command line interfaces. That is why we should run this program with several flags. Here is the table of flags:

| Flag  | Purpose | Requred or not | Default value |
| ------------- | ------------- | ------------- | ------------- |
| -a FLOAT, --alpha FLOAT  | learning rate for the model | Required  | No default value  |
| -g FLOAT, --gamma FLOAT  | discount factor for the model  | Required  | No default value  |
| -e FLOAT, --epsilon FLOAT  | probability of random exploration  | Required  | No default value  |


The program also has the -h flag to show the help message to the user about usage of flags. It was included by the argparse package itself.


## Flowchart of the program

As below figure you can see the general flowchart of the programs. After that you can easily understand what the crucial functions do and interact each other.

![image](https://user-images.githubusercontent.com/56725845/234514739-dd86e112-6ee2-4b9a-89cd-fd819e4249f5.png)
