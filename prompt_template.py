from langchain_core.prompts import PromptTemplate
from langchain_google_vertexai import VertexAI

llm = VertexAI(model_name="gemini-1.5-flash-002")

template = """質問: {question}

ステップバイステップで考えてください。"""

prompt_template = PromptTemplate.from_template(template)

chain = prompt_template | llm

question = """
10 + 2 * 3 - 4 * 2
"""
print(chain.invoke({"question": question}))

# pip install pydantic==2.9.0
