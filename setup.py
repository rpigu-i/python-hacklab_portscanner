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
    version='0.0.1',
    description='Port scanner',
    long_description=long_description,
    maintainer='patamechanix',
    license='MIT',
    url='https://github.com/patamechanix/python_hacklab_portscanner',
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
