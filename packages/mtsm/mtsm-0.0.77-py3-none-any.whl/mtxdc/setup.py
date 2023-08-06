from setuptools import setup
import setuptools
import os

print("--------setup.py-----------", flush=True)

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
    exclude=("test.*", "mtxcms*", "mtx_cloud.*", "mtxauth*", "gallery*"))
# print("所有packages", packages)

setup(name='mtsm',
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
      packages=["sm"],
      package_dir={
          'sm': 'sm'
      },
      #   package_data={'demo': ['data/*.txt']},
      install_requires=[
        'markdown',
        'flask',
        'pyyaml',
        'python-dotenv',
        'requests>=2.26.0',
        'lxml>=4.2.3',
        'monotonic>=1.5',
        'docker',
        'wheel',
        'boto3',
        'aiohttp',
        'django>=4.0',
        'django-cors-headers',
        'zappa',
        'psycopg2-binary',
        'django-s3-sqlite',
        'django-s3-storage',
        'django-storages',
        'django-filter>=2',
        'django-dotenv==1.4.1',
        'django-extensions',
        'djangorestframework',
        'python-dotenv',
        'djangorestframework-simplejwt',
        'pyjwt>=2.0.0',
        'authlib',
        'django-oauth-toolkit',
        'django-lifecycle',
        'pillow',
        'packaging>=21.0',
        'celery',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      package_data={
        #   'demo': ['data/*.txt'],
          'sm': ['data/*.conf'],
      },
      zip_safe=False,
      entry_points={
          'console_scripts': [
              #   'dc=sm.dc:console_script_entry',
              'dc=sm.app:entry_dc',
              'sm=sm.main:console_script_entry',
              'dockerdev=sm.dockerdev:console_script_entry',
              'gitup=sm.gitup:console_script_entry',
          ]
      },
      )
