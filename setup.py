from setuptools import setup

setup(
    name='easyemail',
    version='0.01-dev',
    url='http://github.com/niktto/easyemail/',
    license='BSD',
    author=u'Marek Szwalkiewicz',
    author_email='marek@szwalkiewicz.waw.pl',
    packages=['easyemail'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Mako==0.7.3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    #test_suite='easyemail.tests'
)