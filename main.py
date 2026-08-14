from prompts import (
    add_prompt,
    get_all_prompts,
    get_prompts_by_category,
    get_prompt_by_id,
    search_prompts,
)


def view_all_prompts():
    """모든 프롬프트 조회"""
    prompts = get_all_prompts()
    if not prompts:
        print("\n저장된 프롬프트가 없습니다.\n")
        return

    print("\n" + "=" * 50)
    print("📚 전체 프롬프트")
    print("=" * 50)
    for prompt in prompts:
        print(f"\n[ID: {prompt['id']}] {prompt['title']}")
        print(f"카테고리: {prompt['category']}")
        print(f"내용: {prompt['content'][:50]}...")
    print("\n" + "=" * 50 + "\n")


def view_prompts_by_category():
    """카테고리별 프롬프트 조회"""
    category = input("조회할 카테고리를 입력하세요: ").strip()
    prompts = get_prompts_by_category(category)

    if not prompts:
        print(f"\n'{category}' 카테고리에 프롬프트가 없습니다.\n")
        return

    print("\n" + "=" * 50)
    print(f"📚 {category} 카테고리 프롬프트")
    print("=" * 50)
    for prompt in prompts:
        print(f"\n[ID: {prompt['id']}] {prompt['title']}")
        print(f"내용: {prompt['content'][:50]}...")
    print("\n" + "=" * 50 + "\n")


def view_prompt_detail():
    """프롬프트 상세 조회"""
    view_all_prompts()
    try:
        prompt_id = int(input("조회할 프롬프트 ID를 입력하세요: "))
        prompt = get_prompt_by_id(prompt_id)

        if not prompt:
            print("\n해당 ID의 프롬프트가 없습니다.\n")
            return

        print("\n" + "=" * 50)
        print("📖 프롬프트 상세 정보")
        print("=" * 50)
        print(f"ID: {prompt['id']}")
        print(f"제목: {prompt['title']}")
        print(f"카테고리: {prompt['category']}")
        print(f"내용:\n{prompt['content']}")
        print("=" * 50 + "\n")
    except ValueError:
        print("\n숫자를 입력해주세요.\n")


def search_prompt():
    """프롬프트 검색"""
    keyword = input("검색 키워드를 입력하세요: ").strip()
    results = search_prompts(keyword)

    if not results:
        print(f"\n'{keyword}'에 해당하는 프롬프트가 없습니다.\n")
        return

    print("\n" + "=" * 50)
    print(f"🔍 '{keyword}' 검색 결과")
    print("=" * 50)
    for prompt in results:
        print(f"\n[ID: {prompt['id']}] {prompt['title']}")
        print(f"카테고리: {prompt['category']}")
        print(f"내용: {prompt['content'][:50]}...")
    print("\n" + "=" * 50 + "\n")


def view_menu():
    """조회 메뉴"""
    while True:
        print("=" * 50)
        print("📖 프롬프트 조회")
        print("=" * 50)
        print("1. 전체 프롬프트 조회")
        print("2. 카테고리별 프롬프트 조회")
        print("3. 프롬프트 상세 조회")
        print("0. 돌아가기")
        print("=" * 50)

        choice = input("선택: ").strip()

        if choice == "1":
            view_all_prompts()
        elif choice == "2":
            view_prompts_by_category()
        elif choice == "3":
            view_prompt_detail()
        elif choice == "4":
            search_prompt()
        elif choice == "0":
            break
        else:
            print("\n잘못된 선택입니다.\n")


def main_menu():
    """메인 메뉴"""
    while True:
        print("=" * 50)
        print("🎯 프롬프트 관리 프로그램")
        print("=" * 50)
        print("1. 프롬프트 저장")
        print("2. 프롬프트 조회")
        print("0. 종료")
        print("=" * 50)

        choice = input("선택: ").strip()

        if choice == "1":
            category = input("카테고리: ").strip()
            title = input("제목: ").strip()
            content = input("내용: ").strip()
            add_prompt(category, title, content)
            print("\n✅ 프롬프트가 저장되었습니다.\n")
        elif choice == "2":
            view_menu()
        elif choice == "0":
            print("\n👋 프로그램을 종료합니다.\n")
            break
        else:
            print("\n잘못된 선택입니다.\n")


if __name__ == "__main__":
    main_menu()
