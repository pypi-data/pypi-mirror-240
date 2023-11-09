from unittest import TestCase

from convergence.security.rule_expression import AuthorizationRuleExpression


class TestAuthorizationRuleExpression(TestCase):
    def test_general_dot_operator(self):
        rule = AuthorizationRuleExpression()
        rule.parse('sin(a).cos(b).value')

        self.assertEqual(['sin', '(', 'a', ')', '.', 'cos', '(', 'b', ')', '.', 'value'], rule._tokens)
        self.assertEqual(['sin', 'a', '__call__:1', 'cos', '.', 'b', '__call__:1', 'value', '.'], rule._postfix_tokens)

    def test_function_call_finder_1(self):
        rule = AuthorizationRuleExpression()
        rule.parse('sin(a and b, c or d)')

        self.assertEqual(['sin', '(', 'a', 'and', 'b', ',', 'c', 'or', 'd', ')'], rule._tokens)
        self.assertEqual(['sin', 'a', 'b', 'and', 'c', 'd', 'or', '__call__:2'], rule._postfix_tokens)

    def test_function_call_finder_2(self):
        rule = AuthorizationRuleExpression()
        rule.parse('arcsin(sin(30, "deg")) or pi() and tan(cot(5,  6, 7), 8, cos(4, "aa"))')

        self.assertEqual(
            ['arcsin', '(', 'sin', '(', '30', ',', '"deg"', ')', ')', 'or', 'pi', '(', ')', 'and',
             'tan', '(', 'cot', '(', '5', ',', '6', ',', '7', ')', ',', '8', ',',
             'cos', '(', '4', ',', '"aa"', ')', ')'], rule._tokens)
        self.assertEqual(
            ['arcsin', 'sin', '30', '"deg"', '__call__:2', '__call__:1', 'pi', '__call__:0',
             'or', 'tan', 'cot', '5', '6', '7', '__call__:3', '8', 'cos', '4', '"aa"', '__call__:2',
             '__call__:3', 'and'], rule._postfix_tokens)

    def test_function_call_finder_3(self):
        rule = AuthorizationRuleExpression()
        rule.parse('@math.module.sin(a.aa and b.bb, c.cc or d.dd)')

        self.assertEqual(
            ['@math', '.', 'module', '.', 'sin', '(', 'a', '.', 'aa', 'and', 'b', '.', 'bb', ',', 'c', '.', 'cc', 'or',
             'd', '.', 'dd', ')'], rule._tokens)
        self.assertEqual(
            ['@math', 'module', '.', 'sin', '.', 'a', 'aa', '.', 'b', 'bb', '.', 'and', 'c', 'cc', '.', 'd', 'dd', '.',
             'or', '__call__:2'], rule._postfix_tokens)

    def test_function_call_finder_4(self):
        rule = AuthorizationRuleExpression()
        rule.parse('@math.sin(a.aa and (b.bb or c.cc))')

        self.assertEqual(
            ['@math', '.', 'sin', '(', 'a', '.', 'aa', 'and', '(', 'b', '.', 'bb', 'or', 'c', '.', 'cc', ')', ')'],
            rule._tokens)
        self.assertEqual(
            ['@math', 'sin', '.', 'a', 'aa', '.', 'b', 'bb', '.', 'c', 'cc', '.', 'or', 'and', '__call__:1'],
            rule._postfix_tokens)

    def test_single_check_rule_parsing(self):
        rule = AuthorizationRuleExpression()
        rule.parse('@acl.has_authority("a.b")')

        self.assertEqual(['@acl', '.', 'has_authority', '(', '"a.b"', ')'], rule._tokens)
        self.assertEqual(['@acl', 'has_authority', '.', '"a.b"', '__call__:1'], rule._postfix_tokens)

    def test_and_check_rule_parsing(self):
        rule = AuthorizationRuleExpression()
        rule.parse('@acl.has_authority("a.b") and @acl.has_authority("a.c")')

        self.assertEqual(
            ['@acl', '.', 'has_authority', '(', '"a.b"', ')',
             'and', '@acl', '.', 'has_authority', '(', '"a.c"', ')'], rule._tokens)
        self.assertEqual(['@acl', 'has_authority', '.', '"a.b"', '__call__:1', '@acl', 'has_authority', '.',
                          '"a.c"', '__call__:1', 'and'], rule._postfix_tokens)

    def test_or_check_rule_parsing(self):
        rule = AuthorizationRuleExpression()
        rule.parse('@acl.has_authority("a.b") or @acl.has_authority("a.c")')

        self.assertEqual(['@acl', '.', 'has_authority', '(', '"a.b"', ')', 'or', '@acl', '.', 'has_authority',
                          '(', '"a.c"', ')'], rule._tokens)
        self.assertEqual(['@acl', 'has_authority', '.', '"a.b"', '__call__:1', '@acl', 'has_authority', '.',
                          '"a.c"', '__call__:1', 'or'], rule._postfix_tokens)

    def test_complex_check_rule_parsing(self):
        rule = AuthorizationRuleExpression()
        rule.parse('@acl.has_authority("a.b") or (@acl.has_authority("a.c") and @acl.has_authority("a.d"))')

        self.assertEqual(
            ['@acl', '.', 'has_authority', '(', '"a.b"', ')', 'or', '(', '@acl', '.', 'has_authority', '(', '"a.c"',
             ')', 'and', '@acl', '.', 'has_authority', '(', '"a.d"', ')', ')'], rule._tokens)
        self.assertEqual(['@acl', 'has_authority', '.', '"a.b"', '__call__:1', '@acl', 'has_authority', '.',
                          '"a.c"', '__call__:1', '@acl', 'has_authority', '.', '"a.d"', '__call__:1', 'and', 'or'], rule._postfix_tokens)
