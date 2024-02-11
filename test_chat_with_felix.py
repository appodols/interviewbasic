import unittest
from chat_with_felix import analyze_excerpt

class ChatFelixTest(unittest.TestCase):
    total_excerpts = 0
    correct_boolean_matches = 0
    correct_question_identification = 0
    reasoning_summary = {}

    @classmethod
    def setUpClass(cls):
        cls.total_excerpts = 0
        cls.correct_boolean_matches = 0
        cls.correct_question_identification = 0
        cls.reasoning_summary = {}

    def test_analyze_excerpt(self):
        test_cases = [
             {
        "excerpt": {
            "conversation": "Hey, there we go.\nHey, are going hmm, all\nright. Yeah. Hey, Gordon. Sorry. I was trying to troubleshoot. I wasn't sure if you were running late, or maybe I had the wrong link and it wasn't working. So I tried on my phone first.\nThat's nice. How are you doing\ntoday? Good man. glad. Glad you were able to make time to chat. I'm excited to learn more about open phone. What about yourself? How's the Thursday going?",
            "contains_question": True,
            "question": "How's the Thursday going?"
        }
    },
    {
        "excerpt": {
            "conversation": "Sounds like the game plan. Let's do it.\nCool. Why don't you start with a brief intro?",
            "contains_question": True,
            "question": "Why don't you start with a brief intro?"
        }
    },
    {
        "excerpt": {
            "conversation": "Sure. So I'm Sasha, I've been in tech for about five years, the first half that was in at Google as an engineer before transitioning the product both first partially at Google that Instacart for two years until layoff last year, and I split time now between building my own products right now. I'm working on a podcast transcription site and interviewing for my next role.",
            "contains_question": False,
            "question": ""
        }
    },
    {
        "excerpt": {
            "conversation": "Nice. Wow, that is so cool. Can Do you expect to do like to keep your the transcription service as well?",
            "contains_question": True,
            "question": "Can Do you expect to do like to keep your the transcription service as well?"
        }
    },
    {
        "excerpt": {
            "conversation": "I haven't fully thought through that. Right now. It's mainly just focusing on that MVP. And there's really two goals from it. One is I personally use this service. I think that one of the reasons I'm into open phones is it's a way of getting all this information. The parallels between the podcast and open phones is a bit tangent are, how do you make sense of all this information? The world has an in a thoughtful way. And I like those types of problems. But to answer the question, I'm not sure I'd like to get that MVP and see if I have product market fit. When a good part of it I'm doing it's also just part of the job search. It is helping me learn skills and just communicate my value externally beyond just representing myself on Zoom. So when I get a full month's Alisher, but it's been a good learning so far.",
            "contains_question": False,
            "question": ""
        }
    },
    {
        "excerpt": {
            "conversation": "So for me, Gordon here, I joined open forum about a month ago, still enjoying it. Before that I was at Facebook or meetup. And before that I was at Microsoft Teams, then a Fintech startup in Miami, and then another eight years at Microsoft. I'm also an advisor on the side to help grow businesses for FinTech software, Martex startup in Asia.",
            "contains_question": False,
            "question": ""
        }
    },
    {
        "excerpt": {
            "conversation": "Wow. So you did a bunch of different things. What's what's been your favorite learning and of all those experiences? Is it the current one was this particular phase you felt you grew out during that journey?",
            "contains_question": True,
            "question": "What's what's been your favorite learning and of all those experiences?"
        }
    },
    {
        "excerpt": {
            "conversation": "My favorite learning would be actually how I motivate team members and support them. To to do wonders, like I love it when there are product members that like oh, here's what I think. Here's why. And then here's the result. If that would be like my job. Now, I guess my favorite theoretical moment,",
            "contains_question": False,
            "question": ""
        }
    }
            # Your test cases here
        ]

        for index, test_case in enumerate(test_cases, start=1):
            response = analyze_excerpt(test_case["excerpt"]["conversation"])
            self.assertIsInstance(response, dict, "The response should be a dictionary.")

            # Manually check for boolean match
            expected_contains_question = test_case["excerpt"]["contains_question"]
            actual_contains_question = response["contains_question"]
            if expected_contains_question == actual_contains_question:
                ChatFelixTest.correct_boolean_matches += 1
            else:
                print(f"Test case {index} failed boolean match: expected {expected_contains_question}, got {actual_contains_question}")

            # Check for question identification
            expected_question = test_case["excerpt"]["question"].lower()
            actual_question = response["detected_question"].lower()
            if expected_contains_question and expected_question in actual_question:
                ChatFelixTest.correct_question_identification += 1
            elif expected_contains_question:
                print(f"Test case {index} failed question match: expected '{expected_question}', got '{actual_question}'")

            # Record reasoning
            ChatFelixTest.reasoning_summary[f"reasoning{index}"] = response.get("reasoning", "No reasoning provided.")

            ChatFelixTest.total_excerpts += 1

    @classmethod
    def tearDownClass(cls):
        print(f"{cls.correct_boolean_matches}/{cls.total_excerpts} boolean statements and {cls.correct_question_identification}/{cls.total_excerpts} questions were identified correctly.")
        for key, value in cls.reasoning_summary.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    unittest.main()
