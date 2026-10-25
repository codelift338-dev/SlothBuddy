import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="SlothBuddy AI",
    page_icon="🦥",
    layout="centered",
)

st.title("🦥 SlothBuddy AI")
st.subheader("Your personal slow-and-steady task planner")

st.write(
    "Give me your messy to-do list. "
    "I'll help you decide what to do first."
)

st.info(
    "Your tasks are sent to a hosted AI model for processing. "
    "Avoid entering sensitive personal information."
)

tasks = st.text_area(
    "What do you need to get done?",
    placeholder=(
        "Finish my assignment\n"
        "Reply to my teacher\n"
        "Buy groceries\n"
        "Prepare for tomorrow's interview"
    ),
    height=180,
)

model_id = "deepseek-ai/DeepSeek-V4.1-Flash-1017"

if st.button("🦥 Organize My Tasks", use_container_width=True):
    if not tasks.strip():
        st.warning("Please enter at least one task.")
    else:
        try:
            token = st.secrets["HF_TOKEN"]

            client = InferenceClient(
                model=model_id,
                token=token,
                timeout=60,
            )

            with st.spinner("Your sloth is thinking slowly... 🦥"):
                response = client.chat_completion(
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are SlothBuddy, a friendly task "
                                "planning assistant. Organize the user's "
                                "tasks into Urgent, Important, and Can Wait. "
                                "Explain your reasoning briefly. Do not "
                                "invent deadlines. If deadlines are unknown, "
                                "say so. Suggest one small first step and "
                                "encourage reasonable breaks. Be concise."
                            ),
                        },
                        {
                            "role": "user",
                            "content": tasks,
                        },
                    ],
                    max_tokens=500,
                    temperature=0.4,
                )

            answer = response.choices[0].message.content

            st.subheader("Your relaxed action plan")
            st.markdown(answer)

            st.success("Your plan is ready! Take it one step at a time.")

        except KeyError:
            st.error(
                "HF_TOKEN is missing. Check "
                ".streamlit/secrets.toml."
            )

        except Exception as error:
            st.error(
                "The AI request did not succeed. "
                "Check your model access, inference credits, and internet "
                "connection, then try again."
            )
            with st.expander("Technical details"):
                st.code(str(error))

st.divider()

st.caption(
    "Built with Python, Streamlit, and Hugging Face. "
    "Small steps, less stress. 🦥"
)