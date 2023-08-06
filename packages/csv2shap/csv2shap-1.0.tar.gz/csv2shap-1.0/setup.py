from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = "csv2shap",
    version = "1.0",
    author = "Dinghongyu",
    author_email = "dinghongyu1122@163.com",
    description = "输入csv文件以及二分类的label名称，输出shap value图",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    package_dir = {"": "src"},
    packages = find_packages(where = "src"),
    install_requires=['pandas', 'numpy', 'catboost', 'sklearn', 'Ipython',
                      'plotly', 'shap', 'matplotlib', 'seaborn']
)