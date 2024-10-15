import streamlit as st
import openai


CHATGPT_API_KEY = st.secrets["openai"]["api_key"]
openai.api_key = CHATGPT_API_KEY

animal_list = ['犬', '猫', '人間', 'ハムスター', '魚', '爬虫類', '虫']
gender_list = ['オス', 'メス', 'オカマ', '答えたくない']


#chatGPT使用によるネーミング
def generate_name(animal, gender, color, character):
    res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": f"性別{gender}の{animal}に名前を付けようと思っています。色は{color}で性格は{character}です。10個の名前の候補をあげてください。6,7,8は日本人のフルネームのようにしてください。また、9はとても長い名前にしてください。10は必殺技のような名前にしてください。解説はせず、名前だけ答えてください。"
        },
    ],
    )
    return res["choices"][0]["message"]["content"]

st.title('ペットネーミング')
st.caption('性別、イメージカラー、特徴を選んで名前の案を10つ提案します')

with st.form(key='form'):
    selected_animal = st.selectbox("動物を選択してください", animal_list)
    selected_gender = st.radio('性別を選択してください', gender_list)
    selected_color = st.color_picker('イメージカラーを指定してください')
    selected_character = st.multiselect(
        '特徴を選んでください',
        ('かっこいい', 'かわいい', '優しい','オシャレ', '大人しい', '小賢しい', '賢い', '優柔不断', '反社会的')
        )

    submit_btn = st.form_submit_button('ネーミング')

if(submit_btn):
    names = generate_name(animal=selected_animal, gender=selected_gender, color=selected_color, character=selected_character)
    st.text('名前を生成しました')
    for name in names.split(','):
        st.code(name)
