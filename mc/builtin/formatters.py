def usual_syntax(phrase: str) -> str:
    """Formats phrase as usual sentence"""
    formatted = ""

    for i in range(len(phrase)):
        if i == 0:
            formatted += phrase[i].upper()

        elif i > 1:
            if phrase[i - 1] == " " and phrase[i - 2] in [".", "?", "!"]:
                formatted += phrase[i].upper()

            else:
                formatted += phrase[i]

        else:
            formatted += phrase[i]

    if formatted[-1] not in [".", "?", "!"]:
        formatted += "."

    return formatted
