# Azure AI Foundry SDK Chat Application

This repository contains a Python-based generative AI chat application built with the Microsoft Foundry SDK as part of the Microsoft Learn exercise **"Develop an AI app with the Microsoft Foundry SDK"**.

The project demonstrates how to connect to an Azure AI Foundry project, interact with deployed language models, and generate AI-powered responses from a console application.

## Overview

The application:

* Connects to an Azure AI Foundry project.
* Authenticates using Azure credentials.
* Uses the Microsoft Foundry SDK.
* Sends prompts to a deployed generative AI model.
* Displays AI-generated responses in a conversational chat interface.

## Architecture

```text
User
 │
 ▼
Python Chat Application
 │
 ▼
Microsoft Foundry SDK
 │
 ▼
Azure AI Foundry Project
 │
 ▼
Deployed Language Model
```

## Prerequisites

Before running the application, ensure you have:

* An active Azure subscription.
* An Azure AI Foundry project.
* A deployed chat-capable model.
* Python 3.10 or later.
* Azure CLI installed and authenticated.

## Project Structure

```text
.
├── src/
│   └── chat_app.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-org>/<your-repo>.git
cd <your-repo>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

#### Windows

```powershell
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
PROJECT_ENDPOINT=https://<your-foundry-project>.services.ai.azure.com/api/projects/<project-name>
MODEL_DEPLOYMENT=<deployment-name>
```

Replace the values with those from your Azure AI Foundry project.

## Authentication

Login to Azure:

```bash
az login
```

The application uses Azure identity credentials provided by the Azure SDK.

## Running the Application

Start the chat application:

```bash
python src/chat_app.py
```

Example:

```text
You: What is Azure AI Foundry?

Assistant: Azure AI Foundry is a platform that enables developers to build,
deploy, and manage AI applications using a variety of foundation models and tools.
```

## Sample Code

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential()
)

response = project.inference.get_chat_completions(
    model=MODEL_DEPLOYMENT,
    messages=[
        {"role": "user", "content": "Explain Azure AI Foundry"}
    ]
)

print(response.choices[0].message.content)
```

## Learning Objectives

This project demonstrates how to:

* Use the Microsoft Foundry SDK.
* Connect to Azure AI Foundry projects.
* Authenticate with Azure services.
* Send prompts to deployed AI models.
* Build a simple conversational AI application.

## Technologies Used

* Python
* Azure AI Foundry
* Microsoft Foundry SDK
* Azure Identity
* Azure CLI

## References

* Microsoft Learn - Develop an AI app with the Microsoft Foundry SDK
* https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/03-foundry-sdk.html

## Disclaimer

This repository was created for educational purposes following Microsoft Learn training content and may require updates as Azure AI Foundry and the Microsoft Foundry SDK evolve.
