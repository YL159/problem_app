'''
Given 2 strings s1, s2 of only lower English letters, with some internal conflicts.
Interleave them together into 1 string, find result string's min conflicts.

Interleave: put chars of s1 and s2 by their respective orders into result string.
Conflict: 2 chars in a string appear in reversed alphabetical order
    <=> index of a char with larger lex < index of a char with smaller lex
    => add conflict count lex(left_char) - lex(right_char) to total conflict

Observation:
Consider the final string s, mark all chars from s1 as blue, s2 as red.

If s1 and s2 don't have internal conflicts (sorted)
    => just use merge sort to get s also with no conflicts.

Each blue char's contribution to conflict depends on its position among s2:
    => red chars before blue c with larger lex + red chars after c with smaller lex
    => pre compute each letter a-z conflict contribution if placed at index i of s2, and vise versa for s1


'''