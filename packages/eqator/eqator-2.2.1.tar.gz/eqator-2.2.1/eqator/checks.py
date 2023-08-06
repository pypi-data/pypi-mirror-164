from importlib.util import find_spec
from .helpers import shell_run
from .helpers import print_error
from .helpers import print_ok
from .helpers import run_unit_tests
from django.conf import settings
from .helpers import print_default
from .helpers import check_needed
import re


def check_flake(directory: str, verbose: bool, config_file: str, all: bool, flake: bool, variables_passed: bool) -> int:
    if check_needed(all, flake, variables_passed):
        print_default(f'Checking style guide with flake8 (see "{config_file}")')
        backend_dir = directory
        cmd = f'flake8 {backend_dir}'
        lines = shell_run(cmd)
        if lines == '':
            print_ok(lines, verbose)
            return 0
        print_error(lines)
        return 1
    return 0


def check_radon(directory: str, verbose: bool, config_file: str, all: bool, radon: bool, variables_passed: bool) -> int:
    if check_needed(all, radon, variables_passed):
        print_default(f'Cyclomatic complexity with radon (see "{config_file}")')
        cmd = f'radon cc {directory}'
        lines = shell_run(cmd)
        if lines == '':
            print_ok(lines, verbose)
            return 0
        print_error(lines)
        return 1
    return 0


def check_security_linter(directory: str, verbose: bool, config_file: str, all: bool, linter: bool,
                          variables_passed: bool) -> int:
    if check_needed(all, linter, variables_passed):
        print_default(f'Security lint with bandit (only high-severity issues, see "{config_file}")')
        lines = shell_run(f'bandit -r {directory} -lll')
        if 'No issues identified' in lines:
            print_ok(lines, verbose)
            return 0
        print_error(lines)
        return 1
    return 0


def check_migrations(directory: str, verbose: bool, all: bool, migrations: bool, variables_passed: bool) -> int:
    if check_needed(all, migrations, variables_passed):
        print_default('Project migrations')
        cmd = f'python3 {directory}/manage.py makemigrations --check --dry-run'
        lines = shell_run(cmd)
        if 'No changes detected' in lines:
            print_ok(lines, verbose)
            return 0
        print_error(lines)
        return 1
    return 0


def check_unit_tests(directory: str, verbose: bool, all: bool, tests: bool, variables_passed: bool, test_coverage: bool) -> int:
    if check_needed(all, tests, variables_passed):
        command_pref = 'coverage run ' if check_needed(all, test_coverage, variables_passed) else ''

        if find_spec('pytest') is not None:
            print_default('Django pytest')
            backend_dir = directory
            cmd = f'{command_pref}pytest {backend_dir}'
            lines = shell_run(cmd)
            tests_count: list = re.findall(r'collected (\d+) item', lines)
            passed_count: list = re.findall(r'(\d+) passed', lines)
            skipped_count: list = re.findall(r'(\d+) skipped', lines)

            if int(tests_count[0]) == sum(list(map(int, skipped_count)) + list(map(int, passed_count))):
                print_ok(lines, verbose)
                return 0

            print_error(lines)
            return 1
        else:
            print_default('Django unit tests')

            if command_pref != '':
                shell_run(f'{command_pref}{directory}/manage.py test')

            failures, output = run_unit_tests(())

            if failures:
                print_error(output)
                return 1
            print_ok('', verbose)
            return 0
    return 0


def check_garpix_page_tests(verbose: bool, all: bool, garpix_page: bool, variables_passed: bool) -> int:
    if 'garpix_page' in settings.INSTALLED_APPS and check_needed(all, garpix_page, variables_passed):
        print_default('Django unit tests garpix_page')
        failures, output = run_unit_tests(('garpix_page',))

        if failures:
            print_error(output)
            return 1
        print_ok('', verbose)
    return 0


def check_test_coverage(verbose: bool, all: bool, coverage: bool, variables_passed: bool) -> (int, int):

    coverage_result = -1

    if check_needed(all, coverage, variables_passed):

        print_default('Test coverage')

        cmd = 'coverage report'
        lines = shell_run(cmd)

        result_line: list = re.findall(r'TOTAL[ \d]+ (\d+)%', lines)

        coverage_result = int(result_line[0])

        if coverage_result < getattr(settings, 'TEST_COVERAGE_RATE', 70):
            print_error(lines)
            return 1, coverage_result
        print_ok('', verbose)

    return 0, coverage_result


def check_lighthouse(verbose: bool = False, clear_reports: bool = False, all: bool = False) -> int:
    if all:
        print_default('Lighthouse CI')
        shell_run('lhci collect')
        lines = shell_run('lhci assert')
        if clear_reports:
            shell_run('rm -rf .lighthouseci')
        if 'Assertion failed' in lines:
            print_error(lines)
            return 1
        print_ok(lines, verbose)
    return 0
