"""
Basic test to check project import
"""


def test_import_project():
    """
    Test root project import
    """

    from {{ cookiecutter.project_slug }}.main import main

    assert main() is None
