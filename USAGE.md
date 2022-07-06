py setup.py sdist

py manage.py sdist bdist_wheel

twine upload dist/*

twine upload --skip-existing dist/*