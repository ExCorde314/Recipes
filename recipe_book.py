#!/bin/env python

import os
import jinja2
from jinja2 import Template
from titlecase import titlecase

# Jinja 2 template settings
#
# Some of jinja2's default template markings interfere
# with latex, so they are changed below:
latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

exception_dirs = [".git"]
subfolders = [ f for f in os.listdir('.') if os.path.isdir(f) and f not in exception_dirs ]

sections = []
for folder in subfolders:
    section_name = titlecase(folder.replace("_", " "))

    is_intro = False
    recipes = []
    for file in os.listdir(folder):
        if file.endswith(".tex"):
            if file == "introduction.tex":
                is_intro = True
            else:
                recipes += [folder + "/" + file[:-4]]

    recipes.sort()
    print (recipes)

    if is_intro:
        recipes = [folder + "/introduction.tex"] + recipes

    if recipes != []:
        sections += [(section_name, recipes)]

sections.sort()

template = latex_jinja_env.get_template('recipe_book.j2.tex')

with open("recipe_book.tex", "w") as f:
    f.write(template.render(sections = sections))
