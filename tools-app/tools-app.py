import os
import time
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# Function to get the current time
def get_time():
    return f"The time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"


def main(): 
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Get configuration settings 
        load_dotenv()
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")
        vector_id = os.getenv("VECTOR_STORE_ID") #complete with your vector store id generated runing the tools-vector-creation.py file.

        # Initialize the OpenAI client
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(), "https://ai.azure.com/.default"
        )
            
        openai_client = OpenAI(
            base_url=azure_openai_endpoint,
            api_key=token_provider
        )        

        # Track conversation state
        last_response_id = None
               
        # Loop until the user wants to quit
        while True:
            input_text = input('\nEnter a question (or type "quit" to exit): ')
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a question.")
                continue

            # Get a response using tools
            response = openai_client.responses.create(
                model=model_deployment,
                instructions="""
                You are a travel assistant that provides information on travel services available from Margie's Travel.
                Answer questions about services offered by Margie's Travel using the provided travel brochures.
                Search the web for general information about destinations or current travel advice.
                """,
                input=input_text,
                previous_response_id=last_response_id,
                include=["file_search_call.results"], # include additional information in the response object related to the files
                tools=[
                    {
                        "type": "file_search",
                        "vector_store_ids": [vector_id]
                    },
                    {
                        "type": "web_search"
                    },
                    {   
                        "type": "code_interpreter",
                        "container": {"type": "auto"}
                    },
                    {
                        "type": "function",
                        "name": "get_time",
                        "description": "Get the current time"
                    }
                ]
            )
            
            last_response_id = response.id

            print(f"\n🧠 Model output: {response.output_text}")
            print(f"\n🧠 Model output text: {response.output}")

            for item in response.output:                
                if "_call" in item.type:
                        print(f"\n🧠 Tools used: {item.type}")                

                if item.type.endswith("_call"):
                    print(f"\n🔧 Tool executed: {item.type}")

                    if item.type == "file_search_call":
                        for r in getattr(item, "results", []):
                            print(f" - {r.filename} ({r.score})")
                    elif item.type == "web_search_call":
                        print(" - Web search executed")
                    elif item.type == "code_interpreter_call":
                        print(" - Code interpreter executed")
                    elif item.type == "function_call":
                        print(" - Function executed")

            # Was there a function call?
            for item in response.output:
                if item.type == "function_call" and item.name == "get_time":
                    current_time = get_time()                    

                    # Get a follow up response using the tool output
                    response = openai_client.responses.create(
                        model=model_deployment,
                        instructions="Answer only with the tool output.",
                        input=[{
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": current_time
                        }],
                        previous_response_id=last_response_id
                    )

            print(f"\nFinal response: {response.output_text}")
            last_response_id = response.id            

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()
