from setuptools import setup
import setuptools
import os

print("--------setup_mtxp.py-----------", flush=True)

f = open("version.txt","r")
_version = f.read()
f.close()


with open("README.md", "r") as fh:
    long_description = fh.read()


def gen_data_files(*dirs):
    print("gen_data_files =========================================================", dirs)
    results = []
    for src_dir in dirs:
        for root, dirs, files in os.walk(src_dir):
            results.append((root, map(lambda f: root + "/" + f, files)))
    print("gen_data_files result ===============", results)
    return results

packages = setuptools.find_packages(
    exclude=("test*", "gallery*"))
# print("所有packages", packages)

setup(name='mtxp',
    version=_version,
    description='The funniest joke in the world',
    long_description='long_description',  # readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='funniest joke comedy flying circus',
    url='http://github.com/storborg/funniest',
    author='Flying Circus',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=packages,
    package_dir={
        'mtxp':'mtxp',
        'demo': 'demo',
        'console_scripts': 'console_scripts'
    },
    #   package_data={'demo': ['data/*.txt']},
    install_requires=[
        'python-dotenv',
        'requests>=2.26.0',
        'flask',      
        'pyyaml',
        'celery',
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
    include_package_data=True,
    package_data={
        #   '': ['console_scripts/data/*'],
        'mtxp': ['data/*','bin/*'],
    #   'console_scripts': ['data/*.conf'],
    },
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'mtxp=mtxp.app:entry',
            'mtxpagent=mtxp.app_mtxpagent:entry_agent',
            'wiki=mtxp:cli',
            'mtxpcli1=mtxp.app:cli2',
            'hello1=mtxp.app:hello1'
        ],
        'flask.commands': [
            'cmd1=mtxp.commands:cli',
            # 'mtxpagent_flask=mtxp.app:entry_agent'
        ],
    },
)
