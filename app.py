import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title='الذكاء الاصطناعي التوليدي | SDAIA', layout='wide', initial_sidebar_state='collapsed')

st.markdown(
    """
    <style>
        /* Page Background - Soft Cream/Grayish White */
        html, body, [data-testid="stAppViewContainer"] {
            background: #F6F5F2;  /* Warm light cream */
            color: #1E293B;  /* Dark slate text for readability */
        }

        /* Sticky Bar */
        .sticky-bar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #1E3A8A;  /* SDAIA Dark Blue */
            padding: 10px 20px;
            box-shadow: 0 4px 12px rgba(30, 58, 138, 0.4);
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
            top: 50px;
        }

        .sticky-bar img {
            height: 65px;
            width: auto;
            margin-right: 20px;
        }

        .sticky-bar span {
            font-size: 28px;
            font-weight: bold;
            color: white;
        }

        /* Title Styling */
        h1 {
            font-family: 'Arial', sans-serif;
            text-align: center;
            font-size: 54px;
            font-weight: bold;
            color: #1E3A8A;
            margin-top: 20px;
            margin-bottom: 10px;
            text-shadow: 2px 2px 6px rgba(30, 58, 138, 0.15);
        }

        /* Flashcard Styling */
        .flashcard {
            width: 100%;
            height: 250px;
            background-color: #FAFAF9;  /* Light neutral off-white for cards */
            color: #1E3A8A;  /* Dark blue for text */
            text-align: center;
            border-radius: 18px;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
        }

        /* Buttons */
        .stButton button {
            background-color: transparent;
            border: 2px solid #1E3A8A;
            color: #1E3A8A;
            padding: 12px 22px;
            border-radius: 18px;
            font-size: 18px;
            transition: all 0.3s ease;
            animation: fadeIn 1.2s ease-in-out;
        }

        /* Button Hover */
        .stButton button:hover {
            background-color: #1E3A8A;
            color: white;
            transform: scale(1.04);
        }

        /* Fade-in Animation */
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        /* Flashcard Images */
        .flashcard img {
            width: 75%;
            margin-bottom: 12px;
        }

        /* Add margin around sections for spacious feel */
        .container, .flashcard {
            margin-top: 15px;
            margin-bottom: 15px;
        }

    </style>
    """,
    unsafe_allow_html=True
)


# Sticky bar content with photo on the left and text on the right
st.markdown(
    """
    <div class="sticky-bar">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/%D8%B4%D8%B9%D8%A7%D8%B1_%D8%A7%D9%84%D9%87%D9%8A%D8%A6%D8%A9_%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9_%D9%84%D9%84%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA_%D9%88%D8%A7%D9%84%D8%B0%D9%83%D8%A7%D8%A1_%D8%A7%D9%84%D8%A7%D8%B5%D8%B7%D9%86%D8%A7%D8%B9%D9%8A_SDAIA.svg/2560px-%D8%B4%D8%B9%D8%A7%D8%B1_%D8%A7%D9%84%D9%87%D9%8A%D8%A6%D8%A9_%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9_%D9%84%D9%84%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA_%D9%88%D8%A7%D9%84%D8%B0%D9%83%D8%A7%D8%A1_%D8%A7%D9%84%D8%A7%D8%B4%D8%B7%D9%86%D8%A7%D8%B9%D9%8A_SDAIA.svg.png" alt="Logo"> 
        <span> Generative AI </span>
    </div>
    """,
    unsafe_allow_html=True
)

# Add padding to the top of the page to avoid content overlap with the sticky bar
st.markdown("<div style='padding-top: 70px;'></div>", unsafe_allow_html=True)

# Title
st.markdown("<h1>الذكاء الاصطناعي التوليدي</h1>", unsafe_allow_html=True)
st.markdown("---")

# Image container
st.markdown('<div class="container">', unsafe_allow_html=True)
st.image("photos/A.IE.gif", use_column_width=True)  # Replace with your image path
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Flashcard content with charts
flashcard_content = {
    "ماهو الذكاء الاصطناعي ؟": { "answer":" الـذكاء الاصطناعـي التوليـدي هـو نـوع مـن أنـواع الـذكاء الاصطناعـي الـذي يسـتخدم تقنيـات تعلـم الآلـة والشـبكات ويمكـن لنمـاذج الـذكاء الاصطناعـي التوليـدي توليـد مخرجـات مـن نفـس نوع المدخلات  مثـل: مـن نـص إلـى نـص، أو مـن نـوع مختلـف، مثـل: مـن نـص إلـى صـورة أو مقطـع فيديـو", "image": "photos/introm.png"},
    "خطوات بناء نموذج": { "answer":"تعتمـــد نمـــاذج الـــذكاء الاصطناعـــي التوليـــدي علـــى تقنيـــات التعلـــم العميـــق وتســـتخدم الشـــبكات العصبيـــة والبنـــى المختلفـة لإنشـاء بيانـات جديـدة بنـاء ً علـى البيانـات الموجـودة فـي مجموعـة التدريـب، ويتضمـن بنـاء هـذه النمـاذج خطـوات أساسـية مـن أبرزهـا: تجهيـز البيانـات، وبنـاء النمـوذج، واختبـار النمـوذج، ونشـر النمـوذج، وتحسـين النمـوذج.", "image": "photos/modelm.png"},
    "أنواع المخرجات": { "answer":"توجـد عـدة أنـواع مـن المخرجـات التـي يمكـن توليدهـا باسـتخدام نمـاذج الـذكاء الاصطناعـي التوليـدي، ويمكـن تصنيفها إلـى الأنـواع الرئيسـية الآتية:", "image": "photos/typesm.png"},
    "حالات الاستخدام": { "answer":"يمكن استخدام نماذج الذكاء الاصطناعي التوليدي في إنجاز مهام متعددة في مختلف المجالات، مثل: خدمة العملاء والتسويق والتصميم والبرمجة، وتتميز هذه النماذج بقدرتها على الإبداع وتسريع سير الأعمال ورفع الإنتاجية.", "image": "photos/usem.png"},
    " مخاطر": { "answer":" تزداد المخاطر المتعلقة بالمعلومات المضللة مع تطور الذكاء الاصطناعي التوليدي بسبب قدرته المتقدمة على إنشاء محتوى يشبه المحتوى البشري بدقة عالية، مثل النصوص والصور والفيديوهات المزيفة (Deepfakes). هذه التقنيات تسهل انتشار الأخبار الكاذبة والتلاعب بالمعلومات مما يستدعي حلولًا فعالة لضمان استخدامه المسؤول", "image": "photos/dnm.png"},
    "امثلة لاستخدام": { 
    "answer": "تعتمد <a href='https://www.elevenlabs.io' target='_blank' style='color:#3B82F6; text-decoration: none;'>ElevenLabs</a> على الذكاء الاصطناعي التوليدي لتحويل النصوص إلى أصوات طبيعية أو تغيير الصوت، مما يسمح بإنشاء كلام بشري قابل للتخصيص بدقة. تُعد هذه التقنية مثالًا مبتكرًا على قدرة الذكاء الاصطناعي في توليد المحتوى الصوتي بشكل واقعي.", 
    "image": "photos/fff.gif"
}
}

# Initialize session state for card flipping
if "card_flipped" not in st.session_state:
    st.session_state.card_flipped = {key: False for key in flashcard_content.keys()}

# Function to flip a card
def flip_card(card_id):
    st.session_state.card_flipped[card_id] = not st.session_state.card_flipped[card_id]

# Render flashcards in rows of two
keys = list(flashcard_content.keys())
for i in range(0, len(keys), 2):  # Step by 2 to create rows
    row_keys = keys[i:i+2]  # Get two keys for the current row
    cols = st.columns(2)  # Create two columns for the row
    for col, key in zip(cols, row_keys):
        with col:
            if st.button(key, key=f"btn_{key}"):  # Button to simulate card click
                flip_card(key)
            if st.session_state.card_flipped[key]:
                st.markdown(
                    f"""
                    <div class="flashcard">
                        <p>{flashcard_content[key]['answer']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.image(flashcard_content[key]['image'], use_column_width=True)  # Display the image
            else:
                st.markdown(
                    f"""
                    <div class="flashcard">
                        <p>{key}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                ) 