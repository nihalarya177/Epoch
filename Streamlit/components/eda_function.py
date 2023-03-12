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

