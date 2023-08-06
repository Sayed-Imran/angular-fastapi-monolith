from pydantic import BaseSettings

class _MongoDB(BaseSettings):
    mongo_uri: str = 'mongodb://localhost:27017'

MongoDB = _MongoDB()