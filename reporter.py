import json

from config import MODEL
from llm import client


SYSTEM_PROMPT = """
你是一名 Research Reporter。

根据用户问题、研究计划和各任务的研究结果，
生成最终答案。

要求：

1. 回答用户真正的问题。
2. 综合所有研究结果，而不是简单拼接。
3. 信息不足时明确说明。
4. 如果研究结果中包含来源链接，尽量保留。
5. 结构清晰。
6. 不要编造研究结果中没有的信息。
"""


def write_report(
    question: str,
    plan: dict,
    results: list,
) -> str:

    context = json.dumps(
        {
            "question": question,
            "plan": plan,
            "results": results,
        },
        ensure_ascii=False,
        indent=2,
    )

    response = (
        client.chat.completions.create(
            model=MODEL,

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": context,
                },
            ],

            extra_body={
                "thinking": {
                    "type": "disabled"
                }
            },
        )
    )

    return (
        response
        .choices[0]
        .message
        .content
        or "无法生成报告"
    )