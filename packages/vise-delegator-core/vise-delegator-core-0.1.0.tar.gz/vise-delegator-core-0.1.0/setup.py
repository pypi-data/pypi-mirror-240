from setuptools import setup, find_packages

setup(
    name='vise-delegator-core',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-Cors',
        # Adicione outras dependências necessárias aqui
    ],
    entry_points={
        'console_scripts': [
            'vise-delegator-core = vise_delegator_core.delegator:main',
        ],
    },
)