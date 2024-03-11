class ChatFelixTest(unittest.TestCase):
    def test_analyze_excerpt(self):
        # Your test setup...
        for case in test_cases:
            response = analyze_excerpt(case["excerpt"]["conversation"])
            self.assertIsInstance(response, dict, "The response should be a dictionary.")
            
            # Example of checking the structured response
            expected_contains_question = case["excerpt"]["contains_question"]
            actual_contains_question = response["question_detected"] == "yes"
            self.assertEqual(expected_contains_question, actual_contains_question, f"Expected question detection to be {expected_contains_question}, but got {actual_contains_question}. Reasoning: {response.get('reasoning')}")
            
            if expected_contains_question:
                expected_question = case["excerpt"]["question"].lower()
                # Assuming your response includes the detected question or reasoning
                # This is where you'd check if the expected question is in the reasoning or the detected question
                self.assertIn(expected_question, response.get("reasoning", "").lower(), "Expected question not found in response reasoning.")
