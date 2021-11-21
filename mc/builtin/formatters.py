from typing import AnyStr


def usual_syntax(result: AnyStr) -> AnyStr:
    formatted_result = ""

    for i in range(len(result)):
        if i == 0:
            formatted_result += result[i].upper()

        elif i > 1:
            if result[i - 1] == " " and result[i - 2] in [".", "?", "!"]:
                formatted_result += result[i].upper()

            else:
                formatted_result += result[i]

        else:
            formatted_result += result[i]

    if formatted_result[-1] not in [".", "?", "!"]:
        formatted_result += "."

    return formatted_result
