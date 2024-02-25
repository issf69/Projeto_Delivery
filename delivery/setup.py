from setuptools import setup, find_packages

setup(
    name='meu_pacote',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pacote1',
        'pacote2',
    ],
    author='irene',
    author_email='irenesilvafranca2016@gmail.com',
    description='Uma breve descrição do seu pacote',
    url='https://github.com/issf69/Projeto_Delivery.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
