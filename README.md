# Visual Understanding Agentic Chat Assistant 🎬
This project is a Streamlit-based web application that serves as a visual understanding agent. It processes video input, generates a detailed summary of its contents, and allows users to have multi-turn conversations about the video in real-time. The application showcases a powerful agentic workflow .This project implements an agentic chat assistant capable of processing video input, generating a detailed summary of its contents, and then engaging in multi-turn conversations with a user about the video. The solution is built as a web application using Streamlit, providing a user-friendly interface for video uploads and chat interactions. It leverages two powerful large language models: Google's Gemini 1.5 Flash for video analysis and Llama 3.3 70B via Groq Cloud for real-time conversational responses.

## Working Demo

[Demo 1](https://drive.google.com/file/d/1wgI3pnRGNpMZ1WtNG9B9f3blor4vmlkE/view?usp=sharing)

[Demo 2](https://drive.google.com/file/d/1VBB9Z4m-vMptZkoe627TYOOYOyhhrVXs/view?usp=sharing)

## ✨ Features
In-Depth Video Analysis: Utilizes Google's Gemini 1.5 Flash to analyze videos up to 2 minutes long. It generates a comprehensive, time-stamped report on key events, object tracking, and potential violations.

Real-time Conversational AI: Employs Llama 3.1 70B through the low-latency Groq Cloud API to enable fast and context-aware chat interactions with the video summary.

Modular Codebase: The project is structured into separate modules for agents, UI components, and the main application logic, making the code clean, readable, and easy to maintain.

Persistent & Downloadable Summary: The generated video summary remains visible during the entire chat session and can be downloaded as a text file for offline use.

Intuitive UI: A user-friendly interface built with Streamlit allows for simple video uploads and seamless chat interactions.

🏛️ Project Structure
The project is organized into a modular and scalable directory structure.

```
project_directory/
├── .streamlit/
|   |
│   └── secrets.toml
|
├── uploaded_videos/
|
├── src/
|   |
│   ├── agents/
|   |   |
│   │   ├── video_summarizer_agent.py
|   |   | 
│   │   └── chat_agent.py
|   |  
│   └── ui/
|       |
│       └── components.py
|  
├── app.py
|
└── README.md

```

## File Breakdown:
.streamlit/secrets.toml: Securely stores your API keys.

uploaded_videos/: The directory where your uploaded video files are saved.

src/agents/: Contains the logic for the different AI agents.

video_summarizer_agent.py: Handles the video upload and summarization using the Gemini API.

chat_agent.py: Manages the conversational agent and Groq API calls.

src/ui/: Contains reusable Streamlit UI components.

components.py: Holds functions for displaying chat history and handling user input logic.

app.py: The main entry point of the application. It orchestrates the flow by importing functions from the src directory and setting up the Streamlit UI.

README.md: This documentation file.

## 🚀 End-to-End Execution Guide

## 1. Prerequisites
Before you begin, ensure you have the following:

Python 3.8+ installed.

A Gemini API Key.

A Groq API Key.

### 2. Installation and Setup
Follow these steps to set up the project locally.

Step a. Clone the repository
First, clone the project from your repository.

Bash

```
git clone git@github.com:ratnesh134/Video-Summarization-ChatBot.git
cd your-repo
```
Step b. Create a virtual environment
It's highly recommended to use a virtual environment to manage dependencies.

Bash

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Step c. Install dependencies
Install all required Python libraries.

Bash

```
pip install -r requirements.txt
```

Step d. Configure API keys
Create a directory named .streamlit and a file inside it named secrets.toml.


```
your_project_directory/
├── .streamlit/
│   └── secrets.toml
```
Open secrets.toml and add your API keys. Replace "your_gemini_api_key" and "your_groq_api_key" with your actual keys.

Ini, TOML

 .streamlit/secrets.toml

```
GEMINI_API_KEY = "your_gemini_api_key"
GROQ_API_KEY = "your_groq_api_key"
```

## 3. Run the Application
With the setup complete, you can now run the Streamlit application from your project's root directory.

Bash

```
streamlit run app.py
```

This command will launch the application in your web browser.

### 4. Usage
Upload a Video: Use the file uploader widget to select an MP4 or MOV file.

Wait for Analysis: The app will automatically save the video and send it to the Gemini API. A spinner will indicate that the summary is being generated.

View Summary & Chat: Once the analysis is complete, the video summary will be displayed, along with a "Download Summary" button. You can now use the chat box to ask questions about the video's content. The assistant will remember your conversation, allowing for multi-turn dialogue.

Enjoy using your Visual Understanding Agent!

## Collaborators

[Aditya Londhe](adityalondhe052@gmail.com)

[Nitesh Pratap Singh](niteshen1010@gmail.com)

[Ratnesh Kumar](ratnesh134@gmail.com)

