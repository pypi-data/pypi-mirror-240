class IndexTypes(str):
    AzureCognitiveSearch = 'Azure Cognitive Search'
    FAISS = 'FAISS'
    Pinecone = 'Pinecone'
    MLIndexAsset = 'Workspace MLIndex'
    MLIndexPath = 'MLIndex from path'


class EmbeddingTypes(str):
    AzureOpenAI = 'Azure OpenAI'
    OpenAI = 'OpenAI'
    HuggingFace = 'Hugging Face'
