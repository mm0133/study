class StackCalculaton:


    def __init__(self):
        self.top = -1
        self.stack = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%':2, '^': 3, '!':4, '√':5}
        self.result=0

    def is_empty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "stack is empty"

    def push(self, op):
        self.top += 1
        self.stack.append(op)


    def is_num(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def not_first(self, i):
        try:

            a = self.precedence[i]
            b = self.precedence[self.peek()]
            if a==3 and b==3:
                return False
            else:
                return True if a <= b else False
        except KeyError:
            return False



    def printprocess(self):
        print('Stack:', end='')
        print(self.stack)
        print('Postfix Array:', end='')
        print(self.output)


    def printCalporcess(self,i):
        print("  input: %4s   " % i, end='')
        print('Stack:', end='')
        print(ob.stack)



    def infixToPostfix(self, input_text):
        k=''
        count=0
        nega=1
        for i in input_text:

            count=count+1
            if  k != '' and not i.isdigit() and i!='.'  :
                self.output.append(k)
                print('\ninput: %4s   ' % k, end='')
                self.printprocess()
                k = ''
            if i=='-' and nega==1:
                k = k + i
            if i.isdigit()or i=='.':
                k = k+i
                if count==len(input_text):
                    self.output.append(k)
                    print('\ninput: %4s   ' % k, end='')
                    self.printprocess()

            elif i=='R':
                self.output.append(self.result)
                print('\ninput: %4s   '% str(i), end='')
                self.printprocess()


            elif i == '(':
                self.push(i)
                print('\ninput: %4s   ' %i, end='')
                self.printprocess()


            elif i == ')':
                while ((not self.is_empty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)

                if (not self.is_empty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
                print('\ninput: %4s   ' % i, end='')
                self.printprocess()


            elif nega!=1 or i!='-':
                while (not self.is_empty() and self.not_first(i)):

                    self.output.append(self.pop())
                print('\ninput: %4s   ' % i, end='')
                self.printprocess()
                self.push(i)

            if i== '(':
                nega=1
            else:
                nega=0



        while not self.is_empty():
            self.output.append(self.pop())
        print('\npop all op from stack,   ', end='')
        self.printprocess()

    def Calculate_Postfix(self):

        for i in self.output:
            if self.is_num(i):
                self.push(i)
                self.printCalporcess(i)


            elif i == '+':
                op2 = float(self.pop())
                op1 = float(self.pop())
                self.push((op1 + op2))
                self.printCalporcess(i)

            elif i == '-':
                op2 = float(self.pop())
                op1 = float(self.pop())
                self.push((op1 - op2))
                self.printCalporcess(i)

            elif i == '*':
                op2 = float(self.pop())
                op1 = float(self.pop())
                self.push((op1 * op2))
                self.printCalporcess(i)

            elif i == '/':
                op2 = float(self.pop())
                op1 = float(self.pop())
                self.push((op1 / op2))
                self.printCalporcess(i)

            elif i== '%':
                op2 = float(self.pop())
                op1 = float(self.pop())
                self.push((op1 % op2))
                self.printCalporcess(i)

            elif i == '^':
                op2 = float(self.pop())
                op1 = float(self.pop())
                self.push((op1 ** op2))
                self.printCalporcess(i)
            elif i== '√':
                op1=float(self.pop())
                self.push((op1 ** 0.5))
                self.printCalporcess(i)
            elif i=='!':
                op1=int(self.pop())
                op2=1
                for j in range(1,op1+1):
                    op2=op2*j
                self.push(op2)
                self.printCalporcess(i)




        self.result = float(self.pop())
        self.output = []
        return self.result



ob = StackCalculaton()
while(1):
    print("\n\n\nif you want to finish the process, Please enter \"finish\".")
    input_text = input("\nEnter infix expression:")

    if input_text == "finish":
        break

    ob.infixToPostfix(input_text)
    print("\nResult of Coversion Infix to Postfix: ", end='')
    for i in ob.output:
        print (str(i)+' ', end='')
    print("\n\n\n Calculation Using Stack")
    print("\nCalculation Result :%f" %ob.Calculate_Postfix())



