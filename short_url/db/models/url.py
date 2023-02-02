from sqlalchemy import (
    Column,
    String,
    BigInteger,
    FetchedValue
)

from short_url.db.models import Base


class TShortUrl(Base):
    __tablename__ = 'tshort_urls'
    id = Column('id', BigInteger, primary_key=True)
    source_url = Column(String(255), index=True)
    short_url = Column(String(40), unique=True, index=True, server_default=FetchedValue())
