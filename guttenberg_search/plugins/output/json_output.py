import json

from pygments import highlight, lexers, formatters
import pluggy


hookimpl = pluggy.HookimplMarker(project_name="guttenberg-search")


def colorize(formatted_json):
    return highlight(
        formatted_json.encode("UTF-8"),
        lexers.JsonLexer(),
        formatters.TerminalFormatter(),
    )


@hookimpl
def print_output(resp, config):
    """Print output"""
    data = resp.json()

    table = [
        {
            "name": result["authors"][0]["name"],
            "bookshelves": result["bookshelves"],
            "copyright": result["copyright"],
            "download_count": result["download_count"],
            "title": result["title"],
            "media_type": result["media_type"],
            "xml": result["formats"]["application/rdf+xml"],
        }
        for result in data["results"]
    ]

    indent = config.get("indent", 4)

    if config.get('format', '') == 'json':
        formatted_json = json.dumps(table, sort_keys=True, indent=indent)

        if config.get('colorize'):
            print(colorize(formatted_json))
        else:
            print(formatted_json)

