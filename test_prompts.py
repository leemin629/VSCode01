import json

# prompts.json 파일 읽기
with open('prompts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 올바른 접근 방식
print(f"저장된 카테고리: {list(data['prompts'].keys())}")

# 각 카테고리별 프롬프트 개수
for category, prompts in data['prompts'].items():
    print(f"{category}: {len(prompts)}개")

# 첫 번째 프롬프트 확인
first_category = list(data['prompts'].keys())[0]
first_prompt = data['prompts'][first_category][0]
print(f"\n첫 번째 프롬프트:")
print(f"제목: {first_prompt['title']}")
print(f"설명: {first_prompt['description']}")