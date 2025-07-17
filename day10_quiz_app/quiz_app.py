# quiz_app.py

def ask_question(question, correct_answer):
    try:
        answer = input(f"{question} ").strip().lower()
        if answer == correct_answer.lower():
            print("✅ Correct!\n")
            return 1
        else:
            print(f"❌ Incorrect. The correct answer is: {correct_answer}\n")
            return 0
    except Exception as e:
        print("⚠️ An error occurred:", e)
        return 0

print("=== Python Quiz App ===\n")
score = 0

score += ask_question("1. What is the keyword to define a function in Python?", "def")
score += ask_question("2. What symbol is used for comments?", "#")
score += ask_question("3. What does 'len()' return?", "length")

print(f"🎉 You got {score}/3 correct!")
