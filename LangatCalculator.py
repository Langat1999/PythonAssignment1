def add(n1, n2): return n1 + n2
def subtract(n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2): return "⚠️ Error: Cannot divide by zero!" if n2 == 0 else n1 / n2

def calculate(n1, n2, op):
    if op in ["add", "+"]:
        return f"✅ {n1} + {n2} = {add(n1, n2)}"
    elif op in ["subtract", "-"]:
        return f"✅ {n1} - {n2} = {subtract(n1, n2)}"
    elif op in ["multiply", "*", "x"]:
        return f"✅ {n1} * {n2} = {multiply(n1, n2)}"
    elif op in ["divide", "/"]:
        return f"✅ {n1} / {n2} = {divide(n1, n2)}"
    else:
        return "🤔 Unknown operation. Try: add, subtract, multiply, divide or symbols like + - * /"

def calculator_bot():
    print("👋 Karibu! I'm your Langat-style calculator bot.")
    print("📌 Type 'exit' anytime to leave the chat.\n")

    while True:
        try:
            user_op = input("🔧 Operation (add, subtract, multiply, divide): ").lower()
            if user_op == "exit":
                print("👋 See you next time! Keep calculating. 💡")
                break
            
            num1 = float(input("🔢 First number: "))
            num2 = float(input("🔢 Second number: "))
            
            reply = calculate(num1, num2, user_op)
            print(f"\n📬 *RESULT:* {reply}\n")
        
        except ValueError:
            print("🚫 Invalid input. Tafadhali ingiza nambari halali.")

# Run the bot
calculator_bot()