import os
import openai

def analyze_excerpt(excerpt):
    common_questions = [
        "Tell me about a time when you had to prioritize certain product features over others. How did you make your decision?",
        "Describe a situation where you had to work with a difficult stakeholder. How did you handle it?",
        "Give an example of a successful product launch you managed. What was your strategy?",
        "Tell me about a time when you used data to make a product decision. What was the outcome?",
        "Explain a scenario where you had to pivot your product strategy. What led to that decision?",
        "Describe how you work with engineering teams to meet product deadlines.",
        "Tell me about a product failure you experienced. What did you learn from it?",
        "How do you gather user feedback, and how does it influence your product decisions?",
        "Give an example of how you've handled competing priorities across different projects.",
        "Describe a time when you had to advocate for user needs that were not initially recognized by your team."
    ]
    
    # Assuming you have set OPENAI_API_KEY in your environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a smart and helpful assistant trained to identify behavioral interview questions from a conversation, specifically for product managers. After identifying a question, please return a JSON object containing a boolean indicating whether a question is present, the identified question if applicable, and your reasoning. Use these examples of common behavioral interview questions for product managers to guide your detection: [List of examples]."
                },
                {
                    "role": "user",
                    "content": excerpt
                }
            ],
            temperature=0.7,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        # Extract the full response text correctly
        response_text = response.choices[0].message['content'] if 'message' in response.choices[0] else response.choices[0].get('text', '').strip()
        # print("Response Text: " + response_text) 
        # Assuming the response structure includes reasoning as part of the response text
        split_response = response_text.split("Reasoning: ")
        question_detection = "Yes" if "contains a question" in response_text else "No"
        reasoning = split_response[1].strip() if len(split_response) > 1 else "No reasoning provided."
        
        likely_contains_question = "Yes" in question_detection
        detected_question = ""  # You would need to refine how to extract the specific question
        
        # Return a dictionary including the reasoning
        return {"contains_question": likely_contains_question, "detected_question": detected_question, "reasoning": reasoning}
    
    except Exception as e:
        print("Error:", str(e))
        return {"contains_question": False, "detected_question": "", "reasoning": "Error occurred."}

if __name__ == "__main__":
    print("Felix: Hi there. I am Felix, the chatbot. Please share the excerpt you would like me to analyze")
    user_message = input("You: ")
    response = analyze_excerpt(user_message)
    print(f"Contains Question: {response['contains_question']}, Detected Question: '{response['detected_question']}', Reasoning: '{response['reasoning']}'")

