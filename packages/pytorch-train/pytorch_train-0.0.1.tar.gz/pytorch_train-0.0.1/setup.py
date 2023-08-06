from setuptools import setup, find_packages


setup(
	name="pytorch_train",
	version="0.0.1",
	author="Fau",
	author_email="2594797855@qq.com",
	url="https://github.com/Fau818/Fau_module",
	license="MIT",
	description="A python module named torch_train. The main function is for pytorch training.",
	python_requires=">=3.6",
	packages=find_packages(),
	package_data={"": ["*"]},  # 数据文件全部打包
)
