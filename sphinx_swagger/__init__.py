from .swagger_doc import swaggerdoc, visit_swaggerdoc_node, depart_swaggerdoc_node, SwaggerDocDirective
from .swaggerv2_doc import swaggerv2doc, visit_swaggerv2doc_node, depart_swaggerv2doc_node, SwaggerV2DocDirective

def setup(app):
    app.add_node(swaggerdoc,
                 html=(visit_swaggerdoc_node, depart_swaggerdoc_node),
                 latex=(visit_swaggerdoc_node, depart_swaggerdoc_node),
                 text=(visit_swaggerdoc_node, depart_swaggerdoc_node))

    app.add_directive('swaggerdoc', SwaggerDocDirective)

    app.add_node(swaggerv2doc,
                 html=(visit_swaggerv2doc_node, depart_swaggerv2doc_node),
                 latex=(visit_swaggerv2doc_node, depart_swaggerv2doc_node),
                 text=(visit_swaggerv2doc_node, depart_swaggerv2doc_node))

    app.add_directive('swaggerv2doc', SwaggerV2DocDirective)
