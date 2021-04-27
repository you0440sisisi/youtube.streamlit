import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
      latest_iteration.text(f'Iteration {i + 1}')
      bar.progress(i + 1)
      time.sleep(0.3)
      
'Done!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
    
expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ回答1')
expander1 = st.beta_expander('問い合わせ2')
expander1.write('問い合わせ回答2')
expander1 = st.beta_expander('問い合わせ3')
expander1.write('問い合わせ回答3')
# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は?',0,100,50)
# '私の趣味は', text,'です'
# 'コンディション', condition,
# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='Youto Uenishi', use_column_width=True)



# df = pd.DataFrame(
 #   np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
  #  columns=['lat','lon']
#)
#st.dataframe(df.style.highlight_max(axis=0))
#st.map(df) 