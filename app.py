import os
from config import OPENAI_API_KEY
from langchain.document_loaders import YoutubeLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=Ohsik59B3Mc&ab_channel=HubermanLabClips", add_video_info=False)
index = VectorstoreIndexCreator().from_loaders([loader])

response = index.query("what is the video about?")
print(response)