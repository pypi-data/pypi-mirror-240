from setuptools import find_packages, setup
with open("README.md", "r") as f:
    long_description = f.read()
with open("requirements.txt", "r") as f:
    install_requires = [line.strip() for line in f if line.strip()]
setup(
    name="own-knowledge-gpt",
    version="0.0.2",
    description="Custom Knowledge GPT",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://huggingface.co/myn0908",
    author="TinVo",
    author_email="tinprocoder0908@gmail.com",
    keywords=["AI HACKER", "AI", "autoGPT", "Deep Learning", "LLM",
              "Interface"],

    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.9"
)