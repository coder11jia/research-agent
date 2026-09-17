def calculator(
    a: float,
    b: float,
    operation: str,
):
    if operation == "add":
        return a + b

    if operation == "subtract":
        return a - b

    if operation == "multiply":
        return a * b

    if operation == "divide":

        if b == 0:
            raise ValueError(
                "除数不能为 0"
            )

        return a / b

    raise ValueError(
        f"不支持的运算: {operation}"
    )