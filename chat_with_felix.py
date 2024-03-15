import os
import openai
import json


def analyze_excerpt(excerpt):
    try:
        # Assuming this is a placeholder for your actual analysis logic
        # Directly return the analysis results
        return {"interview_question": excerpt + " added"}
    except Exception as e:
        # Simplified error handling
        return {"interview_question": "", "reasoning": f"Error occurred: {str(e)}"}


if __name__ == "__main__":
    user_message = input("Please share the excerpt you would like me to analyze: ")
    analysis_result = analyze_excerpt(user_message)
    print(analysis_result)