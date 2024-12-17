import vertexai
from vertexai.generative_models import GenerativeModel

project_id = "PROJECT_ID" # 書き換える

vertexai.init(project=project_id, location="us-central1")

model = GenerativeModel("gemini-2.0-flash-exp")

prompt = """
以下はニュース記事のタイトルです。「政治」「経済」「芸能」「スポーツ」「科学」「その他」のうち1つに分類してください。
回答だけ一言で出力してください
===========================
「今年度補正予算が成立 13.9兆円」
===========================
以下は例です
「G20 バイデン氏不在で集合写真」:政治
「岡田将生&高畑充希結婚 SNS反応」:芸能
"""

response = model.generate_content(
  contents=prompt
)

print(response.text)

