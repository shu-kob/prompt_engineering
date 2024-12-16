import vertexai
from vertexai.generative_models import GenerativeModel

project_id = "PROJECT_ID" # 書き換える

vertexai.init(project=project_id, location="asia-northeast1")

model = GenerativeModel("gemini-1.5-flash-002")

prompt = """
以下はニュース記事のタイトルです。「政治」「経済」「芸能」「スポーツ」「科学」「その他」のうち1つに分類してください。
回答だけ一言で出力してください
===========================
「紅白出場歌手の選考基準 NHK公開」
===========================
以下は例です
「G20 バイデン氏不在で集合写真」:政治
「岡田将生&高畑充希結婚 SNS反応」:芸能
"""

response = model.generate_content(
  contents=prompt
)

print(response.text)

