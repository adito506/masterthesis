import numpy as np
import random as rnd
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from seller import Seller
from buyer import Buyer

population_seller = 10
population_buyer = 10
average_degree = 8          # Average degree of social network
num_episode = 1

class Simulation(Buyer, Seller):
    
    def __init__(self, population_seller, population_buyer,average_degree):
        self.sellers = self.__generate_sellers(population_seller, population_buyer, average_degree)
        self.initial_honest_sellers = self.__choose_initial_honest_sellers()
        self.buyers = self.__generate_buyers(population_seller, population_buyer, average_degree)
        self.initial_simple_buyers = self.__choose_initial_simple_buyers()
        super().__init__()


    def __generate_buyers(self, population_seller, population_buyer, average_degree):
        rearange_edges = int(average_degree*0.5)
        self.network_buyer = nx.barabasi_albert_graph(population_seller, rearange_edges)#buyerの取引相手のnodeなのでseller
        #num_buyers = int(population_buyer)

        buyers = [Buyer() for id in range(population_seller)]#rangeで0~populationまでの数字をAgentに割り付ける
        for index, focal_buyer in enumerate(buyers):#enumerateでforループの中のリストやタプルにインデックス番号をつける
            next_buyers_id = list(self.network_buyer[index])
            for nb_id in next_buyers_id:
                focal_buyer.next_buyers_id.append(nb_id)#appendで末尾に要素を追加
        return buyers

    def __generate_sellers(self, population_seller, population_buyer, average_degree):
        rearange_edges = int(average_degree*0.5)
        self.network_seller = nx.barabasi_albert_graph(population_buyer, rearange_edges)#sellerの取引相手のnodeなのでbuyer
        #num_sellers = int(population_seller)

        sellers = [Seller() for id in range(population_seller)]#rangeで0~populationまでの数字をAgentに割り付ける
        for index, focal_seller in enumerate(sellers):#enumerateでforループの中のリストやタプルにインデックス番号をつける
            next_sellers_id = list(self.network_seller[index])
            for nb_id in next_sellers_id:
                focal_seller.next_sellers_id.append(nb_id)#appendで末尾に要素を追加
        
        return sellers



    def __generate_buyers(self, population_seller, population_buyer, average_degree):
        rearange_edges = int(average_degree*0.5)
        self.network_buyer = nx.barabasi_albert_graph(population_seller, rearange_edges)#buyerの取引相手のnodeなのでseller
        #num_buyers = int(population_buyer)

    def __choose_initial_honest_sellers(self):
        #population = len(population_seller)
        self.initial_honest_sellers = rnd.sample(range(population_seller), k = int(population_seller/2))


    def __choose_initial_simple_buyers(self):
        #population = len(population_buyer)
        self.initial_simple_buyers = rnd.sample(range(population_buyer), k = int(population_buyer/2))



s = Simulation(population_seller, population_buyer,average_degree)
x = s.sellers
print(x)
print(population_buyer)
# print(Simulation.__mro__)
