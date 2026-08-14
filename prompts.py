import json
import os

# 파일 경로
PROMPTS_FILE = 'prompts.json'

# 1. 프롬프트 저장 함수
def save_prompt(category, title, content):
    """
    새로운 프롬프트를 저장합니다.
    
    예: save_prompt("AI", "ChatGPT 팁", "효과적인 사용법...")
    """
    # 기존 데이터 불러오기
    data = load_prompts()
    
    # 새로운 프롬프트 ID 생성 (마지막 ID + 1)
    if data['prompts']:
        new_id = max(p['id'] for p in data['prompts']) + 1
    else:
        new_id = 1
    
    # 새 프롬프트 생성
    new_prompt = {
        'id': new_id,
        'category': category,
        'title': title,
        'content': content
    }
    
    # 리스트에 추가
    data['prompts'].append(new_prompt)
    
    # 파일에 저장
    with open(PROMPTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 프롬프트 저장 완료! (ID: {new_id})")


# 2. 모든 프롬프트 불러오기
def load_prompts():
    """
    prompts.json에서 모든 프롬프트를 불러옵니다.
    """
    # 파일이 없으면 기본 구조 생성
    if not os.path.exists(PROMPTS_FILE):
        default_data = {'prompts': []}
        with open(PROMPTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, ensure_ascii=False, indent=2)
        return default_data
    
    # 파일에서 읽기
    with open(PROMPTS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return data


# 3. 카테고리별 프롬프트 조회
def get_prompts_by_category(category):
    """
    특정 카테고리의 프롬프트만 반환합니다.
    
    예: get_prompts_by_category("AI")
    """
    data = load_prompts()
    
    # 카테고리가 일치하는 프롬프트만 필터링
    filtered = [p for p in data['prompts'] if p['category'] == category]
    
    return filtered

# 4. ID로 프롬프트 조회
def get_prompt_by_id(prompt_id):
    """특정 ID의 프롬프트를 조회합니다."""
    data = load_prompts()
    
    for prompt in data['prompts']:
        if prompt['id'] == prompt_id:
            return prompt
    
    return None

# 별칭 함수들 (main.py와의 호환성)
def add_prompt(category, title, content):
    """save_prompt의 별칭"""
    return save_prompt(category, title, content)

def get_all_prompts():
    """load_prompts의 별칭"""
    data = load_prompts()
    return data['prompts']

def get_prompt_by_id(prompt_id):
    """특정 ID의 프롬프트를 조회합니다."""
    data = load_prompts()
    for prompt in data['prompts']:
        if prompt['id'] == prompt_id:
            return prompt
    return None

# prompts.py에 추가
def display_prompt_detail(prompt_id):
    """프롬프트 상세 정보 표시"""
    prompt = get_prompt_by_id(prompt_id)
    if prompt:
        print(f"\n📌 ID: {prompt['id']}")
        print(f"📂 카테고리: {prompt['category']}")
        print(f"📝 제목: {prompt['title']}")
        print(f"📄 내용:\n{prompt['content']}\n")
    else:
        print("❌ 프롬프트를 찾을 수 없습니다.")

 def update_prompt(prompt_id, category, title, content):
    """프롬프트 수정"""
    data = load_prompts()
    for prompt in data['prompts']:
        if prompt['id'] == prompt_id:
            prompt['category'] = category
            prompt['title'] = title
            prompt['content'] = content
            save_data(data)
            return True
    return False       

def delete_prompt(prompt_id):
    """프롬프트 삭제"""
    data = load_prompts()
    original_length = len(data['prompts'])
    data['prompts'] = [p for p in data['prompts'] if p['id'] != prompt_id]
    
    if len(data['prompts']) < original_length:
        save_data(data)
        return True
    return False