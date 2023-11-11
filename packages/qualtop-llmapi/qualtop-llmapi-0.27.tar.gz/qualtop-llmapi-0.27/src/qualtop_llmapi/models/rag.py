# -*- coding:utf-8 -*-
import os

import qualtop_llmapi
from qualtop_llmapi.models.loading import load_embedder
from qualtop_llmapi.models.chatgpt_embeddings import create_message_with_context

from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings, LlamaCppEmbeddings

import llama_cpp

def ask(messages, llm, vecdb_id):
    home_dir = os.path.expanduser("~")
    
    if not qualtop_llmapi.embedder:
        # Load mistral embedder
        qualtop_llmapi.embedder = load_embedder("mistral-7b")
    
    embedding_fn = qualtop_llmapi.embedder

    if vecdb_id == "single":
        vecdb = Chroma(persist_directory=os.path.join(home_dir,
                                                      ".cache/embeddings",
                                                      "data/gnp_single"),
                       embedding_function=embedding_fn,
                       )
    elif vecdb_id == "collection":
        vecdb = Chroma(persist_directory=os.path.join(home_dir,
                                                      ".cache/embeddings",
                                                      "data/gnp"),
                       embedding_function=GPT4AllEmbeddings(),
                       )
    else:
        raise ValueError(f"Database {vecdb_id} not existant...")

    # Prompt
    prompt_template = "Usa las siguientes piezas de contexto para responder la pregunta del final. Si no sabes la respuesta, responde 'No lo sé'."
    prompt_template += "\n\n{context}\n\n"
    prompt_template += "Pregunta: {question}\n"
    prompt_template += "Respuesta:"

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Q&A chain
    # TODO: CHECK MODEL NAME TO DECIDE CONTEXT SIZE
    qa_chain = ConversationalRetrievalChain.from_llm(
            llm,
            retriever=vecdb.as_retriever(search_kwargs={'k': 6}),
            return_source_documents=True,
            verbose=True,
            combine_docs_chain_kwargs={"prompt": PROMPT},
    )
    result = qa_chain({"question": messages[-1]['content'], 
                       "chat_history": ""})
    answer = result["answer"].strip()

    # If answer is empty, ask again ONCE
    if answer == "" :
        result = qa_chain({"question": messages[-1]['content'], 
                           "chat_history": ""})
        answer = result["answer"].strip()
        if answer == "" :
            answer = "No lo sé"

    return answer


def ask_manually(messages, llm, df):
    answer = ""
   
    prompt_template = "[INST]\n"
    prompt_template += "Usa las siguientes piezas de contexto para responder la pregunta del final. Si no sabes la respuesta, responde 'No lo sé'."
    prompt_template += "\n\n{context}\n\n"
    prompt_template += "Pregunta: {question}"
    prompt_template += "\n[\INST]"

    PROMPT = PromptTemplate(template=prompt_template,
                            input_variables=["context", "question"])
    
    prompt = create_message_with_context(
            messages[-1]['content'],
            df,
            "llama-7b",
            4096-500,
            PROMPT)
    answer = llm(prompt)
    return answer
