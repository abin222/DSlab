# You are given a sequence of n songs where the ith song is `i minutes long. You
# want to place all of the songs on an ordered series of CDs (e.g. CD 1, CD 2, CD
# 3,…., CDk) where each CD can hold m minutes. Furthermore,
# (1) The songs must be recorded in the given order, song 1, song 2, . . . , song n.
# (2) All songs must be included.
# (3) No song may be split across CDs.
# Your goal is to determine how to place them on the CDs as to minimize the
# number of CDs needed. Give the most efficient algorithm you can to find an
# optimal solution for this problem, prove the algorithm is correct and analyze the
# time complexity.

t_d=10
td1=10
n_s=10
i=1
def greedy_alg(n_cd,t_d,n_s):
    if(n_s<=t_d):
        t_d=t_d-n_s
        n_s+=1
        print("duration:",t_d)
    else:
        t_d=td1
        greedy_alg(n_cd+1,t_d,n_s)
    if(t_d<10 and n_s<10):
        greedy_alg(n_cd,t_d,n_s)
    if(t_d<=0):
        t_d=td1
        print("songs:",n_s)
        greedy_alg(n_cd+1,t_d,n_s)
    if(n_s==10):
        print(n_cd)
greedy_alg(0,10,1)