from langchain_core.prompts import ChatPromptTemplate
from langchain_google_vertexai import VertexAI

llm = VertexAI(model_name="gemini-2.0-flash-exp")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "{system_prompt}"),
    ("human", "{question}"),
])

chain = prompt_template | llm

question = """
生成AIの仕組みを教えてください。
"""

system_prompt = """
ITコンサルタントになったように説明してください。
"""

print(chain.invoke({"system_prompt": system_prompt, "question": question}))

# pip install pydantic==2.9.0
