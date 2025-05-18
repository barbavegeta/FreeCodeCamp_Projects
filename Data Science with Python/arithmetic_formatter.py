def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_row = ''
    bottom_row = ''
    lines = ''
    answers = ''

    for problem in problems:
        first = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second = problem.split(" ")[2]

        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.' # Works

        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.' # Works

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if operator == '+':
            result = str(int(first) + int(second))

        elif operator == '-':
            result = str(int(first) - int(second))

        length = max(len(first), len(second)) + 2
        top_row += first.rjust(length) + '    '
        bottom_row += operator + ' ' + second.rjust(length - 2) + '    '
        lines += '-' * length + '    '
        answers += result.rjust(length) + '    ' 

    arranged_problems = top_row.rstrip() + '\n' + bottom_row.rstrip() + '\n' + lines.rstrip()
    if show_answers:
        arranged_problems += '\n' + answers.rstrip()

    return arranged_problems
    #return string
    
test1 = arithmetic_arranger((["3801 - 2", "123 + 49"]))
test2 = arithmetic_arranger(["1 + 2", "1 - 9380"])
test3 = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
test4 = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
test5 =  arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
test6 = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
test7 = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
test8 = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
test9 = arithmetic_arranger(["3 + 855", "988 + 40"], True)
test10 = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)

print(f'\nTest 1\n\n{test1}') 
print(f'\nTest 2\n\n{test2}') 
print(f'\nTest 3\n\n{test3}') 
print(f'\nTest 4\n\n{test4}') 
print(f'\nTest 5\n\n{test5}') 
print(f'\nTest 6\n\n{test6}')  
print(f'\nTest 7\n\n{test7}') 
print(f'\nTest 8\n\n{test8}') 
print(f'\nTest 9\n\n{test9}') 
print(f'\nTest 10\n\n{test10}') 