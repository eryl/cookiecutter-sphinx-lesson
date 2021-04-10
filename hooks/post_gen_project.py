#!/usr/bin/env python3


POST_CREATION = """
Congratulations! You have just created a project in sphinx-lesson format!

There are few additional steps to perform:

1. Initialize a Git repository in the generated {{cookiecutter.lesson_slug}} folder with:
   * cd {{cookiecutter.lesson_slug}}
   * git init
   * git add .
   * git commit -m "First commit"
   * git branch -M main
   * git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.lesson_slug}}.git
2. Create a new, **empty** repository on GitHub with the name {{cookiecutter.lesson_slug}}
3. Push your local content to the GitHub repository:
   * git push -u origin main

The automated GitHub Action will build the website for you.
Wait a couple of minutes for it to complete. Then open the repository settings on GitHub:

1. go to the "Pages" section
2. under "Source" select "gh-pages" and save.

A website with the rendered lesson materials should appear at: https://{{cookiecutter.github_username|lower}}.github.io/{{cookiecutter.lesson_slug}}
Note that it might take up to 20 minutes for the website to appear!
"""
print(POST_CREATION)
