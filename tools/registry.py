

class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self,name:str,func,description: str,parameters: dict):
        self.tools[name]={
            "func":func,
            "description":description,
            "parameters":parameters,

        }

    def execute(self,name:str,arguments:dict):
        tool = self.tools.get(name)
        if tool is None:
            raise ValueError(
                f"未知工具：{name}"
            )
        return tool["func"](**arguments)

    def get_schemas(self):
        schemas=[]
        for name,tool in self.tools.items():
            schemas.append(
                {
                    "type":"function",
                    "function":{
                        "name":name,
                        "description":tool[
                            "description"
                        ],
                        "parameters":tool[
                            "parameters"
                        ],
                    },
                },
            )
        return schemas
