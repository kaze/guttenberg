import click
import requests
import json
import pluggy
from pygments import highlight, lexers, formatters

from guttenberg_search import hookspecs
from guttenberg_search.plugins.output import json_output


BASE_URL = "http://gutendex.com/books/?search="


def colorize(formatted_json):
    return highlight(
        formatted_json.encode("UTF-8"),
        lexers.JsonLexer(),
        formatters.TerminalFormatter(),
    )


def get_plugin_manager():
    pm = pluggy.PluginManager(project_name='guttenberg-search')
    pm.add_hookspecs(hookspecs)
    pm.register(json_output)
    pm.load_setuptools_entrypoints('guttenberg-search')

    return pm


class Search:
    def __init__(self, term, hook, kwargs):
        self.term = term
        self.hook = hook
        self.kwargs = kwargs

    def make_request(self):
        resp = requests.get(f"{BASE_URL}{self.term}")
        return resp

    def run(self):
        resp = self.make_request()
        self.hook.print_output(resp=resp, config=self.kwargs)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--title", "-t", type=str, help="Title to search")
@click.option("--author", "-a", type=str, help="Author to search")
@click.option("--format", "-f", type=str, help="Output format", default='json')
@click.option("--colorize", "-c", type=bool, is_flag=True, help="Colorize output", default=False)
def search(title, author, **kwargs):
    if not (title or author):
        print("Pass either --title or --author")
        exit(-1)
    else:
        pm = get_plugin_manager()
        search = Search(title or author, pm.hook, kwargs)
        search.run()


def setup():
    pm = get_plugin_manager()
    pm.hook.get_click_group(group=cli)


if __name__ == '__main__':
    cli()

