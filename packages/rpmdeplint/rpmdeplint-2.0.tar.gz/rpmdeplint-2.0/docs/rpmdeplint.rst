rpmdeplint
----------

.. program:: rpmdeplint check-sat

Synopsis
~~~~~~~~

| :program:`rpmdeplint` COMMAND [:option:`--repo` NAME,URL] [RPMPATH]

Description
~~~~~~~~~~~

The :program:`rpmdeplint` command tests the dependency satisfiability of
specified RPM packages against given repositories.

Options
~~~~~~~

.. option:: --repo NAME[,URL_OR_PATH], -r NAME[,URL_OR_PATH]

   Load yum repository specified by name or by URL/path.

   If the repo is already configured in :file:`/etc/yum.repos.d/{*}.repo`
   simply specify its name like::

     --repo=fedora

   Otherwise, specify a name and the base URL or metalink. The NAME is for
   descriptive purposes only in this case. It has no impact on dependency
   resolution. If rpmdeplint identifies a dependency issue relating to a package
   in this repo, the NAME will appear in the error message. Examples::

     --repo=fedora,https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/x86_64/os/

     --repo=fedora,https://mirrors.fedoraproject.org/metalink?repo=rawhide&arch=x86_64

   You can also specify a local filesystem path instead of a URL, like::

     --repo=myrepo,/home/me/my_repo

   Note that the URL/path should point at a directory containing
   ``repodata/repomd.xml``. Examples::

.. option:: --repos-from-system, -R

   Use yum repos from the system-wide configuration in
   :file:`/etc/yum.repos.d/{*}.repo`. Repos which are disabled in the
   configuration (``enabled=0``) are ignored.

   This option can be combined with one or more :option:`--repo` options.

.. option:: --arch ARCH, -a ARCH

   Only consider packages for ARCH when solving dependencies. If a repo
   contains packages for any other arches, they will be ignored.

   Note that the traditional RPM arch compatibility rules are applied, which
   means that ``noarch`` packages and "inferior" arch packages are also
   included (for example, ``i686`` implicitly includes ``i386``).

   This option is normally *not* required, because distribution repos are
   normally split by arch (including the various special cases for multilib).

Arguments
~~~~~~~~~

.. option:: RPMPATH

   Path to an RPM package. This can be a relative or absolute filesystem path.

Commands
~~~~~~~~

check
  Performs each of the checks listed below.

check-sat
  Checks for unmet dependencies with the given RPM packages against the given
  repositories.
  Each unmet dependency is listed.

check-repoclosure
  Checks for unmet dependencies in the given repositories, when considered
  together with the given packages. This check is similar to *check-sat*,
  except it checks only packages in the repositories, not the packages under
  test.

  Packages are only considered to be available for dependency resolution if
  they are the latest version and not obsoleted by any other package.
  Therefore this check can detect problems where a package under test is
  updating an existing package in the repositories, but it no longer provides
  a requirement needed by some other package in the repositories.

  In case a pre-existing repoclosure problem is found (that is, the same
  problem exists when considering only the repositories without the packages
  under test) a warning is printed to stderr, but the check is *not* considered
  to have failed.

check-conflicts
  Checks for undeclared file conflicts in the given RPM packages: that is, when
  a given package contains a file also contained in another package.

  This command will not report a file as conflicting between two packages if:

  * there is an explicit RPM ``Conflicts`` between the two packages; or
  * the file’s checksum, permissions, owner, and group are identical in both
    packages (RPM allows both packages to own the file in this case); or
  * the file’s color is different between the two packages (RPM will
    silently resolve the conflict in favour of the 64-bit file).

check-upgrade
  Checks that there are no existing packages in the repositories which would
  upgrade or obsolete the given packages.

  If this check fails, it means that the package under test will never be
  installed (since the package manager will always pick the newer or obsoleting
  package from the repositories instead) which is not desirable, assuming the
  package is intended as an update.

list-deps
  All dependencies will be listed for each given RPM package.

Exit status
~~~~~~~~~~~

0
    Checks ran successfully, and no problems were found

1
    Error occurred while running checks (including network errors downloading
    repodata)

2
    Command-line usage error

3
    Problems were found with the packages under test

Examples
~~~~~~~~

Imagine you have produced a new pre-release build of your package, and you want
to check if it will cause dependency errors in Fedora::

    rpmdeplint check \
        --repo=fedora,https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/x86_64/os/ \
        greenwave-0.6.1-0.git.2.2529bfb.fc29.noarch.rpm

You don't have to specify the URLs of the repos if they are already configured in `/etc/yum.repos.d/`::

    rpmdeplint check \
        --repo=fedora --repo=updates \
        greenwave-0.6.1-0.git.2.2529bfb.fc29.noarch.rpm

or use all configured repos::

    rpmdeplint check \
        --repos-from-system \
        greenwave-0.6.1-0.git.2.2529bfb.fc29.noarch.rpm

You can also use a local filesystem path instead of an absolute URL for the
repos to test against. For example, if you are offline you could re-use your
local dnf cache. (Note that rpmdeplint may need to fetch packages for file
conflict checking and this step will fail if you use an incomplete repo such as
the dnf cache.)

::

    rpmdeplint check \
        --repo=rawhide,/var/cache/dnf/rawhide-2d95c80a1fa0a67d/
        greenwave-0.6.1-0.git.2.2529bfb.fc29.noarch.rpm

Bugs
~~~~

Bug reports can be submitted to https://github.com/fedora-ci/rpmdeplint/issues.
