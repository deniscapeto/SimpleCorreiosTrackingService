from setuptools import find_packages, setup


def read(fname):
    with open(fname) as f:
        return f.read()


description = 'Simple Correios Tracking Service'
try:
    long_description = read('README.md')
except IOError:
    long_description = description


download_url = 'https://github.com/deniscapeto/scts/tarball/master'

setup(
    name='stsc',
    version='0.0.0',
    install_requires=[],
    url='https://github.com/deniscapeto/stsc',
    author='Luiza Labs',
    author_email='contato@deniscapeto.com',
    keywords='correios tracking',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    download_url=download_url,
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)