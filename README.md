# **LLM Telegram Bot**

**Automatically Create and Deploy Large Language Model (LLM) Telegram Bots with RAG Architecture**

## **Table of Contents**

1. [**Overview**](#overview)
2. [**Key Features**](#key-features)
3. [**Getting Started**](#getting-started)
   1. [**Prerequisites**](#prerequisites)
   2. [**Setup & Deployment**](#setup--deployment)
4. [**How It Works**](#how-it-works)
5. [**Configuring Your LLM Bot**](#configuring-your-llm-bot)
   1. [**Entering Context**](#entering-context)
   2. [**Adding External Resources**](#adding-external-resources)
   3. [**Creating a RAG LLM Bot**](#creating-a-rag-llm-bot)
6. [**Adding Bot to Telegram**](#adding-bot-to-telegram)


## **Overview**
------------

**AutoDeploy LLM Telegram Bot** is an innovative project designed to simplify the creation and deployment of Large Language Model (LLM) Telegram bots, specifically utilizing the Retrieval-Augmented Generator (RAG) architecture. With this tool, users can effortlessly input context, integrate external resources, and automatically generate and deploy a functional LLM Telegram bot, ready to be added to their Telegram account.

## **Key Features**
-----------------

- **Automatic Deployment**: Seamless creation and deployment of LLM Telegram bots.
- **RAG Architecture Support**: Leverages the powerful Retrieval-Augmented Generator model for enhanced conversational capabilities.
- **Customizable Context**: Input your specific context to tailor the bot's understanding and responses.
- **External Resource Integration**: Enhance the bot's knowledge base with external resources.
- **User-Friendly Interface**: Designed for ease of use, from setup to deployment.

## **Getting Started**
---------------------

### **Prerequisites**
- **Telegram API Bot Token**: Obtain a bot token from the [BotFather](https://t.me/BotFather).
- **Basic Understanding of LLMs and Telegram Bots**: Helpful but not required.

### **Setup & Deployment**
1. Clone this repository: `git clone https://github.com/sinanazem/AutoDeploy-LLM-Telegram-Bot.git`
2. Navigate to the project directory: `cd AutoDeploy-LLM-Telegram-Bot`
3. Install dependencies: `pip install -r requirements.txt`
4. Configure your `config.json` with your Telegram API Bot Token.
5. Run the deployment script: `python deploy_bot.py`

## **How It Works**
------------------

1. **User Input**: Context and external resources are collected through a user interface.
2. **LLM Model Generation**: The system automatically generates a RAG LLM model based on the input.
3. **Telegram Bot Creation**: A Telegram bot is created using the generated LLM model.
4. **Deployment**: The bot is deployed and ready for use.

## **Configuring Your LLM Bot**
------------------------------

### **Entering Context**
- Open `context.json`
- Input your desired context in the formatted fields
- Save changes

### **Adding External Resources**
- Open `resources.json`
- Add URLs or paths to your external resources
- Save changes

### **Creating a RAG LLM Bot**
- Run `python generate_llm_bot.py`
- The system will automatically create and configure your RAG LLM bot

## **Adding Bot to Telegram**
1. Open Telegram and search for `@BotFather`.
2. Follow the in-app instructions to add your newly deployed bot.
