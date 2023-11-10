from setuptools import setup, find_packages

VERSION = '1.2'
DESCRIPTION = 'FourthDimension（第四维度）由华中科技大学人工智能与嵌入式实验室联合言图科技研发，是一款基于大语言模型的智能知识问答系统，提供私域知识库、文档问答等多种服务。此外，FourthDimension提供便捷的本地部署方法，方便用户在本地环境中搭建属于自己的应用平台。'

setup(
    name="fourth_dimension",
    version=VERSION,
    author="yantu-tech",
    author_email="wu466687121@qq.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md', encoding="UTF8").read(),
    packages=find_packages(),
    include_package_data=True,
    package_data={'fourth_dimension': ['config/question_regex.txt', 'cache/faiss_cache/temp.index']},
    install_requires=[],
    keywords=["python", "yantu"],
    license="MIT",
    url="https://gitee.com/hustai/Fourth-Dimension",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ]
)
