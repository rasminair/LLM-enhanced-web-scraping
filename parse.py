# Start with creating LLM parsing function using Ollama
# Ollama is a module which helps run LLMs locally in our systems. langchain to link LLM with Python code
from langchain_ollama import OllamaLLM 
from langchain_core.prompts import ChatPromptTemplate

# Template for the prompt
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}"
    "Please follow these instructions carefully: n/n"
    "1. **Extract information:** Only extract the information that directly matches the provided description: {parse_description}."
    "2.  **No Extra Content:** Do not include any additional text, comments, or explanations in your response."
    "3. **Empty Response: If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# loading the gemma3 model (1 billion parameters)
model = OllamaLLM(model="gemma3:1b") 

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    parsed_results = []

   
    for i, chunk in enumerate(dom_chunks, start=1): # Go to the dom_chunk and start from the first position
        response = chain.invoke(({"dom_content": chunk, "parse_description": parse_description})) # parse_description is what you take from the user

        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)

   
