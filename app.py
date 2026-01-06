import streamlit as st

# إعداد الصفحة
st.set_page_config(
    page_title="منصة مهدي للذكاء الاصطناعي",
    page_icon="🤖",
    layout="centered"
)

# عرض الشعار والاسم
st.image("logo.png", width=120)

st.markdown(
    "<h1 style='text-align: center;'>منصة مهدي للذكاء الاصطناعي</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size:16px;'>"
    "تطوير: عبدالرزاق مهدي"
    "</p>",
    unsafe_allow_html=True
)

st.markdown("---")
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Mahdi AI", page_icon="🤖")

st.title("🤖 Mahdi AI")
st.write("ذكاء اصطناعي مجاني – يعمل بدون تسجيل وبدون دفع")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

user_input = st.text_input("اكتب سؤالك هنا:")

if user_input:
    with st.spinner("يفكّر..."):
        result = generator(
            user_input,
            max_length=100,
            num_return_sequences=1
        )
        st.success(result[0]["generated_text"])
