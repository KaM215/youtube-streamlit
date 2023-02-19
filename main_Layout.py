import streamlit as st
import numpy as np
import pandas as p
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

#######################################################################
#sidebarに表示
#######################################################################
text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味 :', text
'コンディション ：', condition


#######################################################################
#(n)column
#######################################################################
left_column, right_column = st.columns(2)                                   #st.colums(n)を定義することで(n)個分のカラムを作成
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


#######################################################################
#expande
#######################################################################
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')