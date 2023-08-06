from setuptools import setup

setup(
    name="runfalcon-build-tools",
    version='1.0.2',
    author="Raul A. de Villa C.",
    author_email="r@runfalcon.com",
    description='Runfalcon tools to build process with quality and efficiency',
    long_description_content_type="text/markdown",
    install_requires=['datetime', 'python-abc'],
    keywords=['runfalcon', 'python', 'deployment', 'pipeline', 'ci', 'cd'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)