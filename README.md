# 🦥 SlothBuddy AI

**Small steps, less stress.**

SlothBuddy AI is a simple, beginner-friendly task planning assistant that helps you organize a messy to-do list into a clear, manageable action plan using AI.

Instead of feeling overwhelmed by a long list of tasks, SlothBuddy helps you identify what is urgent, what is important, and what can wait.

## ✨ Features

- 📝 Enter multiple tasks in one place.
- 🤖 Use a hosted AI model to organize your tasks.
- 🚦 Group tasks into **Urgent**, **Important**, and **Can Wait**.
- 🎯 Get a small, practical first step to help you get started.
- 🌿 Receive simple suggestions for taking reasonable breaks.
- 💻 Use a clean, beginner-friendly web interface.
- ☁️ Run AI requests through Hugging Face instead of downloading a large model locally.

## 🛠️ Built With

- Python
- Streamlit
- Hugging Face Inference Providers

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SlothBuddy
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Create and activate a virtual environment

**Windows Command Prompt:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the dependencies

```cmd
pip install streamlit huggingface_hub
```

### 4. Configure your Hugging Face token

Create a file named `secrets.toml` inside a `.streamlit` folder in your project directory.

Your folder structure should look like this:

```text
SlothBuddy/
├── app.py
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml
```

Add your own Hugging Face access token to `secrets.toml`:

```toml
HF_TOKEN = "YOUR_HUGGING_FACE_TOKEN"
```

Replace the placeholder with your token. **Never publish your actual token or commit `secrets.toml` to GitHub.**

### 5. Start the application

```cmd
python -m streamlit run app.py
```

Open the local address displayed in your terminal, usually `http://localhost:8501`.

Enter your tasks and click **Organize My Tasks**.

## 🔐 Privacy Note

SlothBuddy sends the tasks you submit to a hosted AI service for processing. Do not enter passwords, financial details, or other sensitive personal information.

## 🌱 Project Goal

SlothBuddy was created as a small, practical AI project to demonstrate how Python and hosted AI models can help people manage everyday tasks without requiring a powerful computer.

**Remember: You don't have to do everything at once. Just take the next small step.** 🦥