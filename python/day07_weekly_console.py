def clean_text(text, case_type = "title"):
    text1 = text.strip()
    if case_type == "title":
        text1 = text1.capitalize()
    elif case_type == "lower":
        text1 = text1.lower()
    elif case_type == "upper":
        text1 = text1.upper()
    else:
        raise ValueError("不支持该大小写格式")
    return text1
def sum_multiples(limit, divisor = 3):
    m = 0
    if divisor <= 0:
        raise ValueError("除数不能小于等于0")
        
    elif limit >= 1 :
    
        for i in range (1,limit+1):
            if i % divisor == 0:
                m += i
    return m

def evaluate_score(score):
    if 0 <= score <= 100:
        if score >= 90:
            level = "A"
        elif score >= 80:
            level = "B"
        elif score >= 60:
            level = "C"
        else:
            level = "F"
        return level
    else:
        raise ValueError("成绩不合理")
def main():
    while True:
        # 1. 打印完整菜单
        print("=== Python 第一周能力测试终端 ===\n1. 规范化用户名\n2. 计算区间倍数总和\n3. 成绩评估诊断\n4. 退出系统")
        choice = input("what's your choice " )

        # 3. 使用 if / elif / else 判断选项
        if choice == "1":
            name = input("what's your name? ")
            title = input('which title you choose? you can choose one of the "title" "lower" "upper"')
            name = clean_text(name, case_type = title)
            print(f"处理后的名字是{name}")
            
        elif choice == "2":
            limit = int(input("what's limit "))
            x = int(input("what's divisor "))
            total = sum_multiples(limit, divisor = x)
            print(f"total = {total}")
        elif choice == "3":
            score = int(input("what's your score "))
            level = evaluate_score(score)
            print(f"your score is {score} and your level is {level}")
        elif choice == "4":
            # 打印欢送语
            print("欢迎下次再来")
            # 退出循环
            break
        else:
            print("无效输入，请重新选择")
            
if __name__ == "__main__":
    main()           
    