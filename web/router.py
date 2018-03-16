from collections import namedtuple
import os

from web.handlers import index, index1, tick, create_project


Route = namedtuple('Route', ['name', 'method', 'path', 'handler'])

routes = [
    Route('index', 'GET', '/', index),
    Route('tick', 'GET', '/tick', tick),
    Route('create', 'POST', '/create', create_project)
]

#async def catch_all(request):
#	print("catch all")
#    return



def configure_handlers(app, routing_map, prefix=None):
    for routing in routing_map:
        path = prefix + routing.path if prefix is not None else routing.path
        app.router.add_route(routing.method, path, routing.handler, name=routing.name)
        #app.router.add_static('/static/', path=str(os.getcwd() + '/static/'), name="static")
    app.router.add_route("*", "/{tail:.*}", index)

