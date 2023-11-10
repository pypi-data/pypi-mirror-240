from distutils.core import setup

setup(
    name="rdiff",
    packages=["rdiff"],
    version="0.1.0",
    license="MIT",
    description="An implementation of the rdiff tool by librsync",
    author="Mohit Panchariya",
    author_email="iammohitpanchariya@gmail.com",
    url="https://github.com/MohitPanchariya/rdiff",
    download_url="https://github.com/MohitPanchariya/rdiff/archive/refs/tags/v0.1.0.tar.gz",
    keywords=["rdiff", "librsync", "native", "python", "native python implementation"],
    install_requires=[
        "functools"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
