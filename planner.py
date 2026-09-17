import json
from config import MODEL,MAX_TASKS
from llm import client
SYSTEM_PROMPT=f"""
你是一个Research Planner。

你的任务不是直接回答客户。
而是把用户的问题拆成清晰的研究任务。

规则：
1.只负责制定计划，不执行任务。
2.简单问题不要过度拆分。
3.复杂研究问题拆成 2~{MAX_TASKS}个任务
4.每个任务必须具体，可以独立执行。
5.按合理顺序排序任务。
6.必须输出JSON。

JSON 格式：
{{
    "goal":"用户最终目标",
    "tasks":[
        {{
            "id":1,
            "description":"任务描述"
        }},
        {{
            "id":2,
            "description":"任务描述"
        }},
    ]
}}

"""
def create_plan(question:str,)->dict:
    response = (
        client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role":"system",
                    "content":SYSTEM_PROMPT
                },
                {
                    "role":"user",
                    "content":question,
                },
            ],
            response_format={
                "type":"json_object"
            },
            extra_body={
                "thinking":{
                    "type":"disabled"
                }
            },
        )

    )

    content = (
        response.choices[0].message.content
    )
    if not content:
        raise RuntimeError(
            "Planner 没有返回内容"
        )

    plan = json.loads(content)
    tasks = plan.get(
        "tasks",
        []
    )

    if not tasks:
        raise RuntimeError(
            "Planner 没有生成任务"
        )

        # 防止模型生成过多任务
    plan["tasks"] = tasks[:MAX_TASKS]

    return plan

