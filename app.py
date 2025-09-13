import streamlit as st
import random

st.set_page_config(page_title="Trivia Quiz Game", page_icon="🎮")
st.title("🎉 Advanced Trivia Quiz Game by ABM")

# Questions
quiz = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"], "answer": "William Shakespeare"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": "Blue Whale"},
    {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "NaCl"], "answer": "H2O"},
    {"question": "What is the fastest land animal?", "options": ["Cheetah", "Lion", "Tiger", "Horse"], "answer": "Cheetah"},
    {"question": "Which gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "What is 7 × 8?", "options": ["54", "56", "64", "58"], "answer": "56"},
    {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Van Gogh"], "answer": "Leonardo da Vinci"},
    {"question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"}
]

# Initiali
