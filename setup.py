from setuptools import setup, find_packages
import io

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.md')

setup(
    name='hacklab_portscanner',
    version='3.0.0',
    description='Port scanner',
    long_description=long_description,
    maintainer='rpigu-i',
    license='MIT',
    url='https://github.com/rpigu-i/python_hacklab_portscanner',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    entry_points={
        'console_script': [
            'hacklab_portscanner = hacklab_portscanner.__main__:main'
        ],
    },
    install_requires=[
    ]
)
