import setuptools
import os


with open("README.md", "r") as f:
    long_description = f.read()
with open("requirements.txt") as f:
    install_requires = [pkg.strip() for pkg in f.readlines() if pkg.strip()]
scripts = [
    os.path.join("bin", fname) for fname in os.listdir("bin")]

setuptools.setup(
    name="pz-hyperbolic-temp",
    version="0.0",
    author="Jan Luca van den Busch",
    description="Implementation of hyperbolic magnitudes (Lupton et al. 1999).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jlvdb/hyperbolic",
    packages=setuptools.find_packages(),
    scripts=scripts,
    install_requires=install_requires)
