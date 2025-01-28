from fastapi import HTTPException

from app.core.database.tables.user import User
from app.shared.logger.setup import app_logger

class UserService:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            return self.db.query(User).all()
        except Exception as e:
            app_logger.error(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        
    def add_new(self, data):
        try:
            new_user = User(**data)
            self.db.add(new_user)
            self.db.commit()
            return new_user
        except Exception as e:    
            app_logger.error(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        

    def update(self, id, data):
        try:
            user = self.db.query(User).filter(User.id == id).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            for key, value in data.items():
                setattr(user, key, value)
            self.db.commit()
            return user
        except Exception as e:
            app_logger.error(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        

    def delete(self, id):
        try:
            user = self.db.query(User).filter(User.id == id).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            self.db.delete(user)
            self.db.commit()    
            return "User deleted successfully"
        except Exception as e:
            app_logger.error(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")