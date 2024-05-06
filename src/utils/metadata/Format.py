import re





def remove_non_english_chars(s):
    match = re.search('[a-zA-Z]+', s)
    if match:
        return match.group()
    return ''

# # 使用示例
# print(remove_non_english_chars('$WIF'))  # 输出：WIF