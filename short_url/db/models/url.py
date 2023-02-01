from sqlalchemy import (
    Column,
    String,
    UUID,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TShortUrl(Base):
    __tablename__ = 'tshort_urls'
    id = Column(UUID, primary_key=True)
    source_url = Column(String(255), index=True)
    short_url = Column(String(40), unique=True, index=True)
