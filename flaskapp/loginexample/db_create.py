from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path

def main():
	db.create_all()
	
if __name__ == "__main__":
	main()