from setuptools import setup

setup(
    name='YaGPT',
    version='0.1.0',
    packages=['YaGPT'],
    install_requires=[
        'requests'
    ],
    author='Artem Mot',
    author_email='artem174a@yandex.ru',
    description='This Python library provides a simple wrapper for interacting with Yandex Language Models, making it easy to send requests for text generation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Artem174a/YaGPT_API_metods/',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
