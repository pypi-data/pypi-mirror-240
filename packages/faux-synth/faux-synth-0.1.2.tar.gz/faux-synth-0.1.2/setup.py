from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='faux-synth',
    version='0.1.2',
    description='A package for generating mails and addresses',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/FelixSmtt/FauxSynth',
    author='Felix S',
    author_email='dev@smtt.me',
    license='MIT',
    packages=['FauxSynth', 'FauxSynth.address', 'FauxSynth.mail', 'FauxSynth.types'],
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
)
