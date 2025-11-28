import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(
    page_title="مُنشئ البرومبت الشامل",
    layout="wide",
    page_icon="🎨"
)

# 2. تنسيق CSS (العربية + تحسين التبويبات)
st.markdown("""
<style>
    .stSelectbox, .stTextInput, .stMarkdown, .stButton { direction: rtl; text-align: right; }
    div[data-testid="stMarkdownContainer"] p { direction: rtl; }
    h1, h2, h3 { text-align: center; color: #2c3e50; }
    /* تنسيق التبويبات */
    button[data-baseweb="tab"] { font-size: 18px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🎨 مُنشئ البرومبت الشامل (All-in-One Builder)")
st.markdown("---")

# 3. إنشاء التبويبات الثلاثة
tab1, tab2, tab3 = st.tabs(["📸 صور أشخاص (Photography)", "🛍️ منتجات (Products)", "🎥 فيديو (Video)"])

# ==============================================================================
# التبويب الأول: صور الأشخاص
# ==============================================================================
with tab1:
    st.header("إعدادات صور الأشخاص")
    
    # بيانات الصور
    data_photo = {
        "1️⃣ الشخصية": {"": "", "رجل أعمال": "Businessman", "شابة عربية": "Young Arab woman", "طفل صغير": "Little child", "رجل عجوز": "Elderly man", "مودل أزياء": "Fashion model"},
        "2️⃣ الملابس": {"": "", "بدلة رسمية": "Formal suit", "عباءة سوداء": "Black Abaya", "ملابس كاجوال": "Casual clothes", "فستان أنيق": "Elegant dress"},
        "3️⃣ الوضعية": {"": "", "واقفة بثقة": "Standing confidently", "جالسة على كرسي": "Sitting on a chair", "لقطة قريبة": "Close-up portrait"},
        "4️⃣ التعبير": {"": "", "ابتسامة خفيفة": "Slight smile", "نظرة حادة": "Sharp look", "ضحكة عفوية": "Candid laughter"},
        "5️⃣ الإضاءة": {"": "", "إضاءة ذهبية": "Golden Hour lighting", "إضاءة نيون": "Neon lighting", "ظلال ناعمة": "Soft shadows"},
        "6️⃣ الستايل": {"": "", "سينمائي": "Cinematic", "فيلم كوداك": "Kodak Portra 400", "واقعية فائقة": "Hyper-realistic"}
    }
    
    cols = st.columns(6)
    sel_photo = {}
    for i, (cat, opts) in enumerate(data_photo.items()):
        with cols[5-i]: # عكس الترتيب
            choice = st.selectbox(cat, list(opts.keys()), key=f"photo_{i}")
            if choice: sel_photo[cat] = opts[choice]

    if st.button("✨ إنشاء برومبت الصور", key="btn_photo", type="primary", use_container_width=True):
        final = ", ".join(sel_photo.values())
        if final: st.success("تم!"); st.code(final, language="text")
        else: st.warning("اختر عنصراً واحداً على الأقل.")

# ==============================================================================
# التبويب الثاني: المنتجات
# ==============================================================================
with tab2:
    st.header("إعدادات تصوير المنتجات")
    
    # بيانات المنتجات
    data_prod = {
        "1️⃣ نوع المنتج": {"": "", "زجاجة عطر": "Perfume bottle", "علبة كريم": "Cream jar", "حذاء رياضي": "Sneaker", "ساعة يد": "Luxury watch"},
        "2️⃣ الخامة": {"": "", "زجاج شفاف": "Transparent glass", "بلاستيك غير لامع": "Matte plastic", "معدن ذهبي": "Gold metal", "خشب طبيعي": "Natural wood"},
        "3️⃣ الخلفية": {"": "", "منصة رخامية": "Marble podium", "خلفية ملونة سادة": "Solid color background", "في الطبيعة": "In nature", "طرطشة ماء": "Water splash"},
        "4️⃣ اللقطة": {"": "", "زاوية المنتج (هيرو)": "Hero shot", "من الأعلى (فلات لاي)": "Flat lay", "لقطة تفصيلية": "Macro detail"}
    }
    
    cols = st.columns(4)
    sel_prod = {}
    for i, (cat, opts) in enumerate(data_prod.items()):
        with cols[3-i]:
            choice = st.selectbox(cat, list(opts.keys()), key=f"prod_{i}")
            if choice: sel_prod[cat] = opts[choice]

    if st.button("🛍️ إنشاء برومبت المنتجات", key="btn_prod", type="primary", use_container_width=True):
        final = ", ".join(sel_prod.values())
        if final: st.success("تم!"); st.code(final, language="text")
        else: st.warning("اختر عنصراً واحداً على الأقل.")

# ==============================================================================
# التبويب الثالث: الفيديو
# ==============================================================================
with tab3:
    st.header("إعدادات الفيديو السينمائي")
    
    # بيانات الفيديو
    data_vid = {
        "1️⃣ حركة الكاميرا": {"": "", "كاميرا ثابتة": "Static Camera", "تحرك بطيء": "Slow Motion", "دوران حول الهدف": "Orbit shot", "تحليق درون": "Drone shot"},
        "2️⃣ العدسة": {"": "", "عدسة 35 ملم": "35mm lens", "عدسة واسعة": "Fisheye lens", "جودة 4K": "4K resolution"},
        "3️⃣ الجو العام": {"": "", "ضبابي وغامض": "Foggy and mysterious", "مشرق وحيوي": "Bright and energetic", "تقني ومستقبلي": "Tech and futuristic"}
    }
    
    cols = st.columns(3)
    sel_vid = {}
    for i, (cat, opts) in enumerate(data_vid.items()):
        with cols[2-i]:
            choice = st.selectbox(cat, list(opts.keys()), key=f"vid_{i}")
            if choice: sel_vid[cat] = opts[choice]

    if st.button("🎥 إنشاء برومبت الفيديو", key="btn_vid", type="primary", use_container_width=True):
        final = ", ".join(sel_vid.values())
        if final: st.success("تم!"); st.code(final, language="text")
        else: st.warning("اختر عنصراً واحداً على الأقل.")
