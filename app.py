import streamlit as st
import random

def random_question_picker(questions, num_display):
    questions_list = questions.split("\n")
    random.shuffle(questions_list)
    selected_questions = questions_list[:num_display]

    st.write(f"Randomly selected {num_display} questions out of {len(questions_list)}:")
    for i, question in enumerate(selected_questions):
        st.write(f"{i + 1}. {question}")


def main():
    st.title("Random Question Picker")

    questions = st.text_area("Enter the questions (one per line):")
    num_display = st.number_input("Enter the number of questions to display:", min_value=1, step=1)

    if st.button("Pick Random Questions"):
        random_question_picker(questions, num_display)


if __name__ == "__main__":
    main()
      
