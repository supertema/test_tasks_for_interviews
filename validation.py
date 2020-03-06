# Проверить валидность расстановки скобочек в выражении.
# 
# Скобки могут быть всех трех видов - ()[]{}.
#
# На вход программа или функция должна принимать строку, а на выходе ответить правильно ли расставлены скобочки в ней.
#
# Те есть открывающиеся скобочки корректно закрываются скобочкой того же вида.
#
# Например:
#
# "([])" - true
# "{[(]}" - false


def validation(string):
    stack = []

    bracket = {
        ')':'(',
        ']': '[',
        '}': '{',
    }

    for s in string:
        if s in bracket.values():
            stack.append(s)
        else:
            if not stack:
                return False
            else:
                if stack[-1] == bracket.get(s):
                    stack.pop()
                else:
                    return False

    if stack:
        return False
    else:
        return True
