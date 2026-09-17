from planner import create_plan
from executor import execute_task
from reporter import write_report
from reviewer import review_task
from config import (
    MAX_RETRIES_PER_TASK
)
def run_research_agent(
    question: str,
):

    # =========================
    # 1. Planning
    # =========================

    print(
        "\n========== Planning =========="
    )

    plan = create_plan(
        question
    )

    print(
        f"\n目标：{plan['goal']}"
    )

    for task in plan["tasks"]:

        print(
            f"{task['id']}. "
            f"{task['description']}"
        )

    # =========================
    # 2. Execution
    # =========================

    results = []

    for task in plan["tasks"]:

        print(
            f"\n========== Task "
            f"{task['id']} =========="
        )

        print(
            task["description"]
        )

        feedback = None
        review = None
        result = ""

        # 第一次执行 + 允许的重试次数
        for attempt in range(
                MAX_RETRIES_PER_TASK + 1
        ):

            if attempt > 0:
                print(
                    f"\n--- Retry {attempt} ---"
                )

            # =========================
            # Executor
            # =========================

            result = execute_task(
                question=question,
                task=task,
                previous_results=results,
                feedback=feedback,
            )

            print(
                "\nTask Result:"
            )

            print(
                result
            )

            # =========================
            # Reviewer
            # =========================

            print(
                "\nReviewing..."
            )

            review = review_task(
                question=question,
                task=task,
                result=result,
            )

            print(
                f"Passed: "
                f"{review['passed']}"
            )

            print(
                f"Reason: "
                f"{review['reason']}"
            )

            # 合格
            if review["passed"]:
                break

            # 不合格
            feedback = review.get(
                "feedback",
                "请提高研究质量。",
            )

        # =========================
        # 保存最终结果
        # =========================

        results.append(
            {
                "id": task["id"],

                "task": task[
                    "description"
                ],

                "result": result,

                "review": review,
            }
        )
    # =========================
    # 3. Reporting
    # =========================

    print(
        "\n========== Reporting =========="
    )

    answer = write_report(
        question=question,
        plan=plan,
        results=results,
    )

    return answer