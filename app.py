import streamlit as st
import random
import time

# Setup UI
st.set_page_config(page_title="Racing Game 🚗", page_icon="🏎️", layout="centered")

st.title("🏎️ Racing Game by Gen Z")

# State
if "player_x" not in st.session_state:
    st.session_state.player_x = 2  # posisi awal (0-4)
if "score" not in st.session_state:
    st.session_state.score = 0
if "enemies" not in st.session_state:
    st.session_state.enemies = []
if "game_over" not in st.session_state:
    st.session_state.game_over = False

road_width = 5  # jumlah jalur
road_height = 12  # tinggi arena
car_symbol = "🚙"
enemy_symbol = "🚗"

def reset_game():
    st.session_state.player_x = 2
    st.session_state.score = 0
    st.session_state.enemies = []
    st.session_state.game_over = False

# Kontrol player
col1, col2, col3 = st.columns(3)
if col1.button("⬅️"):
    if st.session_state.player_x > 0:
        st.session_state.player_x -= 1
if col3.button("➡️"):
    if st.session_state.player_x < road_width - 1:
        st.session_state.player_x += 1
if col2.button("🔄 Restart"):
    reset_game()

# Update game
if not st.session_state.game_over:
    # spawn musuh random
    if random.randint(0, 3) == 0:
        st.session_state.enemies.append([random.randint(0, road_width - 1), 0])

    # gerakin musuh ke bawah
    new_enemies = []
    for (ex, ey) in st.session_state.enemies:
        ey += 1
        if ey < road_height:
            new_enemies.append([ex, ey])
        else:
            st.session_state.score += 1
    st.session_state.enemies = new_enemies

    # cek tabrakan
    for (ex, ey) in st.session_state.enemies:
        if ey == road_height - 1 and ex == st.session_state.player_x:
            st.session_state.game_over = True

# Gambar arena
arena = [["⬛" for _ in range(road_width)] for _ in range(road_height)]

# taruh musuh
for (ex, ey) in st.session_state.enemies:
    arena[ey][ex] = enemy_symbol

# taruh player
if not st.session_state.game_over:
    arena[road_height - 1][st.session_state.player_x] = car_symbol
else:
    arena[road_height - 1][st.session_state.player_x] = "💥"

# Tampilkan arena
for row in arena:
    st.write(" ".join(row))

# Skor
st.subheader(f"🏆 Score: {st.session_state.score}")

# Game over
if st.session_state.game_over:
    st.error("Game Over 😭 Tekan 🔄 Restart buat main lagi!")
