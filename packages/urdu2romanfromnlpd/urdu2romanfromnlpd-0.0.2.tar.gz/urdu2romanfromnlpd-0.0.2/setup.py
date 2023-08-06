from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
    ]

setup(
    name='urdu2romanfromnlpd',
    version='0.0.2',
    description='A roman to urdu converter',
    long_description=open('readme.txt').read() + '\n\n' +open('CHANGELOG.txt').read(),
    url='',
    author='Mohammad Ayyaz Azeem',
    author_email='ayyaz.maju@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords = 'urdu2roman,roman',
    packages=find_packages(),
    install_requires=['urdu2romanfromnlpd']
)
