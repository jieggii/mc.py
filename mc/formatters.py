def default(_):
    """
    A stub when there is no formatting needed.
    """
    return _


def usual_syntax(result: str) -> str:
    """
    Capitalizes the first word of every sentence
    and adds a dot if there is no symbol at the end.

    Example: "hello. test test" -> "Hello. Test test."

    :param result: Input string
    :return: Formatted string
    """
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


def uppercase(result: str) -> str:
    """
    Just makes everything upper.

    :param result: Input string
    :return: Formatted string
    """
    return result.upper()


print(usual_syntax("hello. test test"))
