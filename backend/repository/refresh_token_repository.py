from backend import db
from backend.entities.refresh_token import RefreshToken

class RefreshTokenRepository:
    def create_refresh_token(self, user_id, token):
        refresh_token = RefreshToken(user_id=user_id, token=token)
        db.session.add(refresh_token)
        db.session.commit()
        return refresh_token

    def get_refresh_token(self, token):
        return db.session.query(RefreshToken).filter_by(token=token).first()

    def delete_refresh_token(self, token):
        refresh_token = db.session.query(RefreshToken).filter_by(token=token).first()
        if refresh_token:
            db.session.delete(refresh_token)
            db.session.commit()

    def delete_all_user_tokens(self, user_id):
        db.session.query(RefreshToken).filter_by(user_id=user_id).delete()
        db.session.commit()
