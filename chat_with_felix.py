import os
import openai
import json


def analyze_excerpt(excerpt, testing=False):
    print("wtf")
    if excerpt == "":
        return {
            # "has_interview_question": False,
            "interview_question": "",
            # "reasoning": "The excerpt is empty",
        }

    print("                        ")
    print("THIS IS AN EXCERPT" + excerpt)
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
        "Describe a time when you had to advocate for user needs that were not initially recognized by your team.",
    ]
    # Assuming you have set OPENAI_API_KEY in your environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "system",
                    "content": "Provide your answers to the below prompt in JSON format with the following keys: has_interview_question, interview_question, reasoning",
                },
                {
                    "role": "system",
                    "content": "You wll not make questions up unless there is direct evidence of the question from the excerpt",
                },
                {
                    "role": "system",
                    "content": 'If you get a blank excerpt, then you will respond with an empty JSON, i.e "has_interview_question:" false, "interview_question": "", "reasoning": ""',
                },
                {
                    "role": "system",
                    "content": f"""
                    You are an intelligent assistant analyzing interview transcripts. Your task is to extract important interview questions, ignoring any clarification questions such as 'right?' or small talk like 'how are you doing today?' AND explain your reasoning. Focus on identifying substantial questions that contribute to understanding the interviewee's experience and qualifications. Here are examples for guidance:

                    Example 1:
                    User: "What projects have you worked on that you're particularly proud of?"
                    Assistant: This is an important interview question focusing on the candidate's past work.

                    Example 2:
                    User: "You're familiar with Python, right?"
                    Assistant: This is a clarification question and should be ignored.

                    Example 3:
                    User: "How are you doing today?"
                    Assistant: This is small talk and should be disregarded.

                    Example 3:
                    User: "Why don't you start with a brief intro?"
                    Assistant: This is an essential interview question

                    Based on this guidance, analyze the following conversation excerpt for important interview questions: \"{excerpt}\"
                    """,
                },
                {
                    "role": "system",
                    "content": """
    You are an intelligent assistant analyzing interview transcripts. Your task is to extract important interview questions, ignoring any clarification questions such as 'right?' or small talk like 'how are you doing today?' AND explain your reasoning. Focus on identifying substantial questions that contribute to understanding the interviewee's experience and qualifications. Here are examples for guidance:

    Example 1:
    User: "Tell me about a time you had to pivot your product strategy. What led to the pivot?"
    Assistant: This is an important interview question focusing on the candidate's adaptability and decision-making process.

    Example 2:
    User: "?"
    Assistant: This is a clarification question and should be ignored because it does not provide enough context to be considered a substantial interview question.

    Example 3:
    User: "a time when you had to advocate for additional resources for your project. How do you justify the need and what was the outcome?"
    Assistant: This is an important interview question as it explores the candidate's negotiation skills and ability to secure resources.

    Negative Example 1:
    User: "a product vision?"
    Assistant: This excerpt is too brief and lacks context, making it difficult to be considered a substantial interview question. It might be part of a larger question but on its own, it doesn't provide enough information to be an important interview question.

    Negative Example 2:
    User: "well with others. How did you address it?"
    Assistant: While this follows an important question, taken out of context, it appears as a fragment and does not stand alone as a substantial interview question without the preceding context.

    Based on this guidance, analyze the following conversation excerpt for important interview questions: "{excerpt}"
    """,
                },
                {
                    "role": "system",
                    "content": "You always provide your reasoning for determining the interview question (if applicable) by starting the explanation with 'Reasoning'",
                },
            ],
            temperature=0.7,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        # Extract the full response text correctly

        # print("Raw OpenAI API response:", response)
        if "message" in response.choices[0]:
            # Extract the 'content' and clean it by removing the triple backticks and 'json' label
            response_text = response.choices[0].message["content"]
            # Remove the triple backticks and the word 'json'
            response_text = (
                response_text.replace("```json\n", "").replace("\n```", "").strip()
            )
        else:
            # If the 'message' field is not there, fall back to 'text'
            response_text = response.choices[0].get("text", "").strip()

        response_data = json.loads(response_text)
        print("Raw response:", response_text)

        has_interview_question = response_data.get("has_interview_question", False)
        interview_question = response_data.get("interview_question", "")
        reasoning = response_data.get("reasoning", "No reasoning provided.")

        if testing == True:
            print(
                f"Contains Question: {response['has_interview_question']}, Detected Question: '{response['interview_question']}', Reasoning: '{response['reasoning']}'"
            )
            return {
                "has_interview_question": has_interview_question,
                "interview_question": interview_question,
                "reasoning": reasoning,
            }
        else:
            # print("else entered")
            print(f"Detected Question: '{interview_question}'")
            return {"interview_question": interview_question}

    except Exception as e:
        print("Error:", str(e))
        return {
            "contains_question": False,
            "detected_question": "",
            "reasoning": "ErrorS occurred.",
        }


if __name__ == "__main__":
    print(
        "Felix: Hi there. I am Felix, the chatbot. Please share the excerpt you would like me to analyze"
    )
    user_message = input("You: ")
    response = analyze_excerpt(user_message)
