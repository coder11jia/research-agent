from agent import run_research_agent


def main():

    print("Research Agent 已启动")
    print("输入 exit 退出\n")

    while True:

        question = input("你：").strip()

        if question.lower() in {
            "exit",
            "quit",
        }:
            break

        if not question:
            continue

        try:

            answer = run_research_agent(
                question
            )

            print(
                f"\nAgent：\n{answer}\n"
            )

        except Exception as e:

            print(
                f"\n发生错误：{e}\n"
            )


if __name__ == "__main__":
    main()