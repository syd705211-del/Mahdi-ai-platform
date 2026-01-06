import streamlit as st
from transformers import pipeline
import urllib.parse

# =========================
# إعداد الصفحة
# =========================
st.set_page_config(
    page_title="منصة مهدي للذكاء الاصطناعي",
    page_icon="🤖",
    layout="centered"
)

# =========================
# CSS احترافي
# =========================
st.markdown("""
<style>
header {visibility: hidden;}
.footer {visibility: hidden;}

.app-header {
    text-align: center;
    padding: 10px;
}
.app-header img {
    width: 110px;
}
.app-title {
    font-size: 28px;
    font-weight: bold;
}
.app-sub {
    font-size: 15px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# =========================
# الهيدر (الشعار + الاسم)
# =========================
st.markdown("""
<div class="app-header">
    <img src="https://raw.githubusercontent.com/syd7c/your-repo-name/main/logo.png">
    <div class="app-title">منصة مهدي للذكاء الاصطناعي</div>
    <div class="app-sub">تطوير: عبدالرزاق مهدي</div>
</div>
<hr>
""", unsafe_allow_html=True)

# =========================
# اختيار اللغة
# =========================
language = st.selectbox(
    "🌐 اختر اللغة",
    ["العربية", "English"]
)

# =========================
# تحميل النموذج
# =========================
@st.cache_resource
def load_model(lang):
    if lang == "العربية":
        return pipeline("text-generation", model="aubmindlab/aragpt2-base")
    else:
        return pipeline("text-generation", model="gpt2")

generator = load_model(language)

# =========================
# الإدخال
# =========================
if language == "العربية":
    user_input = st.text_area("✍️ اكتب سؤالك أو موضوعك:", height=120)
else:
    user_input = st.text_area("✍️ Write your question:", height=120)

if user_input:
    with st.spinner("🤖 يفكّر..."):
        result = generator(
            user_input,
            max_length=200,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8,
            num_return_sequences=1
        )

    st.success(result[0]["generated_text"])

# =========================
# زر مشاركة واتساب
# =========================
app_url = "https://your-app-name.streamlit.app"
whatsapp_text = f"جرب منصة مهدي للذكاء الاصطناعي 👇\n{app_url}"
whatsapp_link = "https://wa.me/?text=" + urllib.parse.quote(whatsapp_text)

st.markdown(f"""
<a href="{whatsapp_link}" target="_blank">
    <button style="
        background-color:#25D366;
        color:white;
        padding:10px 18px;
        border:none;
        border-radius:6px;
        font-size:16px;
        cursor:pointer;
    ">
    📲 شارك على واتساب
    </button>
</a>
""", unsafe_allow_html=True)

# =========================
# فوتر
# =========================
st.markdown("""
<hr>
<p style="text-align:center; font-size:13px;">
© 2026 منصة مهدي للذكاء الاصطناعي
</p>
""", unsafe_allow_html=True)
