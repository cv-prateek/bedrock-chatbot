import boto3
import json

# Initialize the Bedrock client
client = boto3.client('bedrock')

def get_response_from_bedrock(input_text):
    try:
        # Define the payload with the input text
        payload = {
            "inputText": input_text,
            "model": "text-davinci-002",  # Example model name
            "parameters": {
                "maxTokens": 150,
                "temperature": 0.7
            }
        }
        
        # Call the Bedrock service to get the response
        response = client.invoke_model(
            ModelId='your-model-id',  # Replace with your model ID
            ContentType='application/json',
            Body=json.dumps(payload)
        )
        
        # Parse the response
        response_body = json.loads(response['Body'].read())
        return response_body['outputText']
    
    except Exception as e:
        print(f"Error getting response from Bedrock: {e}")
        return None

def chat():
    print("Welcome to the AWS Bedrock Chatbot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = get_response_from_bedrock(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: Sorry, I couldn't process your request.")

if __name__ == "__main__":
    chat()
