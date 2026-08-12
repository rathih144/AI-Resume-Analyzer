from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@gateway01.ap-northeast-1.prod.aws.tidbcloud.com:4000/github_sample"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ca": "isrgrootx1.pem"
        }
    }
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()