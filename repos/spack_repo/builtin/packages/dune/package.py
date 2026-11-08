# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install dune
#
# You can edit this file again by typing:
#
#     spack edit dune
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Dune(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/ocaml/dune/releases/download/3.24.2/dune-3.24.2.tbz"

    # FIXME: Uncomment and add the upstream supplier (organization or author).
    # If unknown or inapplicable, remove this entire block.
    # supplier = organization_or_author

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("3.24.2", sha256="472798691b0216daf538709f0f4703b3617ef24ad0866c9096068baaba4d762a")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("ocaml@4.21:", type=("build", "link"))

    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
        pass

    def build(self, spec, prefix):
        make("release")

    def install(self, spec, prefix):
        make("install", f"PREFIX={prefix}")
