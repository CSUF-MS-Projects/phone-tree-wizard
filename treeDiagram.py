"""
Purpose:  Create tree diagram from dictionary
"""


import pydot

class drawTreeDiagram(object):
    def drawDiagram(self, company):
        pass

class pyDotDraw(drawTreeDiagram):
    def __init__(self):
        super(pyDotDraw, self).__init__()


    def drawDiagram(self, company):
        menu = {'Main menu':
            {'1 Source Savings Catcher Program': {
                '1 Phone number and location': '',
                '2 Customer': '',
                '3 Current employee': '',
                '4 Becoming a Walmart supplier': ''
            },
                '2 Track a walmart.com order': '',
                '3 All other walmart.com related questions': '',
                '* Hear this message again': ''}
        }

        def draw(parent_name, child_name):
            edge = pydot.Edge(parent_name, child_name)
            graph.add_edge(edge)

        def visit(node, parent=None):
            for k,v in node.items():
                if isinstance(v, dict):
                    # start with the root node whose parent is None
                    # exclude the None node
                    if parent:
                        draw(parent, k)
                    visit(v, k)
                else:
                    draw(parent, k)

        graph = pydot.Dot(graph_type='graph')
        visit(menu)
        print("Generating phone menu in pyDotDraw")
        graph.write_png('tree_graph.png')