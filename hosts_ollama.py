from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain.tools import tool
from langchain_community.document_loaders import TextLoader

ollama_chat = ChatOpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
    model="llama3.2:3b"
)

if (ollama_chat):
    print("OK")
  
@tool
def extract_file_content(path: str) -> list:
    """Read file content for given path, and display it to the user.
        
    Args:
        path: string containing file path
    """
    loader_text = TextLoader(path)
    loader_content = loader_text.load()
    for line in loader_content:
        print(line)

query = "Please show what is in /etc/hosts"

tools = [extract_file_content]
ollama_binded_with_tool = ollama_chat.bind_tools([extract_file_content], tool_choice="extract_file_content")

messages = [HumanMessage(query)]
ai_response = ollama_binded_with_tool.invoke(messages)
messages.append(ai_response)

tool_call = ai_response.tool_calls[0]
selected_tool = {"extract_file_content": extract_file_content}[tool_call["name"].lower()]
tool_output = selected_tool.invoke(tool_call["args"])
