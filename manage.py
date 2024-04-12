#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import cherrypy
from django.core.management import execute_from_command_line
from localserver.wsgi import application


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'localserver.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # main()

    ssl_certfile = 'cert.pem'
    ssl_keyfile = 'key.pem'

    cherrypy.config.update({
        'server.socket_host': '192.168.101.5',
        'server.socket_port': 8000,
        'server.ssl_module': 'builtin',
        'server.ssl_certificate': ssl_certfile,
        'server.ssl_private_key': ssl_keyfile
    })

    cherrypy.tree.graft(application, '/')
    cherrypy.engine.start()
    cherrypy.engine.block()
