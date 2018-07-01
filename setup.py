#! /usr/bin/env python
import os, sys

from setuptools import setup, find_packages

# from Cython.Build import cythonize
from distutils.extension import Extension
import numpy as np
import versioneer

from model_metadata.utils import get_cmdclass, get_entry_points


include_dirs = [
    np.get_include(),
    os.path.join(sys.prefix, "include"),
]


libraries = [
        "bmi_waves",
]


library_dirs = [
]


define_macros = [
]

undef_macros = [
]


extra_compile_args = [
]


ext_modules = [
    Extension(
        "waves._waves",
        ["waves/_waves.pyx"],
        language="c",
        include_dirs=include_dirs,
        libraries=libraries,
        library_dirs=library_dirs,
        define_macros=define_macros,
        undef_macros=undef_macros,
        extra_compile_args=extra_compile_args,
    )
]


packages = find_packages(include=["waves"])
pymt_components = [
    (
        "Waves=waves:Waves",
        "meta",
    )
]

setup(
    name="waves",
    author="Eric Hutton",
    description="Python interface to waves",
    version=versioneer.get_version(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=packages,
    cmdclass=get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass()),
    entry_points=get_entry_points(pymt_components),
)
