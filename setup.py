from setuptools import setup, find_packages

setup(
    name="pizza_api",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask>=2.0.0',
        'flask-sqlalchemy>=2.5.0',
        'flask-migrate>=3.0.0',
        'python-dotenv>=0.19.0',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        'server': ['instance/*.db'],
    },
    entry_points={
        'console_scripts': [
            'pizza-api=server.app:main',
        ],
    },
)