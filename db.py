import sqlalchemy
import os  # .environ.get
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


def get_engine():
    db_url = 'mysql+mysqlconnector://{user}:{pw}@{host}/{db}'.format(
        user=os.environ.get('SQL_USER'),
        pw=os.environ.get('SQL_PASSWORD'),
        host=os.environ.get('SQL_HOST'),
        db=os.environ.get('SQL_DB'),
    )

    return create_engine(db_url)


class GhcnStations(Base):
    """GHCN daily stations from ghcnd-stations.txt
    Technically the dataset is Global Historical Climatology Network Daily

    The format of ghcnd-stations.txt is provided in: readme.md
    Or can be retrieved from: https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt
    """
    __tablename__ = 'ghcn_stations'

    id = Column(Integer, primary_key=True)

    station_id = Column(String(11), nullable=False)
    



