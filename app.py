import streamlit as st
import base64

# إعداد الصفحة
st.set_page_config(
    page_title="منصة مهدي للذكاء الاصطناعي",
    page_icon="🤖",
    layout="centered"
)

# شعار SVG (محوّل إلى Base64)
svg_logo = """
<svg width="140" height="140" viewBox="0 0 140 140" xmlns="http://www.w3.org/2000/svg">
  <circle cx="70" cy="70" r="68" fill="#0f172a"/>
  <text x="70" y="62" text-anchor="middle" font-size="42">🤖</text>
  <text x="70" y="98" text-anchor="middle"
        font-size="14" fill="#e5e7eb"
        font-family="Arial, Helvetica, sans-serif">
    Mahdi AI
  </text>
</svg>
"""

logo_base64 = base64.b64encode(svg_logo.encode("utf-8")).decode("utf-8")

# عرض الشعار
st.markdown(
    f"""
    <div style="text-align:center; margin-top:20px;">
        <img src="data:image/svg+xml;base64,{logo_base64}" width="140"/>
    </div>
    """,
    unsafe_allow_html=True
)

# اسم المنصة
st.markdown(
    "<h1 style='text-align:center;'>منصة مهدي للذكاء الاصطناعي</h1>",
    unsafe_allow_html=True
)

# اسم المطور
st.markdown(
    "<p style='text-align:center; font-size:16px;'>"
    "تطوير: عبدالرزاق مهدي"
    "</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# واجهة الدردشة (تجريبية)
st.write("🤖 ذكاء اصطناعي تجريبي – بدون تسجيل")

user_input = st.text_input("اكتب سؤالك هنا:")

if user_input:
    st.success("تم استلام سؤالك ✔️ (سيتم ربط نموذج ذكي لاحقًا)")
