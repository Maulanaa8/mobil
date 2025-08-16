import streamlit as st
import random

st.set_page_config(page_title="Tebak Kata ✨", page_icon="🧩", layout="centered")

st.title("🧩 Game Tebak Kata per Huruf")

# Daftar kata
word_list = ["python", "streamlit", "teknologi", "komputer", "mahasiswa", "universitas", "algoritma"]

# Init state
if "word" not in st.session_state:
    st.session_state.word = random.choice(word_list)
if "guessed_letters" not in st.session_state:
    st.session_state.guessed_letters = []
if "lives" not in st.session_state:
    st.session_state.lives = 6
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "last_guess" not in st.session_state:
    st.session_state.last_guess = ""

def reset_game():
    st.session_state.word = random.choice(word_list)
    st.session_state.guessed_letters = []
    st.session_state.lives = 6
    st.session_state.game_over = False
    st.session_state.last_guess = ""

# Tampilkan jumlah huruf
display_word = " ".join([letter if letter in st.session_state.guessed_letters else "_" for letter in st.session_state.word])
st.subheader(f"Kata: {display_word}")
st.caption(f"Jumlah huruf: {len(st.session_state.word)}")

# Input huruf langsung diproses
if not st.session_state.game_over:
    guess = st.text_input("Masukkan satu huruf:", max_chars=1, key="guess_input").lower()

    # Cek kalau ada huruf baru diketik (beda dari last_guess)
    if guess and guess != st.session_state.last_guess:
        st.session_state.last_guess = guess
        if guess in st.session_state.guessed_letters:
            st.warning(f"Huruf **{guess}** sudah ditebak!")
        elif guess in st.session_state.word:
            st.success(f"Huruf **{guess}** ada di kata!")
            st.session_state.guessed_letters.append(guess)
        else:
            st.error(f"Huruf **{guess}** tidak ada 😢")
            st.session_state.lives -= 1

        # Cek menang
        if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
            st.success(f"🎉 Selamat! Kamu berhasil menebak kata **{st.session_state.word.upper()}**")
            st.session_state.game_over = True

        # Cek kalah
        if st.session_state.lives <= 0:
            st.error(f"Game Over 😭 Kata yang benar adalah **{st.session_state.word.upper()}**")
            st.session_state.game_over = True

# Tampilkan nyawa
st.write(f"❤️ Kesempatan tersisa: {st.session_state.lives}")

# Tombol restart
if st.button("🔄 Main Lagi"):
    reset_game()
