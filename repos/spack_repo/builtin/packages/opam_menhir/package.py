# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.opam import OpamPackage

from spack.package import *


class OpamMenhir(OpamPackage):
    """Menhir is an LR(1) parser generator for OCaml."""

    has_code = False
    homepage = "https://cambium.inria.fr/~fpottier/menhir"

    maintainers("guanyuming-he")

    version("20260209")

    depends_on("c", type="build")  # generated
    depends_on("opam", type=("build", "run"))

    opam_name = "menhir"

