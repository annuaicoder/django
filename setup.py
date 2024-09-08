from setuptools import setup, find_packages

setup(
    name='Django',
    version='4.0.0',  # Set this to your package version
    url='https://www.djangoproject.com/',
    author='Django Software Foundation',
    author_email='foundation@djangoproject.com',
    description='A high-level Python web framework that encourages rapid development and clean, pragmatic design.',
    long_description=open('README.rst').read(),
    license='BSD-3-Clause',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Documentation': 'https://docs.djangoproject.com/',
        'Release notes': 'https://docs.djangoproject.com/en/stable/releases/',
        'Funding': 'https://www.djangoproject.com/fundraising/',
        'Source': 'https://github.com/django/django',
        'Tracker': 'https://code.djangoproject.com/',
    },
    python_requires='>=3.10',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'asgiref >= 3.7.0',
        'sqlparse >= 0.3.1',
        'tzdata; sys_platform == "win32"',
    ],
    extras_require={
        'argon2': ['argon2-cffi >= 19.1.0'],
        'bcrypt': ['bcrypt'],
    },
    entry_points={
        'console_scripts': [
            'django-admin = django.core.management:execute_from_command_line',
        ],
    },
    # Ensure users get the latest version
    setup_requires=[
        'setuptools>=42',  # or another version of setuptools
    ],
    dependency_links=[
        'https://pypi.org/project/Django/#history',  # Link to the Django release history
    ],
)
