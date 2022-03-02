import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!'

left_column,right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ1内容を書く')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせ2内容を書く')
expander3=st.expander('問い合わせ3')
expander3.write('問い合わせ3内容を書く')

text=st.text_input('あなたの趣味を教えて下さい')


option=st.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1,11)),
)

'あなたの趣味:',text
'あなたの好きな数字は',option,'です'
# if st.checkbox('Show Image'):
#     img=Image.open('猪肉2.png')
#     st.image(img,caption='イノシシ肉',use_column_width=True)

df=pd.DataFrame(np.random.rand(100,2)/[50,50]+[35.69,139.70],columns=['lat','lon'])

st.map(df)

condition=st.slider('あなたの今の調子は？',0,100,50)
'コンディション:',condition