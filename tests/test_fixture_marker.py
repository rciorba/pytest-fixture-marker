# -*- coding: utf-8 -*-
import pytest


def test_help_message(testdir):
    result = testdir.runpytest("--help")
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        ["fixture-marker:", "*--fixture-marker-expression=FIXTURE_MARKER_EXPRESSION*"]
    )


@pytest.mark.parametrize(
    "args,ini",
    [
        pytest.param(["-m fixture_foobar"], None, id="default"),
        pytest.param(["-m foobar_suffix"], "{}_suffix", id="expression-suffix"),
        pytest.param(
            ["-m foobar_arg", "--fixture-marker-expression={}_arg"], None, id="arg"
        ),
        pytest.param(
            ["-m foobar_arg", "--fixture-marker-expression={}_arg"],
            "{}_ini",
            id="arg-has-precedence-over-ini",
        ),
    ],
)
def test_mark_fixture(testdir, args, ini):
    """Test the tests are marked as expected"""

    if ini is not None:
        testdir.makeini(
            """
            [pytest]
            fixture_marker_expression = {}
            """.format(
                ini
            )
        )
    # create a temporary pytest test module
    testdir.makepyfile(
        """
        import pytest
        @pytest.fixture()
        def foobar():
            pass

        def test_uses(foobar):
            pass

        def test_not():
            pass
        """
    )

    assert isinstance(
        args, (list, tuple)
    )  # cause I already shot myself in the foot by not having a trailing comma

    # run pytest with the following cmd args
    result = testdir.runpytest("-v", "--strict-markers", *args)

    # fnmatch_lines does an assertion internally
    # check we collect 2 but only run the test using the fixture
    result.stdout.fnmatch_lines(
        ["*collected 2 items / 1 deselected*", "*::test_uses PASSED*"]
    )
    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
