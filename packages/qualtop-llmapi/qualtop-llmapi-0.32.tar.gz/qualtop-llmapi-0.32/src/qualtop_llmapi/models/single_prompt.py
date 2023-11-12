import os
from langchain.schema.output_parser import StrOutputParser

def ask(messages, llm):
    chain = messages | llm | StrOutputParser()
    output = chain.invoke(input="")
    #output = llm(messages.format())
    output = " ".join(output.split(":")[1:])
    return output.strip()

def ask_code(messages, llm):
    chain = messages | llm | StrOutputParser()
    print(messages.format())
    output = chain.invoke(input="")
    return output.strip()
