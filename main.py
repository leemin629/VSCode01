import json
import os
import re
import sys

FILE_NAME = "prompts.json"

EXIT_COMMANDS = {"q", "quit", "exit"}

def safe_exit():
    print("프로그램을 종료합니다.")
    sys.exit(0)

def check_exit(value):
    if value.strip().lower() in EXIT_COMMANDS:
        safe_exit()

def safe_input(message=""):
    value = input(message).strip()
    check_exit(value)
    return value


CATEGORIES = {
    "1": "학습/교육",
    "2": "비즈니스 디자인"
}

INITIAL_PROMPTS = [    {
        "id": "1-1",
        "category": "학습/교육",
        "title": "강의안 생성 프롬프트",
        "purpose": "특정 주제의 체계적인 강의 자료 생성",
        "content": """주제: [주제명]
대상: [학년/수준]
시간: [강의시간]

위 정보를 바탕으로 다음을 포함한 강의안을 작성하세요:
- 학습목표
- 도입
- 본론
- 활동/실습
- 마무리 및 과제""",
        "example": "고등학교 수학, 대학 프로그래밍, 직무교육",
        "favorite": False
    },
    {
        "id": "1-2",
        "category": "학습/교육",
        "title": "요약문 생성 프롬프트",
        "purpose": "긴 텍스트를 핵심만 추출하여 요약",
        "content": """다음 텍스트를 요약하세요:
[원본 텍스트]

요약 조건:
- 분량: [문장 수]
- 형식: [문단/글머리표]
- 핵심 개념 포함""",
        "example": "논문 요약, 기사 정리, 책 내용 정리",
        "favorite": False
    },
    {
        "id": "1-3",
        "category": "학습/교육",
        "title": "설명글 작성 프롬프트",
        "purpose": "복잡한 개념을 쉽게 설명하는 글 작성",
        "content": """개념: [설명할 개념]
대상 수준: [초급/중급/고급]

다음을 포함해 설명하세요:
- 정의
- 쉬운 예시
- 핵심 특징
- 주의할 점""",
        "example": "AI 개념 설명, 과학 원리 설명, 역사 사건 설명",
        "favorite": False
    },
    {
        "id": "1-4",
        "category": "학습/교육",
        "title": "퀴즈 생성 프롬프트",
        "purpose": "학습 확인용 문제 생성",
        "content": """학습 주제: [주제]
난이도: [쉬움/중간/어려움]
문제 수: [개수]

다음을 포함해 퀴즈를 만드세요:
- 문제
- 선택지
- 정답
- 해설""",
        "example": "시험 대비 문제, 온라인 학습 평가, 복습 퀴즈",
        "favorite": False
    },
    {
        "id": "2-1",
        "category": "비즈니스 디자인",
        "title": "프레젠테이션 슬라이드 프롬프트",
        "purpose": "발표용 슬라이드 구조 설계",
        "content": """주제: [발표 주제]
청중: [대상]
슬라이드 수: [개수]

다음 구조로 슬라이드를 설계하세요:
- 제목
- 개요
- 본론
- 결론
- 마무리""",
        "example": "사업 제안, 팀 발표, 투자 설명",
        "favorite": False
    },
    {
        "id": "2-2",
        "category": "비즈니스 디자인",
        "title": "포스터 디자인 프롬프트",
        "purpose": "홍보용 포스터 콘셉트 기획",
        "content": """포스터 주제: [주제]
목적: [홍보/모집/안내]
대상: [타겟]

다음을 포함한 포스터 구성안을 작성하세요:
- 헤드라인
- 핵심 메시지
- 시각 요소
- 색상 제안
- CTA""",
        "example": "행사 홍보, 동아리 모집, 제품 광고",
        "favorite": False
    },
    {
        "id": "2-3",
        "category": "비즈니스 디자인",
        "title": "브랜드 콘셉트 프롬프트",
        "purpose": "브랜드 이미지와 방향성 기획",
        "content": """브랜드명: [이름]
업종: [업종]
타겟 고객: [대상]

다음을 포함해 브랜드 콘셉트를 제안하세요:
- 브랜드 핵심 가치
- 톤앤매너
- 차별점
- 슬로건 아이디어""",
        "example": "신규 카페 브랜드, 패션 브랜드, 앱 서비스",
        "favorite": False
    },
    {
        "id": "2-4",
        "category": "비즈니스 디자인",
        "title": "마케팅 문구 작성 프롬프트",
        "purpose": "광고/홍보용 문구 작성",
        "content": """제품/서비스: [이름]
타겟: [고객층]
목적: [홍보/판매/인지도]

다음을 작성하세요:
- 메인 카피
- 서브 카피
- SNS 홍보 문구
- 해시태그 제안""",
        "example": "신제품 홍보, 이벤트 광고, SNS 콘텐츠 제작",
        "favorite": False
    }
]

def save_prompts(prompts):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=2)




def load_prompts():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def is_valid_prompt_data(data):
    if not isinstance(data, list):
        return False

    required_keys = {"id", "category", "title", "purpose", "content", "example", "favorite"}

    for item in data:
        if not isinstance(item, dict):
            return False
        if not required_keys.issubset(item.keys()):
            return False
        if item["category"] not in CATEGORIES.values():
            return False
        if not isinstance(item["id"], str):
            return False
        if not isinstance(item["favorite"], bool):
            return False

    return True


def initialize_prompts():
    if not os.path.exists(FILE_NAME):
        save_prompts(INITIAL_PROMPTS)
        return load_prompts()

    try:
        prompts = load_prompts()
        if not is_valid_prompt_data(prompts):
            print("⚠️ prompts.json 데이터 형식이 올바르지 않아 초기 데이터로 복구합니다.")
            save_prompts(INITIAL_PROMPTS)
            return load_prompts()
        return prompts
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ prompts.json 파일을 읽을 수 없어 초기 데이터로 복구합니다.")
        save_prompts(INITIAL_PROMPTS)
        return load_prompts()


def safe_input_non_empty(message):
    while True:
        value = safe_input(message)

        if value:
            return value

        print("⚠️ 빈 값은 입력할 수 없습니다.")


def safe_input_multiline(message):
    print(message)
    print("입력을 마치려면 END 를 입력하세요.")
    print("즉시 종료하려면 q, quit, exit 중 하나를 입력하세요.")

    lines = []

    while True:
        line = safe_input()

        if line.strip().upper() == "END":
            break
            
        lines.append(line)

    return "\n".join(lines).strip()


def input_multiline_non_empty(message):
    while True:
        text = safe_input_multiline(message)
        if text:
            return text
        print("⚠️ 빈 값은 입력할 수 없습니다.")

def fill_prompt_content(content):
    placeholders = re.findall(r"\[([^\]]+)\]", content)

    unique_placeholders = []
    for ph in placeholders:
        if ph not in unique_placeholders:
            unique_placeholders.append(ph)

    if not unique_placeholders:
        print("입력할 항목이 없는 프롬프트입니다.")
        return content

    for ph in unique_placeholders:
        user_input = safe_input_non_empty(f"{ph} 입력: ")
        content = content.replace(f"[{ph}]", user_input)

    return content


def find_prompt_by_id(prompts, prompt_id):
    for prompt in prompts:
        if prompt["id"] == prompt_id:
            return prompt
    return None


def get_category_key_by_value(category_value):
    for key, value in CATEGORIES.items():
        if value == category_value:
            return key
    return None


def get_next_prompt_id(prompts, category_name):
    category_key = get_category_key_by_value(category_name)
    max_number = 0

    for prompt in prompts:
        if prompt["id"].startswith(f"{category_key}-"):
            try:
                number = int(prompt["id"].split("-")[1])
                if number > max_number:
                    max_number = number
            except ValueError:
                continue

    return f"{category_key}-{max_number + 1}"


def choose_category():
    while True:
        print("=" * 50)
        print("📚 카테고리 선택")
        print("=" * 50)
        for key, value in CATEGORIES.items():
            print(f"{key}. {value}")
        print("0. 돌아가기")
        print("q. 프로그램 종료")

        choice = safe_input("선택: ")

        if choice == "0":
            return None
        if choice in CATEGORIES:
            return CATEGORIES[choice]

        print("⚠️ 올바른 번호를 입력하세요.")


def show_prompt_detail(prompt, prompts):
    completed_once = False

    while True:
        has_placeholder = bool(re.search(r"\[[^\]]+\]", prompt["content"]))

        print("=" * 60)
        print("📌 프롬프트 상세 정보")
        print("=" * 60)
        print(f"ID: {prompt['id']}")
        print(f"카테고리: {prompt['category']}")
        print(f"제목: {prompt['title']}")
        print(f"목적: {prompt['purpose']}")
        print(f"내용:\n{prompt['content']}")
        print(f"활용 예시: {prompt['example']}")
        print(f"즐겨찾기: {'예' if prompt['favorite'] else '아니오'}")
        print("=" * 60)

        print("1. 즐겨찾기 추가/제거")
        print("2. 입력값 넣어 완성된 프롬프트 보기")
        print("0. 돌아가기")
        print("q. 프로그램 종료")

        choice = safe_input("선택: ").strip()

        if choice == "1":
            prompt["favorite"] = not prompt["favorite"]
            save_prompts(prompts)
            print("✅ 즐겨찾기 상태가 변경되었습니다.")

        elif choice == "2":
            completed = fill_prompt_content(prompt["content"])

            print("\n" + "=" * 60)
            print("✅ 완성된 프롬프트")
            print("=" * 60)
            print(completed)
            print("=" * 60)

            completed_once = True

            safe_input("Enter 키를 누르면 상세정보 화면으로 돌아갑니다...")

        elif choice == "0":
            return

        else:
            print("⚠️ 올바른 번호를 입력하세요.")

def browse_by_category(prompts):
    category = choose_category()
    if category is None:
        return

    filtered = [p for p in prompts if p["category"] == category]

    if not filtered:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    while True:
        print("=" * 60)
        print(f"📂 {category} 프롬프트")
        print("=" * 60)
        for idx, prompt in enumerate(filtered, start=1):
            print(f"{idx}. {prompt['title']} ({prompt['category']})")
        print("0. 돌아가기")
        print("q. 프로그램 종료")

        choice = safe_input("번호를 선택하세요 (0: 돌아가기): ").strip()

        if choice == "0":
            return

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(filtered):
                show_prompt_detail(filtered[index], prompts)
            else:
                print("⚠️ 올바른 번호를 입력하세요.")
        else:
            print("⚠️ 숫자를 입력하세요.")


def search_prompt_menu(prompts):
    keyword = safe_input_non_empty("검색어를 입력하세요: ").lower()

    results = []
    for prompt in prompts:
        if (
            keyword in prompt["title"].lower()
            or keyword in prompt["purpose"].lower()
            or keyword in prompt["content"].lower()
            or keyword in prompt["example"].lower()
        ):
            results.append(prompt)

    if not results:
        print("검색 결과가 없습니다.")
        return

    while True:
        print("=" * 60)
        print("🔍 검색 결과")
        print("=" * 60)
        for idx, prompt in enumerate(results, start=1):
            print(f"{idx}. {prompt['title']} ({prompt['category']})")
        print("0. 돌아가기")
        print("q. 프로그램 종료")

        choice = safe_input("번호를 선택하세요 (0: 돌아가기): ").strip()

        if choice == "0":
            return

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(results):
                show_prompt_detail(results[index], prompts)
            else:
                print("⚠️ 올바른 번호를 입력하세요.")
        else:
            print("⚠️ 숫자를 입력하세요.")     

def add_prompt(prompts):
    print("=" * 50)
    print("➕ 새 프롬프트 추가")
    print("=" * 50)

    category = choose_category()
    if category is None:
        return

    new_prompt = {
        "id": get_next_prompt_id(prompts, category),
        "category": category,
        "title": safe_input_non_empty("제목: "),
        "purpose": safe_input_non_empty("목적: "),
        "content": safe_input_multiline_non_empty("내용을 입력하세요."),
        "example": safe_input_non_empty("활용 예시: "),
        "favorite": False
    }

    prompts.append(new_prompt)
    save_prompts(prompts)
    print("✅ 프롬프트가 추가되었습니다.")


def edit_prompt(prompts):
    prompt_id = safe_input_non_empty("수정할 프롬프트 ID를 입력하세요: ")
    prompt = find_prompt_by_id(prompts, prompt_id)

    if not prompt:
        print("⚠️ 해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    print("=" * 60)
    print("✏️ 프롬프트 수정")
    print("=" * 60)
    print("Enter만 누르면 기존 값을 유지합니다.")

    new_title = safe_input(f"제목 [{prompt['title']}]: ").strip()
    if new_title:
        prompt["title"] = new_title

    new_purpose = safe_input(f"목적 [{prompt['purpose']}]: ").strip()
    if new_purpose:
        prompt["purpose"] = new_purpose

    print("현재 내용:")
    print(prompt["content"])
    change_content = safe_input("내용을 수정하시겠습니까? (y/n): ").strip().lower()
    if change_content == "y":
        new_content = safe_input_multiline_non_empty("새 내용을 입력하세요.")
        prompt["content"] = new_content

    new_example = safe_input(f"활용 예시 [{prompt['example']}]: ").strip()
    if new_example:
        prompt["example"] = new_example

    change_category = safe_input("카테고리를 변경하시겠습니까? (y/n): ").strip().lower()
    if change_category == "y":
        category = choose_category()
        if category is not None and category != prompt["category"]:
            prompt["category"] = category
            prompt["id"] = get_next_prompt_id(prompts, category)

    save_prompts(prompts)
    print("✅ 프롬프트가 수정되었습니다.")


def delete_prompt(prompts):
    prompt_id = safe_input_non_empty("삭제할 프롬프트 ID를 입력하세요: ")
    prompt = find_prompt_by_id(prompts, prompt_id)

    if not prompt:
        print("⚠️ 해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    print("=" * 60)
    print("🗑️ 삭제할 프롬프트")
    print("=" * 60)
    print(f"ID: {prompt['id']}")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")

    confirm = safe_input("정말 삭제하시겠습니까? (y/n): ").strip().lower()
    if confirm == "y":
        prompts.remove(prompt)
        save_prompts(prompts)
        print("✅ 프롬프트가 삭제되었습니다.")
    else:
        print("삭제가 취소되었습니다.")


def show_favorites(prompts):
    favorites = [p for p in prompts if p["favorite"]]

    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    while True:
        print("=" * 60)
        print("⭐ 즐겨찾기 목록")
        print("=" * 60)
        for idx, prompt in enumerate(favorites, start=1):
            print(f"{idx}. {prompt['title']} ({prompt['category']})")
        print("0. 돌아가기")
        print("q. 프로그램 종료")

        choice = safe_input("번호를 선택하세요 (0: 돌아가기): ").strip()

        if choice == "0":
            return

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(favorites):
                show_prompt_detail(favorites[index], prompts)
                favorites = [p for p in prompts if p["favorite"]]
                if not favorites:
                    print("즐겨찾기한 프롬프트가 없습니다.")
                    return
            else:
                print("⚠️ 올바른 번호를 입력하세요.")
        else:
            print("⚠️ 숫자를 입력하세요.")


def show_all_prompts(prompts):
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    while True:
        print("=" * 60)
        print("📋 전체 프롬프트 목록")
        print("=" * 60)
        for idx, prompt in enumerate(prompts, start=1):
            favorite_mark = "⭐" if prompt["favorite"] else ""
            print(f"{idx}. [{prompt['id']}] {prompt['title']} ({prompt['category']}) {favorite_mark}")
        print("0. 돌아가기")
        print("q. 프로그램 종료")

        choice = safe_input("번호를 선택하세요 (0: 돌아가기): ").strip()

        if choice == "0":
            return

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(prompts):
                show_prompt_detail(prompts[index], prompts)
            else:
                print("⚠️ 올바른 번호를 입력하세요.")
        else:
            print("⚠️ 숫자를 입력하세요.")


def main_menu():
    prompts = initialize_prompts()

    while True:
        print("\n" + "=" * 60)
        print("🧠 프롬프트 관리 프로그램")
        print("=" * 60)
        print("1. 전체 프롬프트 조회")
        print("2. 카테고리별 조회")
        print("3. 프롬프트 검색")
        print("4. 새 프롬프트 추가")
        print("5. 프롬프트 수정")
        print("6. 프롬프트 삭제")
        print("7. 즐겨찾기 목록")
        print("q. 종료")

        choice = safe_input("메뉴 선택: ").strip()

        if choice == "1":
            show_all_prompts(prompts)
        elif choice == "2":
            browse_by_category(prompts)
        elif choice == "3":
            search_prompt_menu(prompts)
        elif choice == "4":
            add_prompt(prompts)
        elif choice == "5":
            edit_prompt(prompts)
        elif choice == "6":
            delete_prompt(prompts)
        elif choice == "7":
            show_favorites(prompts)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("⚠️ 올바른 번호를 입력하세요.")


if __name__ == "__main__":
    main_menu()               