import os
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings, LlamaCppEmbeddings

import llama_cpp

def ask(messages, llm, vecdb_id):
    home_dir = os.path.expanduser("~")
    if not llama_cpp.GGML_USE_CUBLAS:
        raise Exception("This method needs GPU")

    embedding_model_path = os.path.join(home_folder,
                                        ".cache/gpt4all",
                                        "llama-2-13b.Q5_K_M.gguf")
    
    embedding_fn = LlamaCppEmbeddings(model_path=embedding_model_path,
                                      f16_kv=True,
                                      n_batch=1024,
                                      n_gpu_layers=80)

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
    prompt_template = "Usa las siguientes piezas de contexto para responder la pregunta al final. Si no sabes la respuesta, responde 'No lo se'."
    prompt_template += "\n\n{context}\n\n"
    prompt_template += "Pregunta: {question}\n"
    prompt_template += "Respuesta:"

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Q&A chain
    qa_chain = ConversationalRetrievalChain.from_llm(
            llm,
            retriever=vecdb.as_retriever(search_kwargs={'k': 4}),
            return_source_documents=True,
            verbose=True,
            combine_docs_chain_kwargs={"prompt": PROMPT},
    )
    result = qa_chain({"question": messages[-1]['content'], 
                       "chat_history": ""})
    return result['answer']
