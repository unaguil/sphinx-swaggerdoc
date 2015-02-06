from swagger_doc import swagger_doc, visit_swaggerdoc_node, depart_swaggerdoc_node, SwaggerDocDirective

def setup(app):
    app.add_node(swagger_doc,
                 html=(visit_swaggerdoc_node, depart_swaggerdoc_node),
                 latex=(visit_swaggerdoc_node, depart_swaggerdoc_node),
                 text=(visit_swaggerdoc_node, depart_swaggerdoc_node))

    app.add_directive('swaggerdoc', SwaggerDocDirective)