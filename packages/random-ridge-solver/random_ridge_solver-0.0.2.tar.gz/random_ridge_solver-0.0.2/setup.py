from setuptools import setup

DESCRIPTION = 'Ridge regression solver'
LONG_DESCRIPTION = 'Randomized preconditioned conjugate gradient method for ridge regression, with adaptive sketch sizes.'

setup(
    name="random_ridge_solver",
    version='0.0.2',
    license='MIT',
    author="Jonathan Lacotte",
    author_email="<jonathanlacotte@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url='https://github.com/jonathanlctt/randomized_ridge_regression_solver',
    install_requires=[],

    keywords=['ridge regression', 'sketching', 'preconditioning', 'conjugate gradient method', 'effective dimension'],
    classifiers=[]
)