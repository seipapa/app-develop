# from matplotlib.pyplot import text
# from matplotlib.style import use
import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 入門')

#データ羅列＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#st.write('DataFrame')

#df = pd.DataFrame({
    #'1列目':[1,2,3,4],
    #'2列目':[10,20,30,40]
#})

#st.write(df)

#st.dataframe(df.style.highlight_max(axis = 0), width=10000 , height=10000)
##縦と横を引数にできるのはdataframeだけ
##highlightでpandasに用意されている機能で、dataframeである

#st.table(df.style.highlight_max(axis = 0))
##tableでソートはできないが、しっかり表としているもの


##マジックコマンド＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

"""
# 章

## 説

### 項

'''python
import streamlit as st
import numpy as np
import pandas as pd
'''

"""
##マークダウン記法、テキストデータを


##グラフ作成＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#df = pd.DataFrame(
    #np.random.rand(20,3),
    #columns=['a','b','c']
#)
#st.line_chart(df)
##線グラフ

#st.area_chart(df)
#塗りつぶしグラフ

#st.bar_chart(df)
#棒グラフ

##mapのプロット====================================

#   df = pd.DataFrame(
#      np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
#)

#st.map(df)

##画像の表示===================================
# st.write('Desplay Image')

# img = Image.open('sample.jpg')

# if st.checkbox('Show image'):
#     ##チェックボックスの作成,チェックボックス作成できる

#     st.image(img,caption='Children', use_column_width= True)
#     ##usecolumn widthは実際の横幅に合わせて表示してくれる


##相互関係ウィジェット=========================
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、',option, 'です。'
# ##ボックスを選択した値が出力できる

# st.write('Intaractive Widgets')

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は、',text, 'です。'

# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション:',condition

#====================================================
##レイアウトを整える、サイドバー、2カラム、エキスパンダー

#サイドバー
# st.sidebar.write('Intaractive Widgets')

# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
# 'あなたの趣味:',text
# 'コンディション:',condition

#2カラムウィジェット

# st.write('Intaractive Widgets')

# left_column,right_column = st.columns(2)
# ##Please replace st.beta_columns with st.columns.
# #st.beta_columns will be removed after 2021-11-02.


# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラムです')

# ##エクスパンダー
# expander1 = st.expander('問い合わせ1')
# # Please replace st.beta_expander with st.expander.

# # st.beta_expander will be removed after 2021-11-02.

# expander1.write('問い合わせ1回答')
# expander2 = st.expander('問い合わせ2')
# expander2.write('問い合わせ2回答')
# expander3 = st.expander('問い合わせ3')
# expander3.write('問い合わせ3回答')

##プログレスバーの公開

st.write('プログレスバーの表示')
'Start!!'

latest_iteration= st.empty()
bar = st.progress(0)
##プログレスバー

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column,right_column = st.columns(2)
##Please replace st.beta_columns with st.columns.
#st.beta_columns will be removed after 2021-11-02.


button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
# Please replace st.beta_expander with st.expander.

# st.beta_expander will be removed after 2021-11-02.

expander1.write('問い合わせ1回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3回答')
