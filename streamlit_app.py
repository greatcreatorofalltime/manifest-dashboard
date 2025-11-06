import streamlit as st
import random
from datetime import datetime, timedelta
import json

# 页面设置
st.set_page_config(
    page_title="宇宙訂單 - 顯化你的現實",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS样式 - 黑色背景与虹彩色系
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7, #DDA0DD, #98D8C8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
        animation: shimmer 3s ease-in-out infinite alternate;
    }
    @keyframes shimmer {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    .section-header {
        font-size: 2rem;
        background: linear-gradient(45deg, #6C63FF, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 2rem 0 1rem 0;
        border-left: 5px solid;
        border-image: linear-gradient(45deg, #6C63FF, #FF6B6B, #4ECDC4) 1;
        padding-left: 1rem;
    }
    .ingredient-card {
        background: linear-gradient(135deg, rgba(102,126,234,0.8) 0%, rgba(118,75,162,0.8) 100%);
        backdrop-filter: blur(10px);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .ingredient-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(255,255,255,0.2);
    }
    .whatsapp-container {
        background: rgba(229, 221, 213, 0.1);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        max-width: 400px;
        margin-left: auto;
        margin-right: auto;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .whatsapp-message {
        background: rgba(255,255,255,0.1);
        padding: 0.8rem 1.2rem;
        border-radius: 7.5px;
        margin: 0.5rem 0;
        box-shadow: 0 1px 0.5px rgba(255,255,255,0.1);
        position: relative;
        backdrop-filter: blur(5px);
    }
    .message-received {
        background: rgba(255,255,255,0.15);
        margin-right: 20%;
    }
    .message-sent {
        background: linear-gradient(135deg, rgba(220,248,198,0.3) 0%, rgba(180,228,150,0.3) 100%);
        margin-left: 20%;
        text-align: right;
    }
    .message-time {
        font-size: 0.7rem;
        color: #cccccc;
        margin-top: 0.3rem;
    }
    .manifestation-btn {
        background: linear-gradient(135deg, #FF6B6B 0%, #FFE66D 25%, #4ECDC4 50%, #45B7D1 75%, #96CEB4 100%);
        background-size: 200% 200%;
        color: black;
        padding: 1rem 2rem;
        border: none;
        border-radius: 25px;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        margin: 2rem auto;
        display: block;
        animation: gradientShift 3s ease infinite;
        transition: transform 0.3s ease;
    }
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .manifestation-btn:hover {
        transform: scale(1.05);
    }
    .download-btn {
        background: linear-gradient(135deg, #6C63FF 0%, #4A44B5 100%);
        color: white;
        padding: 0.8rem 1.5rem;
        border: none;
        border-radius: 20px;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        margin: 1rem auto;
        display: block;
        transition: transform 0.3s ease;
    }
    .download-btn:hover {
        transform: scale(1.05);
    }
    
    /* 修复输入框和选择框的样式 */
    .stTextArea textarea {
        background-color: rgba(255,255,255,0.9) !important;
        color: #000000 !important;
        border: 1px solid rgba(255,255,255,0.3) !important;
        border-radius: 10px !important;
    }
    .stTextArea textarea:focus {
        border-color: #6C63FF !important;
        box-shadow: 0 0 0 1px #6C63FF !important;
    }
    .stMultiSelect [data-baseweb="select"] {
        background-color: rgba(255,255,255,0.9) !important;
        border: 1px solid rgba(255,255,255,0.3) !important;
        border-radius: 10px !important;
    }
    .stMultiSelect [data-baseweb="select"]:focus-within {
        border-color: #6C63FF !important;
        box-shadow: 0 0 0 1px #6C63FF !important;
    }
    .stMultiSelect [data-baseweb="tag"] {
        background-color: rgba(108, 99, 255, 0.8) !important;
        color: white !important;
    }
    .stButton button {
        background: linear-gradient(135deg, #6C63FF 0%, #4A44B5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.3s ease !important;
    }
    .stButton button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 5px 15px rgba(108, 99, 255, 0.4) !important;
    }
    .stDownloadButton button {
        background: linear-gradient(135deg, #4ECDC4 0%, #45B7D1 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.3s ease !important;
    }
    .stDownloadButton button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 5px 15px rgba(78, 205, 196, 0.4) !important;
    }
    
    /* 修复其他元素的文字颜色 */
    .stMultiSelect [data-baseweb="select"] div {
        color: #000000 !important;
    }
    .stMultiSelect [data-baseweb="popover"] {
        background-color: rgba(255,255,255,0.95) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }
    .stMultiSelect [data-baseweb="popover"] li {
        background-color: transparent !important;
        color: #000000 !important;
    }
    .stMultiSelect [data-baseweb="popover"] li:hover {
        background-color: rgba(108, 99, 255, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# 应用标题
st.markdown('<div class="main-header">🌌 宇宙訂單 - 顯化你的現實</div>', unsafe_allow_html=True)

# 介绍
st.markdown("""
<div style='text-align: center; font-size: 1.2rem; color: #cccccc; margin-bottom: 3rem;'>
歡迎來到你的個人顯化廚房！在這裡，你將像製作美味蛋糕一樣，精心調配屬於你的理想現實。<br>
選擇你的材料，詳細視覺化，然後見證宇宙如何回應你的訂單。
</div>
""", unsafe_allow_html=True)

# 分栏布局
col1, col2 = st.columns([1, 1])

with col1:
    # 第一步：选择显化领域
    st.markdown('<div class="section-header">🎯 第一步：選擇你的顯化領域</div>', unsafe_allow_html=True)
    
    domains = {
        "物質財富": ["豐盛", "創造", "力量"],
        "屬世事業": ["豐盛", "創造", "力量", "陰陽平衡"],
        "健康": ["喜樂", "和平", "愛心", "陰陽平衡"],
        "個人靈性生活": ["和平", "創造", "愛心", "陰陽平衡"],
        "個人興趣": ["喜樂", "創造", "愛心"]
    }
    
    selected_domains = st.multiselect(
        "選擇你想要顯化的生命領域:",
        list(domains.keys()),
        default=["物質財富", "健康"]
    )

with col2:
    # 第二步：选择能量材料
    st.markdown('<div class="section-header">🎨 第二步：調配你的能量材料</div>', unsafe_allow_html=True)
    
    ingredients = {
        "豐盛": "吸引財富和豐裕的能量",
        "喜樂": "帶來內心喜悅與快樂",
        "和平": "創造內在平靜與和諧",
        "創造": "激發創造力與創新思維",
        "力量": "增強個人力量與決心",
        "愛心": "培養無條件的愛與慈悲",
        "陰陽平衡": "達到生命的平衡與和諧"
    }
    
    # 根据选择的领域推荐材料
    recommended_ingredients = []
    for domain in selected_domains:
        recommended_ingredients.extend(domains[domain])
    
    selected_ingredients = st.multiselect(
        "選擇你想要融入的能量材料:",
        list(ingredients.keys()),
        default=list(set(recommended_ingredients))[:3]  # 去重并限制默认选择数量
    )

# 显示选择的材料卡片
if selected_ingredients:
    st.markdown('<div class="section-header">✨ 你的能量配方</div>', unsafe_allow_html=True)
    cols = st.columns(len(selected_ingredients))
    for idx, ingredient in enumerate(selected_ingredients):
        with cols[idx]:
            st.markdown(f'''
            <div class="ingredient-card">
                <h3>{ingredient}</h3>
                <p>{ingredients[ingredient]}</p>
            </div>
            ''', unsafe_allow_html=True)

# 第三步：详细视觉化
st.markdown('<div class="section-header">🌠 第三步：詳細視覺化你的新現實</div>', unsafe_allow_html=True)

visualization_prompts = {
    "物質財富": "詳細描述你理想中的財富狀況：你看到什麼？感受到什麼？具體數字是多少？",
    "屬世事業": "描繪你成功事業的畫面：你在做什麼？環境如何？成就感如何？",
    "健康": "描述你完美的健康狀態：身體感覺如何？能量水平怎樣？日常活動如何？",
    "個人靈性生活": "表達你的靈性經驗：內在感受如何？與宇宙的連結是怎樣的？",
    "個人興趣": "展現你沉浸在嗜好中的喜悅：具體在做什麼？感受如何？"
}

# 存储可视化内容
visualization_data = {}
for domain in selected_domains:
    prompt = visualization_prompts.get(domain, "詳細描述你在這個領域的理想現實：")
    visualization_text = st.text_area(
        f"{domain}的視覺化:",
        value=f"在我的{domain}中，我看到...",
        height=100,
        key=f"viz_{domain}"
    )
    visualization_data[domain] = visualization_text

# 第四步：生成WhatsApp对话
st.markdown('<div class="section-header">💫 第四步：接收宇宙的確認</div>', unsafe_allow_html=True)

order_submitted = st.button("🌌 向宇宙下訂單", use_container_width=True, key="manifest_btn")

# 初始化session state
if 'order_submitted' not in st.session_state:
    st.session_state.order_submitted = False

if order_submitted:
    st.session_state.order_submitted = True

if st.session_state.order_submitted:
    # 生成随机的未来日期（1-30天内）
    future_date = datetime.now() + timedelta(days=random.randint(1, 30))
    date_str = future_date.strftime("%Y年%m月%d日")
    
    # 生成对话内容
    messages = [
        {"type": "received", "text": "嗨！我有一個令人興奮的消息要告訴你！", "time": "上午10:23"},
        {"type": "received", "text": f"關於你{random.choice(selected_domains)}的顯化，宇宙已經收到了你的訂單！", "time": "上午10:23"},
        {"type": "received", "text": f"我看到你在{', '.join(selected_ingredients)}的能量中正在創造美妙的現實。", "time": "上午10:24"},
        {"type": "sent", "text": "太棒了！我能感受到能量已經在流動了！", "time": "上午10:25"},
        {"type": "received", "text": f"是的！預計在{date_str}左右，你會開始看到明顯的跡象。", "time": "上午10:25"},
        {"type": "received", "text": "保持信心，繼續視覺化，宇宙正在為你安排最完美的時機！", "time": "上午10:26"},
        {"type": "sent", "text": "感謝宇宙！我已經準備好要接收這份禮物了！✨", "time": "上午10:26"}
    ]
    
    # 显示WhatsApp对话
    st.markdown('<div class="whatsapp-container">', unsafe_allow_html=True)
    for msg in messages:
        if msg["type"] == "received":
            st.markdown(f'''
            <div class="whatsapp-message message-received">
                {msg["text"]}
                <div class="message-time">{msg["time"]}</div>
            </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown(f'''
            <div class="whatsapp-message message-sent">
                {msg["text"]}
                <div class="message-time">{msg["time"]}</div>
            </div>
            ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 显示成功信息
    st.success("✨ 你的宇宙訂單已成功發送！保持開放的心態，準備接收宇宙的禮物。")
    
    # 创建下载内容
    download_content = f"""宇宙訂單 - 顯化紀錄
生成時間: {datetime.now().strftime("%Y年%m月%d日 %H:%M")}

🎯 顯化領域:
{chr(10).join(['• ' + domain for domain in selected_domains])}

🎨 能量材料:
{chr(10).join(['• ' + ingredient + ': ' + ingredients[ingredient] for ingredient in selected_ingredients])}

🌠 視覺化內容:
"""
    
    for domain, content in visualization_data.items():
        download_content += f"\n{domain}:\n{content}\n"
    
    download_content += f"""
    
💫 宇宙確認對話:
"""
    
    for msg in messages:
        sender = "宇宙" if msg["type"] == "received" else "我"
        download_content += f"\n{msg['time']} {sender}: {msg['text']}"
    
    download_content += f"""

🌟 記住：你本來就是豐盛的，你本來就是完整的。
相信宇宙，更重要的，相信自己！✨
"""
    
    # 提供下载按钮
    st.download_button(
        label="📥 下載我的顯化紀錄",
        data=download_content,
        file_name=f"宇宙訂單_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
        mime="text/plain",
        use_container_width=True
    )

# 第五步：商店引导
st.markdown('<div class="section-header">📚 深化你的顯化旅程</div>', unsafe_allow_html=True)

st.markdown(f"""
<div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(245,247,250,0.1) 0%, rgba(195,207,226,0.1) 100%); border-radius: 15px; border: 1px solid rgba(255,255,255,0.1);'>
    <h3 style='color: white;'>想要更深入地探索顯化藝術？</h3>
    <p style='color: #cccccc;'>造訪我們的宇宙日記商店，獲取更多工具和指導來支持你的旅程。</p>
    <a href='https://honorable-monarch-3bd.notion.site/journaling_the_universe-2843ea49e02c802bb483f23b7e6cb83d?source=copy_link' target='_blank'>
        <button style='
            background: linear-gradient(135deg, #6C63FF 0%, #4A44B5 100%);
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 25px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            margin: 1rem;
            transition: transform 0.3s ease;
        '>
            🛍️ 參觀宇宙日記商店
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# 页脚
st.markdown("""
<div style='text-align: center; margin-top: 4rem; color: #999; font-size: 0.9rem;'>
    <hr style='border-color: #333;'>
    <p>記住：你本來就是豐盛的，你本來就是完整的。這個工具只是提醒你要記起自己的真實本質。</p>
    <p>🌙 相信宇宙，更重要的，相信自己 🌟</p>
</div>
""", unsafe_allow_html=True)
