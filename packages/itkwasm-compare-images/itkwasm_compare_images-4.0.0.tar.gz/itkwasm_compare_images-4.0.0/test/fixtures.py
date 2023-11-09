import pytest
import sys
import pickle

if sys.version_info < (3,10):
    pytest.skip("Skipping pyodide tests on older Python", allow_module_level=True)

from itkwasm_compare_images import __version__ as test_package_version

@pytest.fixture
def package_wheel():
    return f"itkwasm_compare_images-{test_package_version}-py3-none-any.whl"

@pytest.fixture
def input_data():
    from pathlib import Path
    input_base_path = Path('..', '..', 'test', 'data')
    test_files = [
        Path('input') / 'cake_easy.iwi.cbor',
        Path('input') / 'cake_hard.iwi.cbor',
        Path('input') / 'cake_easy.png',
        Path('input') / 'cake_hard.png',
        Path('input') / 'apple.jpg',
        Path('input') / 'orange.jpg',
    ]
    data = {}
    for f in test_files:
        with open(input_base_path / f, 'rb') as fp:
            data[str(f.name)] = fp.read()
    return data
