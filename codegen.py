#!/usr/bin/python3

main_file = open('./main.go', 'w+')
main_file_template = open('./main.go.template', 'r+')
mod_file = open('./go.mod', 'r')

mod_file_str = mod_file.read()
main_file_template_str = main_file_template.read()

print('mod file:')
print(mod_file_str)
print(main_file_template_str)

main_file_template_str_modified = main_file_template_str
main_file_template_str_modified = main_file_template_str_modified.replace(
    '#apps', '')
main_file_template_str_modified = main_file_template_str_modified.replace(
    '#applications_header', '')

main_file.write(main_file_template_str_modified)

mod_file.close()
main_file.close()
