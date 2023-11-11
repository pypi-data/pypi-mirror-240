from setuptools import setup, find_packages

setup(
    name             = 'gptfy',
    version          = '0.3.4',
    packages         = find_packages(),
    install_requires = [
        'openai~=0.28.1'
    ],
    # More configurations can be added here.
)