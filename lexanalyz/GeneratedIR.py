class GeneratedIR():
    reg = 1

    header_text = ""
    main_text = ""
    buffer = ""
    str_i = 0
    main_reg = 1
    br = 0
    stack_pop = True

    br_stack = []
    br_loop = []

    def String_generate(self):
        self.main_text += self.buffer
        self.formatMainText()
        text = ""
        text += "\n"
        text += self.header_text
        text += "define i32 @main() nounwind {\n"
        text += str(self.main_text)
        text += "  ret i32 0\n"
        text += "}\n"
        file = open("../lexanalyz/output.ll", 'w')
        if file:
            file.write(text)
        else:
            print("String_generate ERROR!")
        return text

    def function_start(self, id):
        self.main_text += self.buffer
        main_reg = self.reg
        self.buffer = "define main @ " + id + " () nounwind {\n"
        self.reg = 1

    def function_end(self):
        self.buffer += "ret void\n"
        self.formatself()
        self.buffer += "}\n\n"
        self.header_text += str(self.buffer)
        self.buffer = ""
        self.reg = self.main_reg

    def call(self, id):
        self.buffer += "call void @" + id + "()\n"

    def print(self, text):
        str_len = text.length()

        str_type = "[" + (str_len + 2) + " x i8]"
        self.header_text += "@str" + self.str_i + " = constant" + str_type + " c\"" + text + "\\0A\\00\"\n"
        self.buffer += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ( " + str_type + ", " + str_type + "* @str" + self.str_i + ", i32 0, i32 0))\n"
        self.str_i += 1
        self.reg += 1

    def printf_i32(self, id, globl):
        if globl:
            self.buffer += "%" + self.reg + " = load i32, i32* @" + id + "\n"
        else:
            self.buffer += "%" + self.reg + " = load i32, i32* %" + id + "\n"

        self.reg += 1
        self.buffer += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %" + (
                    self.reg - 1) + ")\n"
        self.reg += 1

    def printf_double(self, id, gloabal):
        if gloabal:
            self.buffer += "%" + self.reg + " = load double, double* @" + id + "\n"
        else:
            self.buffer += "%" + self.reg + " = load double, double* %" + id + "\n"

        self.reg += 1
        self.buffer += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %" + (
                    self.reg - 1) + ")\n"
        self.reg += 1

    def printf_string(self, id, length, globl, function):
        if globl:
            self.buffer += "%" + self.reg + " = getelementptr inbounds [" + (length + 1) + " x i8], [" + (
                        length + 1) + " x i8]* @" + id + ", i32 0, i32 0\n"
        else:
            self.buffer += "%" + self.reg + " = getelementptr inbounds [" + (length + 1) + " x i8], [" + (
                        length + 1) + " x i8]* @" + function + "." + id + ", i32 0, i32 0\n"

        self.reg += 1
        self.reg += 1

    # int to float
    def tr_int_to_float(self, _reg):
        self.buffer += "%" + self.reg + " = sitofp i64 %" + _reg + " to double\n"
        self.reg += 1
        return self.reg - 1

    def declare_i32(self, id, globl, value):
        if globl:
            self.header_text += "@" + id + " = global i32 0\n"
        else:
            self.buffer += "%" + id + " = alloca i32\n"

    def declare_double(self, id, globl, value):
        if globl:
            self.header_text += "@" + id + " = global double 0.0\n"
        else:
            self.buffer += "%" + id + " = alloca double\n"

    # assign
    def assign_i32(self, id, globalNames, value):
        if globalNames:
            self.buffer += "store i32 " + value + ", i32* @" + id + "\n"
        else:
            self.buffer += "store i32 " + value + ", i32* %" + id + "\n"

    def assign_double(self, id, globalNames, value):
        if globalNames:
            self.buffer += "store double " + value + ", double* @" + id + "\n"
        else:
            self.buffer += "store double " + value + ", double* %" + id + "\n"

    def assign_string(self, id, text, globl, function):
        len = text.length() + 1
        str_type = "[" + len + " x i8]"
        if globl:
            self.header_text += "@" + id + " = constant" + str_type + " c\"" + text + "\\00\"\n"
        else:
            self.header_text += "@" + function + "." + id + " = constant" + str_type + " c\"" + text + "\\00\"\n"

    # add
    def add_i32(self, val1, val2):
        self.buffer += "%" + self.reg + " = add i32 " + val1 + ", " + val2 + "\n"
        self.reg += 1

    def add_double(self, val1, val2):
        self.buffer += "%" + self.reg + " = fadd double " + val1 + ", " + val2 + "\n"
        self.reg += 1

    # mul
    def mul_i32(self, val1, val2):
        self.buffer += "%" + self.reg + " = mul i32 " + val1 + ", " + val2 + "\n"
        self.reg += 1

    def mul_double(self, val1, val2):
        self.buffer += "%" + self.reg + " = fmul double " + val1 + ", " + val2 + "\n"
        self.reg += 1

    # sub
    def sub_i32(self, val1, val2):
        self.buffer += "%" + self.reg + " = sub i32 " + val1 + ", " + val2 + "\n"
        self.reg += 1

    def sub_double(self, val1, val2):
        self.buffer += "%" + self.reg + " = fsub double " + val1 + ", " + val2 + "\n"
        self.reg += 1

    # div
    def div_i32(self, val1, val2):
        self.buffer += "%" + self.reg + " = sdiv i32 " + val1 + ", " + val2 + "\n"
        self.reg += 1

    def div_double(self, val1, val2):
        self.buffer += "%" + self.reg + " = fdiv double " + val1 + ", " + val2 + "\n"
        self.reg += 1

    # load
    def load_i32(self, id):
        self.buffer += "%" + self.reg + " = load i32, i32* @" + id + "\n"
        self.reg += 1

    def load_double(self, id):
        self.buffer += "%" + self.reg + " = load double, double* @" + id + "\n"
        self.reg += 1

    # if
    # def icmp(id, value, HashSet<String> globalNames) {
    #     load_i32(id, globalNames)
    #     self.buffer += "%" + self.reg + " = icmp eq i32 %" + (self.reg - 1) + ", " + value + "\n"
    #     self.reg+=1
    # }

    def eq2(self, type):

        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp eq i32 %" + (self.reg - 1) + ", %" + (self.reg - 2) + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ueq double %" + (self.reg - 1) + ", %" + (self.reg - 2) + "\n"

        self.reg += 1

    def eq1(self, value, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp eq i32 %" + (self.reg - 1) + ", " + value + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ueq double %" + (self.reg - 1) + ", " + value + "\n"

        self.reg += 1

    def eq0(self, value1, value2, type):

        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp eq i32 " + value1 + ", " + value2 + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ueq double " + value1 + ", " + value2 + "\n"

        self.reg += 1

    def noeq2(self, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp ne i32 %" + (self.reg - 2) + ", %" + (self.reg - 1) + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp one double %" + (self.reg - 2) + ", %" + (self.reg - 1) + "\n"

        self.reg += 1

    def noeq1(self, value, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp ne i32 %" + (self.reg - 1) + ", " + value + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp one double %" + (self.reg - 1) + ", " + value + "\n"

        self.reg += 1

    def noeq0(self, value1, value2, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp ne i32 " + value1 + ", " + value2 + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp one double " + value1 + ", " + value2 + "\n"

        self.reg += 1

    def more2(self, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sgt i32 %" + (self.reg - 2) + ", %" + (self.reg - 1) + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ogt double %" + (self.reg - 2) + ", %" + (self.reg - 1) + "\n"

        self.reg += 1

    def more1_1(self, value, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sgt i32 %" + (self.reg - 1) + ", " + value + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ogt double %" + (self.reg - 1) + ", " + value + "\n"

        self.reg += 1

    def more1_2(self, value, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sgt i32 " + value + ", %" + (self.reg - 1) + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ogt double " + value + ", %" + (self.reg - 1) + "\n"

        self.reg += 1

    def more0(self, value1, value2, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sgt i32 " + value1 + ", " + value2 + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ogt double " + value1 + ", " + value2 + "\n"

        self.reg += 1

    def less2(self, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp slt i32 %" + (self.reg - 2) + ", %" + (self.reg - 1) + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp olt double %" + (self.reg - 2) + ", %" + (self.reg - 1) + "\n"

        self.reg += 1

    def less1_1(self, value, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp slt i32 %" + (self.reg - 1) + ", " + value + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp olt double %" + (self.reg - 1) + ", " + value + "\n"

        self.reg += 1

    def less1_2(self, value, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp slt i32 " + value + ", %" + (self.reg - 1) + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp olt double " + value + ", %" + (self.reg - 1) + "\n"

        self.reg += 1

    def less0(self, value1, value2, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp slt i32 " + value1 + ", " + value2 + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp olt double " + value1 + ", " + value2 + "\n"

        self.reg += 1

    def moreeq2(self, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sge i32 %" + (self.reg - 2) + ", %" + (self.reg - 1) + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp oge double %" + (self.reg - 2) + ", %" + (self.reg - 1) + "\n"

        self.reg += 1

    def moreeq1_1(self, value, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sge i32 %" + (self.reg - 1) + ", " + value + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp oge double %" + (self.reg - 1) + ", " + value + "\n"

        self.reg += 1

    def moreeq1_2(self, value, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sge i32 " + value + ", %" + (self.reg - 1) + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp oge double " + value + ", %" + (self.reg - 1) + "\n"

        self.reg += 1

    def moreeq0(self, value1, value2, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sge i32 " + value1 + ", " + value2 + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp oge double " + value1 + ", " + value2 + "\n"

        self.reg += 1

    def lesseq2(self, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sle i32 %" + (self.reg - 2) + ", %" + (self.reg - 1) + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ole double %" + (self.reg - 2) + ", %" + (self.reg - 1) + "\n"

        self.reg += 1

    def lesseq1_1(self, value, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sle i32 %" + (self.reg - 1) + ", " + value + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ole double %" + (self.reg - 1) + ", " + value + "\n"

        self.reg += 1

    def lesseq1_2(self, value, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sle i32 " + value + ", %" + (self.reg - 1) + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ole double " + value + ", %" + (self.reg - 1) + "\n"

        self.reg += 1

    def lesseq0(self, value1, value2, type):
        if type.equals("INTEGER"):
            self.buffer += "%" + self.reg + " = icmp sle i32 " + value1 + ", " + value2 + "\n"

        elif type.equals("FLOAT"):
            self.buffer += "%" + self.reg + " = fcmp ole double " + value1 + ", " + value2 + "\n"

        self.reg += 1

    def Or(self, val1, val2):
        self.buffer += "%" + self.reg + " = or i1 %" + val1 + ", %" + val2 + "\n"
        self.reg += 1

    def And(self, val1, val2):
        self.buffer += "%" + self.reg + " = and i1 %" + val1 + ", %" + val2 + "\n"
        self.reg += 1

    def if_start(self):
        self.br += 1
        self.buffer += "br i1 %" + (self.reg - 1) + ", label %true" + self.br + ", label %false" + self.br + "\n"
        self.buffer += "true" + self.br + ":\n"
        self.br_stack.append(self.br)

    def if_end(self):
        b = self.br_stack.pop()
        self.buffer += "br label %false" + b + "\n"
        self.buffer += "false" + b + ":\n"

    def sitofp(self, id):
        self.buffer += "%" + self.reg + " = sitofp i32 " + id + " to double\n"
        self.reg += 1

    def fptosi(self, id):
        self.buffer += "%" + self.reg + " = fptosi double " + id + " to i32\n"
        self.reg += 1

    # helpers
    def formatself(self):
        lines = []
        lines = self.buffer.split("\n")
        sb = []
        sb.append(lines[0])
        sb.append("\n")
        for i in range(0, len(lines)):
            sb.append("  ")
            sb.append(lines[i])
            sb.append("\n")
        self.buffer = sb

    def formatMainText(self):
        lines = []
        lines = self.main_text.split("\n")
        sb = []
        for line in lines:
            sb.append("  ")
            sb.append(line)
            sb.append("\n")

        self.main_text = sb

    # while
    def while_start(self):
        self.stack_pop = False
        self.br += 1
        self.buffer += "br label %while" + self.br + "\n"
        self.buffer += "while" + self.br + ":\n"
        self.br_loop.push(self.br)

    def while_condition(self, ref):
        self.buffer += "br i1 %" + ref + ", label %true" + self.br + ", label %false" + self.br + "\n"
        self.buffer += "true" + self.br + ":\n"
        self.br_stack.push(self.br)

    def while_condition(self, val):
        self.buffer += "br i1 " + val + ", label %true" + self.br + ", label %false" + self.br + "\n"
        self.buffer += "true" + self.br + ":\n"
        self.br_stack.push(self.br)

    def while_end(self):
        b = self.br_stack.pop()
        self.buffer += "br label %while" + b + "\n"
        self.buffer += "false" + b + ":\n"
        if (not self.stack_pop): self.br_loop.pop()

    def Continue(self):
        b = self.br_loop.pop()
        self.buffer += "br label %while" + b + "\n"
        self.br_loop.push(b)
        self.reg += 1

    def Break(self):
        b = self.br_loop.pop()
        self.reg += 1
        self.stack_pop = True
        self.buffer += "br label %false" + b + "\n"

def tokenGen(ast):


    Tokens = {}
    needTokens=[
        "'package'", "'IDENTIFIER'", "'import'", "'INTERPRETED_STRING_LIT'", "'FUNC'", "'parameters'", "'block'", "'var'", "'DECIMAL_LIT'", "'Println'"
    ]
    tempTokens={}

    irGen = GeneratedIR()

    k=0
    for i in range(0,len(ast)):
        if ast[i] == "'":

            for j in range(i+1,len(ast)):
                if ast[j] == "'":

                    tempTokens[k]=[i,j]
                    k+=1
                    break


    for i in range(0, len(tempTokens)):
        token = ast[tempTokens[i][0]:tempTokens[i][1]]+"'"
        for j in range(0,len(needTokens)):
            if token == needTokens[j]:

                if token == "'FUNC'":
                    funcname = ast[tempTokens[i+6][0]:tempTokens[i+6][1]]+"'"

                    if (ast[tempTokens[i+20][0]:tempTokens[i+20][1]]+"'" == "'parameterDecl'"):
                        funcParams = ast[tempTokens[i+28][0]:tempTokens[i+28][1]]+"'"



                    irGen.function_start(funcname)
                    if ast[tempTokens[i+30][0]:tempTokens[i+30][1]]+"'" == "'block'":
                        id = ast[tempTokens[i+58][0]:tempTokens[i+58][1]]
                        id = id[1:]

                        value = ast[tempTokens[i+80][0]:tempTokens[i+80][1]]

                        value = value[1:]

                        irGen.declare_i32(id,False, value)
                        # irGen.assign_i32(id,False,value)

                        i = 80

                    

                    irGen.function_end()



    return irGen.String_generate()