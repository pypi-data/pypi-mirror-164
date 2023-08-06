from setuptools import setup


setup(
    name='setuptools-git-version-cc',
    version='3.0.4',
    author='Rokubun',
    author_email='info@rokubun.cat',
    description='Automatically set package version from Git using Conventional Commit standard.',
    long_description="""# Conventional Commit Semantic Version generator!\n\n Automatically set package version from Git using Conventional Commit standard.""",
    long_description_content_type='text/markdown',
    license='http://opensource.org/licenses/MIT',
    url="https://github.com/rokubun/setuptools-git-version-cc",
    classifiers=[
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    py_modules=['setuptools_git_version_cc'],
    install_requires=[
        'setuptools >= 8.0',
    ],
    entry_points="""
        [distutils.setup_keywords]
        version_cc = setuptools_git_version_cc:get_git_version_cc
        [console_scripts]
        get_version = setuptools_git_version_cc:entry_point
    """,
)
