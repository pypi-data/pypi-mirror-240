import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="get-system-color",
    version="1.1.3",
    author="xiaoshuaiYo",
    author_email="619396351@qq.com",
    description="这个库可快速调用windows平台的主题色及主题的信号",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache2",
    url="https://github.com/xiaoshuaiyo/get-system-color",
    packages=setuptools.find_packages(),
    extras_requirep={
        'full': ['scipy', 'pillow<=9.4.0', 'colorthief']
    },
    project_urls={
        'Source Code': 'https://github.com/xiaoshuaiyo/get-system-color',
        'Bug Tracker': 'https://github.com/xiaoshuaiyo/get-system-color/issues',
    }
)

