import vertexai

vertexai.init(
    project="vertexagentbuilder",
    location="us-central1",
    staging_bucket="gs://vertexaiagentbuilder",
)
from langchain_google_vertexai import VertexAI

# To use model
model = VertexAI(model_name="gemini-1.0-pro-002")