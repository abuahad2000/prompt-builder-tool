import streamlit as st

# 1. إعداد الصفحة (عنوان، أيقونة، وتخطيط عريض)
st.set_page_config(
    page_title="مُنشئ البرومبت الاحترافي",
    layout="wide",
    page_icon="🎨"
)

# 2. تنسيق CSS لدعم اللغة العربية (من اليمين لليسار) وتجميل الواجهة
st.markdown("""
<style>
    /* محاذاة النصوص والقوائم لليمين */
    .stSelectbox, .stTextInput, .stMarkdown, .stButton {
        direction: rtl;
        text-align: right;
    }
    div[data-testid="stMarkdownContainer"] p {
        font-size: 1.2rem;
        direction: rtl;
    }
    /* تنسيق العناوين في المنتصف */
    h1, h2, h3 {
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2c3e50;
    }
    /* تنسيق الأعمدة */
    div[data-testid="column"] {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin: 5px;
    }
</style>
""", unsafe_allow_html=True)

# 3. عنوان التطبيق
st.title("🎨 مُنشئ البرومبت الاحترافي (Midjourney Prompt Builder)")
st.markdown("---")

# 4. قاعدة البيانات (Dictionary) - تشمل 6 أقسام كما في الإكسيل
data = {
    "1️⃣ الشخصية (Subject)": {
        "": "",
        "رجل أعمال": "Businessman",
        "شابة عربية": "Young Arab woman",
        "طفل صغير": "Little child",
        "رجل عجوز": "Elderly man",
        "مودل أزياء": "Fashion model",
        "محارب قديم": "Ancient warrior",
        "رائد فضاء": "Astronaut"
    },
    "2️⃣ الملابس (Outfit)": {
        "": "",
        "بدلة رسمية": "Formal suit",
        "عباءة سوداء": "Black Abaya",
        "ملابس كاجوال": "Casual clothes",
        "فستان أنيق": "Elegant dress",
        "جاكيت جلد": "Leather jacket",
        "زي تقليدي": "Traditional outfit",
        "ملابس رياضية": "Sportswear"
    },
    "3️⃣ الوضعية (Pose)": {
        "": "",
        "واقفة بثقة": "Standing confidently",
        "جالسة على كرسي": "Sitting on a chair",
        "لقطة قريبة للوجه": "Close-up portrait",
        "زاوية جانبية": "Side profile",
        "تمشي في الشارع": "Walking in the street",
        "تنظر للكاميرا": "Looking at camera"
    },
    "4️⃣ التعبير (Expression)": {
        "": "",
        "ابتسامة خفيفة": "Slight smile",
        "نظرة حادة": "Sharp look",
        "ضحكة عفوية": "Candid laughter",
        "هادئة": "Calm",
        "مندهشة": "Surprised",
        "جادة": "Serious",
        "حالمة": "Dreamy look"
    },
    "5️⃣ الإضاءة (Lighting)": {
        "": "",
        "إضاءة ذهبية": "Golden Hour lighting",
        "إضاءة نيون": "Neon lighting",
        "ظلال ناعمة": "Soft shadows",
        "إضاءة استوديو": "Studio lighting",
        "إضاءة درامية": "Dramatic lighting",
        "إضاءة طبيعية": "Natural light",
        "إضاءة سينمائية": "Cinematic lighting"
    },
    "6️⃣ الستايل (Style)": {
        "": "",
        "سينمائي": "Cinematic",
        "فيلم كوداك": "Kodak Portra 400",
        "أبيض وأسود": "Black and White",
        "واقعية فائقة": "Hyper-realistic",
        "أنمي": "Anime style",
        "رسم زيتي": "Oil painting",
        "سايبر بانك": "Cyberpunk style",
        "تصوير فوتوغرافي": "Photography"
    }
}

# 5. بناء الواجهة (6 أعمدة)
# نستخدم reversed لعكس الترتيب ليتناسب مع اتجاه العين العربية (يمين لليسار)
cols = st.columns(6)
keys = list(data.keys())
selections = {}

for i, col in enumerate(reversed(cols)):
    category = keys[i]
    with col:
        # عنوان صغير لكل عمود
        st.markdown(f"### {category.split(' ')[1]}")
        # القائمة المنسدلة
        choice = st.selectbox(
            label=category,
            options=list(data[category].keys()),
            key=category,
            label_visibility="collapsed" # إخفاء العنوان المكرر
        )
        if choice:
            selections[category] = data[category][choice]

st.markdown("---")

# 6. زر التكوين والعرض
col1, col2, col3 = st.columns([1, 2, 1]) # تنسيق لتوسط الزر

with col2:
    if st.button("✨ إنشاء البرومبت (Generate Prompt)", type="primary", use_container_width=True):
        
        # تجميع القيم الإنجليزية المختارة
        # نستخدم الترتيب الأصلي للمفاتيح (keys) لضمان ترتيب الجملة الصحيح (شخصية -> ملابس -> وضعية...)
        final_prompt_parts = []
        for key in keys:
            if key in selections and selections[key]:
                final_prompt_parts.append(selections[key])
        
        final_prompt = ", ".join(final_prompt_parts)
        
        if final_prompt:
            st.success("تم تجهيز البرومبت بنجاح! 👇")
            # st.code يعرض النص في صندوق يسهل نسخه بضغطة زر
            st.code(final_prompt, language="text")
        else:
            st.warning("⚠️ يرجى اختيار عنصر واحد على الأقل من القوائم.")

# تذييل الصفحة
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>تم التطوير باستخدام Python & Streamlit 🚀</div>", unsafe_allow_html=True)
