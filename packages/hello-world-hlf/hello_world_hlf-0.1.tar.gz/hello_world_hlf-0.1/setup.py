from setuptools import setup

setup(
    name='hello_world_hlf',
    version='0.1',
    packages=['hello_world'],
    entry_points={
        'console_scripts': [
            'hello-world = hello_world:hello.say_hello',
        ],
    },
)
