import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(
    page_title="مُنشئ برومبت جيميناي (Gemini Typography)",
    layout="wide",
    page_icon="✨"
)

# 2. تنسيق CSS
st.markdown("""
<style>
    /* تعريب الواجهة */
    .stSelectbox, .stTextInput, .stMarkdown, .stButton, .stSlider, .stMultiSelect, .stRadio, .stTextArea { 
        direction: rtl; text-align: right; 
    }
    div[data-testid="stMarkdownContainer"] p { direction: rtl; }
    div[data-testid="stSidebar"] { direction: rtl; text-align: right; }
    h1, h2, h3, h4 { text-align: center; color: #4285F4; font-family: sans-serif; } /* لون جيميناي الأزرق */
    .stCode { direction: ltr !important; text-align: left !important; }
    
    /* تحسين شكل التبويبات */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 4px 4px 0 0;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e8f0fe;
        color: #1a73e8;
    }
</style>
""", unsafe_allow_html=True)

st.title("✨ مُنشئ برومبت جيميناي (Gemini Advanced Builder)")
st.markdown("### متخصص في التايبوجرافي، الخطوط، والتصاميم الدقيقة")
st.markdown("---")

# ==============================================================================
# ⚙️ القائمة الجانبية: إعدادات جيميناي
# ==============================================================================
with st.sidebar:
    st.header("⚙️ إعدادات التوجيه (Instructions)")
    
    # نسبة الأبعاد (جيميناي يفهم الوصف)
    aspect_ratio = st.selectbox(
        "📏 أبعاد الصورة",
        ["مربع (Square 1:1)", "عريض (Wide 16:9)", "طولي (Portrait 9:16)", "لاندسكيب (4:3)"]
    )
    
    # مستوى التفاصيل
    detail_level = st.select_slider(
        "🔍 مستوى التفاصيل",
        options=["بسيط (Minimalist)", "متوسط (Standard)", "مفصل جداً (Highly Detailed)", "معقد جداً (Intricate)"]
    )
    
    # الإضاءة العامة
    lighting_global = st.selectbox(
        "💡 الإضاءة العامة للمشهد",
        ["", "إضاءة استوديو احترافية", "إضاءة طبيعية ناعمة", "إضاءة سينمائية درامية", "إضاءة نيون سايبر بانك", "إضاءة خافتة غامضة"]
    )
    
    st.info("💡 **نصيحة:** جيميناي يفهم اللغة العربية والإنجليزية، لكن النتائج بالإنجليزية (في البرومبت) تكون أدق أحياناً في وصف الأنماط الفنية.")

# ==============================================================================
# التبويبات
# ==============================================================================
tab_font, tab_photo, tab_brand = st.tabs([
    "✒️ الخطوط والتايبوجرافي (Typography)", 
    "📸 توليد الصور (Image Gen)", 
    "🎨 الهوية والشعارات (Branding)"
])

# ==============================================================================
# التبويب 1: مكتبة الخطوط الشاملة (The Font Engine)
# ==============================================================================
with tab_font:
    st.header("✒️ محرك الخطوط الشامل")
    
    col_text, col_lang = st.columns([3, 1])
    with col_text:
        txt_content = st.text_input("📝 النص المراد كتابته", placeholder="مثال: Google Gemini")
    with col_lang:
        lang_mode = st.radio("لغة النص", ["عربي", "English"], horizontal=True)

    st.markdown("---")

    # 1. مكتبة الخطوط (قوائم منفصلة للعربي والإنجليزي)
    col_f1, col_f2 = st.columns(2)
    
    font_style = ""
    font_cat = ""

    with col_f1:
        if lang_mode == "عربي":
            font_cat = st.selectbox("نوع الخط العربي", [
                "خط الثلث (Thuluth) - فخم ومركب",
                "خط الكوفي (Kufic) - هندسي وقديم",
                "خط النسخ (Naskh) - واضح للقراءة",
                "خط الرقعة (Ruqah) - بسيط وسريع",
                "خط الديواني (Diwani) - انسيابي وملكي",
                "الخط المغربي (Maghribi) - تقليدي",
                "خط حر (Freestyle) - حديث ومودرن",
                "كاليجرافي تجريدي (Abstract Calligraphy)"
            ])
        else:
            font_cat = st.selectbox("Font Category", [
                "Serif (Classic/Elegant)",
                "Sans Serif (Modern/Clean)",
                "Script (Handwritten/Cursive)",
                "Display (Bold/Headline)",
                "Blackletter (Gothic/Medieval)",
                "Graffiti (Street Art)",
                "Monospace (Coding/Tech)"
            ])

    with col_f2:
        # شكل الخط ومادته (Material & Shape)
        font_material = st.selectbox("مادة/تجسيم الخط (Material)", [
            "حبر أسود تقليدي (Traditional Ink)",
            "ذهب بارز ثلاثي الأبعاد (3D Gold Render)",
            "أنابيب نيون مضيئة (Glowing Neon Tubes)",
            "معدن كروم لامع (Liquid Chrome)",
            "حفر على الخشب (Wood Carving)",
            "سحاب ودخان (Cloud/Smoke Form)",
            "زهور ونباتات (Floral Typography)",
            "زجاج شفاف (Glass/Crystal)",
            "ورق مقصوص (Paper Cutout)",
            "بسكويت/طعام (Food Typography)"
        ])

    # 2. التأثيرات والخلفية
    col_e1, col_e2, col_e3 = st.columns(3)
    with col_e1:
        composition = st.selectbox("تنسيق النص", ["في المنتصف (Centered)", "يملأ الكادر (Full Frame)", "مائل (Tilted)", "متداخل (Intertwined Letters)"])
    with col_e2:
        background = st.selectbox("الخلفية", ["خلفية بيضاء نقية", "خلفية سوداء داكنة", "خلفية ورق بردي قديم", "خلفية رخامية", "خلفية ضبابية (Bokeh)", "جدار شارع (Street Wall)"])
    with col_e3:
        colors = st.text_input("الألوان (اختياري)", placeholder="مثال: ذهبي وأسود، أو ألوان الباستيل")

    # زر التوليد
    if st.button("✨ إنشاء برومبت الخط (Gemini)", key="btn_font", type="primary", use_container_width=True):
        if txt_content:
            # بناء البرومبت بصيغة يفهمها جيميناي
            if lang_mode == "عربي":
                style_desc = font_cat.split("-")[0].strip()
                prompt_text = (
                    f"Create a high-quality image featuring the Arabic text '{txt_content}'. "
                    f"The text should be written in {style_desc} style. "
                    f"Render the text as {font_material.split('(')[0]}. "
                    f"Make sure the composition is {composition.split('(')[0]}. "
                    f"Background: {background}. "
                    f"Colors: {colors if colors else 'Colors matching the style'}. "
                    f"Lighting: {lighting_global}. "
                    f"Quality: {detail_level.split('(')[0]}. "
                    f"Aspect Ratio: {aspect_ratio.split('(')[0]}."
                )
            else: # English
                style_desc = font_cat.split("(")[0].strip()
                prompt_text = (
                    f"Create a typography design of the word '{txt_content}'. "
                    f"Use a {style_desc} font style. "
                    f"The text should look like {font_material.split('(')[1][:-1] if '(' in font_material else font_material}. "
                    f"Composition: {composition.split('(')[1][:-1] if '(' in composition else composition}. "
                    f"Background: {background}. "
                    f"Colors: {colors if colors else 'Harmonious colors'}. "
                    f"Lighting: {lighting_global}. "
                    f"Overall Vibe: {detail_level.split('(')[1][:-1] if '(' in detail_level else detail_level}."
                )
            
            st.success("انسخ هذا البرومبت وضعه في Google Gemini:")
            st.code(prompt_text, language="text")
        else:
            st.warning("يرجى كتابة النص أولاً.")

# ==============================================================================
# التبويب 2: الصور (محدث لجيميناي)
# ==============================================================================
with tab_photo:
    st.header("📸 وصف الصور (Image Description)")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1: subject = st.text_input("الموضوع (Subject)", placeholder="قطة ترتدي نظارة، سيارة طائرة...")
    with col_p2: action = st.text_input("ماذا يفعل؟ (Action)", placeholder="تجري في الفضاء، واقفة تحت المطر...")
    
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1: 
        art_style = st.selectbox("النمط الفني", [
            "واقعي (Photorealistic)", "كرتون (Cartoon)", "أنمي (Anime)", 
            "رسم رقمي (Digital Art)", "زيتي (Oil Painting)", "رسم بقلم الرصاص (Pencil Sketch)",
            "ألوان مائية (Watercolor)", "بكسل آرت (Pixel Art)", "أوريغامي (Origami)"
        ])
    with col_s2: 
        camera_angle = st.selectbox("زاوية الكاميرا", ["مستوى العين", "من الأعلى (Bird's eye)", "من الأسفل (Worm's eye)", "زاوية واسعة (Wide angle)", "ماكرو (Macro)"])
    with col_s3:
        mood = st.selectbox("المزاج العام", ["سعيد ومشرق", "مظلم ومرعب", "هادئ ومريح", "مستقبلي وتقني", "فانتازيا سحرية"])

    if st.button("✨ إنشاء وصف الصورة", key="btn_img", use_container_width=True):
        if subject:
            # صيغة جيميناي
            final_p = (
                f"Generate an image of {subject}, {action}. "
                f"Art Style: {art_style.split('(')[0]}. "
                f"Camera Angle: {camera_angle}. "
                f"Lighting: {lighting_global}. "
                f"Mood: {mood}. "
                f"Level of Detail: {detail_level.split('(')[0]}. "
                f"Aspect Ratio: {aspect_ratio.split('(')[0]}."
            )
            st.code(final_p, language="text")
        else:
            st.warning("اكتب موضوع الصورة.")

# ==============================================================================
# التبويب 3: الهوية والشعارات
# ==============================================================================
with tab_brand:
    st.header("🎨 تصميم الشعارات (Logo Design)")
    
    brand_name = st.text_input("اسم العلامة التجارية (للشعارات النصية)", placeholder="اختياري")
    brand_symbol = st.text_input("رمز الشعار", placeholder="مثال: رأس أسد، شجرة، حرف A")
    
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        logo_style = st.selectbox("نوع الشعار", [
            "مينيماليست (Minimalist Line Art)",
            "شعار ثلاثي الأبعاد (3D Glossy)",
            "شعار رياضي (E-sport Mascot)",
            "هندسي (Geometric Abstract)",
            "عتيق (Vintage Badge)",
            "ألوان مائية (Watercolor)"
        ])
    with col_b2:
        bg_logo = st.selectbox("خلفية الشعار", ["خلفية بيضاء سادة (للقص)", "خلفية ملونة", "على جدار مكتب", "على ورقة"])

    if st.button("✨ إنشاء برومبت الشعار", key="btn_logo", use_container_width=True):
        if brand_symbol:
            final_logo = (
                f"Design a professional logo featuring {brand_symbol}. "
                f"{f'Include the text: {brand_name}. ' if brand_name else ''}"
                f"Style: {logo_style.split('(')[0]}. "
                f"Background: {bg_logo}. "
                f"Make it clean, vector-like, and high quality. "
                f"Lighting: {lighting_global}."
            )
            st.code(final_logo, language="text")
        else:
            st.warning("اكتب رمز الشعار على الأقل.")

st.markdown("---")
st.caption("🚀 تم تحسين الأوامر لتناسب نموذج Google Gemini / Imagen 3")
