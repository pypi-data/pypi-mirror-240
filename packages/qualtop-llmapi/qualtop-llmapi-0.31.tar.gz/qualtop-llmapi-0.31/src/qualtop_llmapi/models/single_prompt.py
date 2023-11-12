import os
from langchain.schema.output_parser import StrOutputParser

def ask(messages, llm):
    chain = messages | llm | StrOutputParser()
    output = chain.invoke(input="")
    #output = llm(messages.format())
    output = " ".join(output.split(":")[1:])
    return output.strip()
