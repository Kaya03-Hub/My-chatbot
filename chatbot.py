
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv
load_dotenv()


#1. Instantiate the Groq-backed LLM 
llm = ChatGroq( model="openai/gpt-oss-120b",  temperature=0.7, )


# 2. Create a system prompt to prime behavior 
system_message = SystemMessage(
    content="response like my Teacher."
)

conversation_history = []  # Initialize conversation history

# 4. Function responsible for getting an AI response
def get_ai_response(user_input, conversation_history):
        
        user_message = HumanMessage(content=user_input)

        conversation_history.append(user_message)

        messages = [
              system_message,
              *conversation_history,
    ]

    
    # 5. Call the model 
        ai_msg = llm.invoke(messages)
      
        conversation_history.append(ai_msg)

        return ai_msg.content

# 6. Main conversation loop
print("=== Chatbot with Memory (type 'exit' to quit) ===")

while True:  

    user_input = input("You: ").strip() 

    if user_input.lower() in["quit", "exit","bye"]: 
        print("\n Chatbot:Goodbye!") 
        break 

    response = get_ai_response(
        user_input,
        conversation_history
    )

    print("AI:", response)
    