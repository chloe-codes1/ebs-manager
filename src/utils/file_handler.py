import json

from configs.configs import variables


def write_json(title, contents):
    with open(variables['FILE_PATH'] + title, 'w', encoding='utf-8') as f:
        json.dump(contents, f, default=str, indent=4, sort_keys=True)


def write_file(title, contents):
    with open(variables['FILE_PATH'] + title + '.txt', 'w') as f:
        for content in contents:
            f.write(f'{content}\n')
