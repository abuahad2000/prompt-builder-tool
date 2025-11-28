import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(
    page_title="مُنشئ البرومبت الاحترافي v2",
    layout="wide",
    page_icon="🎨"
)

# 2. تنسيق CSS
st.markdown("""
<style>
    .stSelectbox, .stTextInput, .stMarkdown, .stButton, .stSlider { direction: rtl; text-align: right; }
    div[data-testid="stMarkdownContainer"] p { direction: rtl; }
    h1, h2, h3, h4 { text-align: center; color: #2c3e50; font-family: sans-serif; }
    .stCode { direction: ltr !important; text-align: left !important; }
</style>
""", unsafe_allow_html=True)

st.title("🎨 مُنشئ البرومبت الاحترافي (Midjourney Pro Builder)")
st.markdown("---")

# --- بيانات مشتركة (الأبعاد) ---
ar_options = {
    "مربع (1:1) - انستقرام": "--ar 1:1",
    "طولي (9:16) - ستوري/تيك توك": "--ar 9:16",
    "عرضي (16:9) - يوتيوب/سينمائي": "--ar 16:9",
    "بورتريه (4:5) - فوتوغرافي": "--ar 4:5",
    "لاندسكيب (3:2) - كلاسيك": "--ar 3:2"
}

# --- التبويبات ---
tab1, tab2, tab3 = st.tabs(["📸 صور أشخاص (Photography)", "🛍️ منتجات (Products)", "🎥 فيديو (Video)"])

# ==============================================================================
# التبويب الأول: صور الأشخاص
# ==============================================================================
with tab1:
    st.header("📸 إعدادات التصوير الفوتوغرافي")
    
    # القوائم (تم تنسيقها رأسياً لمنع أخطاء النسخ)
    data_photo = {
        "1️⃣ الشخصية": {
            "": "",
            "رجل أعمال": "Businessman",
            "شابة عربية": "Young Arab woman",
            "طفل صغير": "Little child",
            "رجل عجوز": "Elderly man",
            "مودل أزياء": "Fashion model",
            "سايبورغ": "Cyborg",
            "شخصية خيالية": "Fantasy character"
        },
        "2️⃣ الملابس": {
            "": "",
            "بدلة رسمية": "Formal suit",
            "عباءة سوداء": "Black Abaya",
            "ملابس كاجوال": "Casual clothes",
            "فستان أنيق": "Elegant dress",
            "جاكيت جلد": "Leather jacket",
            "زي فضائي": "Space suit"
        },
        "3️⃣ الوضعية": {
            "": "",
            "واقفة بثقة": "Standing confidently",
            "جالسة على كرسي": "Sitting on a chair",
            "لقطة قريبة جداً": "Extreme close-up",
            "من الخلف": "View from behind",
            "زاوية منخفضة": "Low angle shot"
        },
        "4️⃣ التعبير": {
            "": "",
            "ابتسامة خفيفة": "Slight smile",
            "نظرة حادة": "Sharp look",
            "ضحكة عفوية": "Candid laughter",
            "وجه خالي من التعبير": "Blank expression",
            "غاضب": "Angry face"
        },
        "5️⃣ الإضاءة (موسع)": {
            "": "", 
            "إضاءة ذهبية": "Golden Hour lighting", 
            "إضاءة نيون": "Neon lighting", 
            "إضاءة ناعمة (Softbox)": "Softbox lighting",
            "إضاءة من الأعلى (Top-down)": "Top-down lighting",
            "إضاءة جانبية (Side Light)": "Side lighting",
            "إضاءة خلفية (Rim Light)": "Rim lighting",
            "إضاءة ريمبرانت (درامية)": "Rembrandt lighting",
            "إضاءة سينمائية": "Cinematic lighting"
        },
        "6️⃣ الستايل": {
            "": "",
            "سينمائي": "Cinematic",
            "فيلم كوداك": "Kodak Portra 400",
            "واقعية فائقة": "Hyper-realistic",
            "أنمي": "Anime style",
            "رسم رقمي": "Digital art",
            "أبيض وأسود": "Black and white photography"
        }
    }
    
    cols = st.columns(6)
    sel_photo = {}
    for i, (cat, opts) in enumerate(data_photo.items()):
        with cols[5-i]: 
            choice = st.selectbox(cat, list(opts.keys()), key=f"photo_{i}")
            if choice: sel_photo[cat] = opts[choice]

    st.markdown("---")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p3:
        ar_photo = st.selectbox("📏 أبعاد الصورة (--ar)", list(ar_options.keys()), key="ar_p")
    with col_p2:
        stylize = st.slider("🎨 قوة الستايل (--stylize)", 0, 1000, 250, key="sty_p")
    with col_p1:
        chaos = st.slider("🎲 التنوع/الفوضى (--chaos)", 0, 100, 0, key="ch_p")

    if st.button("✨ إنشاء برومبت الصور", key="btn_photo", type="primary", use_container_width=True):
        desc_parts = [val for val in sel_photo.values() if val]
        description = ", ".join(desc_parts)
        
        if description:
            params = f"{ar_options[ar_photo]} --v 6.0 --s {stylize} --c {chaos}"
            final_prompt = f"{description} {params}"
            st.success("تم التجهيز! انسخ الكود أدناه:")
            st.code(final_prompt, language="text")
        else:
            st.warning("الرجاء اختيار وصف للصورة أولاً.")

# ==============================================================================
# التبويب الثاني: المنتجات
# ==============================================================================
with tab2:
    st.header("🛍️ إعدادات تصوير المنتجات")
    
    data_prod = {
        "1️⃣ المنتج": {
            "": "",
            "زجاجة عطر": "Perfume bottle",
            "علبة كريم": "Cream jar",
            "حذاء رياضي": "Sneaker",
            "حقيبة يد": "Handbag",
            "علبة عصير": "Juice can"
        },
        "2️⃣ الخامة": {
            "": "",
            "زجاج شفاف": "Transparent glass",
            "بلاستيك غير لامع": "Matte plastic",
            "معدن ذهبي": "Gold metal",
            "خشب طبيعي": "Natural wood",
            "قماش حرير": "Silk fabric"
        },
        "3️⃣ الخلفية": {
            "": "",
            "منصة رخامية": "Marble podium",
            "خلفية ملونة سادة": "Solid color background",
            "في الطبيعة": "In nature",
            "طرطشة ماء": "Water splash",
            "صخور سوداء": "Black rocks"
        },
        "4️⃣ الإضاءة": {
            "": "",
            "إضاءة استوديو": "Studio lighting",
            "إضاءة ناعمة": "Soft lighting",
            "إضاءة قوية": "Hard lighting",
            "إضاءة من الجنب": "Side lighting",
            "بدون ظلال": "No shadows"
        },
        "5️⃣ اللقطة": {
            "": "",
            "زاوية المنتج (هيرو)": "Hero shot",
            "من الأعلى (فلات لاي)": "Flat lay",
            "لقطة تفصيلية (ماكرو)": "Macro detail",
            "زاوية 45": "45-degree angle"
        }
    }
    
    cols = st.columns(5)
    sel_prod = {}
    for i, (cat, opts) in enumerate(data_prod.items()):
        with cols[4-i]:
            choice = st.selectbox(cat, list(opts.keys()), key=f"prod_{i}")
            if choice: sel_prod[cat] = opts[choice]
            
    st.markdown("---")
    
    col_pr1, col_pr2 = st.columns(2)
    with col_pr2:
        ar_prod = st.selectbox("📏 أبعاد الصورة", list(ar_options.keys()), key="ar_prod")
    with col_pr1:
        quality = st.select_slider("💎 الجودة (--q)", options=[".25", ".5", "1"], value="1", key="q_prod")

    if st.button("🛍️ إنشاء برومبت المنتجات", key="btn_prod", type="primary", use_container_width=True):
        desc = ", ".join([v for v in sel_prod.values() if v])
        if desc:
            params = f"{ar_options[ar_prod]} --v 6.0 --q {quality}"
            st.success("جاهز للنسخ:")
            st.code(f"{desc} {params}", language="text")
        else:
            st.warning("اختر مواصفات المنتج.")

# ==============================================================================
# التبويب الثالث: الفيديو
# ==============================================================================
with tab3:
    st.header("🎥 إعدادات الفيديو السينمائي")
    
    data_vid = {
        "1️⃣ الحركة": {
            "": "",
            "كاميرا ثابتة": "Static Camera",
            "تحرك بطيء (Slow Mo)": "Slow Motion",
            "دوران حول الهدف": "Orbit shot",
            "زووم للداخل": "Dolly In",
            "تتبع الهدف": "Tracking shot"
        },
        "2️⃣ العدسة": {
            "": "",
            "35 ملم (سينمائي)": "35mm lens",
            "عدسة واسعة (FishEye)": "Fisheye lens",
            "عدسة ماكرو": "Macro lens",
            "عدسة تيلي فوتو": "Telephoto lens"
        },
        "3️⃣ الإضاءة": {
            "": "",
            "إضاءة درامية": "Dramatic lighting",
            "إضاءة نهارية": "Daylight",
            "ساعة زرقاء": "Blue hour",
            "إضاءة ليلية": "Night lighting"
        },
        "4️⃣ الجو العام": {
            "": "",
            "ضبابي وغامض": "Foggy and mysterious",
            "مشرق وحيوي": "Bright and energetic",
            "تقني ومستقبلي": "Tech and futuristic",
            "مرعب": "Horror atmosphere"
        }
    }
    
    cols = st.columns(4)
    sel_vid = {}
    for i, (cat, opts) in enumerate(data_vid.items()):
        with cols[3-i]:
            choice = st.selectbox(cat, list(opts.keys()), key=f"vid_{i}")
            if choice: sel_vid[cat] = opts[choice]
            
    st.markdown("---")
    ar_vid = st.selectbox("📏 أبعاد الفيديو", list(ar_options.keys()), key="ar_vid")

    if st.button("🎥 إنشاء برومبت الفيديو", key="btn_vid", type="primary", use_container_width=True):
        desc = ", ".join([v for v in sel_vid.values() if v])
        if desc:
            params = f"{ar_options[ar_vid]} --v 6.0"
            st.success("جاهز للنسخ:")
            st.code(f"{desc} {params}", language="text")
        else:
            st.warning("اختر إعدادات الفيديو.")

st.markdown("---")
st.caption("🚀 تم التطوير لتسهيل العمل على Midjourney v6")
