print("Hello, Peter!")

# main.py

def show_main_menu():
    """메인 메뉴 표시"""
    print("\n" + "="*40)
    print("🤖 프롬프트 관리 프로그램")
    print("="*40)
    print("1. 학습/교육")
    print("2. 비즈니스디자인")
    print("0. 종료")
    print("="*40)
    choice = input("선택: ")
    return choice


def show_education_menu():
    """학습/교육 카테고리 메뉴"""
    print("\n" + "-"*40)
    print("📚 학습/교육")
    print("-"*40)
    print("1. 강의안 작성")
    print("2. 요약문 작성")
    print("3. 설명글 작성")
    print("4. 퀴즈 생성")
    print("0. 돌아가기")
    print("-"*40)
    choice = input("선택: ")
    return choice


def show_business_menu():
    """비즈니스디자인 카테고리 메뉴"""
    print("\n" + "-"*40)
    print("🎨 비즈니스디자인")
    print("-"*40)
    print("1. 슬라이드 디자인")
    print("2. 포스터 디자인")
    print("3. 명함 디자인")
    print("4. 로고 디자인")
    print("0. 돌아가기")
    print("-"*40)
    choice = input("선택: ")
    return choice

def handle_education(choice):
    """학습/교육 카테고리 처리"""
    
    if choice == "1":
        print("\n🎓 작업안 작성 프롬프트를 불러왔습니다.")
        name = input("프롬프트 이름: ")
        content = input("프롬프트 내용: ")
        print(f"'{name}' 프롬프트가 저장되었습니다!")
    
    elif choice == "2":
        print("\n🎓 요청문 작성 프롬프트를 불러왔습니다.")
    
    elif choice == "3":
        print("\n🎓 질문을 작성 프롬프트를 불러왔습니다.")
    
    elif choice == "4":
        print("\n🎓 귀조 생성 프롬프트를 불러왔습니다.")
    
    elif choice == "0":
        return False
    
    else:
        print("\n❌ 잘못된 선택입니다.")
    
    return True


def handle_business(choice):
    """비즈니스디자인 기능 처리"""
    if choice == "1":
        print("\n🎨 슬라이드 디자인 프롬프트를 불러왔습니다.")
    elif choice == "2":
        print("\n🎨 포스터 디자인 프롬프트를 불러왔습니다.")
    elif choice == "3":
        print("\n🎨 명함 디자인 프롬프트를 불러왔습니다.")
    elif choice == "4":
        print("\n🎨 로고 디자인 프롬프트를 불러왔습니다.")
    elif choice == "0":
        return False  # 돌아가기
    else:
        print("\n❌ 잘못된 선택입니다.")
    return True


def main():
    """메인 함수 - 프로그램 실행"""
    while True:
        choice = show_main_menu()
        
        if choice == "1":  # 학습/교육
            while True:
                sub_choice = show_education_menu()
                if not handle_education(sub_choice):
                    break
                    
        elif choice == "2":  # 비즈니스디자인
            while True:
                sub_choice = show_business_menu()
                if not handle_business(sub_choice):
                    break
                    
        elif choice == "0":  # 종료
            print("\n👋 프로그램을 종료합니다.")
            break
        else:
            print("\n❌ 잘못된 선택입니다.")


if __name__ == "__main__":
    main()

   