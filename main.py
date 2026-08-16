import json
import os

FILE_NAME = "prompts.json"

CATEGORIES = {
    "1": "학습/교육",
    "2": "비즈니스 디자인"
}

INITIAL_PROMPTS = [
    {
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
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        save_prompts(INITIAL_PROMPTS)
        return

    try:
        data = load_prompts()
        if not is_valid_prompt_data(data):
            save_prompts(INITIAL_PROMPTS)
    except (json.JSONDecodeError, FileNotFoundError):
        save_prompts(INITIAL_PROMPTS)


def print_line():
    print("=" * 60)


def pause():
    input("\n엔터를 누르면 계속합니다...")


def input_nonempty(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("❌ 빈 입력은 사용할 수 없습니다.")


def generate_new_id(prompts, category_name):
    category_prefix = "1" if category_name == "학습/교육" else "2"
    numbers = []

    for prompt in prompts:
        prompt_id = prompt["id"]
        if prompt_id.startswith(category_prefix + "-"):
            try:
                numbers.append(int(prompt_id.split("-")[1]))
            except ValueError:
                pass

    next_number = max(numbers) + 1 if numbers else 1
    return f"{category_prefix}-{next_number}"


def show_prompt_list(prompt_list):
    if not prompt_list:
        print("저장된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompt_list, start=1):
        star = "⭐ " if prompt["favorite"] else ""
        print(f"{index}. {star}{prompt['title']} ({prompt['category']})")


def show_prompt_detail(prompt):
    print_line()
    print("📌 프롬프트 상세 정보")
    print_line()
    print(f"ID: {prompt['id']}")
    print(f"카테고리: {prompt['category']}")
    print(f"제목: {prompt['title']}")
    print(f"목적: {prompt['purpose']}")
    print(f"내용:\n{prompt['content']}")
    print(f"활용 예시: {prompt['example']}")
    print(f"즐겨찾기: {'예' if prompt['favorite'] else '아니오'}")
    print_line()


def select_prompt_from_list(prompt_list, message="번호를 선택하세요 (0: 돌아가기): "):
    if not prompt_list:
        return None

    while True:
        choice = input(message).strip()

        if choice == "0":
            return None

        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(prompt_list):
                return prompt_list[choice_num - 1]

        print("❌ 올바른 번호를 입력하세요.")


def toggle_favorite(prompt):
    prompt["favorite"] = not prompt["favorite"]
    return prompt["favorite"]


def prompt_detail_menu(prompts, prompt):
    while True:
        show_prompt_detail(prompt)
        print("1. 즐겨찾기 추가/제거")
        print("0. 돌아가기")

        choice = input("선택: ").strip()

        if choice == "1":
            is_favorite = toggle_favorite(prompt)
            save_prompts(prompts)
            if is_favorite:
                print("✅ 즐겨찾기에 추가되었습니다.")
            else:
                print("✅ 즐겨찾기에서 제거되었습니다.")
            pause()
        elif choice == "0":
            break
        else:
            print("❌ 잘못된 선택입니다.")


def browse_by_category(prompts):
    while True:
        print_line()
        print("📚 카테고리 선택")
        print_line()
        print("1. 학습/교육")
        print("2. 비즈니스 디자인")
        print("0. 돌아가기")

        category_choice = input("선택: ").strip()

        if category_choice == "0":
            break

        if category_choice not in CATEGORIES:
            print("❌ 잘못된 선택입니다.")
            continue

        selected_category = CATEGORIES[category_choice]
        filtered = [p for p in prompts if p["category"] == selected_category]

        print_line()
        print(f"📂 {selected_category} 프롬프트")
        print_line()

        if not filtered:
            print("해당 카테고리에 프롬프트가 없습니다.")
            pause()
            continue

        show_prompt_list(filtered)
        selected_prompt = select_prompt_from_list(filtered)

        if selected_prompt:
            prompt_detail_menu(prompts, selected_prompt)


def search_prompt_menu(prompts):
    while True:
        print_line()
        print("🔍 프롬프트 검색")
        print_line()

        keyword = input("검색어 입력 (0: 돌아가기): ").strip()

        if keyword == "0":
            break

        if not keyword:
            print("❌ 검색어를 입력하세요.")
            continue

        keyword_lower = keyword.lower()
        results = []

        for prompt in prompts:
            search_text = (
                prompt["title"] + " " +
                prompt["purpose"] + " " +
                prompt["content"] + " " +
                prompt["example"]
            ).lower()

            if keyword_lower in search_text:
                results.append(prompt)

        if not results:
            print("검색 결과가 없습니다.")
            pause()
            continue

        print_line()
        print(f"🔎 검색 결과: {len(results)}개")
        print_line()
        show_prompt_list(results)

        selected_prompt = select_prompt_from_list(results)
        if selected_prompt:
            prompt_detail_menu(prompts, selected_prompt)


def add_prompt_menu(prompts):
    print_line()
    print("➕ 프롬프트 추가")
    print_line()
    print("1. 학습/교육")
    print("2. 비즈니스 디자인")
    print("0. 돌아가기")

    category_choice = input("카테고리 선택: ").strip()

    if category_choice == "0":
        return

    if category_choice not in CATEGORIES:
        print("❌ 잘못된 카테고리 선택입니다.")
        pause()
        return

    category_name = CATEGORIES[category_choice]
    title = input_nonempty("제목: ")
    purpose = input_nonempty("목적: ")
    content = input_nonempty("내용: ")
    example = input_nonempty("활용 예시: ")

    new_prompt = {
        "id": generate_new_id(prompts, category_name),
        "category": category_name,
        "title": title,
        "purpose": purpose,
        "content": content,
        "example": example,
        "favorite": False
    }

    prompts.append(new_prompt)
    save_prompts(prompts)
    print("✅ 프롬프트가 추가되었습니다.")
    pause()

def update_prompt_menu(prompts):
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        pause()
        return

    print_line()
    print("✏️ 프롬프트 수정")
    print_line()
    show_prompt_list(prompts)

    selected_prompt = select_prompt_from_list(prompts)
    if not selected_prompt:
        return

    print("수정하지 않으려면 엔터를 누르세요.")

    new_title = input(f"제목 [{selected_prompt['title']}]: ").strip()
    new_purpose = input(f"목적 [{selected_prompt['purpose']}]: ").strip()
    new_content = input(f"내용 [{selected_prompt['content']}]: ").strip()
    new_example = input(f"활용 예시 [{selected_prompt['example']}]: ").strip()

    if new_title:
        selected_prompt["title"] = new_title
    if new_purpose:
        selected_prompt["purpose"] = new_purpose
    if new_content:
        selected_prompt["content"] = new_content
    if new_example:
        selected_prompt["example"] = new_example

    save_prompts(prompts)
    print("✅ 프롬프트가 수정되었습니다.")
    pause()


def delete_prompt_menu(prompts):
    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        pause()
        return

    print_line()
    print("🗑️ 프롬프트 삭제")
    print_line()
    show_prompt_list(prompts)

    selected_prompt = select_prompt_from_list(prompts)
    if not selected_prompt:
        return

    show_prompt_detail(selected_prompt)
    confirm = input("정말 삭제하시겠습니까? (y/n): ").strip().lower()

    if confirm == "y":
        prompts.remove(selected_prompt)
        save_prompts(prompts)
        print("✅ 프롬프트가 삭제되었습니다.")
    else:
        print("삭제가 취소되었습니다.")
    pause()


def show_favorite_prompts_menu(prompts):
    favorites = [prompt for prompt in prompts if prompt["favorite"]]

    print_line()
    print("⭐ 즐겨찾기 프롬프트")
    print_line()

    if not favorites:
        print("즐겨찾기된 프롬프트가 없습니다.")
        pause()
        return

    show_prompt_list(favorites)
    selected_prompt = select_prompt_from_list(favorites)

    if selected_prompt:
        prompt_detail_menu(prompts, selected_prompt)


def main():
    initialize_prompts()
    prompts = load_prompts()

    while True:
        print("\n")
        print_line()
        print("🎯 프롬프트 관리 프로그램")
        print_line()
        print("1. 프롬프트 조회")
        print("2. 프롬프트 검색")
        print("3. 프롬프트 추가")
        print("4. 프롬프트 수정")
        print("5. 프롬프트 삭제")
        print("6. 즐겨찾기 보기")
        print("0. 종료")
        print_line()

        choice = input("선택: ").strip()

        if choice == "1":
            browse_by_category(prompts)
        elif choice == "2":
            search_prompt_menu(prompts)
        elif choice == "3":
            add_prompt_menu(prompts)
        elif choice == "4":
            update_prompt_menu(prompts)
        elif choice == "5":
            delete_prompt_menu(prompts)
        elif choice == "6":
            show_favorite_prompts_menu(prompts)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("❌ 잘못된 선택입니다.")
            pause()


if __name__ == "__main__":
    main() 