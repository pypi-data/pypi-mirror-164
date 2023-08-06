from distutils.core import setup

setup(
    name='PyGitHubSDK',
    packages=['GitHubSDK'],
    version='0.1',
    license='MIT',
    description='Python SDK for GitHub API',
    author='Preethi Kumar',
    author_email='preethi.abkumar@gmail.com',
    url='https://github.com/arcotbha/GitHubSDK',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=['GitHub', 'Python', 'sdk'],  # Keywords that define your package best
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)
