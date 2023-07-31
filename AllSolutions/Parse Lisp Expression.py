"""
Parse Lisp Expression

You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)", where let is always the string "let", then there are one or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let expression is the value of the expression expr.
An add expression takes the form "(add e1 e2)" where add is always the string "add", there are always two expressions e1, e2 and the result is the addition of the evaluation of e1 and the evaluation of e2.
A mult expression takes the form "(mult e1 e2)" where mult is always the string "mult", there are always two expressions e1, e2 and the result is the multiplication of the evaluation of e1 and the evaluation of e2.
For this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally, for your convenience, the names "add", "let", and "mult" are protected and will never be used as variable names.
Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on the scope.
 

Example 1:

Input: expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

Example 2:

Input: expression = "(let x 3 x 2 x)"
Output: 2
Explanation: Assignment in let statements is processed sequentially.

Example 3:

Input: expression = "(let x 1 y 2 x (add x y) (add x y))"
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.
 

Constraints:

1 <= expression.length <= 2000
There are no leading or trailing spaces in expression.
All tokens are separated by a single space in expression.
The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
The expression is guaranteed to be legal and evaluate to an integer.
"""

class Solution:
    def evaluate(self, expression: str) -> int:
        # token and stack to separate different layers of expressions
        # dictionary to memorize let
        tokens, st, d = [''], [], {}
        def evaluateHelper(tokens): # process the current layer of expression
            if tokens[0] in ['add', 'mult']:
                n1, n2 = int(d.get(tokens[1], tokens[1])), int(d.get(tokens[2], tokens[2]))
                return str(n1+n2) if tokens[0] == 'add' else str(n1*n2)
            else: # let, update dictionary
                # skip the last one because it's not updating the dictionary
                # d.get() handles both token being var or integer
                for i in range(1, len(tokens)-2, 2): 
                    d[tokens[i]] = d.get(tokens[i+1], tokens[i+1])
                # the last token cannot be a nested expression which is intercepted before entering this
                # so it can only be a variable, an integer or ''
                return d.get(tokens[-1], tokens[-1]) 
            
        for c in expression:
            # 4 situations: 
            # transit layers: 1. enter the deeper layer, 2. get back from the deeper layer, 
            # current layer: 3. start a new token, 4. continue reading the current token
            # the magic is, by using stack, recursions for the deeper layers are avoided
            if c == '(':
                # update the dictionary before entering the deeper layer
                if tokens[0] == 'let': 
                    evaluateHelper(tokens)
                # tokens is reserved because the "tokens" in the next line is entirely overwritten as a new variable. 
                # (for example, tokens[-1] = 'a' won't reserve it)
                # d is reserved because of dict()
                st.append((tokens, dict(d)))
                tokens = ['']
            elif c == ')': 
                # get the current layer value
                val = evaluateHelper(tokens)
                tokens, d = st.pop()
                # update the outside layer
                tokens[-1] += val
            elif c == ' ': 
                tokens.append('')
            else: 
                tokens[-1] += c
        # make sure to have the return outside the for loop
        return int(tokens[0])