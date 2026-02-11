from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///../../database/orm_tasks.db', echo=True)


print("Ready")