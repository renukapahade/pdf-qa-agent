from setuptools import setup, find_packages

setup(
    name="pdf-qa-agent",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'openai==1.12.0',
        'python-dotenv==1.0.0',
        'PyPDF2==3.0.1',
        'slack-sdk==3.27.0',
        'numpy==1.24.3',
        'scikit-learn==1.3.0',
    ],
)