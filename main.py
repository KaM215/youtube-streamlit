import streamlit as st
import numpy as np
import pandas as p
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')                                                             #テキストの追加

#Display media
st.write('Display Image')
img = Image.open('柴犬唐草模様.jpg')
st.image(img, caption='Test Image', use_column_width=True)                        #use_column_width=TrueはWeb画面のサイズに合わせて表示

#Display
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# #Display charts
# st.line_chart(df)                                                               #折れ線グラフの作成
# st.area_chart(df)
# st.bar_chart(df)                                                                #棒グラフ


# #Map
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)
























# st.write(df)                                                                    #表(df)を画面出力

# st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)             #表(df)を画面出力_表の縦・横の長さを指定可能になる

# st.table(df.style.highlight_max(axis=0))                                        #表(df)を画面出力_静定な表を表示したい場合にしよう（ソートができない）


# """
# # 章
# ## 節
# ### 項

# ```python                                                                       #pythonのコードを画面に書く際の書き方
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```


# """