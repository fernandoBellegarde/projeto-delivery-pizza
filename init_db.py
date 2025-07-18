from models import Base, db

if __name__ == "__main__":
    Base.metadata.create_all(db)
    print("Tabelas criadas com sucesso!")
