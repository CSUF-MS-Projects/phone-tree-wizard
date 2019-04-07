import pydot

menu = {'Main menu':
                {'1 Source Savings Catcher Program': {
                    '1 Phone number and location': '',
                    '2 Customer': '',
                    '3 Current':'',
                    '4 Becoming Supplier':''
                 },
                '2 Track a walmart.com order': '',
                '3 All other walmart.com related questions': '',
                '* Hear this message again':''}
        }

# menu = {'dinner':
#             {'chicken':'good',
#              'beef':'average',
#              'vegetarian':{
#                    'tofu':'good',
#                    'salad':{
#                             'caeser':'bad',
#                             'italian':'average'}
#                    },
#              'pork':'bad'}
#         }

def draw(parent_name, child_name):
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)

def visit(node, parent=None):
    for k,v in node.items():
        if isinstance(v, dict):
            # We start with the root node whose parent is None
            # we don't want to graph the None node
            if parent:
                draw(parent, k)
            visit(v, k)
        else:
            draw(parent, k)
            # drawing the label using a distinct name
            #draw(k, k+'_'+v)
            #draw(k, k + '_' + v)

graph = pydot.Dot(graph_type='graph')
visit(menu)
graph.write_png('example1_graph.png')

