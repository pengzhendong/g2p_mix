# Copyright (c) 2023 Zhendong Peng (pzd17@tsinghua.org.cn)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from setuptools import setup, find_packages


with open("README.md", encoding="utf8") as fin:
    long_description = fin.read()

extras_require = {"g2pw": ["torch", "modelscope", "pypinyin-g2pw"]}

setup(
    name="g2p_mix",
    version=os.getenv("BUILD_VERSION") or "0.3.2",
    author="Zhendong Peng",
    author_email="pzd17@tsinghua.org.cn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="G2P mix",
    url="https://github.com/pengzhendong/g2p_mix",
    packages=find_packages(),
    package_data={
        "g2p_mix": [
            "nltk_data/corpora/cmudict.zip",
            "nltk_data/taggers/averaged_perceptron_tagger.zip",
        ]
    },
    install_requires=["g2p_en", "jieba", "pypinyin", "wordsegment"],
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
)
