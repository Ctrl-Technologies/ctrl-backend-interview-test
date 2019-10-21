# Flask framework
import json
import locale
import platform
from urllib import parse

from flask import Flask, url_for


locale.setlocale(locale.LC_ALL, str('en_US.UTF-8'))

app = Flask(__name__)


def list_routes():
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = f'[{arg}]'

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = parse.unquote(
            f'name={rule.endpoint}, '
            f'METHODS=({methods}), '
            f'url=\'{url}\''
        )
        output.append(line)
    return sorted(output)


@app.route('/', methods=['GET'])
def root():
    return app.response_class(
        json.dumps({
            'message': 'Welcome to the Ctrl API test',
            'endpoints': list_routes()
        }, indent=4)
    )


@app.route('/health', methods=['GET'])
def health():
    platform_string = '{} - {} - {}'.format(
        platform.uname(),
        platform.system(),
        platform.processor()
    )
    return app.response_class(
        json.dumps({
            'message': 'I seem to be healthy',
            'whoami': platform_string,
        })
    )

