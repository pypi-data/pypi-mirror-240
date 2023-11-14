# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import shutil

from data_setup import run_rpmdeplint
from rpmfluff import SimpleRpmBuild
from rpmfluff.yumrepobuild import YumRepoBuild


def test_catches_soname_change(request, dir_server):
    # This is the classic mistake repoclosure is supposed to find... the
    # updated package has changed its soname, causing some other package's
    # dependencies to become unresolvable.
    p_older = SimpleRpmBuild("a", "4.0", "1", ["i386"])
    p_older.add_provides("libfoo.so.4")
    p_depending = SimpleRpmBuild("b", "0.1", "1", ["i386"])
    p_depending.add_requires("libfoo.so.4")
    baserepo = YumRepoBuild([p_older, p_depending])
    baserepo.make("i386")
    dir_server.basepath = baserepo.repoDir

    p_newer = SimpleRpmBuild("a", "5.0", "1", ["i386"])
    p_newer.add_provides("libfoo.so.5")
    p_newer.make()

    def cleanUp():
        shutil.rmtree(baserepo.repoDir)
        p_depending.clean()
        p_older.clean()
        p_newer.clean()

    request.addfinalizer(cleanUp)

    exitcode, out, err = run_rpmdeplint(
        [
            "rpmdeplint",
            "check-repoclosure",
            f"--repo=base,{dir_server.url}",
            p_newer.get_built_rpm("i386"),
        ]
    )
    assert exitcode == 3
    assert err == (
        "Dependency problems with repos:\n"
        "package b-0.1-1.i386 requires libfoo.so.4, but none of the providers can be installed\n"  # noqa: E501
    )


def test_catches_soname_change_with_package_rename(request, dir_server):
    # Slightly more complicated version of the above, where the old provider is
    # not being updated but rather obsoleted.
    p_older = SimpleRpmBuild("foolib", "4.0", "1", ["i386"])
    p_older.add_provides("libfoo.so.4")
    p_depending = SimpleRpmBuild("b", "0.1", "1", ["i386"])
    p_depending.add_requires("libfoo.so.4")
    baserepo = YumRepoBuild([p_older, p_depending])
    baserepo.make("i386")
    dir_server.basepath = baserepo.repoDir

    p_newer = SimpleRpmBuild("libfoo", "5.0", "1", ["i386"])
    p_newer.add_obsoletes("foolib < 5.0-1")
    p_newer.add_provides("libfoo.so.5")
    p_newer.make()

    def cleanUp():
        shutil.rmtree(baserepo.repoDir)
        p_depending.clean()
        p_older.clean()
        p_newer.clean()

    request.addfinalizer(cleanUp)

    exitcode, out, err = run_rpmdeplint(
        [
            "rpmdeplint",
            "check-repoclosure",
            f"--repo=base,{dir_server.url}",
            p_newer.get_built_rpm("i386"),
        ]
    )
    assert exitcode == 3
    assert err == (
        "Dependency problems with repos:\n"
        "package b-0.1-1.i386 requires libfoo.so.4, but none of the providers can be installed\n"  # noqa: E501
    )


def test_ignores_dependency_problems_in_packages_under_test(request, dir_server):
    # The check-sat command will find and report these problems, it would be
    # redundant for check-repoclosure to also report the same problems.
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
            "check-repoclosure",
            f"--repo=base,{dir_server.url}",
            p1.get_built_rpm("i386"),
        ]
    )
    assert exitcode == 0
    assert err == ""


def test_ignores_problems_in_older_packages(request, dir_server):
    # We only care if the *latest* version of each package in the repos is
    # satisfied. If there are dependency problems with an older version, it is
    # irrelevant because nobody will be installing it anyway.
    p_older = SimpleRpmBuild("a", "4.0", "1", ["i386"])
    p_older.add_provides("libfoo.so.4")
    p_older.add_provides("libfoo.so.5")
    p_older_depending = SimpleRpmBuild("b", "0.1", "1", ["i386"])
    p_older_depending.add_requires("libfoo.so.4")
    p_newer_depending = SimpleRpmBuild("b", "0.2", "1", ["i386"])
    p_newer_depending.add_requires("libfoo.so.5")
    baserepo = YumRepoBuild([p_older, p_older_depending, p_newer_depending])
    baserepo.make("i386")
    dir_server.basepath = baserepo.repoDir

    p_newer = SimpleRpmBuild("a", "5.0", "1", ["i386"])
    p_newer.add_provides("libfoo.so.5")
    p_newer.make()

    def cleanUp():
        shutil.rmtree(baserepo.repoDir)
        p_older_depending.clean()
        p_newer_depending.clean()
        p_older.clean()
        p_newer.clean()

    request.addfinalizer(cleanUp)

    exitcode, out, err = run_rpmdeplint(
        [
            "rpmdeplint",
            "check-repoclosure",
            f"--repo=base,{dir_server.url}",
            p_newer.get_built_rpm("i386"),
        ]
    )
    assert exitcode == 0


def test_ignores_problems_in_obsoleted_packages(request, dir_server):
    # As above, we also don't care about any dependency problems in packages
    # that have been obsoleted.
    p_older = SimpleRpmBuild("a", "4.0", "1", ["i386"])
    p_older.add_provides("libfoo.so.4")
    p_older.add_provides("libfoo.so.5")
    p_obsolete_depending = SimpleRpmBuild("foofouruser", "1.0", "1", ["i386"])
    p_obsolete_depending.add_requires("libfoo.so.4")
    p_newer_depending = SimpleRpmBuild("foofiveuser", "0.1", "1", ["i386"])
    p_newer_depending.add_requires("libfoo.so.5")
    p_newer_depending.add_obsoletes("foofouruser <= 1.0-1")
    baserepo = YumRepoBuild([p_older, p_obsolete_depending, p_newer_depending])
    baserepo.make("i386")
    dir_server.basepath = baserepo.repoDir

    p_newer = SimpleRpmBuild("a", "5.0", "1", ["i386"])
    p_newer.add_provides("libfoo.so.5")
    p_newer.make()

    def cleanUp():
        shutil.rmtree(baserepo.repoDir)
        p_obsolete_depending.clean()
        p_newer_depending.clean()
        p_older.clean()
        p_newer.clean()

    request.addfinalizer(cleanUp)

    exitcode, out, err = run_rpmdeplint(
        [
            "rpmdeplint",
            "check-repoclosure",
            f"--repo=base,{dir_server.url}",
            p_newer.get_built_rpm("i386"),
        ]
    )
    assert exitcode == 0


def test_warns_on_preexisting_repoclosure_problems(request, dir_server):
    # If the repos have some existing dependency problems, we don't want that
    # to be an error -- otherwise a bad repo will make it impossible to get any
    # results until the problem is fixed.
    p2 = SimpleRpmBuild("b", "0.1", "1", ["i386"])
    p2.add_requires("doesnotexist")
    baserepo = YumRepoBuild((p2,))
    baserepo.make("i386")
    dir_server.basepath = baserepo.repoDir

    p1 = SimpleRpmBuild("a", "0.1", "1", ["i386"])
    p1.make()

    def cleanUp():
        shutil.rmtree(baserepo.repoDir)
        p2.clean()
        p1.clean()

    request.addfinalizer(cleanUp)

    exitcode, out, err = run_rpmdeplint(
        [
            "rpmdeplint",
            "check-repoclosure",
            f"--repo=base,{dir_server.url}",
            p1.get_built_rpm("i386"),
        ]
    )
    assert exitcode == 0
    assert (
        "Ignoring pre-existing repoclosure problem: "
        "nothing provides doesnotexist needed by b-0.1-1.i386\n" in err
    )


def test_works_on_different_platform_to_current(request, dir_server):
    grep = SimpleRpmBuild("grep", "2.20", "3.el6", ["ppc64"])

    needs_grep = SimpleRpmBuild("search-tool-5000", "1.0", "3.el6", ["ppc64"])
    needs_grep.add_requires("grep = 2.20-3.el6")

    baserepo = YumRepoBuild((grep, needs_grep))
    baserepo.make("ppc64")
    dir_server.basepath = baserepo.repoDir

    package_to_test = SimpleRpmBuild("test-tool", "10", "3.el6", ["ppc64"])
    package_to_test.make()

    def cleanUp():
        shutil.rmtree(baserepo.repoDir)
        grep.clean()
        needs_grep.clean()
        package_to_test.clean()

    request.addfinalizer(cleanUp)

    exitcode, out, err = run_rpmdeplint(
        [
            "rpmdeplint",
            "check-repoclosure",
            f"--repo=base,{dir_server.url}",
            package_to_test.get_built_rpm("ppc64"),
        ]
    )

    assert exitcode == 0
    assert out == ""
    assert err == ""


def test_arch_set_manually_is_passed_to_sack(request, dir_server):
    grep = SimpleRpmBuild("grep", "2.20", "3.el6", ["i686"])

    needs_grep = SimpleRpmBuild("search-tool-5000", "1.0", "3.el6", ["i686"])
    needs_grep.add_requires("grep = 2.20-3.el6")

    package_to_test = SimpleRpmBuild("test-tool", "10", "3.el6", ["i586"])
    package_to_test.make()

    baserepo = YumRepoBuild((grep, needs_grep))
    baserepo.make("i686")
    dir_server.basepath = baserepo.repoDir

    def cleanUp():
        shutil.rmtree(baserepo.repoDir)
        grep.clean()
        needs_grep.clean()
        package_to_test.clean()

    request.addfinalizer(cleanUp)

    exitcode, out, err = run_rpmdeplint(
        [
            "rpmdeplint",
            "check-repoclosure",
            "--arch=i586",
            f"--repo=base,{dir_server.url}",
            package_to_test.get_built_rpm("i586"),
        ]
    )

    assert exitcode == 0
    assert out == ""
    assert err == ""

    exitcode, out, err = run_rpmdeplint(
        [
            "rpmdeplint",
            "check-repoclosure",
            "--arch=i686",
            f"--repo=base,{dir_server.url}",
            package_to_test.get_built_rpm("i586"),
        ]
    )

    assert exitcode == 0
    assert out == ""
    assert err == ""
