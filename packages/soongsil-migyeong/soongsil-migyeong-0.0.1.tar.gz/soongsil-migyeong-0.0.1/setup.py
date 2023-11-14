from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='soongsil-migyeong',
    version='0.0.1',
    description='PyPI를 활용한 패키지 배포 과정 알아보기 (tutorial)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Junwon Moon',
    author_email="diayoak@kakao.com",
    url='https://github.com/diayoak/soongsil-migyeong',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['soongsil', 'migyeong'],
    python_requires='>=3',
    package_data={},
    entry_points={
        'console_scripts': [
            'git-tagup=git_tagup.__main__:main',
            'gtu=git_tagup.__main__:main',
        ],
    },
)