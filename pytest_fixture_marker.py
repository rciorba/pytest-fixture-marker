# -*- coding: utf-8 -*-


def pytest_addoption(parser):
    group = parser.getgroup("fixture-marker")
    help_text = (
        "Format string to configure how the marker names get generated. "
        "Defaults to fixture_{}"
    )
    parser.addini("fixture_marker_expression", help=help_text)
    group.addoption(
        "--fixture-marker-expression",
        action="store",
        dest="fixture_marker_expression",
        help=help_text,
    )


def pytest_collection_modifyitems(config, items):
    expression = config.getoption("fixture_marker_expression")
    if expression is None:
        expression = config.getini("fixture_marker_expression") or "fixture_{}"
    markers = set()
    for item in items:
        for fixture in item.fixturenames:
            marker = expression.format(fixture)
            if marker not in markers:
                config.addinivalue_line(
                    "markers", "{}: mark test as using the named fixture".format(marker)
                )
                markers.add(marker)
            item.add_marker(marker)
