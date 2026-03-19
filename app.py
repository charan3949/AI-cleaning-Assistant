from openai import OpenAI

client = OpenAI(api_key="sk-REAL_KEY")

def handle_issue(user_input):
    prompt = f"""
You are an operations assistant for a building services company.

Analyze the issue below and return:
1. Issue Category
2. Priority (Low, Medium, High)
3. Suggested Action
4. Short professional response for manager/team

Issue: {user_input}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You help service operations teams classify and prioritize issues."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

print("AI Cleaning Operations Assistant")
issue = input("Enter issue: ")

result = handle_issue(issue)

print("\n--- AI Analysis ---")
print(result)