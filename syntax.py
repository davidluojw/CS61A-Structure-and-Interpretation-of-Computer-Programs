# Trees

from os import read
from re import S
from textwrap import dedent


def tree(root_label, branches = []):
    for branch in branches:
        assert is_tree(branch),'branches must be trees'
    return [root_label] + list(branches)


def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

# Utilities function

def fib_tree(n):
    if n <= 1:
        return tree(n)     # here is a leaf, but must construct as a tree
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left)+label(right), [left, right])
    
def count_leaf(t):
    """Count the leaves of a tree."""
    if is_leaf(t):
        return 1
    else:
        branch_counts = [count_leaf(b) for b in branches(t)]  
        return sum(branch_counts)
    
def leaves(tree):
    """Return  a list containing the leaf labels of tree.
    
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [tree]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented.

    
    """
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)
    

def increment(t):
    """Return a tree like t but with all labels incremented."""
    
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent = 0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
        

# Syntax
def phrase(tag, branches):
    return tree(tag, branches)

def word(tag, text):
    return tree([tag, text])

def tag(t):  # t either word or phrase
    """Return the tag of a constituent (word or phrase)

    """
    if is_leaf(t):  # if is word
        return label(t)[0]
    else:    # else if a phrase
        return label(t)

def text(w):
    assert is_leaf(w)
    return label(w)[1]


treebank_examples = """
( ROOT ( SBARQ ( WHNP ( WP what ) )
    ( SQ ( VP ( AUX is ) ) ( NP ( DT the ) ( NN rabbit ) ) ( VP ( VBG doing ) ) )
    ( . ? ) ) )

( ROOT ( SQ ( AUX is ) ( NP ( PRP he ) ) ( VP ( VBG hopping ) ) ( . ? ) ) )
""".split('\n')

def read_sentences(input):
    """Yield parsed sentences as lists of token for a list of lines.

    >>> for s in read_sentences(treebank_examples):
    ...    print(' '.join(s[:20]), '...')
    ( ROOT ( SBARQ ( WHNP ( WP what ) ) ( SQ ( VP ( AUX is ) ) ...
    ( ROOT ( SQ ( AUX is ) ( NP ( PRP he ) ) ( VP ( VBG hopping ...
    """
    sentences = []
    tokens = []
    for line in input:
        if line.strip():
            # make sure every parenthesis is seperated by whitespace
            tokens.extend(line.replace('(', ' ( ').replace(')', ' ) ').split()) 
            if tokens.count('(') == tokens.count(')'):
                sentences.append(tokens) # append a whole sentence to sentences
                tokens = []
    return sentences

def all_sentences():
    return read_sentences(open('suppes.parsed').readlines())

def tokens_to_parse_tree(tokens):
    """Return a tree for a list of tokens representing a parsed sentences.

    >>> print_tree(tokens_to_parse_tree(read_sentences(treebank_examples)[0]))
    ROOT
      SBARQ
        WHNP
          ['WP', 'what']
        SQ
          VP
            ['AUX', 'is']
          NP
            ['DT', 'the']
            ['NN', 'rabbit']
          VP
            ['VBG', 'doing']
        ['.', '?']
    """
    assert tokens[0] == '('
    t, end = read_parse_tree(tokens, 1)
    return t

def read_parse_tree(tokens, i):
    tag = tokens[i]
    i += 1
    if tokens[i] != '(':  # if the next element is not '(', then is must be text, because text after tag
        assert tokens[i + 1] == ')' # if the element after the text is not ')'，the input is wrong
        text = tokens[i]
        return word(tag, text), i + 2
    branches = []
    while tokens[i] != ')':
        assert tokens[i] == '('
        b, i = read_parse_tree(tokens, i + 1)
        branches.append(b)
    return phrase(tag, branches), i + 1
 
def print_parse_tree(t):
    """Print the parse tree in its original format.
    >>> print_parse_tree(tokens_to_parse_tree(read_sentences(treebank_examples)[0]))
    '(ROOT (SBARQ (WHNP (WP what)) (SQ (VP (AUX is)) (NP (DT the) (NN rabbit)) (VP (VBG doing))) (. ?)))'
    """
    if is_leaf(t):
        return '(' + tag(t) + ' ' + text(t) + ')'
    else:
        result = '(' + tag(t)
        for b in branches(t):
            result += ' ' + print_parse_tree(b)
        result += ')'
        return result

from string import punctuation

def words(t):
    """Return the words of a tree as a string.
    
    >>> words(tokens_to_parse_tree(read_sentences(treebank_examples)[0]))
    'what is the rabbit doing?'
    """
    s = ''
    for leaf in leaves(t):
        w = text(leaf)
        if not s or (w in punctuation and w not in '$') or w in ["n't", "'s", "'re", "'ve", "'ll"]:
            s = s + w
        else:
            s = s + ' ' + w
    return s
 
# Generating Language
import random
random.seed(5)

def gen_tree(t, tree_index, flip):
    """Return a version of t in which constituents are randomly replaced."""
    if is_leaf(t):
        return t
    new_branches = []
    for b in branches(t):
        if flip():
            original = b
            b = random.choice(tree_index[tag(b)])
            print('Swarpped', print_parse_tree(original), 'for', print_parse_tree(b))
        new_branches.append(gen_tree(b, tree_index, flip))
    return phrase(tag(t), new_branches)

def coin(prob):
    def flip():
        """Return True if a coin flip comes up heads."""
        return random.random() < prob
    return flip

def generate(gen=gen_tree):
    trees = [tokens_to_parse_tree(s) for s in all_sentences() if len(s) > 100]
    tree_index = index_trees(trees)
    while True:
        original = random.choice(trees)
        print('Original', words(original).lower())
        print('        ', print_parse_tree(original))
        edited = gen(original, tree_index, coin(0.3))
        input()
        print('Generated', words(edited).lower())
        input()

def nodes(t):
    """List all (tag, node) pairs of a parse tree."""
    result = []
    def traverse(t):
        result.append([tag(t), t])
        for b in branches(t):
            traverse(b)
    traverse(t)
    return result

def index_trees(trees):
    """Return a dictionary from tags to lists of trees."""
    result = {}
    for t in trees:
        for tag, node in nodes(t):
            if tag not in result:
                result[tag] = [node]
            else:
                result[tag].append(node)
    return result
    
    

 
 
     

