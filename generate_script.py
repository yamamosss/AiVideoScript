import openai
import json
import datetime
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

GENRES = ["心理学", "雑学", "お金の豆知識", "ライフハック"]
OUTPUT_DIR = "scripts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PROMPT_TEMPLATE = """
次の条件でTikTokショート動画向けの台本を作成してください：

- ジャンル：{genre}
- 尺：45秒以内
- 話し言葉でテンポ良く
- JSON形式で出力
- 以下の形式：
{{
  "title": "タイトル",
  "script": "本文",
  "tags": ["タグ1","タグ2"]
}}
"""

for genre in GENRES:
    prompt = PROMPT_TEMPLATE.format(genre=genre)
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "あなたは短い動画台本を作る専門家です。"},
            {"role": "user", "content": prompt}
        ]
    )
    content = response.choices[0].message["content"]
    filename = f"{genre}_{datetime.date.today()}.json"
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ {genre} の台本を保存しました。")
