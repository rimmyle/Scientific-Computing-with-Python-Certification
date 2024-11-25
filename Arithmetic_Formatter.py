import re

def calculate_spacing(component, max_space, char):
    space = ''
    for _ in range(max_space - len(component)):
        space += char
    return space + component



def arithmetic_arranger(problems, show_answers=False):
    print(len(problems))
    if len(problems) > 5:
        return 'Error: Too many problems.'
    top = ''
    bottom = ''
    separator = ''
    answers = ''
    for problem in problems:
        components = problem.split(' ')
        if len(components[0]) > 4 or len(components[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        operation = components[1]
        if not re.match(r'[+-]', operation):
            return "Error: Operator must be '+' or '-'."
        if not components[0].isnumeric() or not components[2].isnumeric():
            return "Error: Numbers must only contain digits."
        
        spacing = max(len(components[0]), len(components[2])) + 2

        top += calculate_spacing(components[0], spacing, ' ') + '    '

        bottom += operation + calculate_spacing(components[2], spacing - 1, ' ') + '    '

        separator += calculate_spacing('', spacing, '-') + '    '

        if operation == '+':
            answers += calculate_spacing(str(int(components[0]) + int(components[2])), spacing, ' ') + '    '
        else:
            answers += calculate_spacing(str(int(components[0]) - int(components[2])), spacing, ' ') + '    '

    result = top.rstrip(top[-4]) + '\n' + bottom.rstrip(bottom[-4]) + '\n' + separator.rstrip(separator[-4])

    if show_answers:
        result += '\n' + answers.rstrip(answers[-4])

    return result

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')