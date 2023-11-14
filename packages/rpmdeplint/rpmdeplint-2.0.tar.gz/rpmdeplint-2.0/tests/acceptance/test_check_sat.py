# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import shutil

from data_setup import run_rpmdeplint
from rpmfluff import SimpleRpmBuild
from rpmfluff.yumrepobuild import YumRepoBuild


def test_shows_error_for_rpms(request, dir_server):
    p2 = SimpleRpmBuild("b", "0.1", "1", ["i386"])
    baserepo = YumRepoBuild((p2,))
    baserepo.make("i386")
    dir_server.basepath = baserepo.repoDir

    p1 = SimpleRpmBuild("a", "0.1", "1", ["i386"])
    p1.add_requires("doesnotexist")
    p1.make()

    def cleanUp():
        shutil.rmtree(baserepo.repoDir)
        p2.clean()
        p1.clean()

    request.addfinalizer(cleanUp)

    exitcode, out, err = run_rpmdeplint(
        [
            "rpmdeplint",
            "check-sat",
            f"--repo=base,{dir_server.url}",
            p1.get_built_rpm("i386"),
        ]
    )
    assert exitcode == 3
    assert (
        err
        == "Problems with dependency set:\nnothing provides doesnotexist needed by a-0.1-1.i386\n"  # noqa: E501
    )
    assert out == ""


def test_error_if_repository_names_not_provided(tmp_path):
    exitcode, out, err = run_rpmdeplint(
        ["rpmdeplint", "check-sat", f"--repo={tmp_path}"]
    )
    assert exitcode == 2
    assert f"error: argument -r/--repo: invalid repo value: '{tmp_path}'" in err
