from distutils.core import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "description.md").read_text()

setup(
    name='BiomationScripter',
    version='0.2.0',
    description='Tools for scripting bio-automation protocols',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author='Bradley Brown',
    author_email='bradley.brown4@hotmail.co.uk',
    packages=[
        'BiomationScripter',
        'BiomationScripter.EchoProto',
        'BiomationScripter.OTProto',
        'BiomationScripter.EchoProto.Templates',
        'BiomationScripter.OTProto.Templates'
    ],
)
