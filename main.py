from question_wrapper import run_all_questions

if __name__ == "__main__":
    questions = __import__("questions")
    run_all_questions(require_input=True)
