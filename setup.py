from setuptools import setup, find_packages

setup(
    name='Token-Spy',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # 项目依赖的其他包列表
        'requests==2.31.0',
        'pandas==2.2.1',
        'numpy==1.26.4',
        'dune_client==1.5.1',
        'helius==0.0.3',
        'python-dotenv==1.0.1',
        "openpyxl"
    ],
    entry_points={
        'console_scripts': [
            'token-spy-test=main:test',
            'test-dune=main:test_dune',
            "test-cmc=main:test_cmc",
            "test-helius=main:test_helius",
            'analyse=main:address_analysis',
            'profit=main:profit_calculation',
        ],
    },
    # 其他元数据
    author='Clindy',
    author_email='shaoqinghuang999@gmail.com',
    description='A tool for spying on crypto tokens',
    keywords='crypto, token, spy, solana',
    url='https://github.com/Darclindy/Token-Spy',
)
