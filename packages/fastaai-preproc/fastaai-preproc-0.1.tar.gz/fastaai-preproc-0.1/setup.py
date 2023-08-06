import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="fastaai-preproc",
	version="0.1",
	author="Kenji Gerhardt",
	author_email="kenji.gerhardt@gmail.com",
	description="Protein predictions and HMM searches",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	include_package_data=False,
	python_requires='>=3',
	install_requires=[
		'pyrodigal',
		'pyhmmer',
	],
	entry_points={
		"console_scripts": [
			"fastaai-preproc=Protein_pred_and_HMM_search:main",
		]
	}
)

