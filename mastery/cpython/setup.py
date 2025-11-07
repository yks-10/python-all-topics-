from setuptools import setup, Extension

module = Extension('hello', sources=['hello.c'])

setup(
    name='hello',
    version='1.0',
    description='Simple Hello World C Extension',
    ext_modules=[module]
)
