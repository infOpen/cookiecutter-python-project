import json
import pytest
import re
import yaml

# Functions
# ==============================================================================


# Common checks
def common_tests(data, result):

    # General assert
    assert result.exit_code == 0
    assert result.exception is None

    # Structure assert
    assert_root_directory(data, result)
    assert_directories(data, result)
    assert_testing_files(result)
    assert_license_file(result)
    assert_readme_file(data, result)


# Check root project
def assert_root_directory(data, result):
    assert result.project.basename == '{}'.format(data.get('project_slug'))
    assert result.project.isdir()


# Check directories
def assert_directories(data, result):

    # Root directories
    project_directories = ['docs', data.get('project_slug'), 'tests']

    # Check project directories
    for directory in project_directories:
        assert result.project.join(directory).isdir()


# Check test files
def assert_testing_files(result):

    # All files about tests
    test_files = [
        'CHANGELOG.md',
        'docker-compose.yml',
        'Dockerfile',
        'LICENSE',
        'README.rst',
        'requirements.txt',
        'setup.cfg',
        'setup.py',
        'tests/unit/test_import_root_module.py',
        'tox.ini',
        'VERSION',
    ]

    # Check project directories with main.yml file
    for test_file in test_files:
        assert result.project.join(test_file).isfile()


# Check license file
def assert_license_file(result):

    license_file = result.project.join('LICENSE')
    license_lines = license_file.readlines(cr=False)

    assert license_file.isfile()
    assert 'MIT License' in license_lines


# Check README file
def assert_readme_file(data, result):

    readme_file = result.project.join('README.rst')
    readme_lines = readme_file.readlines(cr=False)

    assert readme_file.isfile()
    assert '    python setup.py test' in readme_lines


# Tests
# ==============================================================================

# Template test
@pytest.mark.parametrize('data_filename, project_slug', [
    ('./cookiecutter.json', 'project_slug'),
    ('./tests/test_01.json', 'project_slug'),
    ('./tests/test_02.json', 'test_01'),
])
def test_json_values(cookies, data_filename, project_slug):

    # Load data file
    with open(data_filename) as data_file:
        data = json.load(data_file)

    # Create project
    result = cookies.bake(extra_context=data)

    # Common tests
    assert data.get('project_slug') == project_slug
    common_tests(data, result)
