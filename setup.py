from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    )

tests_require = [
    'zope.app.testing',
    'zope.app.zcmlfiles',
    'zope.component',
    'zope.configuration',
    'zope.testing',
    ]

setup(
    name='grokcore.site',
    version='1.1dev',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='http://grok.zope.org',
    download_url='http://pypi.python.org/pypi/grokcore.site',
    description='Grok-like configuration for Zope local site and utilities',
    long_description=long_description,
    license='ZPL',
    classifiers=['Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Zope Public License',
                 'Programming Language :: Python',
                 'Framework :: Zope3',
                 ],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['grokcore'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools',
                      'ZODB3',
                      'grokcore.component',
                      'martian',
                      'zope.annotation',
                      'zope.app.component',
                      'zope.app.container',
                      'zope.interface',
                      ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
