"""
Setup file for package `easychem`.
"""

from numpy.distutils.core import Extension, setup
import os

use_compiler_flags = True

if use_compiler_flags:
    extra_compile_args = [
        "-O3",
        "-funroll-loops",
        "-ftree-vectorize",
        "-msse",
        "-msse2",
        "-m3dnow"
    ]
    extra_compile_args_debug = [
        "-mcmodel=large",
        "-std=gnu",
        "-Wall",
        "-pedantic",
        "-fimplicit-none",
        "-fcheck-array-temporaries",
        "-fbacktrace",
        "-fcheck=all",
        "-ffpe-trap=zero,invalid",
        "-g",
        "-Og"
    ]
else:
    extra_compile_args = None


ecfortran = Extension(
    name = "easychem.ecfortran",
    sources = ["src/easychem/ecfortran.f95"],
    extra_compile_args = extra_compile_args
)

extensions = [ecfortran]


def setup_function():
    setup(
        name='easychem',
        version='1.0.0',

        description='Chemistry equilibrium computation tool',
        long_description=open(os.path.join(
            os.path.dirname(__file__), 'README.md')).read(),
        url='https://gitlab.com/EliseLei/easychem',

        author='Elise Lei',
        author_email='elise.lei@etu.minesparis.psl.eu',
        license='MIT License',

        packages=["easychem"],
        package_dir={'':'src'},
        include_package_data=True,
        install_requires=[
            'numpy'
        ],
        zip_safe=False,
        ext_modules=extensions,
        data_files=[('easychem', ['src/easychem/thermo_easy_chem_simp_own.inp'])]
    )


setup_function()