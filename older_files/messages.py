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