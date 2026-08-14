import json
from prompts import save_prompt, load_prompts, get_prompts_by_category

print("=== 프롬프트 저장 테스트 ===")
save_prompt("AI", "프롬프트 작성법", "좋은 프롬프트를 작성하는 방법")
save_prompt("Python", "리스트 사용법", "Python 리스트의 기본 사용법")

print("\n=== 모든 프롬프트 조회 ===")
all_prompts = load_prompts()
print(f"총 {len(all_prompts['prompts'])}개의 프롬프트")

print("\n=== AI 카테고리만 조회 ===")
ai_prompts = get_prompts_by_category("AI")
for prompt in ai_prompts:
    print(f"- {prompt['title']}")

print("\n=== Python 카테고리만 조회 ===")
python_prompts = get_prompts_by_category("Python")
for prompt in python_prompts:
    print(f"- {prompt['title']}")