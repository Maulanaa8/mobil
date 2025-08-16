import streamlit as st
import random

st.set_page_config(page_title="Flappy Bird 🐦", page_icon="🐦", layout="centered")

st.title("🐦 Flappy Bird Streamlit")

# Inisialisasi state
if "bird_y" not in st.session_state:
    st.session_state.bird_y = 5
if "pipes" not in st.session_state:
    st.session_state.pipes = [[15, random.randint(2, 8)]]
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

height = 12
width = 20
gap = 4

# Fungsi reset
def reset_game():
    st.session_state.bird_y = 5
    st.session_state.pipes = [[15, random.randint(2, 8)]]
    st.session_state.score = 0
    st.session_state.game_over = False

# Tombol kontrol
col1, col2, col3 = st.columns(3)
if col1.button("⬆️ Flap"):
    st.session_state.bird_y -= 2
if col3.button("🔄 Restart"):
    reset_game()

# Update game hanya kalau belum game over
if not st.session_state.game_over:
    st.session_state.bird_y += 1  # efek gravitasi

    # Gerakin pipa
    new_pipes = []
    for x, hole_y in st.session_state.pipes:
        x -= 1
        if x > 0:
            new_pipes.append([x, hole_y])
        else:
            st.session_state.score += 1
    st.session_state.pipes = new_pipes

    # Spawn pipa baru
    if len(st.session_state.pipes) == 0 or st.session_state.pipes[-1][0] < width - 8:
        st.session_state.pipes.append([width - 1, random.randint(2, height - gap - 2)])

    # Cek tabrakan
    for x, hole_y in st.session_state.pipes:
        if x == 2:  # posisi burung (fix di kolom 2)
            if not (hole_y <= st.session_state.bird_y <= hole_y + gap):
                st.session_state.game_over = True

    if st.session_state.bird_y < 0 or st.session_state.bird_y >= height:
        st.session_state.game_over = True

# Gambar arena
arena = [["⬛" for _ in range(width)] for _ in range(height)]

# Gambar pipa
for x, hole_y in st.session_state.pipes:
    for y in range(height):
        if not (hole_y <= y <= hole_y + gap):
            arena[y][x] = "🟩"

# Gambar burung
if not st.session_state.game_over:
    arena[st.session_state.bird_y][2] = "🐦"
else:
    arena[st.session_state.bird_y if 0 <= st.session_state.bird_y < height else height-1][2] = "💀"

# Render arena
for row in arena:
    st.write("".join(row))

st.subheader(f"🏆 Score: {st.session_state.score}")

if st.session_state.game_over:
    st.error("Game Over 😭 Tekan 🔄 Restart untuk main lagi")

# Auto refresh
st.experimental_rerun()
