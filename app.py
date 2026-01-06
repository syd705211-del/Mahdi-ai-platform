import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Saeed AI", layout="wide")

st.title("🤖 منصة سعيد للذكاء الاصطناعي")
st.markdown("منصة مجانية للتجربة")

task = st.sidebar.selectbox(
    "اختر الخدمة",
    ["دردشة ذكية", "كتابة محتوى", "تلخيص نصوص", "إعادة صياغة"]
)

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

model = load_model()

if task == "دردشة ذكية":
    user_input = st.text_area("اكتب سؤالك هنا")
    if st.button("إرسال"):
        result = model(user_input, max_length=150)
        st.success(result[0]['generated_text'])

elif task == "كتابة محتوى":
    topic = st.text_input("اكتب عنوان الموضوع")
    if st.button("اكتب"):
        result = model(f"اكتب مقال عن {topic}", max_length=200)
        st.write(result[0]['generated_text'])

elif task == "تلخيص نصوص":
    text = st.text_area("الصق النص هنا")
    if st.button("لخّص"):
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=100)
        st.write(summary[0]['summary_text'])

elif task == "إعادة صياغة":
    text = st.text_area("الصق النص لإعادة الصياغة")
    if st.button("إعادة صياغة"):
        result = model(f"أعد صياغة النص التالي:\n{text}", max_length=200)
        st.write(result[0]['generated_text'])
