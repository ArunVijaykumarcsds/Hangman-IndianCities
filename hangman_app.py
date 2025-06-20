# ===================================================
# 🇮🇳 Hangman Game – Streamlit Edition (2025)
# ---------------------------------------------------
# 🎮 Author: Arun VK
# 📌 Description: A web-based Hangman game featuring
#     Indian cities, patriotic styling, and clean UX.
# 💻 Built with: Python & Streamlit
# 🧠 Purpose: Portfolio project blending culture & code
# ===================================================

import streamlit as st
import random

# Hangman stages as emoji art
HANGMAN_PICS = [
    "😵\n/|\\\n/ \\",  # 0 lives
    "😣\n/|\\\n/ ",   # 1 life
    "😟\n/|\\",       # 2 lives
    "😕\n/|",         # 3 lives
    "😐\n/",          # 4 lives
    "🙂",             # 5 lives
    "😃"              # 6 lives (full)
]

CITIES = [
    "Delhi", "Mumbai", "Chennai", "Bhopal", "Agra", "Jaipur", "Indore",
    "Lucknow", "Bengaluru", "Hyderabad", "Kolkata", "Pune", "Ahmedabad",
    "Surat", "Kanpur", "Nagpur", "Patna", "Vadodara", "Visakhapatnam",
    "Ludhiana", "Nashik", "Faridabad", "Meerut", "Rajkot", "Varanasi",
    "Srinagar", "Amritsar", "Ranchi", "Jabalpur", "Gwalior", "Coimbatore",
    "Madurai", "Raipur", "Kota", "Guwahati", "Thiruvananthapuram", "Vijayawada",
    "Mysuru", "Noida", "Howrah", "Aurangabad", "Dhanbad", "Navi Mumbai",
    "Prayagraj", "Chandigarh", "Shimla", "Dehradun", "Udaipur", "Jodhpur", "Panaji"
]

st.set_page_config(page_title="🇮🇳 Hangman – I ❤ My India", page_icon="🎮")
st.title("🇮🇳 Hangman – I ❤ My India")
st.caption("Created by Arun VK using Streamlit")

if "word" not in st.session_state:
    st.session_state.word = random.choice(CITIES).upper()
    st.session_state.guessed = set()
    st.session_state.lives = 6
    st.session_state.playing = True

def reset_game():
    st.session_state.word = random.choice(CITIES).upper()
    st.session_state.guessed = set()
    st.session_state.lives = 6
    st.session_state.playing = True

if st.button("🔁 Restart Game"):
    reset_game()

word_display = " ".join([letter if letter in st.session_state.guessed else "_" for letter in st.session_state.word])
st.header(f"Word: {word_display}")
st.subheader(f"Lives: {st.session_state.lives}   {HANGMAN_PICS[st.session_state.lives]}")

cols = st.columns(13)
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    if letter in st.session_state.guessed or not st.session_state.playing:
        cols[i % 13].button(letter, disabled=True)
    else:
        if cols[i % 13].button(letter):
            st.session_state.guessed.add(letter)
            if letter not in st.session_state.word:
                st.session_state.lives -= 1

if st.session_state.playing:
    if all(letter in st.session_state.guessed for letter in st.session_state.word):
        st.success(f"You guessed it! 🎉 The word was **{st.session_state.word}**.")
        st.session_state.playing = False
    elif st.session_state.lives == 0:
        st.error(f"You lost! 💀 The word was **{st.session_state.word}**.")
        st.session_state.playing = False
