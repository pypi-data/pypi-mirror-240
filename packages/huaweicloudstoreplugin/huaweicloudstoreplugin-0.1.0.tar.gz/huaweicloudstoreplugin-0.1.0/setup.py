from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='huaweicloudstoreplugin',
    version='0.1.0',
    description='Plugin that provides Huawei Cloud OBS Artifact Store functionality for MLflow',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='HuaweiCloud',
    author_email='',
    url="https://gitee.com/HuaweiCloudDeveloper/huaweicloud-mlflow-plugins",
    packages=find_packages(),
    install_requires=[
        'mlflow',
        'esdk-obs-python>=3.23.9.1'
    ],
    entry_points={
        "mlflow.artifact_repository": [
            "obs=huaweicloudstoreplugin.store.artifact.huaweicloud_obs_artifact_repo:HuaweiCloudObsArtifactRepository"
        ]
    },
    license="Apache License 2.0",
)
