# coding: utf-8
from pathlib import Path
import re

from pkg_resources import Requirement
from setuptools import find_packages
from setuptools import setup


_COMMENT_RE = re.compile(r'(^|\s)+#.*$')


def _get_requirements(file_path):
    if isinstance(file_path, str):
        file_path = Path(file_path)
    if not file_path.is_absolute():
        file_path = Path(__file__).parent.joinpath(file_path)

    with open(file_path, 'r') as file:
        for line in file:
            line = _COMMENT_RE.sub('', line)
            line = line.strip()
            if line.startswith('-r '):
                for req in _get_requirements(
                    Path(file_path).parent.joinpath(line[3:])
                ):
                    yield req
            elif line:
                req = Requirement(line)
                req_str = req.name + str(req.specifier)
                if req.marker:
                    req_str += '; ' + str(req.marker)
                yield req_str


setup(
    name='librbac',
    author="BARS Group",
    author_email='education_dev@bars-open.ru',
    description='Общая библиотека контроля доступа для микросервисов',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://stash.bars-open.ru/projects/EDUEO/repos/librbac/',
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    dependency_links=(
        'http://pypi.bars-open.ru/simple/m3-builder',
    ),
    setup_requires=(
        'm3-builder>=1.2,<2',
    ),
    install_requires=tuple(_get_requirements('requirements/prod.txt')),
    set_build_info=Path(__file__).parent,
)
