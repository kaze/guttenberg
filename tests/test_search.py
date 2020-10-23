from click.testing import CliRunner

from guttenberg_search.main import search


def test_search():
    runner = CliRunner()
    result = runner.invoke(
        search,
        ["-t", "My freedom and My bondage"],
    )

    expected_output = """
[
    {
        "bookshelves": [
            "African American Writers",
            "Slavery"
        ],
        "copyright": false,
        "download_count": 1828,
        "media_type": "Text",
        "name": "Douglass, Frederick",
        "title": "My Bondage and My Freedom",
        "xml": "http://www.gutenberg.org/ebooks/202.rdf"
    }
]
    """
    assert result
    assert result.output.strip() == expected_output.strip()
