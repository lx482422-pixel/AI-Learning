def show_config(config_dict):
    if not config_dict:
        print("[提示] 暂无配置信息！")
    else:
        for k, v in config_dict.items():
            print(f"> {k}: {v}")

def main():
    config = {
    "model": "deepseek-chat",
    "temperature": "0.7",
    "max_tokens": "2048",
    "stream": "True"
    }
    while True:
        print("---简易控制台菜单---")
        print("1:查看当前所有配置 2:安全查询指定配置项 3: 修改/新增配置项 4: 退出系统")
        choice = input("what's your choice? ")
        if choice == "1":
            show_config(config)
        elif choice == "2":
            cx = input("输入要查询的配置键 ").strip()
            result = config.get(cx)
            if result is not None:
                print(f"{cx}: {result}")
            else:
                print("未找到该配置项，请检查拼写")
        elif choice == "3":
            key = input("请输入配置项名称 ").strip()
            value = input("请输入配置值 ").strip()
            if not key or not value:
                print("配置项或配置值不能为空")
            else:
                config[key] = value
                print("更新成功 ")
        elif choice == "4":
            print("欢迎下次再来")
            break
        else:
            print("输入无效，请在一到四之间重新选")
            
if __name__ == "__main__":
    main()           
        
        
        
          