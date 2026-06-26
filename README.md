# Azure AI Foundry Labs

This repository contains the exercises completed from the Microsoft Learn **Azure AI Foundry** learning path.

The goal of this repository is to demonstrate how to build Generative AI applications using Azure AI Foundry, the Microsoft Foundry SDK, and the Responses API, including the integration of tools such as Web Search, File Search, Code Interpreter, and custom Functions.

---

# Labs Included

## Lab 03 - Develop an AI App with the Microsoft Foundry SDK

Build a Python chat application that:

* Connects to an Azure AI Foundry project.
* Authenticates using Azure credentials.
* Uses the Microsoft Foundry SDK.
* Sends prompts to a deployed language model.
* Supports both synchronous and asynchronous chat interactions.

---

## Lab 04A - Create a Generative AI App that Uses Tools

Extend the application by integrating Azure AI Foundry tools.

Implemented tools include:

* **Code Interpreter**
* **Function Calling**
* **Web Search**
* **File Search**
* **Responses API**

These tools enable the model to execute code, search the web, retrieve information from uploaded documents, and invoke custom functions.

---

# Repository Structure

```text
.
├── chat-app/
│   ├── .env
│   ├── chat-app.py
│   ├── chat-async.py
│   └── requirements.txt
│
├── tools-app/
│   ├── brochures/
│   ├── .env
│   ├── tools-app.py
│   ├── tools-vector-creation.py
│   └── requirements.txt
│
└── README.md
```

---

# Features

## Chat Application

* Azure AI Foundry SDK
* GPT model interaction
* Synchronous chat
* Asynchronous chat
* Azure authentication using `DefaultAzureCredential`

## Tools Application

* Responses API
* Code Interpreter
* Function Calling
* Web Search
* File Search
* Vector Store creation
* Document indexing for Retrieval-Augmented Generation (RAG)

---

# Prerequisites

Before running the samples, ensure you have:

* Azure Subscription
* Azure AI Foundry Project
* A deployed GPT model
* Python 3.13+
* Azure CLI
* Visual Studio Code (recommended)

Authenticate with Azure:

```bash
az login
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/<your-org>/<repository>.git

cd <repository>
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

**Windows**

```powershell
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install dependencies for each sample:

```bash
cd chat-app
pip install -r requirements.txt
```

or

```bash
cd tools-app
pip install -r requirements.txt
```

---

# Running the Samples

## Chat Application

```bash
cd chat-app

python chat-app.py
```

or

```bash
python chat-async.py
```

---

## Tools Application

First create the vector store used by the File Search tool:

```bash
cd tools-app

python tools-vector-creation.py
```

Then run the application:

```bash
python tools-app.py
```

---

# Tool Samples

The following prompts can be used to test each implemented tool.

| Tool                 | Sample Prompt                                   |
| -------------------- | ----------------------------------------------- |
| **Code Interpreter** | `The square root of 16 is 4.`                   |
| **Function Calling** | `What time is it?`                              |
| **Web Search**       | `Give me the current weather in New York.`      |
| **File Search**      | `What hotels does Margie's Travel offer there?` |

---

# Learning Objectives

By completing these labs you will learn how to:

* Create Azure AI Foundry projects.
* Deploy foundation models.
* Use the Microsoft Foundry SDK.
* Build AI chat applications.
* Work with the Responses API.
* Integrate external tools into AI workflows.
* Create and use Vector Stores.
* Ground model responses using enterprise documents.
* Implement Retrieval-Augmented Generation (RAG) patterns.

---

# Technologies Used

* Python
* Azure AI Foundry
* Microsoft Foundry SDK
* Azure Identity
* Azure OpenAI
* GPT Models
* Responses API
* Code Interpreter
* Function Calling
* Web Search
* File Search
* Vector Stores

---

# References

* Microsoft Learn – Develop an AI App with the Microsoft Foundry SDK
* Microsoft Learn – Create a Generative AI App that Uses Tools
* Azure AI Foundry Documentation

---

# Disclaimer

This repository contains educational implementations based on Microsoft Learn labs. It is intended for learning and experimentation purposes and may require updates as Azure AI Foundry evolves.
