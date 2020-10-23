import json

import requests

from guttenberg_search.plugins.output.json_output import print_output


def test_print_output(capsys):
    resp = requests.get("http://gutendex.com/books/?search=Kafka")
    print_output(resp, {})
    # import pdb; pdb.set_trace()
    captured = capsys.readouterr()
    assert len(json.loads(captured.out)) >= 1
