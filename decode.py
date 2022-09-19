#/usr/bin/python3

import re
from pprint import pprint

word_list_pattern = r"var sjana = (\[.*\])"

get_word_func_call_pattern = r"get_word\((\d+)\)"

js_file = open("app.min.js", "r")

js_content = js_file.read()

word_list = re.search(word_list_pattern, js_content).groups()[0].strip('"]["').split('", "')

indices = re.findall(get_word_func_call_pattern, js_content)

new_js_content = js_content

total_words = len(word_list)

for index in indices:
    index = int(index)
    if index > total_words or index < 119:
        # print(f'range of index for {index - 119}/{total_words} is exceeded skipping')
        continue
    # print(f'replacing {index} call')
    new_js_content = re.sub(get_word_func_call_pattern, f'"{word_list[index - 119]}"', new_js_content, 1)

with open('new_app.js', 'w') as f:
    f.write(new_js_content)

print('New file created check!')
