# -*- coding: utf-8 -*-

import unittest
from sphinx_testing import with_app

class TestSphinxSwagger(unittest.TestCase):

    @with_app(buildername='html', srcdir='tests/docs/basic/')
    def test_build_html(self, app, status, warning):
        app.builder.build_all()
        html = (app.outdir / 'index.html').read_text()

        output = open('/tmp/output.html', 'w')
        output.write(html)
        output.close()
