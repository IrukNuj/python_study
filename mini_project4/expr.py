class Expression:
    def eval(self, x_value):
        '''変数 x の値が x_value だった時の式の値を返すメソッド'''
        raise NotImplementedError
    
    def diff(self):
        '''式を変数 x で微分した式に対応する Expression オブジェクト
        を返すメソッド'''
        raise NotImplementedError

class Number(Expression):
    def __init__(self, number):
        self.number = number
    
    def eval(self, x_value):
        return self.number
    
    def diff(self):
        return str(self.number)

class X(Expression):
    def eval(self, x_value):
        return x_value

    def diff(self):
        return "x"


class Add(Expression):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def eval(self, x_value):
        return self.number1.eval(x_value) + self.number2.eval(x_value)

    def diff(self):
        return '{0}+{1}'.format(self.number1.diff, self.number2.diff)


class Sub(Expression):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def eval(self, x_value):
        return self.number1.eval(x_value) - self.number2.eval(x_value)

    def diff(self):
        return '{0}+{1}'.format(self.number1.diff, self.number2.diff)

class Mul(Expression):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def eval(self, x_value):
        return self.number1.eval(x_value) * self.number2.eval(x_value)

    def diff(self):
        return '{0}+{1}'.format(self.number1.diff, self.number2.diff)

class Div(Expression):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def eval(self, x_value):
        return self.number1.eval(x_value) / self.number2.eval(x_value)

    def diff(self):
        return '{0}+{1}'.format(self.number1.diff, self.number2.diff)
