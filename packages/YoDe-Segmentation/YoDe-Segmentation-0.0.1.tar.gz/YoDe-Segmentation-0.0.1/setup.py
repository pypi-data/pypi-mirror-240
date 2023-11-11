from setuptools import setup

setup(
    name='YoDe-Segmentation',
    version='0.0.1',
    description='An open sourced software for automatic chemical molecular structure maps extraction.',
    url='https://github.com/OneChorm/YoDe-Segmentation',
    author='zconechorm',
    author_email='zconechorm@163.com',
    license='MIT',
    packages=['YoDe-Segmentation'],
    install_requires=[
        'matplotlib',
		'numpy==1.25.2',
		'opencv_python',
		'pandas',
		'Pillow==10.0.0',
		'PyYAML==6.0.1',
		'scipy',
		'seaborn==0.11.2',
		'tqdm==4.64.1',
		'python-office'
    ],
    zip_safe=False
)