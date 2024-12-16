from langchain_core.prompts import ChatPromptTemplate
from langchain_google_vertexai import VertexAI

llm = VertexAI(model_name="gemini-1.5-flash-002")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "ステップバイステップで考えてください。"),
    ("human", "{question}"),
])

chain = prompt_template | llm

question = """
10 + 2 * 3 - 4 * 2
"""
print(chain.invoke({"question": question}))

# pip install pydantic==2.9.0
