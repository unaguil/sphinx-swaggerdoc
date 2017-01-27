========================
sphinxcontrib-swaggerdoc
========================

Sphinx extension for documenting Swagger 2.0 APIs

Usage
=====

Include extension in ``conf.py``

.. code:: python

   extensions = ['sphinxcontrib.swaggerdoc']

Add directive pointing to Swagger api-docs

.. code:: restructuredtext

    .. swaggerv2doc:: URL/swagger.json

For example

.. code:: restructuredtext

    .. swaggerv2doc:: http://petstore.swagger.io/v2/swagger.json

If the Swagger description contains multiple tags, you can select a subset
for the documentation generation. For example, the following directive only
generates the documentation for the methods contained in tags **pet** and
**store**.

.. code:: restructuredtext

    .. swaggerv2doc:: http://petstore.swagger.io/v2/swagger.json
       pet
       store

Note
====

The old directive for Swagger 1.0 is still usable. For example,

.. code:: restructuredtext

    .. swaggerdoc:: http://petstore.swagger.wordnik.com/api/api-docs/pet
    .. swaggerdoc:: http://petstore.swagger.wordnik.com/api/api-docs/user
    .. swaggerdoc:: http://petstore.swagger.wordnik.com/api/api-docs/store
