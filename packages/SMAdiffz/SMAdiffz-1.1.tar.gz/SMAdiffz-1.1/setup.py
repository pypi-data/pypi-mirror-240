from setuptools import setup, find_packages


VERSION = '1.1'
DESCRIPTION = 'Powerful data structures for data analysis, time series for information diffusion analysis'
LONG_DESCRIPTION = 'The proposed package is designed to facilitate comprehensive work on information diffusion analysis. It provides a versatile set of tools and functionalities that empower users to explore, model, and analyze the intricate dynamics of information spread within a given system.'

# Setting up
setup(
    name="SMAdiffz",
    version=VERSION,
    author="H.M.M.Caldera",
    author_email="<maneeshac2020@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    keywords=['python', 'social media'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)