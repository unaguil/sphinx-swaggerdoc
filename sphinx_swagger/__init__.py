from swagger_doc import swaggerdoc, visit_swaggerdoc_node, depart_swaggerdoc_node, SwaggerDocDirective

def setup(app):
    app.add_node(swaggerdoc,
                 html=(visit_swaggerdoc_node, depart_swaggerdoc_node),
                 latex=(visit_swaggerdoc_node, depart_swaggerdoc_node),
                 text=(visit_swaggerdoc_node, depart_swaggerdoc_node))

    app.add_directive('swaggerdoc', SwaggerDocDirective)