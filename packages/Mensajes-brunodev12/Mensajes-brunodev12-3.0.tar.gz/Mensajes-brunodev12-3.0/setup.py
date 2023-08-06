from setuptools import setup, find_packages

setup(
    name='Mensajes-brunodev12',
    version='3.0',
    description='Paquete para saludar y despedir',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mike Tower',
    author_email='hola@mike.dev',
    license_files=['LICENSE'],
    url='https://www.bruno.dev',
    packages=find_packages(),
    scripts=[],
    test_suite='tests',
    install_requires=[paquete.strip() for paquete in open("requirements.txt").readlines()],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
        ],
)
