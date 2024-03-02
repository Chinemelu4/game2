import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Dice game", page_icon="🤖", layout="wide")

st.title("Dice game")
st.subheader("Roll for your chance win big")

st.sidebar.image("dice_animation.gif")

st.image("dice3.gif")

def dice_game():
    a, b = np.random.randint(1,7,2)
    st.write(f"Your numbers are {a} and {b}")
    if a==6 and b==6:
        st.balloons()
        return('Congratulations! You win')

    else:
        return("Almost there! Keep trying")
    
if st.button("Play"):
    st.image("dice3.gif",width=100)
    st.write(dice_game())

    