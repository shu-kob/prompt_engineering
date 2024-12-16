from langchain_google_vertexai import VertexAI

model = VertexAI(model_name="gemini-1.5-flash-002")

messages = [
  ("human", "ネコの鳴き真似をしてください。"),
]

output = model.invoke(messages)
print(output)
