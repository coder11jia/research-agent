import json
from llm import client
from config import MODEL

SYSTEM_PROMPT="""
你是一名 Research Reviewer。
你的职责是检查一个研究任务的执行结果是否合格。

你需要判断：
1.是否真正完成了当前任务。
2.信息是否足够回答任务。
3.是否明显偏题。
4.是否明显遗漏。
5.如果涉及事实研究，结果是否提供了有价值的信息

不要重新执行任务。
不要自己搜索。
只负责评价结果。
必须输出JSON:
{
    "passed":true,
    "reason":"评价原因",
    "feedback":"如果不合格,告诉Executor应该如何改造"
}

"""
def review_task(
        question:str,
        task:dict,
        result:str,
)->dict:
    user_prompt = f"""
用户原始问题：

{question}

当前研究任务：

{task["description"]}

Executor的执行结果：

{result}

请检查这个结果是否足以完成当前研究任务

"""
    response=(
        client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role":"system",
                    "content":user_prompt,
                },
                {
                    "role":"user",
                    "content":user_prompt,
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
            "Reviewer没有返回内容"
        )
    return json.loads(content)
