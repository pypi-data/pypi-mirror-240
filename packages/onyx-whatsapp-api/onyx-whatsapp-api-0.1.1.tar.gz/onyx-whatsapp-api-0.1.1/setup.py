from setuptools import setup, find_packages

setup(
    name='onyx-whatsapp-api',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'whatsapp-api = whatsapp_api.whatsapp_api:main',
        ],
    },
    author='Tasaddaq Hussain',
    author_email='bc110200816@gmail.com',
    description='A Python module for sending WhatsApp messages using a third-party API (https://onyxberry.com/services/wapi)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://onyxberry.com/services/wapi',
    license='MIT',
)
