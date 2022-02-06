
def leaves(tree):
    """Return  a list containing the leaf labels of tree.
    
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [tree]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def print_tree(t, indent = 0):
    print('  ' * indent + str(tag(t))) ### !!!how to change?
    for b in branches(t):
        print_tree(b, indent + 1)
        

# Syntax
def phrase(tag, branches):
    return ['(', tag] + sum(branches, []) + [')']

def word(tag, text):
    return ['(', tag, text, ')']

def tag(t):  # t either word or phrase
    """Return the tag of a constituent (word or phrase)

    """
    assert t[0] == '('
    return t[1]

def text(w):
    assert is_leaf(w)
    return w[2]

def branches(t):
    if is_leaf(t):
        return []
    branch = []
    branches = []
    opened = 1
    for token in t[2:]:
        branch.append(token)
        if token == '(':
            opened += 1
        if token == ')':
            opened -= 1
            if opened == 1:
                branches.append(branch)
                branch = []
    return branches

def is_leaf(t):
    return len(t) == 4
            
            


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
    return tokens




 
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
    
    

 
 
     

