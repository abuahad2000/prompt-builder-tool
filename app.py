import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(
    page_title="مُنشئ برومبت جيميناي الشامل (Gemini Pro Ultimate)",
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
    h1, h2, h3, h4 { text-align: center; color: #4285F4; font-family: sans-serif; }
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

st.title("✨ مُنشئ برومبت جيميناي الشامل (Gemini Pro Ultimate)")
st.markdown("### التحكم الكامل في الخطوط، الصور، الفيديو، والشعارات")
st.markdown("---")

# ==============================================================================
# ⚙️ القائمة الجانبية: إعدادات التوجيه العامة
# ==============================================================================
with st.sidebar:
    st.header("⚙️ إعدادات التوجيه (Instructions)")
    
    # 1. أبعاد الصورة/الفيديو
    aspect_ratio = st.selectbox(
        "📏 الأبعاد (Aspect Ratio)",
        ["مربع (Square 1:1)", "عريض سينمائي (Cinematic 21:9)", "عريض قياسي (Wide 16:9)", "طولي (Portrait 9:16)", "لاندسكيب (4:3)"]
    )
    
    # 2. مستوى التفاصيل
    detail_level = st.selectbox(
        "🔍 مستوى التفاصيل",
        [
            "بسيط (Minimalist)", 
            "متوسط (Standard)", 
            "مفصل جداً (Highly Detailed)", 
            "معقد ودقيق (Intricate & Complex)"
        ]
    )
    
    # 3. الإضاءة العامة
    lighting_global = st.selectbox(
        "💡 الإضاءة العامة للمشهد",
        ["", "إضاءة استوديو احترافية", "إضاءة طبيعية ناعمة", "إضاءة سينمائية درامية (Rembrandt)", "إضاءة نيون سايبر بانك", "إضاءة خافتة غامضة (Low Key)"]
    )
    
    st.info("💡 **نصيحة:** الإعدادات هنا تطبق على جميع التبويبات (صور، فيديو، خطوط).")

# ==============================================================================
# التبويبات (تمت إضافة الفيديو)
# ==============================================================================
tab_font, tab_photo, tab_video, tab_brand = st.tabs([
    "✒️ الخطوط (Typography)", 
    "📸 الصور (Image Gen)", 
    "🎥 الفيديو (Video Gen)",
    "🎨 الشعارات (Branding)"
])

# ==============================================================================
# التبويب 1: محرك الخطوط (النسخة المحدثة)
# ==============================================================================
with tab_font:
    st.header("✒️ محرك الخطوط والتأثيرات")
    
    col_text, col_lang = st.columns([3, 1])
    with col_text:
        txt_content = st.text_input("📝 النص المراد كتابته", placeholder="مثال: Google Gemini")
    with col_lang:
        lang_mode = st.radio("لغة النص", ["عربي", "English"], horizontal=True)

    st.markdown("---")

    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if lang_mode == "عربي":
            font_cat = st.selectbox("نوع الخط العربي", ["خط الثلث (Thuluth) - فخم", "خط الكوفي (Kufic) - هندسي", "خط النسخ (Naskh) - واضح", "خط الرقعة (Ruqah) - بسيط", "خط الديواني (Diwani) - انسيابي", "خط حر (Freestyle) - مودرن"])
        else:
            font_cat = st.selectbox("Font Category", ["Serif (Classic)", "Sans Serif (Modern)", "Script (Handwritten)", "Display (Bold)", "Blackletter (Gothic)"])

    with col_f2:
        font_material = st.selectbox("مادة/تجسيم الخط", ["حبر أسود تقليدي", "ذهب بارز 3D", "أنابيب نيون مضيئة", "معدن كروم لامع", "حفر على الخشب", "حجر منحوت", "زجاج شفاف", "ورق مقصوص"])

    st.subheader("🎨 تفاصيل وتأثيرات الخط")
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        line_effect = st.selectbox("شكل وتأثير الخط", ["بدون تأثيرات إضافية", "خط حفر غائر (Engraved)", "خط بارز (Embossed)", "يلتف حول كائن (Wrapped)", "مسار دائري (Circular)", "تدرج لوني (Gradient)"])
    with col_d2:
        background = st.selectbox("الخلفية", ["خلفية بيضاء نقية", "خلفية سوداء داكنة", "خلفية ورق بردي", "خلفية رخامية", "خلفية ضبابية (Bokeh)"])

    colors = st.text_input("الألوان (اختياري)", placeholder="مثال: تدرجات الأزرق والبنفسجي")

    if st.button("✨ إنشاء برومبت الخط", key="btn_font", type="primary", use_container_width=True):
        if txt_content:
            style_desc = font_cat.split("-")[0].strip() if lang_mode == "عربي" else font_cat.split("(")[0].strip()
            prompt_text = (
                f"Create a high-quality typography design of '{txt_content}'. "
                f"Font Style: {style_desc}. Material: {font_material}. Effect: {line_effect}. "
                f"Background: {background}. Colors: {colors if colors else 'Harmonious'}. "
                f"Lighting: {lighting_global}. Detail: {detail_level.split('(')[0]}. Aspect Ratio: {aspect_ratio.split('(')[0]}."
            )
            st.code(prompt_text, language="text")

# ==============================================================================
# التبويب 2: الصور
# ==============================================================================
with tab_photo:
    st.header("📸 وصف الصور الثابتة")
    col_p1, col_p2 = st.columns(2)
    with col_p1: subject = st.text_input("الموضوع", placeholder="قطة، سيارة...")
    with col_p2: action = st.text_input("الفعل", placeholder="تجري، تطير...")
    
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1: art_style = st.selectbox("النمط الفني", ["واقعي (Photorealistic)", "سينمائي (Cinematic)", "كرتون (Cartoon)", "أنمي (Anime)", "رسم رقمي (Digital Art)", "زيتي (Oil Painting)"])
    with col_s2: camera_angle = st.selectbox("زاوية الكاميرا", ["مستوى العين", "من الأعلى (Bird's eye)", "من الأسفل (Worm's eye)", "ماكرو (Macro)", "زاوية واسعة (Wide)"])
    with col_s3: mood = st.selectbox("المزاج", ["سعيد ومشرق", "مظلم ومرعب", "هادئ ومريح", "مستقبلي", "فانتازيا"])

    if st.button("✨ إنشاء وصف الصورة", key="btn_img", use_container_width=True):
        if subject:
            final_p = (
                f"Generate an image of {subject}, {action}. "
                f"Style: {art_style.split('(')[0]}. Angle: {camera_angle.split('(')[0]}. "
                f"Lighting: {lighting_global}. Mood: {mood}. "
                f"Detail: {detail_level.split('(')[0]}. Aspect Ratio: {aspect_ratio.split('(')[0]}."
            )
            st.code(final_p, language="text")

# ==============================================================================
# التبويب 3: الفيديو (تمت إعادته) 🔥
# ==============================================================================
with tab_video:
    st.header("🎥 إعدادات الفيديو السينمائي")
    
    col_v1, col_v2 = st.columns(2)
    with col_v1: video_subject = st.text_input("موضوع الفيديو", placeholder="مثال: سيارة رياضية مسرعة في نفق")
    with col_v2: video_style = st.selectbox("ستايل الفيديو", ["سينمائي واقعي (Cinematic Realistic)", "أنميشن (Animation)", "وثائقي (Documentary)", "فيديو موسيقي (Music Video Vibe)"])

    col_v3, col_v4, col_v5 = st.columns(3)
    with col_v3: camera_move = st.selectbox("حركة الكاميرا", ["ثابتة (Static)", "تحرك بطيء (Slow Pan)", "تتبع (Tracking Shot)", "دوران (Orbit)", "زووم للداخل (Dolly In)", "درون (Drone Flyover)"])
    with col_v4: lens_type = st.selectbox("نوع العدسة", ["عدسة سينمائية (Anamorphic)", "عدسة واسعة (Wide Angle)", "عدسة ماكرو (Macro)", "عدسة زووم (Telephoto)"])
    with col_v5: frame_rate = st.selectbox("معدل الإطارات/السرعة", ["سرعة عادية (Real-time)", "تصوير بطيء (Slow Motion)", "سريع جداً (Timelapse)"])

    if st.button("✨ إنشاء برومبت الفيديو", key="btn_video", use_container_width=True):
        if video_subject:
            video_prompt = (
                f"Generate a high-quality video clip of {video_subject}. "
                f"Style: {video_style.split('(')[0]}. "
                f"Camera Movement: {camera_move.split('(')[0]}. "
                f"Lens: {lens_type.split('(')[0]}. "
                f"Speed: {frame_rate.split('(')[0]}. "
                f"Lighting: {lighting_global}. "
                f"Aspect Ratio: {aspect_ratio.split('(')[0]}."
            )
            st.code(video_prompt, language="text")
        else:
            st.warning("اكتب موضوع الفيديو أولاً.")

# ==============================================================================
# التبويب 4: الشعارات
# ==============================================================================
with tab_brand:
    st.header("🎨 تصميم الشعارات")
    brand_symbol = st.text_input("رمز الشعار", placeholder="مثال: رأس صقر")
    col_b1, col_b2 = st.columns(2)
    with col_b1: logo_style = st.selectbox("نوع الشعار", ["مينيماليست (Line Art)", "ثلاثي الأبعاد (3D)", "هندسي (Geometric)", "عتيق (Vintage Badge)"])
    with col_b2: bg_logo = st.selectbox("خلفية الشعار", ["بيضاء سادة (للقص)", "ملونة متدرجة", "محفورة على جدار"])

    if st.button("✨ إنشاء برومبت الشعار", key="btn_logo", use_container_width=True):
        if brand_symbol:
            final_logo = (
                f"Design a professional logo features {brand_symbol}. "
                f"Style: {logo_style.split('(')[0]}. Background: {bg_logo}. "
                f"Lighting: {lighting_global}. Detail: {detail_level.split('(')[0]}."
            )
            st.code(final_logo, language="text")

st.markdown("---")
st.caption("🚀 شامل لجميع احتياجات التوليد (صور، فيديو، خطوط، شعارات) - مخصص لـ Gemini")
