# import os
# import openai
# import json


# def analyze_excerpt(excerpt):
#     if excerpt == "":
#         return {"interview_question": ""}

#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     print(excerpt + "this is excerpt")

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4-0125-preview",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": "Provide your answers to the below prompt in JSON format with the following keys: has_interview_question, interview_question, reasoning",
#                 },
#                 {
#                     "role": "system",
#                     "content": "You wll not make questions up unless there is direct evidence of the question from the excerpt",
#                 },
#                 {
#                     "role": "system",
#                     "content": f"""
#                     You are an intelligent assistant analyzing interview transcripts. Your task is to extract important interview questions, ignoring any clarification questions such as 'right?' or small talk like 'how are you doing today?' AND explain your reasoning. Focus on identifying substantial questions that contribute to understanding the interviewee's experience and qualifications. Here are examples for guidance:

#                     Example 1:
#                     User: "What projects have you worked on that you're particularly proud of?"
#                     Assistant: This is an important interview question focusing on the candidate's past work.

#                     Example 2:
#                     User: "You're familiar with Python, right?"
#                     Assistant: This is a clarification question and should be ignored.

#                     Example 3:
#                     User: "How are you doing today?"
#                     Assistant: This is small talk and should be disregarded.

#                     Example 3:
#                     User: "Why don't you start with a brief intro?"
#                     Assistant: This is an essential interview question

#                     Based on this guidance, analyze the following conversation excerpt for important interview questions: \"{excerpt}\"
#                     """,
#                 },
#             ],
#             temperature=0.7,
#             max_tokens=512,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0,
#         )

#         print("response generated")

#         response_text = (
#             response.choices[0].message["content"]
#             if "message" in response.choices[0]
#             else response.choices[0].get("text", "").strip()
#         )
#         response_text = (
#             response_text.replace("```json\n", "").replace("\n```", "").strip()
#         )  # Clean the response text
#         response_data = json.loads(response_text)
#         print(response_data + "response data")

#         interview_question = response_data.get("interview_question", "")
#         print(f"Detected Question: '{interview_question}'")
#         return {"interview_question": interview_question}

#     except Exception as e:
#         print("Error:", str(e))
#         return {"interview_question": "", "reasoning": "Error occurred."}


# if __name__ == "__main__":
#     user_message = input("Please share the excerpt you would like me to analyze: ")
#     response = analyze_excerpt(user_message)

# lfg = ""
