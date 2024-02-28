import os
import openai
import json


def is_equal(question1, question2):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Provide your answers to the below prompt in JSON format with the following keys: is_same_question (boolean if the questions are largely the same) reasoning (your reasoning for determining this)",
                },
                {"role": "user", "content": question1 + question2},
            ],
            temperature=0.3,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        # print("Full response object in JSON format:")
        # print(json.dumps(response, indent=4, sort_keys=True))

        # response_data = json.loads(response_json_string)

        message_content = response["choices"][0]["message"]["content"]

        # Parse the JSON string inside 'content'
        content_data = json.loads(message_content)

        # Now you can access 'is_same_question' and 'reasoning' directly
        is_same_question = content_data["is_same_question"]
        reasoning = content_data.get("reasoning", "No reasoning provided.")

        return {
            "is_same_question": is_same_question,
            "reasoning": reasoning,
        }

    except Exception as e:
        print("Error:", e)
        return {
            "is_same_question": False,
            "reasoning": "Error occurred.",
        }


if __name__ == "__main__":
    print("Please share the two questions you have, separated by a comma.")
    questions = input("You: ").split(",")
    if len(questions) >= 2:
        question1, question2 = questions[0].strip(), questions[1].strip()
        response = is_equal(question1, question2)
        # print(
        #     f"Is Same Question: {response['is_same_question']}, Reasoning: {response['reasoning']}"
        # )
    else:
        print("Error: Please provide two questions separated by a comma.")
