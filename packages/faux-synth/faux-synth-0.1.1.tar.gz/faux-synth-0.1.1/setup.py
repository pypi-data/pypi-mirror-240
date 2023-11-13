from setuptools import setup

setup(
    name='faux-synth',
    version='0.1.1',
    description='A package for generating mails and addresses',
    url='https://github.com/FelixSmtt/FauxSynth',
    author='Felix S',
    author_email='felix-dev@smtt.me',
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
