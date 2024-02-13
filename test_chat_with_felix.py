from chat_with_felix import analyze_excerpt


def run_test_cases():
    test_cases = [
        {
            "excerpt": {
                "conversation": "Sounds like the game plan. Let's do it.\nCool. Why don't you start with a brief intro?",
                "contains_question": True,
                "question": "Why don't you start with a brief intro?",
            }
        }
        # Add more test cases as needed
    ]

    total_excerpts = len(test_cases)
    correct_boolean_matches = 0
    correct_question_identification = 0
    reasoning_summary = {}

    for index, test_case in enumerate(test_cases, start=1):
        response = analyze_excerpt(test_case["excerpt"]["conversation"])

        if not isinstance(response, dict):
            print(f"Response for test case {index} is not a dictionary.")
            continue

        expected_has_interview_question = test_case["excerpt"]["contains_question"]
        actual_has_interview_question = response.get("has_interview_question", False)
        if expected_has_interview_question == actual_has_interview_question:
            correct_boolean_matches += 1

        expected_question = test_case["excerpt"]["question"].lower()
        actual_question = response.get("interview_question", "").lower()
        print(
            "  expected_question"
            + expected_question
            + "    actual question"
            + actual_question
        )
        if expected_has_interview_question and expected_question == actual_question:
            correct_question_identification += 1

        reasoning_summary[f"reasoning{index}"] = response.get(
            "reasoning", "No reasoning provided."
        )
    print(
        f"{correct_boolean_matches}/{total_excerpts} boolean statements and {correct_question_identification}/{total_excerpts} questions were identified correctly."
    )
    for key, value in reasoning_summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    run_test_cases()
