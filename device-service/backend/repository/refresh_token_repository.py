from backend import db
from backend.entities.refresh_token import RefreshToken
from backend.error.business_errors import RefreshTokenNotFound
from datetime import datetime

class RefreshTokenRepository:
    def create_refresh_token(self, user_id, token, expires_at):
        # Tự động xóa refresh token cũ của user (nếu chỉ cho phép 1 token mỗi user)
        self.delete_by_user_id(user_id)

        refresh_token = RefreshToken(
            user_id=user_id,
            token=token,
            expires_at=expires_at,  # Token có thời gian sống 7 ngày
            created_at=datetime.utcnow()
        )

        try:
            db.session.add(refresh_token)
            db.session.commit()
            return refresh_token
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_by_user_id(self, user_id):
        """Xóa tất cả refresh token cũ của user (nếu chỉ muốn duy trì 1 token mỗi user)."""
        db.session.query(RefreshToken).filter_by(user_id=user_id).delete()
        db.session.commit()

    def get_by_token(self, token):
        """Lấy Refresh Token từ database."""
        return db.session.query(RefreshToken).filter_by(token=token).first()

    def delete_by_token(self, token):
        """Xóa Refresh Token dựa trên token."""
        db.session.query(RefreshToken).filter_by(token=token).delete()
        db.session.commit()
        
    def verify_refresh_token(self, token):
        """Kiểm tra xem refresh token có hợp lệ không."""
        refresh_token = self.get_by_token(token)
        if not refresh_token:
            raise RefreshTokenNotFound()
        return refresh_token
