from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="migarcia",
    author_email="migarcia@student.42urduliz.com",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mirgc/Python-for-Data-Science/tree/main/0-Starting/ex09/ft_package",
    packages=find_packages(),  # Encuentra automáticamente subpaquetes
    classifiers=[],
    python_requires=">=3.6",
    license="MIT",
)

