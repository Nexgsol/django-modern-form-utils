from setuptools import setup, find_packages

with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='django-modern-form-utils',
    version='1.1.0',  # or 2.0.0 if major refactor
    description='Modernized form utilities for Django 3.2–5.2+',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Muhammad Ziauldin',
    author_email='ziauldin@nexgsol.com',
    url='https://github.com/yourusername/django-modern-form-utils',
    packages=find_packages(exclude=["tests*", "docs*"]),
    include_package_data=True,
    license='BSD-3-Clause',
    zip_safe=False,
    install_requires=[
        'Django>=3.2',
        'Pillow>=7.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8',
    package_data={
        'form_utils': [
            'templates/form_utils/*.html',
            'media/form_utils/js/*.js',
        ],
    },
    test_suite='tests.runtests.runtests',
    tests_require=[
        'Django>=3.2',
        'mock',
        'Pillow',
    ],
)
