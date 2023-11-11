from setuptools import setup, find_packages

setup(
    name             = 'gptfy',
    version          = '0.3.2',
    packages         = find_packages(),
    install_requires = [
        'openai~=1.2.2'
    ],
    # More configurations can be added here.
)