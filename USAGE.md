py setup.py sdist

py setup.py sdist bdist_wheel

twine upload dist/*

twine upload --skip-existing dist/*



1 . len(stage) > len(sign_required) 
2 . each transition in stage 
3 . WE_in api 
4 . Nested serializer




{
"type":"TRANSACTION.PROGRAMS",
"action":"SUBMIT",
"t_id":"11"
}