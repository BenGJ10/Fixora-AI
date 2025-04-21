import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:8000/debug/"  # Updated API endpoint for FixoraAI

st.set_page_config(page_title="FixoraAI", page_icon="🤖", layout="wide")

# Sidebar - Settings & Chat History
with st.sidebar:
    st.title("⚙️ Settings")
    theme = st.radio("Choose theme", ["Dark", "Light"])
    st.markdown("Built by [Ben Gregory John]")

    st.title("🕰️ Chat History")
    for i, session in enumerate(st.session_state.get("chat_sessions", [])):
        if st.button(f"Conversation {i+1}"):
            st.session_state.messages = session.copy()
            st.rerun()
    
    # New chat button
    if st.button("New Chat"):
        if st.session_state.get("messages"):
            st.session_state.chat_sessions.append(st.session_state.messages.copy())
        st.session_state.messages = []
        st.rerun()

# Theme-based Colors
if theme == "Dark":
    bg_color = "#dbdafb"
    user_bubble_color = "#a49ce4"
    bot_bubble_color = "#bcb4ee"
    text_color = "black"
else:
    bg_color = "#fdfbfb"
    user_bubble_color = "#"
    bot_bubble_color = "#"
    text_color = "black"

# CSS Styling
st.markdown(
    f"""
    <style>
    body {{
        background: linear-gradient(to right, #a18cd1, #fbc2eb);
        color: {text_color};
        font-family: 'Poppins', sans-serif;
    }}
    .nav-bar {{
        background-color: #8785A2;
        padding: 10px;
        color: white;
        text-align: center;
        font-size: 1rem;
        font-weight: bold;
        border-radius: 10px;
    }}
    .title {{
        text-align: center;
        font-size: 2.8rem;
        font-weight: bold;
        color: white !important;
        font-family: 'Poppins', sans-serif;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }}
    .subtitle {{
        text-align: center;
        font-size: 1.1rem;
        color: {text_color};
    }}
    button:hover {{
        background-color: #1B56FD !important;
        color: white !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown('<div class="title">Welcome to 🤖FixoraAI, BenGJ</div>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your AI-powered debugging assistant</p>', unsafe_allow_html=True)

# Initialize session state for messages and chat sessions
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = []

# Function to format messages as styled bubbles
def format_message(role, text):
    return f'''
        <div style="background-color:{user_bubble_color if role == "user" else bot_bubble_color};
                    color:{text_color};
                    padding:10px;
                    border-radius:10px;
                    margin:5px 0;
                    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);">
            {"👨‍💻 <b>You:</b>" if role == "user" else "🤖 <b>FixoraAI:</b>"} {text}
        </div>
    '''

# Display chat history
for role, text in st.session_state.messages:
    st.markdown(format_message(role, text), unsafe_allow_html=True)

# User input
user_input = st.chat_input("Enter your code snippet for debugging...")

if user_input:
    # Store & Display User Message
    st.session_state.messages.append(("user", user_input))
    st.markdown(format_message("user", user_input), unsafe_allow_html=True)

    # Show typing animation
    typing_placeholder = st.empty()
    typing_placeholder.markdown("🤖 FixoraAI is analyzing your code...")
    time.sleep(1.5)
    typing_placeholder.empty()

    # Send request to FastAPI backend
    response = requests.post(API_URL, json={"code": user_input})
    
    if response.status_code == 200:
        bot_reply = response.json().get("debugging_details", "No debugging suggestions found.")
    else:
        bot_reply = "❌ Error: Unable to fetch response."

    # Store Bot Response
    st.session_state.messages.append(("assistant", bot_reply))
    st.markdown(format_message("assistant", bot_reply), unsafe_allow_html=True)

# Buttons for Chat Management
col1, col2 = st.columns(2)
with col1:
    chat_text = "\n\n".join([f"{role.upper()}: {text}" for role, text in st.session_state.messages])
    st.download_button("Download Current Chat", chat_text, file_name="fixora_chat", use_container_width=True)
with col2:
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
