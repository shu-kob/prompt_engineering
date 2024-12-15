import vertexai
from vertexai.generative_models import GenerativeModel

project_id = "pristine-nomad-424014-d7" # 書き換える

vertexai.init(project=project_id, location="asia-northeast1")

model = GenerativeModel("gemini-1.5-flash-002")

response = model.generate_content(
  "プロンプトエンジニアリングとは"
)

print(response.text)
