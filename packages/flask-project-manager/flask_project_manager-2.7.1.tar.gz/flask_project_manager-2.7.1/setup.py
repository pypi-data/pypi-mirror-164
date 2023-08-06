from setuptools import setup, find_packages


setup(
    name='flask_project_manager',
    version='2.7.1',
    license='MIT',
    author="Raja Osian",
    author_email='omid22ssh@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/sinasox/sina_seifouri',
    keywords='This is just an introduction.',
    entry_points={
        'console_scripts': [
            'flask_project_manager=flask_project_manager:main'
        ]
    },
    install_requires=[
    'requests'

    ],

)
