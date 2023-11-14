import pathlib

from mlstac.sample.datamodel import Sample, SampleMetadata, SampleTensor
from mlstac.collection.datamodel import Collection
from mlstac.api.main import load, download
from mlstac.api.datasets import LocalDataset, StreamDataset

from mlstac.api.nest_asyncio import apply as nest_asyncio_apply
from typing import Union

# Patch asyncio to make its event loop reentrant.
nest_asyncio_apply()


# Huggingface utils
def hf_getlink(repoinfo, path: Union[str, pathlib.Path]):
    if isinstance(path, str):
        path = pathlib.Path(path)
    return {
        "n_items": len(list(path.glob("*.safetensors.gz"))),
        "link": f"{str(repoinfo)}/resolve/main/{path.stem}/",
    }
