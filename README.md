# PeopleRecords

* Simple demo project with flask REST server.
* 2019/08/11: basic structure of project; running flask server; running CLI; not yet wired together.
* 2019/08/12: add tests of model and CLI code, wire it all together

To run the CLI: `./file_parser/parse_file.py tests/data/sample.csv` (or some other file if you like) 
To run the server locally: `python rest_server/server.py` then navigate to http://0.0.0.0:5000/api/ui/#/People 
To run the tests: `python -m unittest tests.test_model.TestPersonMethods` 
