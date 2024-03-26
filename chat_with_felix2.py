import os
import openai
import json


def analyze_excerpt(excerpt, testing=False):
    if not excerpt:
        return {"interview_question": ""}

    print("Excerpt here:  " + excerpt)
    # Assuming you have set OPENAI_API_KEY in your environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
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
                     User: "Tell me about a time you had to pivot your product strategy. What led to the pivot?"
                     Assistant: This is an important interview question focusing on the candidate's adaptability and decision-making process.
                     
                    Example 2:
                    User: "Tell me about a time when you had to advocate for additional resources for your project. How do you justify the need and what was the outcome?"
                    Assistant: This is an important interview question as it explores the candidate's negotiation skills and ability to secure resources.
                    
                    Example 3:
                    User: "What projects have you worked on that you're particularly proud of?"
                    Assistant: This is an important interview question focusing on the candidate's past work.

                    Example 3:
                    User: "You're familiar with Python, right?"
                    Assistant: This is a clarification question and should be ignored.

                    Example 4:
                    User: "How are you doing today?"
                    Assistant: This is small talk and should be disregarded.

                    Example 5:
                    User: "Why don't you start with a brief intro?"
                    Assistant: This is an essential interview question

                    Based on this guidance, analyze the following conversation excerpt for important interview questions: \"{excerpt}\"
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
        # Extract response directly without unnecessary replacements
        response_text = (
            response.choices[0].get("message", {}).get("content", "").strip()
            or response.choices[0].get("text", "").strip()
        )
        response_data = json.loads(response_text)

        # Directly return the analysis results
        return {
            "interview_question": response_data.get("interview_question", "")
            # "reasoning": response_data.get("reasoning", "No reasoning provided."),
        }

    except Exception as e:
        # Simplified error handling
        return {"interview_question": "", "reasoning": f"Error occurred: {str(e)}"}


if __name__ == "__main__":
    user_message = input("Please share the excerpt you would like me to analyze: ")
    analysis_result = analyze_excerpt(user_message)
    print(analysis_result)
