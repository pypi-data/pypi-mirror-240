from setuptools import setup


setup(
    name='flet_restyle',

    packages=['flet_restyle'],

    version='1.0.0',

    license='MIT',

    description='Flet ReStyle.',

    long_description_content_type='text/x-rst',
    long_description=open('README.rst', 'r').read(),

    author='Ivan Perzhinsky.',
    author_email='name1not1found.com@gmail.com',

    url='https://github.com/xzripper/flet_restyle',
    download_url='https://github.com/xzripper/flet_restyle/archive/refs/tags/v1.0.0.tar.gz',

    keywords=['utility'],

    install_requires=['BlurWindow'],

    classifiers=[
        'Development Status :: 5 - Production/Stable ',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
