
import argparse
import os
from dotenv import load_dotenv
from google import genai


load_dotenv()





api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

def main():

#   parser help us to take the input from the commmand line it self
    parser = argparse.ArgumentParser(description='ChatBot')
    parser.add_argument("user_prompt", type=str, help='user prompt')
    args = parser.parse_args()


    response = client.models.generate_content(
        model='gemini-2.5-flash', contents= args.user_prompt
    )

    print(f"user prompt: {args.user_prompt}")
    print(f"prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f'response tokens: {response.usage_metadata.candidates_token_count}')

    print(f'response: \n {response.text}')

if __name__ == "__main__":
    main()
