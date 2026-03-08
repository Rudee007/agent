import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompt import system_prompt
from call_function import available_functions, call_function

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():

    parser = argparse.ArgumentParser(description='ChatBot')
    parser.add_argument("user_prompt", type=str, help='user prompt')
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    for _ in range(20):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0,
                tools=[available_functions]
            )
        )

        # Add model responses to conversation
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        # If no tool call → final answer
        if not response.function_calls:
            print("\nFinal response:\n")
            print(response.text)
            return

        function_responses = []

        # Execute each tool
        for function_call in response.function_calls:

            function_call_result = call_function(function_call, args.verbose)

            if not function_call_result.parts:
                raise Exception("No parts returned from function call")

            part = function_call_result.parts[0]

            if not part.function_response:
                raise Exception("No function response returned")

            if part.function_response.response is None:
                raise Exception("Function response is empty")

            function_responses.append(part)

        # Send tool results back to model
        messages.append(
            types.Content(role="user", parts=function_responses)
        )

    print("Agent stopped after 20 iterations without finishing.")
    exit(1)


if __name__ == "__main__":
    main()