# sphinx-swagger
Sphinx extension that automatically documents Swagger APIs

**Usage**

Include extension in *conf.py*

    extensions = ['sphinx_swagger']

Add directive pointing to Swagger api-docs

    .. swaggerv2doc:: URL

For example    

    .. swaggerv2doc:: http://petstore.swagger.wordnik.com/api/api-docs/pet

    .. swaggerv2doc:: http://petstore.swagger.wordnik.com/api/api-docs/user

    .. swaggerv2doc:: http://petstore.swagger.wordnik.com/api/api-docs/store
