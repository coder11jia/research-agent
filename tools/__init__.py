from tools.registry import ToolRegistry
from tools.calculator import calculator
from tools.search import search_web
from tools.webpage import read_webpage

registry = ToolRegistry()


registry.register(
    name="calculator",

    func=calculator,

    description=(
        "用于两个数字之间的数学运算"
    ),

    parameters={
        "type": "object",

        "properties": {
            "a": {
                "type": "number"
            },

            "b": {
                "type": "number"
            },

            "operation": {
                "type": "string",

                "enum": [
                    "add",
                    "subtract",
                    "multiply",
                    "divide",
                ],
            },
        },

        "required": [
            "a",
            "b",
            "operation",
        ],
    },
)


registry.register(
    name="search_web",

    func=search_web,

    description=(
        "搜索互联网获取最新信息。"
        "当用户的问题需要实时信息、"
        "最新资料或未知事实时使用。"
    ),

    parameters={
        "type": "object",

        "properties": {
            "query": {
                "type": "string",

                "description": (
                    "适合搜索引擎的查询关键词"
                ),
            },
        },

        "required": [
            "query"
        ],
    },
)

registry.register(
    name="read_webpage",

    func=read_webpage,

    description=(
        "读取指定网页的正文内容。"
        "通常先使用 search_web搜索。"
        "再使用本工具读取有价值的网页。"
    ),

    parameters={
        "type":"object",
        "properties":{
            "url":{
                "type":"string",
                "desceiption":(
                    "需要读取的网页URL"
                ),
            },
        },

        "required":[
            "url"
        ],
    },
)