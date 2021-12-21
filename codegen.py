#!/usr/bin/python3

import os


main_file = open('./main.go', 'w+')
main_file_template = open('./main.go.template', 'r+')
mod_file = open('./go.mod', 'r')

mod_file_str = mod_file.read()
main_file_template_str = main_file_template.read()


print('mod file:')
print(mod_file_str)
print(main_file_template_str)

dirs = os.listdir('./apps')

module_name = ''

for line in mod_file_str.split('\n'):
    if 'module ' in line:
        module_name = line.split(' ')[1]


dirs_import_str = ''
apps_str = ''

for dir in dirs:
    if not dir.startswith('.'):
        dirs_import_str += f'"{module_name}/apps/{dir}"\n'

        dir_split_slash = dir.split('/')
        dir_breakdown =  dir_split_slash[len(dir_split_slash) - 1]

        apps_str += f'{dir_breakdown}.Core()\n'

main_file_template_str_modified = main_file_template_str
main_file_template_str_modified = main_file_template_str_modified.replace(
    '#apps', apps_str)
main_file_template_str_modified = main_file_template_str_modified.replace(
    '#applications_header', dirs_import_str)

main_file.write(main_file_template_str_modified)

mod_file.close()
main_file.close()
