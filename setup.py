from setuptools import setup
from setuptools import find_packages

version = '1.0.dev0'
description = open("README.rst").read() + "\n" + open("CHANGES.rst").read()

setup(
    name='collective.explicitacquisition',
    version=version,
    description="Disallow access to acquired content outside the current path.",  # noqa
    long_description=description,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='traversal acquisition',
    author='Godefroid Chapelle',
    url='https://github.com/collective/collective.explicitacquisition',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFCore',
        'Products.CMFPlone',
        'Zope2',  # ZPublisher
        'zExceptions',
        'zope.component',
        'zope.interface',
    ],
    extras_require={
        'test': [
            'plone.testing',
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """
)