import databases
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings

# Cấu hình kết nối cơ sở dữ liệu
class Settings(BaseSettings):
    database_url: str = "postgresql://user:newpassword@localhost/dbbook"

    class Config:
        env_file = ".env"  # Bạn có thể lưu thông tin cấu hình trong file .env nếu cần

settings = Settings()

# Cấu hình SQLAlchemy
DATABASE_URL = settings.database_url
database = databases.Database(DATABASE_URL)
metadata = MetaData()
Base = declarative_base(metadata=metadata)

# Tạo kết nối và sessionmaker
engine = create_engine(DATABASE_URL, pool_size=3, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
