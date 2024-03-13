from sqlalchemy import create_engine

from api.models.note import Base as Note

DB_URL = "mysql+pymysql://root@db:3306/hackit-sample?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Note.metadata.drop_all(bind=engine)
    Note.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
