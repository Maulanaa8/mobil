import streamlit as st
import random

st.set_page_config(page_title="Game Tebak Kata 🎮", page_icon="🧩", layout="centered")

st.title("🎮 Game Tebak Kata")
st.write("Coba tebak kata yang disembunyikan! Kamu punya 6 kesempatan ❌.")

# Daftar kata
word_list = ["python", "streamlit", "teknologi", "komputer", "mahasiswa", "kecerdasan", "universitas"]

# Inisialisasi state
if "word" not in st.session_state:
    st.session_state.word = random.choice(word_list)
if "guessed" not in st.session_state:
    st.session_state.guessed = []
if "lives" not in st.session_state:
    st.session_state.lives = 6
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Fungsi reset game
def reset_game():
    st.session_state.word = random.choice(word_list)
    st.session_state.guessed = []
    st.session_state.lives = 6
    st.session_state.game_over = False

# Input huruf
guess = st.text_input("Masukkan huruf (a-z):", max_chars=1).lower()

if st.button("Tebak") and not st.session_state.game_over:
    if guess and guess.isalpha():
        if guess in st.session_state.word:
            st.success(f"Huruf **{guess}** ada di kata!")
            st.session_state.guessed.append(guess)
        else:
            st.error(f"Huruf **{guess}** tidak ada 😢")
            st.session_state.lives -= 1

    # Cek kondisi menang / kalah
    if all(letter in st.session_state.guessed for letter in set(st.session_state.word)):
        st.session_state.game_over = True
        st.balloons()
        st.success(f"🎉 Selamat! Kamu berhasil menebak kata **{st.session_state.word}**")

    if st.session_state.lives <= 0:
        st.session_state.game_over = True
        st.error(f"Game Over 😭 Kata yang benar adalah **{st.session_state.word}**")

# Tampilkan kata dengan huruf yang sudah ditebak
display_word = " ".join([letter if letter in st.session_state.guessed else "_" for letter in st.session_state.word])
st.subheader(f"**{display_word}**")

# Nyawa tersisa
st.write(f"❤️ Kesempatan tersisa: {st.session_state.lives}")

# Tombol restart
if st.button("🔄 Main Lagi"):
    reset_game()
