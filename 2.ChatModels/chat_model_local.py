# chat.py
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

def main():
    MODEL_ID = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    # Create the pipeline
    llm_pipeline = HuggingFacePipeline.from_model_id(
        model_id=MODEL_ID,
        task="text-generation",
        pipeline_kwargs={
            "temperature": 0.5,
            "max_new_tokens": 100,
        }
    )

    # Create chat model (model_id must be passed again)
    chat_model = ChatHuggingFace(llm=llm_pipeline, model_id=MODEL_ID)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = chat_model.invoke(user_input)
        print("TinyLlama:", response.content)

if __name__ == "__main__":
    main()
