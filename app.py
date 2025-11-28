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
    
    /* تنسيق خاص للأقسام في التبويب الجديد */
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
    detail_level = st.selectbox("🔍 مستوى التفاصيل", ["Minimalist", "Standard", "Highly Detailed", "Intricate & Complex"])
    lighting_global = st.selectbox("💡 الإضاءة العامة", ["", "Studio Lighting", "Natural Soft", "Cinematic Rembrandt", "Neon Cyberpunk", "Low Key"])
    st.info("💡 الإعدادات هنا تطبق على كافة التبويبات.")

# ==============================================================================
# التبويبات (تمت إضافة التبويب الخامس)
# ==============================================================================
tab_font, tab_photo, tab_video, tab_brand, tab_custom = st.tabs([
    "✒️ الخطوط", 
    "📸 الصور", 
    "🎥 الفيديو",
    "🎨 الشعارات",
    "🎭 شخصية مخصصة"
])

# ==============================================================================
# التبويب 1: الخطوط
# ==============================================================================
with tab_font:
    st.header("✒️ محرك الخطوط")
    col_text, col_lang = st.columns([3, 1])
    with col_text: txt_content = st.text_input("النص", placeholder="مثال: Google Gemini")
    with col_lang: lang_mode = st.radio("اللغة", ["عربي", "English"], horizontal=True)
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        if lang_mode == "عربي":
            font_cat = st.selectbox("نوع الخط", ["خط الثلث (Thuluth)", "خط الكوفي (Kufic)", "خط النسخ (Naskh)", "خط الرقعة (Ruqah)", "خط الديواني (Diwani)", "خط حر (Freestyle)"])
        else:
            font_cat = st.selectbox("Font Category", ["Serif", "Sans Serif", "Script", "Display", "Blackletter"])
    with col_f2:
        font_material = st.selectbox("المادة", ["Traditional Ink", "3D Gold", "Neon Tubes", "Liquid Chrome", "Wood Carving", "Stone Chiseled", "Glass", "Paper Cutout"])
    
    col_d1, col_d2 = st.columns(2)
    with col_d1: line_effect = st.selectbox("تأثيرات الخط", ["Standard", "Engraved", "Embossed", "Wrapped", "Circular", "Gradient"])
    with col_d2: background_font = st.selectbox("خلفية الخط", ["White", "Black", "Paper", "Marble", "Bokeh"])
    
    if st.button("✨ إنشاء برومبت الخط", key="btn_font", use_container_width=True):
        if txt_content:
            prompt = f"Typography design of '{txt_content}', {font_cat.split('(')[0]} style, made of {font_material}, {line_effect} effect, {background_font} background, {lighting_global}, {detail_level}."
            st.code(prompt, language="text")

# ==============================================================================
# التبويب 2: الصور
# ==============================================================================
with tab_photo:
    st.header("📸 وصف الصور")
    c1, c2 = st.columns(2)
    with c1: sub_img = st.text_input("الموضوع", placeholder="قطة، سيارة...")
    with c2: act_img = st.text_input("الفعل", placeholder="تجري، تطير...")
    c3, c4 = st.columns(2)
    with c3: style_img = st.selectbox("الستايل", ["Photorealistic", "Cinematic", "Cartoon", "Anime", "Digital Art", "Oil Painting"])
    with c4: angle_img = st.selectbox("الزاوية", ["Eye Level", "Bird's Eye", "Worm's Eye", "Macro", "Wide Angle"])
    
    if st.button("✨ إنشاء وصف الصورة", key="btn_img", use_container_width=True):
        if sub_img:
            st.code(f"Image of {sub_img}, {act_img}, {style_img} style, {angle_img} angle, {lighting_global}, {detail_level}, {aspect_ratio}.", language="text")

# ==============================================================================
# التبويب 3: الفيديو
# ==============================================================================
with tab_video:
    st.header("🎥 إعدادات الفيديو")
    sub_vid = st.text_input("موضوع الفيديو", placeholder="سيارة مسرعة...")
    v1, v2, v3 = st.columns(3)
    with v1: v_style = st.selectbox("ستايل الفيديو", ["Cinematic Realistic", "Animation", "Documentary", "Music Video"])
    with v2: v_move = st.selectbox("حركة الكاميرا", ["Static", "Slow Pan", "Tracking Shot", "Orbit", "Dolly In", "Drone Flyover"])
    with v3: v_lens = st.selectbox("العدسة", ["Anamorphic", "Wide Angle", "Macro", "Telephoto"])
    
    if st.button("✨ إنشاء برومبت الفيديو", key="btn_vid", use_container_width=True):
        if sub_vid:
            st.code(f"High-quality video clip of {sub_vid}, {v_style}, {v_move}, {v_lens} lens, {lighting_global}, {aspect_ratio}.", language="text")

# ==============================================================================
# التبويب 4: الشعارات
# ==============================================================================
with tab_brand:
    st.header("🎨 تصميم الشعارات")
    sym = st.text_input("رمز الشعار", placeholder="رأس صقر")
    b1, b2 = st.columns(2)
    with b1: l_style = st.selectbox("نوع الشعار", ["Minimalist Line Art", "3D Glossy", "Geometric", "Vintage Badge"])
    with b2: l_bg = st.selectbox("خلفية الشعار", ["White background", "Gradient", "Wall texture"])
    
    if st.button("✨ إنشاء برومبت الشعار", key="btn_logo", use_container_width=True):
        if sym:
            st.code(f"Professional logo of {sym}, {l_style} style, {l_bg}, {lighting_global}, {detail_level}.", language="text")

# ==============================================================================
# التبويب 5: شخصية مخصصة (Custom Character) - الجديد! 🔥
# ==============================================================================
with tab_custom:
    st.header("🎭 تصميم شخصية مخصصة ومتقدمة")
    
    # 1. تحديد الشخصية (صورة أو اسم)
    st.markdown("##### 1️⃣ تحديد الشخصية")
    col_char1, col_char2 = st.columns([1, 2])
    with col_char1:
        uploaded_file = st.file_uploader("ارفع صورة الشخصية (اختياري)", type=['png', 'jpg', 'jpeg'])
    with col_char2:
        char_name = st.text_input("أو اكتب اسم الشخصية / الوصف", placeholder="مثال: باتمان، أو شاب عربي يرتدي شماغ...")

    # تجميع الخيارات في أقسام (Expanders) للتنظيم
    
    # القسم أ: الكاميرا واللقطة
    with st.expander("🎥 الكاميرا، اللقطة، والزاوية (Camera & Shot)", expanded=True):
        c_1, c_2, c_3 = st.columns(3)
        with c_1:
            shot_type = st.selectbox("1. نوع اللقطة (Shot Type)", ["", "Full shot", "Medium shot", "Close-up", "Extreme close-up", "Head-to-toe", "Waist-up", "Over-the-shoulder", "Profile shot", "¾ view"])
        with c_2:
            cam_angle = st.selectbox("2. زاوية الكاميرا (Angle)", ["", "Eye level", "Low angle", "High angle", "Bird’s-eye view", "Worm’s-eye view", "Tilted / Dutch angle", "Front view", "Back view"])
        with c_3:
            cam_param = st.selectbox("12. إعدادات الكاميرا (Lens)", ["", "35mm Lens", "50mm Portrait Lens", "85mm", "f/1.8 Aperture (Bokeh)", "Wide Angle", "Macro Lens"])

    # القسم ب: الأسلوب والشخصية
    with st.expander("🎨 الأسلوب الفني وتصميم الشخصية (Style & Design)"):
        s_1, s_2, s_3 = st.columns(3)
        with s_1:
            art_style_cust = st.selectbox("3. نوع الأسلوب (Artistic Style)", ["", "Realistic", "Hyperrealistic", "Photorealistic", "3D Pixar-style", "3D Caricature", "Anime", "Comic style", "Minimalist", "Surreal", "Clay model", "Fantasy Illustration"])
        with s_2:
            char_feat = st.selectbox("4. خصائص الشخصية", ["", "Natural facial features", "Expressive facial features", "Oversized head", "Exaggerated proportions", "Chibi style", "Muscular build", "Slim build"])
        with s_3:
            render_qual = st.selectbox("11. جودة الإخراج (Rendering)", ["", "Ultra-detailed", "8K Resolution", "Clean render", "Cinematic quality", "Sharp textures", "Unreal Engine 5"])

    # القسم ج: المظهر والحركة
    with st.expander("👕 الملابس، الحركة، والتعبير (Outfit, Pose & Expression)"):
        o_1, o_2 = st.columns(2)
        with o_1:
            outfit_details = st.text_input("5. الملابس والملحقات (تفاصيل)", placeholder="مثال: بدلة سوداء، ربطة عنق حمراء، نظارات شمسية...")
        with o_2:
            materials = st.selectbox("6. الخامات (Materials)", ["", "Fabric & Cloth", "Leather", "Metallic Armor", "Plastic-like", "Soft clay", "Glossy surfaces", "Matte finish", "Rough texture"])
        
        p_1, p_2 = st.columns(2)
        with p_1:
            pose_motion = st.selectbox("13. الحركة والوضعية", ["", "Standing confidently", "Walking forward", "Dynamic action pose", "Sitting relaxed", "Arms crossed", "Looking at camera", "Looking away"])
        with p_2:
            face_exp = st.selectbox("14. تعبير الوجه", ["", "Neutral", "Happy & Smiling", "Serious", "Thinking", "Surprised", "Confident", "Calm", "Angry"])

    # القسم د: البيئة والإضاءة
    with st.expander("💡 الإضاءة، الألوان، والخلفية (Light & Env)"):
        l_1, l_2 = st.columns(2)
        with l_1:
            lighting_cust = st.selectbox("7. الإضاءة (Lighting)", ["", "Soft ambient lighting", "Studio lighting", "Three-point lighting", "Rim light", "Dramatic lighting", "Natural sunlight", "Neon light", "Volumetric light"])
        with l_2:
            color_pal = st.selectbox("8. الألوان (Palette)", ["", "Vibrant colors", "Muted tones", "Pastel colors", "Monochrome", "Warm colors", "Cold colors", "High contrast"])
        
        b_1, b_2 = st.columns(2)
        with b_1:
            bg_cust = st.selectbox("9. الخلفية (Background)", ["", "Minimal background", "Solid color", "Gradient", "Bokeh (Blurred)", "White studio", "Dark studio"])
        with b_2:
            env_cust = st.text_input("10. تفاصيل البيئة (Environment)", placeholder="مثال: شارع مستقبلي، غرفة مكتب، غابة...")

    # القسم هـ: إضافات
    with st.expander("✨ تفاصيل إضافية (Enhancements)"):
        enhancements = st.multiselect("15. تحسينات إضافية", ["Highly stylized", "Ultra-clean", "Soft shadows", "Subsurface scattering", "Global illumination", "Perfect anatomy", "Symmetrical face"])

    # زر التوليد لهذا التبويب
    if st.button("✨ إنشاء برومبت الشخصية المخصص", key="btn_custom", type="primary", use_container_width=True):
        # تحديد اسم الشخصية (من النص أو إشارة للصورة)
        final_subject = char_name if char_name else "A character"
        if uploaded_file:
            final_subject += " [Reference Image Used]"
        
        # تجميع الأجزاء غير الفارغة فقط
        prompt_parts = [
            f"Subject: {final_subject}",
            f"Outfit: {outfit_details}" if outfit_details else "",
            f"Shot: {shot_type}" if shot_type else "",
            f"Angle: {cam_angle}" if cam_angle else "",
            f"Style: {art_style_cust}" if art_style_cust else "",
            f"Design: {char_feat}" if char_feat else "",
            f"Pose: {pose_motion}" if pose_motion else "",
            f"Expression: {face_exp}" if face_exp else "",
            f"Lighting: {lighting_cust}" if lighting_cust else "",
            f"Colors: {color_pal}" if color_pal else "",
            f"Material: {materials}" if materials else "",
            f"Background: {bg_cust}" if bg_cust else "",
            f"Environment: {env_cust}" if env_cust else "",
            f"Camera: {cam_param}" if cam_param else "",
            f"Quality: {render_qual}" if render_qual else "",
            f"Enhancements: {', '.join(enhancements)}" if enhancements else ""
        ]
        
        # تنظيف القائمة من العناصر الفارغة ودمجها
        full_prompt = ", ".join([p for p in prompt_parts if p])
        
        # إضافة الأبعاد
        full_prompt += f" --ar {aspect_ratio.split(' ')[-1] if '--ar' not in aspect_ratio else aspect_ratio}"

        st.success("تم تجهيز البرومبت الاحترافي! انسخه أدناه:")
        st.code(full_prompt, language="text")
        
        if uploaded_file:
            st.info("ℹ️ ملاحظة: عند استخدام هذا البرومبت في جيميناي، تأكد من رفع الصورة التي اخترتها معه في الشات.")

st.markdown("---")
st.caption("🚀 تم التطوير لتسهيل العمل على Google Gemini & Midjourney")
