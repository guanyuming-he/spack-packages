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
#     spack install racuda
#
# You can edit this file again by typing:
#
#     spack edit racuda
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack.package import *


class Racuda(AutotoolsPackage):
    """The artifact for Muller and Hoffmann's POPL 2021 paper Modeling and
    Analyzing Evaluation Cost of CUDA Kernels"""

    git = "https://github.com/smuller/RaCUDA.git"
    supplier = "smuller"
    maintainers("guanyuming-he")
    license("BSD-2-Clause-Views", checked_by="guanyuming-he")

    version("main", branch="main")

    depends_on("gmp@4.2:", type=("build", "link"))
    depends_on("mpfr@2.2:", type=("build", "link"))
    depends_on("gsl@1.6:", type=("build"))
    depends_on("ocaml@4.0:", type=("build"))
	# for all opam related, please use the modified opam root,
	# and install manually with opam install.
    depends_on("opam", type=("build", "run"))
    depends_on("opam-ocamlbuild", type=("build", "run"))

    # The readme didn't mention these which turn out to be needed
    depends_on("opam-ocamlfind", type=("build", "run"))
    depends_on("opam-menhir", type=("build", "run"))
    #depends_on("dune", type=("build"))
    depends_on("clp", type=("build", "link"))
    depends_on("coinutils", type=("build", "link"))

    depends_on("c", type=("build"))
    depends_on("cxx", type=("build"))

    def configure_args(self):
        clpdir = self.spec["clp"].prefix
        coindir = self.spec["coinutils"].prefix
        return [
            "-clp",
            clpdir,
            "-coin-utils",
            coindir,
        ]
