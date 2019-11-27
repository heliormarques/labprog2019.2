class Stack():
    def __init__(self):
        self.items = [];

    def push(self, item):
        self.items.append(item);

    def pop(self):
        if not self.is_empty():
            return self.items.pop();
        else:
            print("Tried to remove from empty stack"); 

    def is_empty(self):
        return self.items == [];

def is_equal(s1, s2):
    return True if (s1 + s2) in ["()", "[]", "{}"] else False;

def is_total_balanced(paren_string):
    pilha = Stack();
    is_balanced = True;
    contador = 0;

    while contador < len(paren_string) and is_balanced:
        paren = paren_string[contador];
        if paren in "([{":
            pilha.push(paren);
        else:
            if pilha.is_empty():
                is_balanced = False;
                return("N");
            else:
                top = pilha.pop();
                if not is_equal(top, paren):
                    is_balanced = False;
                    return("N");
        contador += 1;
    if pilha.is_empty() and is_balanced:
        return "S";
    else:
        return "N";


N = input();
for vezes in range(int(N)):
    temp = input();
    if len(temp) % 2 != 0:
        print("N");
    else:
        print(is_total_balanced(temp));


