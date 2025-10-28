###################################################################################################################################################################################
# There are 5 datasets to test the algorithms.
# Choose one and start to test ans simulate.
###################################################################################################################################################################################

# 1-th dataset
# number of categories 
M = 2
# w_i for each node in category c_i
w = [4, 1]
# price of each active node in category c_i  
pa = [20, 5]
# price of each standby node in category c_i 
ps = [2, 0.5]
# failure rate of each active node in category c_i 
fa = [0.01, 0.04]
# failure rate of each standby node in category c_i 
fs = [0.001, 0.004]

# total number of nodes
N = 200
# M_i for each category c_i
Mi = [100, 100] 

# parameter of SFC
K = 6
Nk = [5, 5, 5, 5, 3, 2]
Lk = [[10, 20, 5, 6, 9], [1, 1, 1, 1, 1], [20, 40, 50, 45, 45], [10, 20, 25, 25, 20], [3, 4, 8], [2, 2]]
Rk = [0.99, 0.999, 0.9999, 0.9999, 0.99999, 0.99]
Tk = [80, 10, 100, 100, 5, 8]
Bk = [1, 3, 4, 1, 2, 3]

# paramete of model
t0 = 1
alpha, beta = 0.65, 0.35

###################################################################################################################################################################################
# 2-th dataset
# number of categories 
M = 3
# w_i for each node in category c_i
w = [5, 4, 1]
# price of each active node in category c_i  
pa = [25, 20, 5]
# price of each standby node in category c_i 
ps = [2.5, 2, 0.5]
# failure rate of each active node in category c_i 
fa = [0.008, 0.01, 0.04]
# failure rate of each standby node in category c_i 
fs = [0.0008, 0.001, 0.004]

# total number of nodes
N = 250
# M_i for each category c_i
Mi = [50, 100, 100] 

# parameter of SFC
K = 8
Nk = [5, 5, 5, 5, 3, 2, 5, 3]
Lk = [[10, 20, 5, 6, 9], [1, 1, 1, 1, 1], [20, 40, 50, 45, 45], [10, 20, 25, 25, 20], [3, 4, 8], [2, 2], [10, 20, 5, 6, 9], [3, 4, 8]]
Rk = [0.99, 0.999, 0.9999, 0.9999, 0.99999, 0.99, 0.99999, 0.9999]
Tk = [80, 10, 100, 100, 5, 8, 80, 5]
Bk = [4, 2, 1, 3, 4, 1, 2, 3]

# paramete of model
t0 = 1
alpha, beta = 0.65, 0.35

###################################################################################################################################################################################
# 3-th dataset
# number of categories 
M = 2
# w_i for each node in category c_i
w = [4, 1]
# price of each active node in category c_i  
pa = [20, 5]
# price of each standby node in category c_i 
ps = [2, 0.5]
# failure rate of each active node in category c_i 
fa = [0.01, 0.04]
# failure rate of each standby node in category c_i 
fs = [0.001, 0.004]

# total number of nodes
N = 200
# M_i for each category c_i
Mi = [100, 100] 

# parameter of SFC
K = 5
Nk = [5, 5, 5, 3, 2]
Lk = [[10, 20, 5, 6, 9],[20, 40, 50, 45, 45], [10, 20, 25, 25, 20], [3, 4, 8], [2, 2]]
Rk = [0.99, 0.9999, 0.9999, 0.99999, 0.99]
Tk = [80, 100, 100, 5, 8]
Bk = [1, 3, 4, 2, 3]

# paramete of model
t0 = 1
alpha, beta = 0.65, 0.35

###################################################################################################################################################################################
# 4-th dataset
# number of categories 
M = 3
# w_i for each node in category c_i
w = [5, 4, 1]
# price of each active node in category c_i  
pa = [25, 20, 5]
# price of each standby node in category c_i 
ps = [2.5, 2, 0.5]
# failure rate of each active node in category c_i 
fa = [0.008, 0.01, 0.04]
# failure rate of each standby node in category c_i 
fs = [0.0008, 0.001, 0.004]

# total number of nodes
N = 800
# M_i for each category c_i
Mi = [200, 300, 300] 

# parameter of SFC
K = 10
Nk = [5, 5, 5, 5, 3, 2, 5, 3, 2, 5]
Lk = [[10, 20, 5, 6, 9], [1, 1, 1, 1, 1], [20, 40, 50, 45, 45], [10, 20, 25, 25, 20], [3, 4, 8], [2, 2], [10, 20, 5, 6, 9], [3, 4, 8], [2, 2], [20, 40, 50, 45, 45]]
Rk = [0.99, 0.999, 0.9999, 0.9999, 0.99999, 0.99, 0.99999, 0.9999, 0.999999, 0.999]
Tk = [80, 10, 100, 100, 5, 8, 80, 5, 8, 100]
Bk = [1, 3, 4, 1, 2, 3, 2, 2, 4, 1]

# paramete of model
t0 = 1
alpha, beta = 0.65, 0.35

###################################################################################################################################################################################
# 5-th dataset
# number of categories 
M = 2
# w_i for each node in category c_i
w = [5, 1]
# price of each active node in category c_i  
pa = [25, 5]
# price of each standby node in category c_i 
ps = [2.5, 0.5]
# failure rate of each active node in category c_i 
fa = [0.008, 0.04]
# failure rate of each standby node in category c_i 
fs = [0.0008, 0.004]

# total number of nodes
N = 1200
# M_i for each category c_i
Mi = [500, 700] 

# parameter of SFC
K = 15
Nk = [5, 5, 5, 5, 3, 2, 5, 3, 2, 5, 5, 5, 5, 5, 3]
Lk = [[10, 20, 5, 6, 9], [1, 1, 1, 1, 1], [20, 40, 50, 45, 45], [10, 20, 25, 25, 20], [3, 4, 8], [2, 2], [10, 20, 5, 6, 9], [3, 4, 8], [2, 2], [20, 40, 50, 45, 45], [10, 20, 5, 6, 9], [1, 1, 1, 1, 1], [20, 40, 50, 45, 45], [10, 20, 25, 25, 20], [3, 4, 8]]
Rk = [0.99, 0.999, 0.9999, 0.9999, 0.99999, 0.99, 0.99999, 0.9999, 0.999999, 0.999, 0.99, 0.999, 0.9999, 0.9999, 0.99999]
Tk = [80, 10, 100, 100, 5, 8, 80, 5, 8, 100, 80, 10, 100, 100, 5]
Bk = [1, 3, 4, 1, 2, 3, 2, 2, 4, 1, 4, 4, 2, 3, 1]

# paramete of model
t0 = 1
alpha, beta = 0.65, 0.35
