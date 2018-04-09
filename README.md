# cookiecutter-python-script

Cookiecutter template for Infopen Python scripts

## Default variables

```json
{
    "project_slug": "project_slug",
    "project_name": "project_name",
    "project_description": "Python project description",
    "git_provider": "github",
    "git_username": "inf0pen",
    "git_repository": "{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug }}",
    "author_email": "foo@bar",
    "author_full_name": "Foo Bar",
    "company_name": "Infopen",
    "company_url": "http://infopen.pro",
    "copyright_year": "{% now 'utc', '%Y' %}",
    "version": "0.1.0-a1",
    "_copy_without_render": []
}
```
