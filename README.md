# sphinx-swagger
Sphinx extension that automatically documents Swagger APIs

**Usage** 

Include extension in *conf.py*

    extensions = ['sphinx_swagger']
    
Add directive pointin to Swagger api-docs

    .. swaggerdoc:: URL

For example    
  
    .. swaggerdoc:: http://petstore.swagger.wordnik.com/api/api-docs/pet
    
    .. swaggerdoc:: http://petstore.swagger.wordnik.com/api/api-docs/user
    
    .. swaggerdoc:: http://petstore.swagger.wordnik.com/api/api-docs/store
