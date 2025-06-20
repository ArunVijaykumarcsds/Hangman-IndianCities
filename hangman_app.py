# hangman_app.py

import streamlit as st
import random
import string

# ---------- Setup ----------
st.set_page_config(page_title="🇮🇳 Hangman – I ❤ My India", page_icon="🇮🇳")

CITIES = [
    "Delhi", "Mumbai", "Chennai", "Bhopal", "Agra", "Jaipur", "Indore", "Lucknow",
    "Bengaluru", "Hyderabad", "Kolkata", "Pune", "Ahmedabad", "Surat", "Kanpur", "Nagpur",
    "Patna", "Vadodara", "Visakhapatnam", "Ludhiana", "Nashik", "Faridabad", "Meerut", "Rajkot",
    "Varanasi", "Srinagar", "Amritsar", "Ranchi", "Jabalpur", "Gwalior", "Coimbatore", "Madurai",
    "Raipur", "Kota", "Guwahati", "Thiruvananthapuram", "Vijayawada", "Mysuru", "Noida", "Howrah",
    "Aurangabad", "Dhanbad", "Navi Mumbai", "Prayagraj", "Chandigarh", "Shimla", "Dehradun", "Udaipur",
    "Jodhpur", "Panaji"
]

# ---------- Session State ----------
if "word" not in st.session_state:
    st.session_state.word = random.choice(CITIES).upper()
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.used_letters = set()
    st.session_state.lives = 7
    st.session_state.game_over = False
    st.session_state.result_message = ""

def get_display_word():
    return " ".join([letter if letter in st.session_state.used_letters else "_" for letter in st.session_state.word])

# ---------- Header ----------
st.title("🇮🇳 Hangman – I ❤ My India")
st.caption("A tribute to Indian cities and culture, one guess at a time.")

# ---------- Author & Tribute ----------
with st.container():
    st.markdown("---")
    st.markdown(
        "<h5 style='text-align: center;'>Created with ❤️ by <strong>Arun VK</strong><br>"
        "🇮🇳 Proud to be an Indian 🇮🇳</h5>",
        unsafe_allow_html=True
    )
    st.markdown("---")

# ---------- Game Display ----------
st.markdown(f"### Word: `{get_display_word()}`")
st.markdown(f"**Lives:** {st.session_state.lives}")
st.markdown(f"**Guessed Letters:** {' '.join(sorted(st.session_state.used_letters)) or 'None yet'}")

# ---------- Game Logic ----------
if not st.session_state.game_over:
    col1, col2 = st.columns([3, 1])
    with col1:
        guess = st.text_input("Your Guess", max_chars=1).upper().strip()
    with col2:
        submit = st.button("Guess")

    if submit:
        if not guess or guess not in string.ascii_uppercase:
            st.warning("Please enter a single valid English letter.")
        elif guess in st.session_state.used_letters:
            st.info(f"You already guessed '{guess}'. Try another letter.")
        else:
            st.session_state.used_letters.add(guess)
            if guess in st.session_state.word_letters:
                st.session_state.word_letters.remove(guess)
            else:
                st.session_state.lives -= 1

        if not st.session_state.word_letters:
            st.session_state.result_message = f"🎉 Congratulations! You guessed it! The city was **{st.session_state.word}**."
            st.session_state.game_over = True
        elif st.session_state.lives <= 0:
            st.session_state.result_message = f"😢 Game Over! You ran out of lives. The city was **{st.session_state.word}**."
            st.session_state.game_over = True

# ---------- Show Result and Restart ----------
if st.session_state.game_over:
    st.markdown("---")
    st.markdown(st.session_state.result_message)
    if st.button("🔁 Play Again"):
        for key in ["word", "word_letters", "used_letters", "lives", "game_over", "result_message"]:
            del st.session_state[key]
        st.rerun()
