from chat_with_felix import analyze_excerpt


def run_test_cases():
    test_cases = [
        {
            "excerpt": {
                "conversation": "Sounds like the game plan. Let's do it.\nCool. Why don't you start with a brief intro?",
                "contains_question": True,
                "question": "Why don't you start with a brief intro?",
            }
        },
        {
            "excerpt": {
                "conversation": "Yeah, it's very interesting. Cool, man. So I'm just wondering if you could like, maybe share an example, I was like, a product that you released, that you're very proud of, walk me through the journey and tell me why you chose you chose STM as part of product mix.",
                "contains_question": True,
                "question": "So I'm just wondering if you could like, maybe share an example, I was like, a product that you released, that you're very proud of, walk me through the journey and tell me why you chose you chose STM as part of product mix.",
            }
        },
        {
            "excerpt": {
                "conversation": "And so context was Instacart, like many other tech companies use this experience to decide whether to keep end user facing products. And use this across the board. Basically, all PMS and data, scientists use an internal experiment tool to reach those decisions. The problem was that in 20, that we had a very basic tool that we hadn't grown for a years and 2022, there was a lot of intense user distrust that not only was this tool, really difficult to use, there was perhaps giving us incorrect readings and costing the company a lot of money. So that was the problem space, my mission was to come on to the product that had an end product owner and yours and understand where's the actual problem area, and figure out how to improve it. And I had a disambiguate between three basic areas, the first one being the user experience of this experiment tool, the second one being with the communications between internal stakeholders.",
                "contains_question": False,
                "question": "",
            }
        },
        {
            "excerpt": {
                "conversation": "And you could use that to basically interpret existing behavior like that, again, really simplified analogies. If your friend is always 30 minutes late, and you plan to get lunch, and that friend shows up 30 minutes late, that the friend isn't trying to be like, who is maybe I don't need this analogy, but the friend isn't trying to be additionally late to to you and he that person is always like that. And that can have you if you are trying to remove like, I don't want any friends who treated disrespectfully go, oh, well, Sasha is always 30 minutes late. So he's not it's not intentional. is like the way so\n\nUnknown Speaker 12:59\nhow does that apply to experimentation? Sorry, Miss arias.",
                "contains_question": True,
                "question": "How does that apply to experimentation?",
            }
        },
        {
            "excerpt": {
                "conversation": "Yeah, that's pretty cool. I remember the question like, yeah, what is the reason that you're looking for like a product or brand term, like a full time job at a company? And also, the follow up? Question is, what are you looking for exactly in the next year?",
                "contains_question": True,
                "question": "what is the reason that you're looking for like a product or brand term, like a full time job at a company? And also, what are you looking for exactly in the next year?",
            }
        },
        {
            "excerpt": {
                "conversation": "Yeah, I think I'd love to, I'd love to share more about and I bought open from this, but I'm just generally interested in like, what do you expect? What what is your ideal situation in terms of in your next career that I think I heard about culture? wondering is, is there anything else you want to add?",
                "contains_question": True,
                "question": "what do you expect? What what is your ideal situation in terms of in your next career? wondering, is there anything else you want to add?",
            }
        },
        {
            "excerpt": {
                "conversation": "So yeah, in general, it varies. Is this role? Is the PMO a little more? Is it what's the balance? I would say between like executional work versus more like early stage, the PRD slash roadmap work? Is it like 5050? Definitely very, is it evolved based on where you guys are, in terms of",
                "contains_question": True,
                "question": "Is this role? Is the PMO a little more? Is it what's the balance? I would say between like executional work versus more like early stage, the PRD slash roadmap work? Is it like 5050? Definitely very, is it evolved based on where you guys are, in terms of",
            }
        },
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
