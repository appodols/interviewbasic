from chat_with_felix import analyze_excerpt


def run_test_cases():
    test_cases = [
        {
            "excerpt": {
                "conversation": "Hey, there we go.\nHey, are going hmm, all\nright. Yeah. Hey, Gordon. Sorry. I wasn't sure if you were running late, or maybe I had the wrong link and it wasn't working. So I tried on my phone first.\nThat's nice. How are you doing\ntoday? Good man. glad. Glad you were able to make time to chat. I'm excited to learn more about open phone. What about yourself? How's the Thursday going?",
                "contains_question": True,
                "question": "How's the Thursday going?",
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

        expected_contains_question = test_case["excerpt"]["contains_question"]
        actual_contains_question = response.get("contains_question", False)
        if expected_contains_question == actual_contains_question:
            correct_boolean_matches += 1

        expected_question = test_case["excerpt"]["question"].lower()
        actual_question = response.get("detected_question", "").lower()
        if expected_contains_question and expected_question == actual_question:
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
