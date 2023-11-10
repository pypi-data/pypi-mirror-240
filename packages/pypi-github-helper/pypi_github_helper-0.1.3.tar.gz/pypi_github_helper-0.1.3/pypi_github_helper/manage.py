import subprocess


def dev():
    cmd = "python main.py"
    subprocess.run(cmd, shell=True, check=True)


def pylint():
    # cmd = "pylint $(git ls-files '*.py')"
    cmd = "pylint **/**/*.py --disable=missing-docstring --disable=line-too-long --disable=consider-using-with"
    subprocess.run(cmd, shell=True, check=True)


def fix():
    # cmd = "autopep8 --in-place --aggressive --aggressive **/**/*.py"
    cmd = "yapf -ir main.py ./pypi_github_helper ./src ./tests"
    subprocess.run(cmd, shell=True, check=True)
