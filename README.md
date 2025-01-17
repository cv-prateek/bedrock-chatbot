# Bedrock Chatbot

This project is a simple AI chatbot using the AWS Bedrock service. The chatbot takes user input, sends it to an AWS Bedrock model, and returns the generated response.

## Prerequisites

- **Python 3.6+**: Make sure you have Python installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
- **AWS Account**: An AWS account with appropriate permissions to use AWS Bedrock.
- **AWS CLI**: The AWS Command Line Interface (CLI) to configure your AWS credentials. You can install it from [here](https://aws.amazon.com/cli/).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/cv-prateek/bedrock-chatbot.git
   cd bedrock-chatbot
   ```

2. **Install Dependencies:**:
   Install the required Python package boto3 using pip:
   ```bash
   pip install boto3

3. **Configure AWS Credentials**:
    Configure your AWS credentials using the AWS CLI:
    ```bash
    aws configure
    ```
    

    Alternatively, you can set your credentials as environment variables:
    ```bash
    export AWS_ACCESS_KEY_ID='your_access_key_id'
    export AWS_SECRET_ACCESS_KEY='your_secret_access_key'
    export AWS_DEFAULT_REGION='your_aws_region'
    ```

## Usage

1. **Replace the Model ID**:
   
   Open the chatbot.py file and replace 'your-model-id' with the actual model ID you want to use from AWS Bedrock.

2. **Run the Script**:
   
   Navigate to the directory where main.py is located and run the script:
    ```bash
    python main.py
    ```

3. **Interact with the Chatbot**:
    
    Once the script is running, you can interact with the chatbot by typing your messages. Type 'exit' to end the chat.


## Code Overview
    The main components of the code are:
   * Initialization: Sets up the AWS Bedrock client using Boto3.
   * Function get_response_from_bedrock: Sends the user input to the Bedrock model and returns the generated response.
   * Function chat: Manages the chat loop, taking user input and displaying the chatbot's responses.

## Example

```sh
Welcome to the AWS Bedrock Chatbot! Type 'exit' to end the chat.
You: Hello, how are you?
Chatbot: I'm an AI chatbot created using AWS Bedrock. How can I assist you today?
You: What is the weather like today?
Chatbot: I'm not sure about the current weather. Please check a weather service for the latest information.
You: exit
Goodbye!
```