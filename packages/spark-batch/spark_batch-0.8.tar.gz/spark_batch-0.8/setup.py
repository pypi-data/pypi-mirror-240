from setuptools import setup, find_packages

setup(
    name="spark_batch",
    version="0.8",
    description="spark_delta_batch for bronze > silve > gold > mart auto",
    author="GunSik Choi",
    author_email="cgshome@gmail.com", 
    packages=find_packages(where="src/spark_batch"),
    package_dir={"":"src/spark_batch"}, 
    install_requires=[
        "pyyaml",
        "psycopg2-binary",
        "delta-spark",
        "boto3",
        "cryptography"
    ],
)

setup(
    name="spark_batch_ent",
    version="0.8",
    description="spark_delta_batch for bronze > silve > gold > mart auto",
    author="GunSik Choi",
    author_email="cgshome@gmail.com", 
    packages=find_packages(where="src/spark_batch_ent"),
    package_dir={"":"src/spark_batch_ent"}, 
    install_requires=[
        "pyyaml",
        "psycopg2-binary",
        "delta-spark",
        "boto3",
        "cryptography"
    ],
)

