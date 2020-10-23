import pluggy


hookspec = pluggy.HookspecMarker(project_name="guttenberg-search")


@hookspec
def print_output(resp, config):
    """Print formatted output"""

