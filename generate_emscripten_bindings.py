import os
import json

SNIPPETS_PATH = './target/.cargo-web/snippets'
OUTPUT_FILE = 'snippet.c'

content_header = '''// This file is generated by generate_emscripten_bindings.py
// Do not edit this file manually

#include <emscripten.h>

'''

def generate_function_arguments(arg_count):
    parameters = '('
    arguments = ''
    for i in range(arg_count):
        parameters += 'const char*'
        arg = 'arg' + str(i)
        if i != arg_count - 1:
            arg += ', '
        parameters += arg
        arguments += arg
    parameters += ')'
    return parameters, arguments

with open(OUTPUT_FILE, 'w') as output:
    output.write(content_header)

    for snippet_dir in os.listdir(SNIPPETS_PATH):
        snippet_files = os.listdir(os.path.join(SNIPPETS_PATH, snippet_dir))
        
        for snippet_file in snippet_files:
            json_file_path = os.path.join(SNIPPETS_PATH, snippet_dir, snippet_file)
            
            with open(json_file_path, 'r') as json_file:
                json_data = json.load(json_file)

                parameters, arguments = generate_function_arguments(json_data['arg_count'])
                escaped_code = json_data['code'].replace('"', '\\"')

                output.write('extern ')
                output.write('int ' if json_data['has_return'] else 'void ')
                output.write(f"{json_data['name']} {parameters} {{\n")
                output.write('  return ' if json_data['has_return'] else '')
                output.write('EM_ASM_INT' if json_data['has_return'] else '  EM_ASM')
                output.write(f'("{escaped_code}", {arguments});\n')
                output.write('}\n\n')
