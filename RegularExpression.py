import re

# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

def is_valid_email(addr):
    """Check addr whether a valid email address.

    >>> assert is_valid_email('someone@gmail.com')
    >>> assert is_valid_email('bill.gates@microsoft.com')
    >>> assert not is_valid_email('bob#example.com')
    >>> assert not is_valid_email('mr-bob@example.com')
    >>> print('ok')
    ok
    """
    if re.match(r'\w+\.?\w+\@\w+\.com$', addr):
        return True
    else:
        return False

# 可以提取出带名字的Email地址：
def name_of_email(addr):
    """Extract the name of email

    >>> assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
    >>> assert name_of_email('tom@voyager.org') == 'tom'
    >>> print('ok')
    ok
    """
    # re_name = re.compile(r'^<?(\w+\s?\w+)>?')
    # return re_name.match(addr).group(1)
    
    name_check=re.compile(r'^\<?([a-zA-Z\s]+)\>?')
    return name_check.match(addr).group(1)

def is_comment(string):
    """Check the string s whether a comment

    >>> is_comment('<review id="0">\\n')
    False
    >>> is_comment('请问这机不是有个遥控器的吗？\\n')
    True
    >>> is_comment('</review>\\n')
    False
    >>> is_comment('\\n')
    False
    >>> is_comment('<review id="0"  label="0">\\n')
    False
    """
    import re
    if re.match(r'^<review id="\d+">\n', string):
        return False
    elif re.match(r'^</review>\n?', string):
        return False
    elif re.match(r'^\n', string):
        return False
    elif re.match(r'^<review id="\d"\s+label="\d">\n', string):
        return False
    else:
        return True
train_pos_file = "data/train_positive.txt"
train_neg_file = "data/train_negative.txt"
train_pos_lines = open(train_pos_file, 'r', encoding='utf-8').readlines()[1:-1]
train_neg_lines = open(train_neg_file, 'r', encoding='utf-8').readlines()[1:-1]
train_pos_comments = [x for x in train_pos_lines if is_comment(x)]
train_neg_comments = [x for x in train_neg_lines if is_comment(x)]
train_comments = train_pos_comments + train_neg_comments
train_comments = [re.sub(r'\n$', '', x) for x in train_comments]
train_labels = [1 for i in range(len(train_pos_comments))] + [0 for i in range(len(train_neg_comments))]
test_comments = []
test_labels = []
    
        