from setuptools import setup, find_packages
setup(
    name = 'steemhd',
    packages = find_packages(exclude=['test']),
    install_requires = ['requests >= 2.23.0', 'pycryptodome >= 3.9.8','ecdsa >= 0.17.0','crcmod >= 1.7','eth_utils >= 0.9.0'],
    version = '1.0.4',
    description = 'Bitcoin/Ethereum/STEEM key manipulation',
    author = 'maiyude',
    author_email = 'steem@steem.vip',
    url = 'https://github.com/maiyude2018/steem_to_hdwallet',
    keywords = ['steem','security', 'cryptography', 'cryptocurrency', 'bitcoin'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3',
    include_package_data=True
)






