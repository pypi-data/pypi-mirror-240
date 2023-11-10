from setuptools import setup, find_packages


setup(
    name='ntt-injector',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
    ],
    author='threezinedine',
    author_email='threezinedine@email.com',
    description='The small library for configuring the depedency injector design pattern',
    long_description='Go to source project to get more information (https://github.com/threezinedine/ntt-injector)',
    long_description_content_type='text/markdown',
    url='https://github.com/threezinedine/ntt-injector',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='dependency injector',
    project_urls={
        'Source': 'https://github.com/threezinedine/ntt-injector',
        'Tracker': 'https://github.com/threezinedine/ntt-injector/issues',
    },
)