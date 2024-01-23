# What this repository is
This repository contains the source material for the Introduction to Python course.

# Contributing
We love contributions!
We welcome fixes for existing bugs, as well as corrections for task and test mistakes.
The current tasks can be found in the [open issues](https://github.com/jetbrains-academy/introduction_to_python/issues) section of the project.
If you have any questions, or discover bugs or mistakes, please do not hesitate to open new issues.

Please add a comment to the issue if you're starting work on it.

If you add some common functionality, such as for the test system, it is important to include comments that describe the new behavior.
This will assist other developers and users in utilizing them correctly.

## Submitting patches
The best way to submit a patch is to [fork the project on GitHub](https://help.github.com/articles/fork-a-repo/)
and then send us a [pull request](https://help.github.com/articles/creating-a-pull-request/)
to the `master` branch via [GitHub Pull requests](https://github.com/jetbrains-academy/introduction_to_python/pulls).

If you create your own fork, it might be helpful to enable rebase by default when you pull. You can do this by executing:
``` bash
git config --global pull.rebase true
```
This will prevent your local repository from having too many merge commits, helping to keep your pull request simple and easy to apply.

## Checklist
Before submitting the pull request, make sure that you can say "YES" to each point in this short checklist:

-[ ] You provided the link to the related issue(s) from the repository;
-[ ] You made a reasonable amount of changes related only to the provided issues;
-[ ] You can explain the changes made in the pull request;
-[ ] You ran the build locally and verified new functionality/fixed bugs;
-[ ] You ran related tests locally (or added new ones) and they passed;
-[ ] You do not have merge conflicts in the pull request.
-[ ] You've made sure that all tests in [GitHub Actions](https://github.com/jetbrains-academy/introduction_to_python/tree/master/.github/workflows) pass