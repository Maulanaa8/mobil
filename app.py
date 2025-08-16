import streamlit as st
import random

st.set_page_config(page_title="Game Tebak Kata 🧩", page_icon="🧩", layout="centered")

st.title("🧩 Game Tebak Kata Versi Kompleks (Wordle Style)")

# Level & kata
word_bank = {
    "Mudah": ["kucing", "pisang", "burung", "mobil", "bunga"],
    "Normal": ["teknologi", "komputer", "mahasiswa", "universitas", "perpustakaan"],
    "Sulit": ["kecerdasan", "algoritma", "implementasi", "pengembangan", "streamlit"]
}

# Init state
if "level" not in st.session_state:
    st.session_state.level = "Mudah"
if "word" not in st.session_state:
    st.session_state.word = random.choice(word_bank[st.session_state.level])
if "guesses" not in st.session_state:
    st.session_state.guesses = []
if "max_attempts" not in st.session_state:
    st.session_state.max_attempts = 6
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Reset game
def reset_game():
    st.session_state.word = random.choice(word_bank[st.session_state.level])
    st.session_state.guesses = []
    st.session_state.game_over = False

# Pilih level
level = st.radio("Pilih Level:", ["Mudah", "Normal", "Sulit"], horizontal=True)
if level != st.session_state.level:
    st.session_state.level = level
    reset_game()

# Input tebakan
if not st.session_state.game_over:
    guess = st.text_input("Masukkan tebakan kata:", "").lower()

    if st.button("Tebak"):
        if len(guess) == len(st.session_state.word):
            st.session_state.guesses.append(guess)
        else:
            st.warning(f"Kata harus {len(st.session_state.word)} huruf!")

# Render tebakan dengan warna
def render_guess(guess, word):
    result = []
    for i, ch in enumerate(guess):
        if ch == word[i]:
            result.append(f"🟩 {ch.upper()} ")
        elif ch in word:
            result.append(f"🟨 {ch.upper()} ")
        else:
            result.append(f"⬜ {ch.upper()} ")
    return "".join(result)

for g in st.session_state.guesses:
    st.write(render_guess(g, st.session_state.word))

# Cek kondisi akhir
if len(st.session_state.guesses) > 0:
    if st.session_state.guesses[-1] == st.session_state.word:
        st.success(f"🎉 Selamat! Kata yang benar adalah **{st.session_state.word.upper()}**")
        st.session_state.game_over = True
    elif len(st.session_state.guesses) >= st.session_state.max_attempts:
        st.error(f"Game Over 😭 Kata yang benar adalah **{st.session_state.word.upper()}**")
        st.session_state.game_over = True

# Tombol restart
if st.session_state.game_over:
    if st.button("🔄 Main Lagi"):
        reset_game()
