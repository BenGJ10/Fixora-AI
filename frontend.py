import streamlit as st
import requests
import time

# Set up Streamlit page configuration
st.set_page_config(page_title="FixoraAI - Debugging Assistant", layout="wide")

# Custom CSS for UI styling and text wrapping fix
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        body { background-color: #1E1E1E; color: white; font-family: 'Poppins', sans-serif; }
        .main-container { display: flex; justify-content: center; align-items: center; height: 90vh; }
        .chat-container { width: 70%; background: #2A2A2A; padding: 20px; border-radius: 15px; box-shadow: 0px 0px 15px rgba(255,255,255,0.1); }
        .stTextArea textarea { font-size: 18px; padding: 10px; border-radius: 10px; background: #333; color: white; }
        .stButton button { background-color: #7D3C98; color: white; font-size: 18px; padding: 10px 20px; border-radius: 8px; }
        
        /* Chat Message Styling */
        .message-container { 
            background-color: #2A2A2A; padding: 12px; border-radius: 10px; 
            margin-bottom: 12px; display: flex; align-items: flex-start; 
            width: 100%; max-width: 800px; 
            word-wrap: break-word; overflow-wrap: break-word; white-space: pre-wrap;
        }
        
        .user-message { color: #FFD700; font-weight: bold; }
        .ai-message { color: #50C8F0; font-weight: bold; }
        .avatar { width: 35px; height: 35px; border-radius: 50%; margin-right: 12px; }
        
        /* Typing Effect */
        .typing-animation { font-style: italic; color: #AAAAAA; }

        /* Input Box */
        .stChatInput input { 
            border: 2px solid transparent;
            border-image: linear-gradient(90deg, #8E44AD, #C0392B) 1; 
            border-radius: 12px; 
            padding: 14px; 
            color: #FFFFFF; 
            background: #1E1E1E; 
            width: 98%; 
            max-width: 100%; 
            box-sizing: border-box; 
            font-size: 16px; 
            transition: all 0.3s ease-in-out; 
        }

        .stChatInput input:focus {
            border-color: #C0392B;
            outline: none;
            box-shadow: 0 0 10px rgba(192, 57, 43, 0.7);
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Professional Header
st.markdown("""
    <h1 style='text-align: center;'>🤖 Welcome to FixoraAI, Ben GJ</h1>
    <h3 style='text-align: center; font-weight: 300;'>AI-powered debugging assistant that helps you fix code errors efficiently.</h3>
""", unsafe_allow_html=True)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for role, text in st.session_state.messages:
    avatar = "👤" if role == "user" else "🤖"
    with st.chat_message(role):
        st.markdown(f"<div class='message-container'><span class='avatar'>{avatar}</span><span class='{role}-message'>{text}</span></div>", unsafe_allow_html=True)

# User input field
user_input = st.chat_input("Enter your code snippet here...")

if user_input:
    # Display user message
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(f"<div class='message-container'><span class='avatar'>👤</span><span class='user-message'>{user_input}</span></div>", unsafe_allow_html=True)
    
    # Show typing animation
    with st.chat_message("assistant"):
        typing_placeholder = st.empty()
        for _ in range(3):
            typing_placeholder.markdown("<span class='typing-animation'>FixoraAI is thinking...</span>", unsafe_allow_html=True)
            time.sleep(0.5)
        typing_placeholder.empty()
    
    # Send request to FastAPI backend
    response = requests.post("http://127.0.0.1:8000/debug/", json={"code": user_input})
    
    if response.status_code == 200:
        bot_reply = response.json().get("debugging_details", "No suggestions available.")
    else:
        bot_reply = "❌ Error: Unable to fetch response."
    
    # Display bot response with real-time typing effect (ChatGPT-like)
    st.session_state.messages.append(("assistant", bot_reply))
    with st.chat_message("assistant"):
        bot_placeholder = st.empty()
        bot_response = ""
        for char in bot_reply:
            bot_response += char
            bot_placeholder.markdown(f"<div class='message-container'><span class='avatar'>🤖</span><span class='ai-message'>{bot_response}</span></div>", unsafe_allow_html=True)
            time.sleep(0.01)  # Simulate typing effect
        bot_placeholder.markdown(f"<div class='message-container'><span class='avatar'>🤖</span><span class='ai-message'>{bot_response}</span></div>", unsafe_allow_html=True)
