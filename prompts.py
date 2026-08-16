import json
import os
from datetime import datetime

PROMPTS_FILE = "prompts.json"

def initialize_prompts():
    """처음 실행 시 prompts.json 초기화"""
    if not os.path.exists(PROMPTS_FILE):
        initial_data = [
            {"id": "1", "title": "프롬프트 작성법", "category": "학습/교육", "content": "좋은 프롬프트를 작성하는 방법", "favorite": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"id": "2", "title": "AI 학습 가이드", "category": "학습/교육", "content": "AI 기초부터 심화까지 학습하는 방법", "favorite": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"id": "3", "title": "Python 기초", "category": "학습/교육", "content": "Python 프로그래밍 기초 학습", "favorite": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"id": "4", "title": "효과적인 학습법", "category": "학습/교육", "content": "시간을 절약하면서 효과적으로 학습하는 방법", "favorite": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"id": "5", "title": "온라인 강의 활용법", "category": "학습/교육", "content": "온라인 강의를 효과적으로 활용하는 팁", "favorite": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"id": "6", "title": "이메일 작성법", "category": "비즈니스", "content": "전문적이고 효과적인 이메일 작성 방법", "favorite": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"id": "7", "title": "보고서 작성법", "category": "비즈니스", "content": "명확하고 설득력 있는 보고서 작성 방법", "favorite": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"id": "8", "title": "프레젠테이션 기획", "category": "비즈니스", "content": "효과적인 프레젠테이션 기획 및 구성 방법", "favorite": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"id": "9", "title": "회의록 작성법", "category": "비즈니스", "content": "정확하고 효율적인 회의록 작성 방법", "favorite": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
            {"id": "10", "title": "마케팅 전략 수립", "category": "비즈니스", "content": "효과적인 마케팅 전략을 수립하는 방법", "favorite": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        ]
        save_prompts(initial_data)


def load_prompts():
    """JSON 파일에서 프롬프트 로드"""
    if os.path.exists(PROMPTS_FILE):
        with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_prompts(prompts):
    """프롬프트를 JSON 파일에 저장"""
    with open(PROMPTS_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)


def get_all_prompts():
    """모든 프롬프트 반환"""
    return load_prompts()


def add_prompt(prompts):
    """새 프롬프트 추가"""
    print("\n" + "="*60)
    print("📝 새 프롬프트 추가")
    print("="*60)
    
    title = input("제목: ").strip()
    if not title:
        print("❌ 제목을 입력하세요.")
        return
    
    category = input("카테고리 (학습/교육/비즈니스): ").strip()
    content = input("내용: ").strip()
    
    if not content:
        print("❌ 내용을 입력하세요.")
        return
    
    # 새 ID 생성
    new_id = str(max([int(p["id"]) for p in prompts], default=0) + 1)
    
    new_prompt = {
        "id": new_id,
        "title": title,
        "category": category,
        "content": content,
        "favorite": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    prompts.append(new_prompt)
    print("✅ 프롬프트가 추가되었습니다.")


def find_prompt_by_id(prompts, prompt_id):
    """ID로 프롬프트 찾기"""
    for prompt in prompts:
        if prompt["id"] == prompt_id:
            return prompt
    return None


def show_all_prompts(prompts):
    """모든 프롬프트 표시"""
    if not prompts:
        print("❌ 저장된 프롬프트가 없습니다.")
        return
    
    print("\n" + "="*60)
    print("📝 전체 프롬프트")
    print("="*60)
    
    for prompt in prompts:
        star = "⭐" if prompt.get("favorite", False) else "  "
        print(f"{star} [{prompt['id']}] {prompt['category']} - {prompt['title']}")
    
    print("="*60 + "\n")


def show_prompt_detail(prompt):
    """프롬프트 상세 정보 표시"""
    print("\n" + "="*60)
    print(f"📌 {prompt['title']}")
    print("="*60)
    print(f"ID: {prompt['id']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {'⭐ 예' if prompt.get('favorite') else '아니오'}")
    print(f"생성일: {prompt.get('created_at', 'N/A')}")
    print(f"\n내용:\n{prompt['content']}")
    print("="*60 + "\n")


def view_prompt_detail(prompts):
    """프롬프트 상세 보기"""
    show_all_prompts(prompts)
    
    try:
        prompt_id = input("보기할 프롬프트 ID 입력: ").strip()
        prompt = find_prompt_by_id(prompts, prompt_id)
        
        if prompt:
            while True:
                show_prompt_detail(prompt)
                
                print("선택:")
                print("1. ⭐ 즐겨찾기 토글")
                print("0. 🔙 돌아가기")
                
                choice = input("선택: ").strip()
                if choice == "1":
                    prompt["favorite"] = not prompt.get("favorite", False)
                    print("✅ 즐겨찾기가 업데이트되었습니다.")
                elif choice == "0":
                    break
        else:
            print("❌ 해당 ID의 프롬프트가 없습니다.")
    except Exception as e:
        print(f"❌ 오류: {e}")


def search_prompts(prompts):
    """프롬프트 검색"""
    keyword = input("검색 키워드: ").strip()
    
    results = [p for p in prompts if keyword.lower() in p["title"].lower() or keyword.lower() in p["content"].lower()]
    
    if results:
        print(f"\n검색 결과: {len(results)}개")
        for prompt in results:
            star = "⭐" if prompt.get("favorite") else "  "
            print(f"{star} [{prompt['id']}] {prompt['title']}")
    else:
        print("❌ 검색 결과가 없습니다.")


def update_prompt(prompts):
    """프롬프트 수정"""
    show_all_prompts(prompts)
    
    prompt_id = input("수정할 프롬프트 ID: ").strip()
    prompt = find_prompt_by_id(prompts, prompt_id)
    
    if prompt:
        print(f"\n현재 제목: {prompt['title']}")
        new_title = input("새 제목 (엔터로 유지): ").strip()
        if new_title:
            prompt["title"] = new_title
        
        print(f"현재 내용: {prompt['content']}")
        new_content = input("새 내용 (엔터로 유지): ").strip()
        if new_content:
            prompt["content"] = new_content
        
        print("✅ 프롬프트가 수정되었습니다.")
    else:
        print("❌ 해당 ID의 프롬프트가 없습니다.")


def delete_prompt(prompts):
    """프롬프트 삭제"""
    show_all_prompts(prompts)
    
    prompt_id = input("삭제할 프롬프트 ID: ").strip()
    
    for i, prompt in enumerate(prompts):
        if prompt["id"] == prompt_id:
            confirm = input(f"'{prompt['title']}'을(를) 삭제하시겠습니까? (y/n): ").strip().lower()
            if confirm == "y":
                prompts.pop(i)
                print("✅ 프롬프트가 삭제되었습니다.")
            return
    
    print("❌ 해당 ID의 프롬프트가 없습니다.")


def show_favorite_prompts(prompts):
    """즐겨찾기 프롬프트 표시"""
    favorites = [p for p in prompts if p.get("favorite", False)]
    
    if not favorites:
        print("❌ 즐겨찾기된 프롬프트가 없습니다.")
        return
    
    print("\n" + "="*60)
    print("⭐ 즐겨찾기 프롬프트")
    print("="*60)
    
    for prompt in favorites:
        print(f"⭐ [{prompt['id']}] {prompt['category']} - {prompt['title']}")
    
    print("="*60 + "\n")

def search_prompt(prompts):
    """프롬프트 검색"""
    keyword = input("검색 키워드: ").strip()
    
    if not keyword:
        print("❌ 검색 키워드를 입력하세요.")
        return
    
    results = [
        p for p in prompts 
        if keyword.lower() in p["title"].lower() 
        or keyword.lower() in p["content"].lower()
    ]
    
    if results:
        print(f"\n🔍 검색 결과: {len(results)}개")
        print("="*60)
        for prompt in results:
            star = "⭐" if prompt.get("favorite", False) else "  "
            print(f"{star} [{prompt['id']}] {prompt['category']} - {prompt['title']}")
        print("="*60 + "\n")
    else:
        print("❌ 검색 결과가 없습니다.\n")

def toggle_favorite(prompts, prompt_id):
    """즐겨찾기 토글"""
    show_all_prompts(prompts)
    
    try:
        prompt_id = input("즐겨찾기 토글할 프롬프트 ID: ").strip()
        prompt = find_prompt_by_id(prompts, prompt_id)
        
        if prompt:
            prompt["favorite"] = not prompt.get("favorite", False)
            status = "⭐ 즐겨찾기 추가됨" if prompt["favorite"] else "즐겨찾기 제거됨"
            print(f"✅ {status}\n")
        else:
            print("❌ 해당 ID의 프롬프트가 없습니다.\n")
    except Exception as e:
        print(f"❌ 오류: {e}\n")      

def search_prompts(prompts, keyword):
    """키워드로 프롬프트 검색"""
    results = []
    for prompt in prompts:
        if keyword.lower() in prompt['title'].lower() or \
           keyword.lower() in prompt['content'].lower():
            results.append(prompt)
    return results