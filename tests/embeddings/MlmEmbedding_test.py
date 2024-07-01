import pytest
from swarmauri.standard.embeddings.concrete.MlmEmbedding import MlmEmbedding

@pytest.mark.unit
def test_ubc_resource():
	assert MlmEmbedding().resource == 'Embedding'

@pytest.mark.unit
def test_ubc_type():
	assert MlmEmbedding().type == 'MlmEmbedding'

@pytest.mark.unit
def test_serialization():
	embedder = MlmEmbedding()
	assert embedder.id == MlmEmbedding.model_validate_json(embedder.json()).id


@pytest.mark.unit
def test_fit_transform():
	embedder = MlmEmbedding()
	documents = ['test', 'test1', 'test2']
	embedder.fit_transform(documents)
	assert documents == embedder.extract_features()