### How to Setup

virtualenv my-venv
. my-venv/bin/activate
pip3 install 

### quizz2
1.GET "/" => "Hello World"
2.POST "/users" => "name=foo"

3.GET "/users/1"    200

    response-json:  {
                    "id": 1,
                    "name": foo
                    }

4.DELETE "/users/1" 204

### GET /