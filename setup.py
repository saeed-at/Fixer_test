from setuptools import setup


setup(
    name='fixer-demo',
    version='0.2',
    description="Fixer service demo package",
    url='https://github.com/saeed-at/fixer_test',
    author='Saeed0047',
    author_email='saeed0047.sa@gmail.com',
    license='MIT',
    packages=['fixer'],
    install_requires=['requests'],
    zip_safe=False,
)

