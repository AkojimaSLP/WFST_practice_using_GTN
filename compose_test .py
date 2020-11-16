# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:46:56 2020

@author: a-kojima
"""

import gtn

if __name__ == "__main__":
    
    # ============================================
    # params
    # ============================================
    is_grad = True
    
    # ============================================
    # WFST G: trunsduce words to sequence of words
    # ============================================
    
    id2words = {0:'赤',
                1:'青',
                2:'黒'}
    
    words2id = {'赤':0,
                '青':1,
                '黒':2}

    
    # whether gradien needs or not
    G = gtn.Graph(is_grad)        
    
    G.add_node(True, False) # start node
    G.add_node(False, True) # accept node   

    G.add_arc(0, 1, 0, 0, weight=0.2)
    G.add_arc(0, 1, 1, 1, weight=0.8)
    gtn.draw(G, "G.pdf", id2words)    
    
    # ============================================
    # WFST L: trunsduce phone to worrds
    # ============================================
    # speller
    
    id2phones = {0: 'a',
                 1: 'k',
                 2: 'o',
                 3: 'r',
                 4: 'u'}

    phones2id = {'a':0,
                 'k':1,
                 'o':2,
                 'r':3,
                 'u':4}
    
    L = gtn.Graph(is_grad)
    
    # start node    
    L.add_node(True, False) # 0
    
    # aka
    L.add_node() #1       
    L.add_node() #2   
    L.add_node(False, True) #3

    # ao    
    L.add_node(False, True) #4
    
    # kuro    
    L.add_node()    #5
    L.add_node()    #6    
    L.add_node()      #7
    L.add_node(False, True) #8
        
    L.add_arc(0, 1, phones2id['a'], gtn.epsilon, weight=0.5)
    L.add_arc(1, 4, phones2id['o'], words2id['青'], weight=0.2)    
    
    L.add_arc(1, 2, phones2id['k'], gtn.epsilon, weight=0.7)    
    L.add_arc(2, 3, phones2id['a'], words2id['赤'], weight=0.6)        
    
    L.add_arc(0, 5, phones2id['k'], gtn.epsilon, weight=0.3)
    L.add_arc(5, 6, phones2id['u'], gtn.epsilon, weight=0.4)    
    L.add_arc(6, 7, phones2id['r'], gtn.epsilon, weight=0.1)        
    L.add_arc(7, 8, phones2id['o'], words2id['黒'], weight=0.5)            
    
    gtn.draw(L, "L.pdf",  id2phones, id2words)        



    # ============================================
    # compose
    # ============================================
    compose = (gtn.compose(L, G))
    gtn.draw(compose, "compose.pdf",  id2phones, id2words)    