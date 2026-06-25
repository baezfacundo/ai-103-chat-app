import os
import subprocess
from dotenv import load_dotenv

# import namespaces
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


def main(): 
    # Clear the console
    # system is deprecated in Python 3.5 and later, so we use subprocess.run instead
    # os.system('cls' if os.name == 'nt' else 'clear')
    subprocess.run(["cls" if os.name == 'nt' else "clear"], shell=True)

    try:
        # Get configuration settings 
        load_dotenv()
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")

        # Initialize the OpenAI client
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(), "https://ai.azure.com/.default"
        )
            
        openai_client = OpenAI(
            base_url=azure_openai_endpoint,
            api_key=token_provider
        )

        # Initialize the last_response_id variable to None for Response API
        last_response_id = None

        # Loop until the user wants to quit
        while True:
            input_type = input('\nSelect ChatCompletions API (chat-completions) or Response API with stream or without (response-with-stream / response-without-stream): ')
            if input_type.lower() == "quit":
                break
            if input_type.lower() not in ("chat-completions", "response-with-stream", "response-without-stream"):
                print("Please enter a valid option (chat-completions, response-with-stream, or response-without-stream).")
                continue
            
            input_text = input('\nEnter a prompt (or type "quit" to exit): ')
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            if input_type.lower() == "chat-completions":
                # Get a response from ChatCompletions API 
                completion = openai_client.chat.completions.create(
                    model=model_deployment,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful AI assistant that answers questions and provides information."
                        },
                        {
                            "role": "user",
                            "content": input_text
                        }
                    ]
                )
                print(completion.choices[0].message.content)
                print("**Response from ChatCompletions API**")
            else:
                streamEnabled = False
                if input_type.lower() == "response-with-stream":
                    streamEnabled = True

                # Get a response from Response API                
                response = openai_client.responses.create(
                            model=model_deployment,
                            instructions="You are a helpful AI assistant that answers questions and provides information.",
                            input=input_text,
                            previous_response_id=last_response_id,
                            stream=streamEnabled
                )                

                if streamEnabled:
                    for event in response:
                        if event.type == "response.output_text.delta":
                            print(event.delta, end="")
                        elif event.type == "response.completed":
                            last_response_id = event.response.id                   
                    print("\n**Response from Response API with stream**")
                else:
                    print(response.output_text)
                    last_response_id = response.id                                    
                    print("\n**Response from Response API without stream**")                

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()
