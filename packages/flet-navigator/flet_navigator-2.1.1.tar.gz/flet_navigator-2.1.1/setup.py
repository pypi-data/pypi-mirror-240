from setuptools import setup


setup(
    name='flet_navigator',

    packages=['flet_navigator'],

    version='2.1.1',

    license='MIT',

    description='Navigator for Flet.',

    long_description_content_type='text/x-rst',
    long_description=open('README.rst', 'r').read(),

    author='Ivan Perzhinsky.',
    author_email='name1not1found.com@gmail.com',

    url='https://github.com/xzripper/flet_navigator',
    download_url='https://github.com/xzripper/flet_navigator/archive/refs/tags/v2.1.1.tar.gz',

    keywords=['navigator', 'router', 'utility', 'flet'],

    classifiers=[
        'Development Status :: 5 - Production/Stable ',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
