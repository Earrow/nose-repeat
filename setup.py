from setuptools import setup

setup(
    name='nose-repeat',
    packages=['nose_repeat'],
    version='0.1.0',
    description='Repeat tests',
    author='Earrow',
    author_email='earrow.liu@gmail.com',
    url='https://github.com/Earrow/nose-repeat',
    install_requires=['nose'],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points={
        'nose.plugins.0.10': [
            'repeat = nose_repeat.repeat:Repeat'
        ]
    }
)
