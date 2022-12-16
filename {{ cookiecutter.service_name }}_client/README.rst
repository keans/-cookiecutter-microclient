{{ cookiecutter.service_name }}_client
=======================

setup
-----

in development

::

    python -m venv env
    source env/bin/activate
    pip install -e .

in production

::

    python -m venv env
    source env/bin/activate
    pip install -U {{ cookiecutter.service_name }}_client


usage via command line command
------------------------------


get JWT token
~~~~~~~~~~~~~

::
    
    {{ cookiecutter.service_name }}_client gettoken

store the `access_token` for the further calls.


add a {{ cookiecutter.item_name }}
~~~~~~~~~~~~~~

::
    
    {{ cookiecutter.service_name }}_client --token <token> {{ cookiecutter.item_name }}s create --id 1 --name foo


update {{ cookiecutter.item_name }} by ID
~~~~~~~~~~~~~~

::

    {{ cookiecutter.service_name }}_client --token <token> {{ cookiecutter.item_name }}s update --id 1 --name foo_new



delete {{ cookiecutter.item_name }} by ID
~~~~~~~~~~~~~~

::
    
    {{ cookiecutter.service_name }}_client --token <token> {{ cookiecutter.item_name }}s delete --id 1


get {{ cookiecutter.item_name }} by ID
~~~~~~~~~~~~~~

::
    
    {{ cookiecutter.service_name }}_client --token <token> {{ cookiecutter.item_name }}s get --id 1



get all {{ cookiecutter.item_name }}s
~~~~~~~~~~~~~~~

::
    
    {{ cookiecutter.service_name }}_client --token <token> {{ cookiecutter.item_name }}s list


usage via Python module
-----------------------

get access token

::
    from {{ cookiecutter.service_name }}_client import MicroClient

    mc = MicroClient(base_url="http://127.0.0.1:8000")
    token = mc.get_token(username="username", password="password")
    print(token)


manage {{ cookiecutter.item_name }}s

::
    from {{ cookiecutter.service_name }}_client import MicroClient as {{ cookiecutter.item_name.title() }}MicroClient

    mc = {{ cookiecutter.item_name.title() }}MicroClient(
        base_url="http://127.0.0.1:8000", 
        access_token="token"
    )
    
    # add item
    mc.create(id=1, name="foo")

    # update item
    mc.update(id=1, name="foo_new")

    # delete item
    mc.delete(id=1)

    # get item
    mc.get(id=1)

    # get all items
    mc.get_all()
