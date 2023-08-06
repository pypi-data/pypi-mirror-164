import setuptools

VERSION = '0.1.6'

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Akkoma.py',
    version=VERSION,
    author='spla',
    author_email='llemena_obrer.0u@icloud.com',
    description='Python wrapper for the [Akkoma](https://akkoma.dev/AkkomaGang/akkoma) API.',
    packages=['akkoma'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://git.mastodont.cat/spla/Akkoma.py',
    install_requires=['pytz', 'requests', 'python-dateutil', 'decorator'],
    project_urls={
        'Bug Tracker': 'https://git.mastodont.cat/spla/Akkoma.py/issues',
    },
    keywords='akkoma api microblogging',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "Intended Audience :: Developers",
        'Programming Language :: Python :: 3',
    ],
    include_package_data=True,
    python_requires = ">=3.8",
)
