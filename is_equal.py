import os
import openai
import json


def is_equal(question1, question2):
    # Assuming you have set OPENAI_API_KEY in your environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Please return a boolean that describes whether the 2 questions are asking the same general concept",
                },
                {
                    "role": "system",
                    "content": f"""
                    You are an intelligent assistant analyzing whether two questions are essential synomyns of each other"

                    Example 1:
                    Question 1: "Why don't you start with a brief intro"
                    Question 2: "Can you provide me a brief intro?"
                    Assistant: True. These questions are both asking about an intro.
                    
                    Example 2:
                    Question 1: "What is your ideal situation in terms of in your next career?
                    Question 2: "What do you expect in your next career?"
                    Assistant: True. Both of these questions ask about what the candidate wants / expects in their next career.
                    
                    Example 3:
                    Question 1: "What is the reason that you're looking for a full time job?"
                    Question 2: "What is your favorite aspect of a full-time job"
                    Assistant: False. These questions ask different things.  The first asks for the reason a candidate wants a job; the second asks about favorite aspect of a job.
        
                    Based on this guidance, analyze the following conversation excerpt for important interview questions: {question1} and  {question2}
                    """,
                },
                {
                    "role": "system",
                    "content": "You always provide your reasoning for determining the intervieq question (if applicable) by starting the explanation with 'Reasoning'",
                    # note, we will turn this off, this is just for the reasoning
                },
            ],
            temperature=0.3,
            # note, maybe this temp is too low?
            max_tokens=512,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        response_text = response.choices[0].get("text", "").strip()
        print("Response Text: " + response_text)

        is_same_question = response_text.lower() == "true"
        print("Is Same Question: ", is_same_question)

        return {
            "is_same_question": is_same_question,
        }

    except Exception as e:
        print("Error:", str(e))
        return {"is_same_question": False}


# if __name__ == "__main__":
#     # print(
#     #     "Felix: Hi there. I am Felix, the chatbot. Please share the excerpt you would like me to analyze"
#     # )
#     # user_message = input("You: ")
