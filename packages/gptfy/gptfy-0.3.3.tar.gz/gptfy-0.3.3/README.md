# gptfy

## Overview
The `gptfy` library provides an interface for seamless interaction with various models of OpenAI's GPT, facilitating the management of conversation sessions and processing of instructions. Commonly used to establish continuous two–way API between Open AI GPT models and your application.

---

## Installation
To install `gptfy`, use the following pip command:

```sh
pip install gptfy
```

---

## Conversation Class

### Overview
The `Conversation` class is the central manager for initiating and managing interactions between a client and a model. It is responsible for the dynamic loading of model and client classes, as well as handling the conversation flow.

### Initialization
To initialize a `Conversation` instance, provide the following parameters:

- `api_key` (str): The API key for authentication with OpenAI's services.
- `model` (dict): The definition of the model you wish to use.
- `client` (gptfy.client.Client): The instance of the `Client` class for the conversation.
- `instructions` (list[str]): Initial system instructions.

### Methods
- `start()`: Begins the conversation with the model and client.
- `prompt(prompt)`: Sends a prompt to the model and returns its response.

---

## Usage

Certainly, Alexander. Here is an example of how a user might utilize the `Conversation` class to start a conversation, along with explanations on usage:

```markdown
# Starting a Conversation with `Conversation` Class

## Usage Example

The following is a simple example of how to use the `Conversation` class from the `gptfy` library to start a conversation session with a model and a client:

```python
from gptfy.conversation import Conversation

# Replace 'your_api_key_here' with your actual OpenAI API key.
api_key = 'your_api_key_here'

# The model and client names are assumed to be defined in your settings or passed as strings.
model_name = 'gpt-3.5-turbo'  # Example model name
client_name = 'your-client-class'  # Example client name (Extends Client)

# Creating a Conversation instance
conversation = Conversation(api_key, model_name, client_name)

# Starting the conversation
conversation.start()
```

## Explanation

1. **Import the Conversation Class**: The `Conversation` class is imported from the `gptfy` library.
2. **API Key**: Your unique API key for OpenAI's API is required to authenticate requests.
3. **Model and Client Names**: Specify the model and client you wish to use. These should correspond to the models and clients you have set up in your library.
4. **Create an Instance**: Instantiate the `Conversation` class with the required parameters.
5. **Start the Conversation**: Call the `start()` method to begin the interaction with the model and client. This will involve the model and client classes you have defined, loading instructions, and managing the conversation flow.

This process will initialize the conversation with the appropriate model and client based on your provided details, allowing you to begin sending prompts and receiving responses.

Remember to replace `'your_api_key_here'`, `'gpt-3.5-turbo'`, and `'default_client'` with your actual API key and the specific model and client names you have set up in your `gptfy` library.

---

## Model Class

### Overview
`Model` serves as a base class for different model implementations. It handles the interaction with OpenAI's API, tracking usage, and updating conversation states.

### Initialization
To create an instance of `Model`, the following parameters are required:

- `model` (dict): A defined in module dictionary containing model details such as model name, prices, and token limits.
- `conversation` (Conversation): A reference to the associated `Conversation` instance.
- `api_key` (str): The API key for OpenAI's services.
- `temperature` (float): Optional. The temperature setting for the model's responses.

### Methods
- `name`: The name property of the model.
- `get_usage()`: Retrieves the current usage statistics, including costs.
- `unwind()`: Removes the last message from the conversation if it is not from the system.
- `start(instructions)`: Starts the model with the provided instructions.
- `prompt(content, role)`: Sends a prompt to the model and processes the response.


---

## Client Class

### Overview
The `Client` class is a foundational class designed for client-specific operations, including loading instructions and managing client-side interaction.

### Initialization
To initialize a `Client`, you need create class, that exends a `Client` and implements its methods.

### Methods
- `start()`: Starts client-specific operations. [Implementation details required]
- `prompt(content)`: Handles the prompt received from the conversation. [Implementation details required]

---

## Settings and Error Handling

The library includes settings management and custom error handling through `settings` and `peer_error` modules, ensuring proper configuration and graceful error reporting.

---

## Models

The library supports various models with different capabilities and pricing, such as `GPT_35_TURBO`, `GPT_35_TURBO_INSTRUCT`, `GPT_40`, `GPT_40_TURBO`, `GPT_40_TURBO_VISION`, and `GPT_40_32K`.

---
