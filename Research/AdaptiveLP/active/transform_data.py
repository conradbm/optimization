# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:48:38 2019

@author: bmccs
"""

import numpy as np
import pandas as pd
import pickle

with open("raw_data.pkl", "rb") as handle:
    memory=pickle.load(handle)


# Construct real dataset
i=0
num_games = len(memory['states'])
unique_states={}
unique_actions={}
main_df=pd.DataFrame({'state':[],'action':[],'reward':[]})
main_df.state = main_df.state.astype('str', copy=False)
for i in range(num_games):
    states=memory['states'][i]
    actions=memory['actions'][i]
    rewards=memory['rewards'][i]
    df=pd.DataFrame({'state':states,'action':actions,'reward':rewards})
    df.state = df.state.astype('str', copy=False)
    main_df = pd.concat([main_df, df], axis=0)

# Reshape into tableau
main_df.pivot_table(values='reward', index=['state'], columns='action', aggfunc='mean')
main_df=main_df.fillna(-100).copy()

main_df.to_csv("clean_data.csv", index=False)