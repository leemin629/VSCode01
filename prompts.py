import json
import os

PROMPTS_FILE = "prompts.json"

def load_prompts():
    """프롬프트 데이터 로드"""
    if os.path.exists(PROMPTS_FILE):
        with open(PROMPTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"prompts": []}

def save_prompts(data):
    """프롬프트 데이터 저장"""
    with open(PROMPTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_prompt(category, title, content):
    """프롬프트 추가"""
    data = load_prompts()
    new_prompt = {
        "id": len(data["prompts"]) + 1,
        "category": category,
        "title": title,
        "content": content
    }
    data["prompts"].append(new_prompt)
    save_prompts(data)
    return new_prompt

def get_all_prompts():
    """모든 프롬프트 조회"""
    data = load_prompts()
    return data["prompts"]

def get_prompts_by_category(category):
    """카테고리별 프롬프트 조회"""
    data = load_prompts()
    return [p for p in data["prompts"] if p["category"] == category]

def get_prompt_by_id(prompt_id):
    """ID로 프롬프트 조회"""
    data = load_prompts()
    for prompt in data["prompts"]:
        if prompt["id"] == prompt_id:
            return prompt
    return None