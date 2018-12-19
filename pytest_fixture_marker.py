# -*- coding: utf-8 -*-


def pytest_addoption(parser):
    group = parser.getgroup("fixture-marker")
    group.addoption(
        "--fixture-marker-expression",
        action="store",
        dest="fixture_marker_expression",
        default="{}_fixture",
        help="Cocos.",
    )


def pytest_collection_modifyitems(config, items):
    expression = config.getoption("fixture_marker_expression")
    for item in items:
        for fixture in item.fixturenames:
            item.add_marker(expression.format(fixture))
