import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(
    page_title="مُنشئ برومبت جيميناي الشامل (Gemini Ultimate)",
    layout="wide",
    page_icon="✨"
)

# 2. تنسيق CSS
st.markdown("""
<style>
    /* تعريب الواجهة */
    .stSelectbox, .stTextInput, .stMarkdown, .stButton, .stSlider, .stMultiSelect, .stRadio, .stTextArea, .stFileUploader { 
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
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e8f0fe;
        color: #1a73e8;
    }
    
    /* تنسيق خاص للأقسام */
    .streamlit-expanderHeader {
        font-weight: bold;
        color: #1a73e8;
        background-color: #f8f9fa;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.title("✨ مُنشئ برومبت جيميناي الشامل (Gemini Pro Ultimate)")
st.markdown("### أداة التصميم والتوجيه الفني المتكاملة")
st.markdown("---")

# ==============================================================================
# ⚙️ القائمة الجانبية: إعدادات عامة
# ==============================================================================
with st.sidebar:
    st.header("⚙️ إعدادات عامة")
    aspect_ratio = st.selectbox("📏 الأبعاد", ["Square 1:1", "Cinematic 21:9", "Wide 16:9", "Portrait 9:16", "Landscape 4:3"])
    
    detail_dict = {
        "بسيط (Minimalist)": "Minimalist",
        "متوسط (Standard)": "Standard",
        "عالي التفاصيل (Highly Detailed)": "Highly Detailed",
        "معقد جداً (Intricate & Complex)": "Intricate & Complex"
    }
    detail_sel = st.selectbox("🔍 مستوى التفاصيل", list(detail_dict.keys()))
    
    lighting_dict = {
        "": "",
        "إضاءة استوديو (Studio)": "Studio Lighting",
        "طبيعية ناعمة (Natural Soft)": "Natural Soft Lighting",
        "سينمائية درامية (Cinematic)": "Cinematic Rembrandt Lighting",
        "نيون سايبر بانك (Neon)": "Neon Cyberpunk Lighting",
        "خافتة غامضة (Low Key)": "Low Key Lighting"
    }
    lighting_sel = st.selectbox("💡 الإضاءة العامة", list(lighting_dict.keys()))
    
    st.info("💡 الإعدادات هنا تطبق على كافة التبويبات.")

# ==============================================================================
# التبويبات
# ==============================================================================
tab_font, tab_photo, tab_video, tab_brand, tab_custom = st.tabs([
    "✒️ الخطوط", 
    "📸 الصور", 
    "🎥 الفيديو",
    "🎨 الشعارات",
    "🎭 شخصية مخصصة"
])

# ==============================================================================
# التبويب 1: الخطوط (مختصر للكود)
# ==============================================================================
with tab_font:
    st.header("✒️ محرك الخطوط")
    col_text, col_lang = st.columns([3, 1])
    with col_text: txt_content = st.text_input("النص", placeholder="مثال: Google Gemini")
    with col_lang: lang_mode = st.radio("اللغة", ["عربي", "English"], horizontal=True)
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if lang_mode == "عربي":
            font_cat = st.selectbox("نوع الخط", ["خط الثلث", "خط الكوفي", "خط النسخ", "خط الرقعة", "خط الديواني", "خط حر"])
            font_en = font_cat # تبسيط للترجمة
        else:
            font_cat = st.selectbox("Font Category", ["Serif", "Sans Serif", "Script", "Display", "Blackletter"])
            font_en = font_cat
            
    with col_f2:
        mat_dict = {"حبر تقليدي": "Traditional Ink", "ذهب 3D": "3D Gold", "نيون": "Neon Tubes", "كروم سائل": "Liquid Chrome", "خشب محفور": "Wood Carving", "حجر": "Stone Chiseled"}
        font_mat_ar = st.selectbox("المادة", list(mat_dict.keys()))
    
    if st.button("✨ إنشاء برومبت الخط", key="btn_font", use_container_width=True):
        if txt_content:
            prompt = f"Typography design of '{txt_content}', {font_en} style, made of {mat_dict[font_mat_ar]}, {lighting_dict[lighting_sel]}, {detail_dict[detail_sel]}."
            st.code(prompt, language="text")

# ==============================================================================
# التبويب 2: الصور (مختصر)
# ==============================================================================
with tab_photo:
    st.header("📸 وصف الصور")
    c1, c2 = st.columns(2)
    with c1: sub_img = st.text_input("الموضوع", placeholder="قطة، سيارة...")
    with c2: act_img = st.text_input("الفعل", placeholder="تجري، تطير...")
    if st.button("✨ إنشاء وصف الصورة", key="btn_img", use_container_width=True):
        if sub_img: st.code(f"Image of {sub_img}, {act_img}, {lighting_dict[lighting_sel]}, {detail_dict[detail_sel]}, {aspect_ratio}.", language="text")

# ==============================================================================
# التبويب 3: الفيديو (مختصر)
# ==============================================================================
with tab_video:
    st.header("🎥 إعدادات الفيديو")
    sub_vid = st.text_input("موضوع الفيديو", placeholder="سيارة مسرعة...")
    if st.button("✨ إنشاء برومبت الفيديو", key="btn_vid", use_container_width=True):
        if sub_vid: st.code(f"High-quality video clip of {sub_vid}, {lighting_dict[lighting_sel]}, {aspect_ratio}.", language="text")

# ==============================================================================
# التبويب 4: الشعارات (مختصر)
# ==============================================================================
with tab_brand:
    st.header("🎨 تصميم الشعارات")
    sym = st.text_input("رمز الشعار", placeholder="رأس صقر")
    if st.button("✨ إنشاء برومبت الشعار", key="btn_logo", use_container_width=True):
        if sym: st.code(f"Professional logo of {sym}, {lighting_dict[lighting_sel]}, {detail_dict[detail_sel]}.", language="text")

# ==============================================================================
# التبويب 5: شخصية مخصصة (Custom Character) - القواميس الكاملة
# ==============================================================================
with tab_custom:
    st.header("🎭 تصميم شخصية مخصصة (خيارات كاملة)")
    
    # 1. تحديد الشخصية
    st.markdown("##### 1️⃣ تحديد الشخصية")
    col_char1, col_char2 = st.columns([1, 2])
    with col_char1:
        uploaded_file = st.file_uploader("ارفع صورة الشخصية (اختياري)", type=['png', 'jpg', 'jpeg'])
    with col_char2:
        char_name = st.text_input("اسم الشخصية أو الوصف", placeholder="مثال: باتمان، رجل عربي، فتاة صغيرة...")

    # --- تعريف القواميس (عربي: إنجليزي) ---
    shots_dict = {"": "", "لقطة كاملة (Full shot)": "Full shot", "لقطة متوسطة (Medium shot)": "Medium shot", "لقطة قريبة (Close-up)": "Close-up", "قريبة جداً (Extreme close-up)": "Extreme close-up", "من الرأس للقدم (Head-to-toe)": "Head-to-toe", "من الخصر (Waist-up)": "Waist-up", "من فوق الكتف (Over-the-shoulder)": "Over-the-shoulder", "جانبية (Profile shot)": "Profile shot", "ثلاثة أرباع (¾ view)": "¾ view"}
    
    angles_dict = {"": "", "مستوى العين (Eye level)": "Eye level", "زاوية منخفضة (Low angle)": "Low angle", "زاوية مرتفعة (High angle)": "High angle", "من الأعلى (Bird’s-eye)": "Bird’s-eye view", "من الأسفل (Worm’s-eye)": "Worm’s-eye view", "مائلة (Dutch angle)": "Dutch angle", "أمامية (Front view)": "Front view", "خلفية (Back view)": "Back view"}
    
    lens_dict = {"": "", "35 ملم (35mm)": "35mm lens", "50 ملم (50mm)": "50mm lens", "85 ملم بورتريه (85mm)": "85mm lens", "فتحة واسعة (f/1.8 Aperture)": "f/1.8 Aperture", "زاوية عريضة (Wide Angle)": "Wide Angle", "ماكرو (Macro)": "Macro Lens", "عمق المجال (Depth of field)": "Depth of field"}
    
    styles_dict = {"": "", "واقعي (Realistic)": "Realistic", "واقعي جداً (Hyperrealistic)": "Hyperrealistic", "فوتوغرافي (Photorealistic)": "Photorealistic", "ثلاثي الأبعاد (3D Render)": "3D Render", "بيكسار (Pixar-style)": "Pixar-style", "كاريكاتير 3D": "3D caricature", "أنمي (Anime)": "Anime", "كوميك (Comic style)": "Comic style", "رسم توضيحي (Illustration)": "Illustration", "مينيماليست (Minimalist)": "Minimalist", "سريالي (Surreal)": "Surreal", "صلصال (Clay model)": "Clay model", "لعبة/فيجر (Toy figure)": "Toy figure"}
    
    chars_dict = {"": "", "ملامح طبيعية": "Natural facial features", "ملامح معبرة": "Expressive facial features", "رأس كبير (Oversized head)": "Oversized head", "نسب مبالغ فيها": "Exaggerated proportions", "جسم عضلي": "Muscular build", "جسم نحيف": "Slim build", "تشيبي (Chibi)": "Chibi style", "نسب طبيعية": "Neutral proportions"}
    
    outfits_dict = {"": "", "بدلة رسمية": "Formal Suit", "ملابس كاجوال": "Casual Clothes", "زي تقليدي/شعبي": "Traditional Outfit", "ملابس رياضية": "Sportswear", "زي عسكري/درع": "Military Armor", "فستان سهرة": "Evening Dress", "عباءة": "Abaya/Robe", "جاكيت جلد": "Leather Jacket", "تيشيرت وجينز": "T-shirt and Jeans", "زي رائد فضاء": "Astronaut Suit"}
    
    colors_dict = {"": "", "ألوان زاهية": "Vibrant colors", "ألوان هادئة (Muted)": "Muted tones", "باستيل": "Pastel colors", "أبيض وأسود": "Monochrome", "ألوان دافئة": "Warm colors", "ألوان باردة": "Cold colors", "تباين عالي": "High contrast", "داكن": "Dark colors"}
    
    materials_dict = {"": "", "قماش": "Fabric", "جلد": "Leather", "معدن": "Metallic", "بلاستيك": "Plastic-like", "صلصال ناعم": "Soft clay", "سطح لامع": "Glossy surface", "سطح مطفي": "Matte finish", "خشن": "Rough texture", "خشب": "Wood texture"}
    
    lighting_cust_dict = {"": "", "إضاءة ناعمة محيطة": "Soft ambient lighting", "إضاءة استوديو": "Studio lighting", "إضاءة ثلاثية النقاط": "Three-point lighting", "إضاءة حواف (Rim light)": "Rim light", "إضاءة درامية": "Dramatic lighting", "ضوء شمس طبيعي": "Natural sunlight", "ضوء نيون": "Neon light", "إضاءة دافئة": "Warm tone lighting", "إضاءة باردة": "Cool tone lighting"}
    
    bg_dict = {"": "", "بسيط (Minimal)": "Minimal background", "لون سادة (Solid color)": "Solid color background", "تدرج لوني (Gradient)": "Gradient background", "بوكيه (معزول)": "Bokeh background", "استوديو أبيض": "White studio", "استوديو أسود": "Dark studio", "بيئة واقعية": "Realistic Environment"}
    
    env_dict = {"": "", "داخلي (Indoor)": "Indoor", "خارجي (Outdoor)": "Outdoor", "بيئة مستقبلية": "Futuristic environment", "طبيعة خلابة": "Natural scenery", "مدينة حضرية": "Urban city", "خيال علمي": "Sci-fi world", "عالم فانتازيا": "Fantasy world", "غرفة معيشة": "Living room", "مكتب": "Office", "شارع": "Street"}
    
    poses_dict = {"": "", "واقف (Standing)": "Standing", "مشي (Walking)": "Walking", "وضعية حركة ديناميكية": "Dynamic action pose", "وضعية كاجوال": "Casual pose", "جالس (Sitting)": "Sitting", "مكتوف الأيدي": "Arms crossed", "ينظر للكاميرا": "Looking at camera", "ينظر بعيداً": "Looking away"}
    
    exps_dict = {"": "", "محايد (Neutral)": "Neutral expression", "سعيد (Happy)": "Happy", "جاد (Serious)": "Serious", "يفكر (Thinking)": "Thinking", "مندهش (Surprised)": "Surprised", "واثق (Confident)": "Confident", "هادئ (Calm)": "Calm", "غاضب (Angry)": "Angry"}
    
    render_dict = {"": "", "دقة فائقة (Ultra-detailed)": "Ultra-detailed", "دقة عالية (High resolution)": "High resolution", "ريندر نظيف (Clean render)": "Clean render", "جودة سينمائية": "Cinematic quality", "أسطح ناعمة": "Smooth surfaces", "أنريل إنجن 5": "Unreal Engine 5 render"}

    # --- التخطيط (Layout) ---
    
    # القسم أ: الكاميرا واللقطة
    with st.expander("🎥 الكاميرا، اللقطة، والزاوية", expanded=True):
        c_1, c_2, c_3 = st.columns(3)
        with c_1: s_shot = st.selectbox("1. نوع اللقطة", list(shots_dict.keys()))
        with c_2: s_angle = st.selectbox("2. زاوية الكاميرا", list(angles_dict.keys()))
        with c_3: s_lens = st.selectbox("12. أسلوب الكاميرا", list(lens_dict.keys()))

    # القسم ب: الأسلوب والشخصية
    with st.expander("🎨 الأسلوب الفني وتصميم الشخصية"):
        s_1, s_2, s_3 = st.columns(3)
        with s_1: s_style = st.selectbox("3. نوع الأسلوب", list(styles_dict.keys()))
        with s_2: s_char = st.selectbox("4. خصائص الشخصية", list(chars_dict.keys()))
        with s_3: s_render = st.selectbox("11. جودة الإخراج", list(render_dict.keys()))

    # القسم ج: المظهر والحركة (تم تحويل الملابس لقائمة)
    with st.expander("👕 الملابس، الحركة، والتعبير"):
        o_1, o_2 = st.columns(2)
        with o_1: s_outfit = st.selectbox("5. نوع الملابس", list(outfits_dict.keys()))
        with o_2: s_mat = st.selectbox("6. الخامات", list(materials_dict.keys()))
        
        p_1, p_2 = st.columns(2)
        with p_1: s_pose = st.selectbox("13. الحركة والوضعيّة", list(poses_dict.keys()))
        with p_2: s_exp = st.selectbox("14. تعبير الوجه", list(exps_dict.keys()))

    # القسم د: البيئة والإضاءة
    with st.expander("💡 الإضاءة، الألوان، والخلفية"):
        l_1, l_2 = st.columns(2)
        with l_1: s_light = st.selectbox("7. الإضاءة", list(lighting_cust_dict.keys()))
        with l_2: s_color = st.selectbox("8. باليت الألوان", list(colors_dict.keys()))
        
        b_1, b_2 = st.columns(2)
        with b_1: s_bg = st.selectbox("9. الخلفية", list(bg_dict.keys()))
        with b_2: s_env = st.selectbox("10. البيئة / المشهد", list(env_dict.keys()))

    # القسم هـ: إضافات
    with st.expander("✨ تفاصيل إضافية (اختياري)"):
        enh_dict = {
            "منمق جداً": "Highly stylized", "نظيف جداً": "Ultra-clean", "ظلال ناعمة": "Soft shadows",
            "تشتت تحت السطح": "Subsurface scattering", "إضاءة عالمية": "Global illumination",
            "إضاءة حجمية": "Volumetric light", "تشريح مثالي": "Perfect anatomy"
        }
        s_enh = st.multiselect("15. تحسينات إضافية", list(enh_dict.keys()))

    # زر التوليد
    if st.button("✨ إنشاء برومبت الشخصية المخصص", key="btn_custom", type="primary", use_container_width=True):
        final_subject = char_name if char_name else "A character"
        if uploaded_file: final_subject += " [Reference Image Used]"
        
        # تجميع القيم الإنجليزية
        parts = [
            f"Subject: {final_subject}",
            f"Shot: {shots_dict[s_shot]}" if s_shot else "",
            f"Angle: {angles_dict[s_angle]}" if s_angle else "",
            f"Style: {styles_dict[s_style]}" if s_style else "",
            f"Character: {chars_dict[s_char]}" if s_char else "",
            f"Outfit: {outfits_dict[s_outfit]}" if s_outfit else "",
            f"Material: {materials_dict[s_mat]}" if s_mat else "",
            f"Pose: {poses_dict[s_pose]}" if s_pose else "",
            f"Expression: {exps_dict[s_exp]}" if s_exp else "",
            f"Lighting: {lighting_cust_dict[s_light]}" if s_light else "",
            f"Colors: {colors_dict[s_color]}" if s_color else "",
            f"Background: {bg_dict[s_bg]}" if s_bg else "",
            f"Environment: {env_dict[s_env]}" if s_env else "",
            f"Camera: {lens_dict[s_lens]}" if s_lens else "",
            f"Quality: {render_dict[s_render]}" if s_render else "",
            f"Enhancements: {', '.join([enh_dict[e] for e in s_enh])}" if s_enh else ""
        ]
        
        full_prompt = ", ".join([p for p in parts if p])
        full_prompt += f" --ar {aspect_ratio.split(' ')[-1] if '--ar' not in aspect_ratio else aspect_ratio}"

        st.success("تم تجهيز البرومبت الاحترافي! انسخه أدناه:")
        st.code(full_prompt, language="text")
        
        if uploaded_file:
            st.info("ℹ️ تأكد من رفع الصورة مع هذا البرومبت في جيميناي.")

st.markdown("---")
st.caption("🚀 تم التطوير لتسهيل العمل على Google Gemini & Midjourney")
