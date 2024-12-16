from langchain_core.prompts import PromptTemplate
from langchain_google_vertexai import VertexAI, HarmBlockThreshold, HarmCategory

safety_settings = {
    HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
}

llm = VertexAI(model_name="gemini-1.5-flash-002", safety_settings=safety_settings)

template = """Question: {question}

Answer: Let's think step by step."""

prompt_template = PromptTemplate.from_template(template)

chain = prompt_template | llm

question = """
I have five apples. I throw two away. I eat one. How many apples do I have left?
"""
print(chain.invoke({"question": question}))

# pip install pydantic==2.9.0
