import re

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    top = ''
    bottom = ''
    separator = ''
    answers = ''

    for problem in problems:
        components = problem.split(' ')
        operation = components[1]
        spacing = max(len(components[0]), len(components[2])) + 2

        if len(components[0]) > 4 or len(components[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        if not re.match(r'[+-]', operation):
            return "Error: Operator must be '+' or '-'."
        
        if not ''.join(components[0] + components[2]).isnumeric():
            return "Error: Numbers must only contain digits."
        
        top += ' ' * (spacing - len(components[0])) + components[0] + '    '

        bottom += operation + ' ' * ((spacing - 1) - len(components[0])) + components[0] + '    '

        separator += '-' * spacing + '    '

        match operation:
            case '+':
                answer = str(int(components[0]) + int(components[2]))
                answers += ' ' * (spacing - len(answer)) + answer + '    '
            case _:
                answer = str(int(components[0]) - int(components[2]))
                answers += ' ' * (spacing - len(answer)) + answer + '    '
        
    result = top.rstrip(top[-4]) + '\n' + bottom.rstrip(bottom[-4]) + '\n' + separator.rstrip(separator[-4])

    if show_answers:
        result += '\n' + answers.rstrip(answers[-4])

    return result

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')