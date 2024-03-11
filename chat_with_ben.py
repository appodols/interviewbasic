import os
import openai
import json

def analyze_excerpt(excerpt, testing=False):
    # Assuming you have set OPENAI_API_KEY in your environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                    You are an intelligent assistant analyzing interview transcripts..
                    """,
                },
            ],
            temperature=0.7,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        # Extract the full response text correctly
        response_text = (
            response.choices[0].message["content"]
            if "message" in response.choices[0]
            else response.choices[0].get("text", "").strip()
        )

        response_data = json.loads(response_text)
        # print("Raw response:", response_text)

        has_interview_question = response_data.get("has_interview_question", False)
        interview_question = response_data.get("interview_question", "")
        reasoning = response_data.get("reasoning", "No reasoning provided.")
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
            "reasoning": "Error occurred.",
        }


if __name__ == "__main__":
    print(
        "Felix: Hi there. I am Felix, the chatbot. Please share the excerpt you would like me to analyze"
    )
    user_message = input("You: ")
    response = analyze_excerpt(user_message)
#     if testing:
#         print(
#             f"Contains Question: {response['has_interview_question']}, Detected Question: '{response['interview_question']}', Reasoning: '{response['reasoning']}'"
#         )
# else:
#     # Corrected the syntax here
#     print(f"Detected Question: '{response['interview_question']}'")
