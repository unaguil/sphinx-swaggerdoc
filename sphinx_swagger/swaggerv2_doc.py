# -*- coding: utf-8 -*-
from docutils import nodes
import traceback

from docutils.parsers.rst import Directive

from sphinx.locale import _

import requests
import json

class swaggerv2doc(nodes.Admonition, nodes.Element):
    pass

def visit_swaggerv2doc_node(self, node):
    self.visit_admonition(node)

def depart_swaggerv2doc_node(self, node):
    self.depart_admonition(node)

class SwaggerV2DocDirective(Directive):

    # this enables content in the directive
    has_content = True

    def processSwaggerURL(self, url):
        r = requests.get(url)
        return r.json()

    def create_item(self, key, value):
        para = nodes.paragraph()
        para += nodes.strong('', key)
        para += nodes.Text(value)

        item = nodes.list_item()
        item += para

        return item

    def expand_values(self, list):
        expanded_values = ''
        for value in list:
            expanded_values += value + ' '

        return expanded_values

    def make_method(self, path, method_type, method):
        swagger_node = swaggerv2doc(path)
        swagger_node += nodes.title(path, method_type.upper() + ' ' + path)

        content = nodes.paragraph()
        content += nodes.Text(method['summary'])

        bullet_list = nodes.bullet_list()
        bullet_list += self.create_item('Description: ', method.get('description', ''))
        bullet_list += self.create_item('Consumes: ', self.expand_values(method.get('consumes', '')))
        bullet_list += self.create_item('Produces: ', self.expand_values(method.get('produces', '')))
        content += bullet_list

        swagger_node += content

        return [swagger_node]

    def group_tags(self, api_desc):
        groups = {}

        for tag in api_desc['tags']:
            groups[tag['name']] = []

        for path, methods in api_desc['paths'].items():
            for method_type, method in methods.items():
                for tag in method['tags']:
                    groups[tag].append((path, method_type, method))

        return groups

    def create_section(self, title):
        section = nodes.section(ids=[title])
        section += nodes.title(title, title)
        return section

    def run(self):
        try:
            api_desc = self.processSwaggerURL(self.content[0])

            groups = self.group_tags(api_desc)

            entries = []
            for tag_name, methods in groups.items():
                section = self.create_section(tag_name)

                for path, method_type, method in methods:
                    section += self.make_method(path, method_type, method)

                entries.append(section)

            return entries
        except Exception as e:
            error_message = 'Unable to process URL: %s' % self.content[0]
            print error_message
            traceback.print_exc()

            error = nodes.error('')
            para_error = nodes.paragraph()
            para_error += nodes.Text(error_message + '. Please check that the URL is a valid Swagger api-docs URL and it is accesible')
            para_error_detailed = nodes.paragraph()
            para_error_detailed = nodes.strong('Processing error. See console output for a more detailed error')
            error += para_error
            error += para_error_detailed
            return [error]
