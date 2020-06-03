import re
import os
import json

json_list = []

for filename in os.listdir('bibitems'):
    if not filename.endswith('.bib'):
        continue

    with open(os.path.join('bibitems', filename), 'r') as f:
        content = f.read()

    #content = map(lambda x: x.strip(), content)
    #print(content)
    result = dict()
    m = re.search('@.+{(.+?),', content)
    if m:
        found = m.group(1)
    result['bibitem'] = 'https://raw.githubusercontent.com/ndem0/pubblications/master/bibitems/{}.bib'.format(found)
    content = content[content.find('\n'):]
    m = re.findall('(.+?)=(.*?),\n', content, flags=re.DOTALL)

    for key, value in m:
        if key and value: 
            result[key.strip().lower()] = value.replace('{', '').replace('}', '').strip()
    for k, v in result.items():
        print(k, v)

    author = result['author']
    author_str = ''
    for name in author.split(' and '):
        name = name.split()
        author_str += '{}. {}, '.format(name[0][0].upper(), name[1])
    author_str = author_str[:-2]
    result['author'] = author_str

    json_list.append(result)
    

with open('publications.json', 'w') as f:
    json.dump(json_list, f)

