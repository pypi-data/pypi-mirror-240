# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

from data_setup import run_rpmdeplint


def test_prints_usage_when_no_subcommand_is_given():
    exitcode, out, err = run_rpmdeplint(["rpmdeplint"])

    assert "usage:" in err
    assert "error: the following arguments are required: subcommand" in err
    assert exitcode == 2


# https://bugzilla.redhat.com/show_bug.cgi?id=1537961
def test_prints_usage_when_no_repos_are_defined():
    exitcode, out, err = run_rpmdeplint(["rpmdeplint", "check", "some.rpm"])
    assert "usage:" in err
    assert "error: no repos specified to test against" in err
    assert exitcode == 2
