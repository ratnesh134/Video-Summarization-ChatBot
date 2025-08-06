# Visual Understanding Agentic Chat Assistant
## 📄 Project Overview

This project implements an agentic chat assistant capable of processing video input, generating a detailed summary of its contents, and then engaging in multi-turn conversations with a user about the video. The solution is built as a web application using Streamlit, providing a user-friendly interface for video uploads and chat interactions. It leverages two powerful large language models: Google's Gemini 1.5 Flash for video analysis and Llama 3.3 70B via Groq Cloud for real-time conversational responses.

<br>

## Working Demo 

[Demo](https://drive.google.com/file/d/1yBA1TDtyY8yzZOr75JsoqSrWdKRE4yDT/view?usp=sharing)


<br>

## ✨ Core Features

Video Event Recognition & In-Depth Summarization: The system processes a user-uploaded video (up to 2 minutes long) and generates a comprehensive report. This report includes a detailed log of all objects, persons, and events, along with their timestamps. It also identifies potential guideline violations and provides a narrative summary.

Multi-Turn Conversations: The assistant retains context from the generated video summary and the ongoing chat history, allowing users to ask natural, follow-up questions about the video's content.

Agentic Workflow: The system employs a clear two-agent workflow: a Gemini Video Agent for initial processing and a Groq Conversational Agent for user interaction.

Intuitive UI: A Streamlit frontend makes it simple for users to upload a video, view the generated summary, and chat with the assistant in a single interface.

<br>

## 🏛️ Architecture

The system follows a decoupled, two-stage architecture:

Video Processing Stage: A user uploads a video via the Streamlit front-end. The application saves the video temporarily and sends it to the Gemini 1.5 Flash API. This model, acting as the Video Agent, analyzes the video based on a detailed prompt and returns a comprehensive summary. This summary is then stored in the Streamlit session_state.

Conversational Stage: Once the summary is ready, the user can ask questions. The Groq Conversational Agent is activated, taking the video summary and the chat history as its context. It uses the Llama 3.3 70B model via the low-latency Groq Cloud API to generate fast, accurate responses to the user's queries.

<br>

## 💻 Tech Stack Justification

Streamlit: Chosen for its ability to quickly build interactive and beautiful data applications in pure Python. It provides an excellent front-end for a prototype, requiring minimal effort to create a polished user experience.

Gemini 1.5 Flash: A powerful multimodal model with a long context window, making it ideal for processing video files and generating detailed, time-stamped summaries and event logs.

Groq Cloud (with Llama 3.3 70B): Selected for its exceptional inference speed and low latency. This ensures that the conversational part of the application feels instantaneous, providing a highly responsive and satisfying chat experience. Using Groq avoids the need to download and run a large model locally, simplifying deployment and enhancing performance.

<br>

## 🛠️ Setup and Installation

Follow these steps to get the project running on your local machine.

1. Clone the repository:

Bash
```
git clone https://github.com/ratnesh134/Video-Summarization-ChatBot.git
cd your-repo-name
```

2. Install dependencies:

Bash
```
pip install -r requirements.txt
```

3. Configure API keys:
Create a new directory named .streamlit in the root of your project. Inside this directory, create a file named secrets.toml. Add your API keys to this file:

Ini, TOML

# .streamlit/secrets.toml
```
GEMINI_API_KEY = "your_gemini_api_key"
GROQ_API_KEY = "your_groq_api_key"
```
4. Run the application:

Bash

streamlit run app.py
The application will open in your default web browser at http://localhost:8501.

<br>

🚀 Usage Instructions
Upload Video: Use the file uploader to select a video file (MP4 or MOV).

Wait for Analysis: The application will automatically send the video to Gemini for analysis. A spinner will indicate that the process is underway. Once complete, the detailed summary will be displayed on the screen.

Start Chatting: A chat box will appear below the summary. You can now ask questions about the video's content.

Multi-turn Conversation: Ask follow-up questions. The assistant will remember the context of the summary and your previous questions.

Example Scenario:

User uploads video: A video of a traffic intersection.

Gemini provides summary: "At 00:15, a red sedan runs a red light. Potential issue: Traffic violation. At 00:35, a pedestrian crosses against the signal. Potential issue: Jaywalking."

User asks: "What color was the car that ran the red light?"

Assistant responds: "The car that ran the red light at 00:15 was a red sedan."

<br>

# Project Structure

Here is the project structure for the Visual Understanding Agentic Chat Assistant.

```
Video-Summarization-ChatBot/
|
|
├── .streamlit/
|    |
|    |
│    └── secrets.toml
|
|
├── uploaded_videos/
|   |
|   |
│   └── (Your video files for testing, e.g., 1.mp4)
|
|
├── app.py
|
|
└── README.md
```

File and Folder Descriptions
your_project_directory/: This is the root directory of your project.

.streamlit/: A mandatory folder for Streamlit to manage local configurations and secrets.

secrets.toml: This file is where you securely store your API keys for Gemini and Groq.

uploads/: This is a directory where you can place video files to test with the application, though the app also supports uploading directly.

app.py: This is the main Python script containing all the application logic, including the Streamlit UI, the Gemini video summarization function, and the Groq-powered chat agent.

README.md: This file provides comprehensive documentation for your project, including its overview, features, architecture, and setup instructions.

<br>

## 📝 Evaluation Criteria

This project was developed with the following criteria in mind:

Functionality: The core features—video summarization, event recognition, and multi-turn conversations—are fully implemented and operational.

Code Quality: The codebase is modular, well-commented, and adheres to good Python coding practices.

System Design: The architectural design is clear, robust, and leverages the strengths of each chosen tool (Gemini for vision, LLAMA 3.3-70B via Groq Cloud for chat).

Documentation: This README.md file provides a comprehensive overview, setup instructions, and usage guidelines.

Innovation: The use of a decoupled agentic workflow with best-in-class models (Gemini and Groq) demonstrates a creative approach to building a responsive and powerful visual assistant.


## Collaborators

Aditya Londhe - adityalondhe052@gmail.com

Nitesh Pratap Singh - niteshen1010@gmail.com

Ratnesh Kumar - ratnesh134@gmail.com













