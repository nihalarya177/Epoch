import pandas as pd
from pycaret.classification import *
import streamlit as st
import os
from streamlit.components.v1.components import declare_component
import streamlit.components.v1 as components
from pathlib import Path

dir_dict = {'distplots_nums.html':'Distrubution Plot',
            'heatmaps.html':'Correlation Heatmap',
            'kde_plots.html':'KDE Plot', 
            'pair_scatters.html':'Paired Scatter Plot',
            'scatterplots.html':'Scatter Plot',
            'violinplots.html':'Violin Plot'}

info_dict = {'heatmaps.html':['A correlation heatmap is a way of showing how two things are related to each other. A correlation heatmap is like a picture made up of little boxes, or cells. Each cell shows a different level of correlation between two things. Each cell would show how strongly the row and columns are related. The colour is to differentiate between 1 and -1. 1 indicates that if one increases the other increases and -1 indicates that if one decreases the other increases and vice versa. The stronger the colour, the stronger they are related', 2]}

def launch_eda(df):

    exp_name = setup(data=df, target='species', session_id=123)

    eda(display_format='html')

    path = 'AutoViz_Plots/species/'
    dir_list = os.listdir(path)
    col1, col2 = st.columns([2, 1], gap="small")
    for i in range(len(dir_list)):
        HTMLFile = open("AutoViz_Plots/species/"+dir_list[i], "r")
        report = HTMLFile.read()
        with col1:
                components.html(report, height = 600)
        with col2:
                st.subheader(dir_dict[dir_list[i]])
                st.write(info_dict[dir_list[i][0]])
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")

