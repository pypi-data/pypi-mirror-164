import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jacksonreport",
    version="1.0.0",
    author="jackson",
    author_email="1349983371@qq.com",
    description="封装好的接口自动化测试报告",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/shanhaiqiu/jacksonreport.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)