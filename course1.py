# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:41:46 2019
@author: huyuxin
这是大段的注释
今天学习1.定义函数 和 2.调用
"""
import math
import numpy as np  # 这里的as就是起个昵称，一般为了简化代码


# 定义一个生成网络的方法
# num 代表网络中有多少节点
# prob 代表节点与节点之间相连的概率
"""
表示这个网络的方法之一是构建一个领接矩阵 0表示没有连接 1表示已连接
这个矩阵是对称的，所以生成时只需要遍历一次
  0 1 2 3 4 5... n
0 1 1 0 1 0 0... 1
1 1 1 0
2 0 1 1 
3 1
4 0
5 0
...
n 1
"""

def generate_node(num, prob):
    graph = np.eye(num,k=0) # numpy.eye()方法生成对角阵，默认k=0,表示对角线不平移
    i = 0
    j = 0
    for i in range(num-1):    # range(x) 是python的原生语法，代表生成一个从0 到x-1的序列 这是python 最简单的for循环写法
        for j in range(i+1,num): # range(x,y) 代表生成从x到y-1间隔为1的序列
            flag = np.random.uniform()  # 从0~1的均匀分布中生成一个随机数 如果小于我们设定的阈值则连接
            if flag<prob:
                graph[i][j] = 1
                graph[j][i] = 1
    return graph


if __name__ =='__main__': # 这一句代码如果在pycharm中将在左侧出现一个绿色的启动按钮，在整体执行代码时，这一句是起点
    node_num = 10
    link_prob = 0.5
    G = generate_node(node_num, link_prob)
    print(G)


