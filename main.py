# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import re


operators_open_print = {
        '|':    "<or>\n",
        '&':    "<and>\n",
        '!':    "<not>\n",
        '(':    "",
        ')':    "",
}

operators_closed_print = {
        '|':    "</or>\n",
        '&':    "</and>\n",
        '!':    "</not>\n",

}

operator_values = {
        '|':    2,
        '&':    2,
        '!':    1,
        '(':    0,
        ')':    0,
        '':    0
}


if True:
    #inputName = input('Unesite ime fajla: ')
    inputName="input.txt"
    print(49, inputName)
    #if inputName == ':q':
    #    break
    inputFile = open(inputName, 'r')
    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    lines.sort(reverse=False, key=len)
    for line in lines:

        unclosed = 0
        error = ""
        result = "Valid"
        print(lines.index(line),')')
        print(line)
        for char in line:
            if char in operator_values:
                #if operators_open_print[char]:
                #    print("Operator: "+operators_open_print[char].strip())
                #else:
                #    print(char)
                if char == '(':
                    unclosed += 1
                elif char == ")":
                    unclosed -= 1
            #elif re.search('[A-Z]', char):
            #    print("Operand: "+char)
        if(unclosed):
            error = ('Parentheses not paired: ' + str(unclosed))
        if not error:
            tmp_line = line
            while len(tmp_line) > 1:
                first_par = 0
                last_par = len(tmp_line)
                operator_sum = 0
                for i in range(0, len(tmp_line)):
                    if tmp_line[i] == '(':
                        first_par = i
                        last_par = i
                        operator_sum = 0
                    elif tmp_line[i] in operator_values:
                        operator_sum += operator_values[tmp_line[i]]
                    if tmp_line[i] == ')' and last_par == first_par:
                        last_par = i
                        if operator_sum > 2:
                            error = 'Invalid expression'
                            break
                        tmp_line = tmp_line[0:first_par]+tmp_line[last_par+1:len(tmp_line)]
                        break
                    if i == len(tmp_line)-1 and first_par==0:
                        if operator_sum > 2:
                            error = "Invalid expression"
                        tmp_line = tmp_line[0:0]
                        print('\n')
                if error:
                    break


        if error == "":
            result_stack = []
            operators_stack = []
            for element in line:
                if re.search('[A-Z]', element):
                    result_stack.append("<operand>"+element+"</operand>")
                elif element in operator_values:
                    if operator_values[element]:
                        operators_stack.append(element)
                    elif element == ')' or line.index(element)==len(line)-1:
                        tmp_operator = operators_stack.pop()
                        if operator_values[tmp_operator] == 1:
                            result = operators_open_print[tmp_operator] + result_stack.pop() + operators_closed_print[tmp_operator]
                            result_stack.append(result)
                        elif operator_values[tmp_operator] == 2:
                            result = operators_open_print[tmp_operator] + result_stack.pop() + result_stack.pop() + operators_closed_print[tmp_operator]
                            result_stack.append(result)

        if error:
            result = error
        write_file = open('output-'+str(lines.index(line)), "w")
        write_file.write(result)
        write_file.close()
        print('Result:\n' + result)
        print('\n')

