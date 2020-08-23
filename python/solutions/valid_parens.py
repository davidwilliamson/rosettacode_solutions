#! /usr/bin/env python

""" https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

"""

import logging

logging.basicConfig(
    format="%(message)s",
    level=logging.INFO
)
MATCHES = {
    '(': ')',
    '[': ']',
    '{': '}'
}


def is_valid(input_str: str) -> bool:
    """determne whether input_str is a valid sequence of nested () {} []"""
    logging.debug("-------- %s ----------------", input_str)
    stack = list()
    # Empty string is defined as valid
    if not input_str:
        return True
    # iterate chars from left to right.
    # * If opening paren char, push on stack
    # * If closing paren char, pop from stack and verify correct type of paren
    # Return false if:
    # * popped char is of wrong type (unbalanced chars, i.e. '(' paired with ']'
    # * stack is empty when we pop (more closing chars than opening chars)
    # * stack not empty at end of string (more opening chars than closing chars)
    # * char other than expected (, {, [, ), }, ]
    for char in input_str:
        logging.debug("checking %s", str(char))
        if char in MATCHES:
            logging.debug("Pushing %s", str(char))
            stack.append(MATCHES[char])
        elif char in MATCHES.values():
            if stack:
                # pop() in python implements a LIFO.
                last_pushed = stack.pop()
                logging.debug("last pushed is %s", last_pushed)
                if last_pushed != char:
                    logging.debug("%s does not match %s", last_pushed, char)
                    return False
            else:
                logging.debug("Stack prematurely empty")
                return False
        else:
            logging.debug("Unexpected char '%s'", char)
            return False
    if stack:
        logging.debug("Unmatched : %s", str(stack))
        return False
    return True


def main():
    """main"""
    test_cases = {
        '': True,
        '()': True,
        '()[]{}': True,
        '(]': False,
        '](': False,
        '([)]': False,
        '(([[{{}}]]))()': True,
        '(([[{{}}]]))': True,
        '{[]}': True
    }
    for test_case, expected_result in test_cases.items():
        assert is_valid(test_case) == expected_result, "'{0}' should be {1}".format(
            test_case, expected_result)
        print("'{0}' is {1} -- OK".format(test_case, str(expected_result)))


if __name__ == '__main__':
    main()
