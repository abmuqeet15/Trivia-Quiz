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

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "questions_order" not in st.session_state:
    st.session_state.questions_order = random.sample(range(len(quiz)), len(quiz))
if "high_score" not in st.session_state:
    st.session_state.high_score = 0
if "rounds_played" not in st.session_state:
    st.session_state.rounds_played = 0
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None  # default value

# Function to handle answer submission
def submit_answer():
    q_index = st.session_state.questions_order[st.session_state.question_index]
    selected_option = st.session_state.selected_option
    if selected_option == quiz[q_index]["answer"]:
        st.session_state.score += 1
    st.session_state.question_index += 1
    st.session_state.selected_option = None  # reset for next question

# Display current round and score
st.write(f"**Round:** {st.session_state.rounds_played + 1}")
st.write(f"**Current Score:** {st.session_state.score}")

# Quiz logic
if st.session_state.question_index < len(quiz):
    q_index = st.session_state.questions_order[st.session_state.question_index]
    q = quiz[q_index]
    st.subheader(q["question"])
    st.radio("Choose your answer:", q["options"], key="selected_option")
    st.button("Submit Answer", on_click=submit_answer)
else:
    st.success(f"🎉 Round Completed! Your score: {st.session_state.score} / {len(quiz)}")
    
    if st.session_state.score > st.session_state.high_score:
        st.session_state.high_score = st.session_state.score
        st.balloons()
        st.write("🏆 New High Score!")

    st.write(f"**High Score:** {st.session_state.high_score}")
    st.session_state.rounds_played += 1

    if st.button("Next Round"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.questions_order = random.sample(range(len(quiz)), len(quiz))
        st.experimental_rerun()
    
    if st.button("Restart Game"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.questions_order = random.sample(range(len(quiz)), len(quiz))
        st.session_state.high_score = 0
        st.session_state.rounds_played = 0
        st.experimental_rerun()
