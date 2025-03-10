from backend import db
from backend.entities.user import User
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

users_to_groups = db.Table('users_to_groups',
    db.Column('user_id', db.Integer, db.ForeignKey(User.id), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey("group.id"), primary_key=True)
)

class Group(db.Model):
    __tablename__ = 'group'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship(User.__name__, secondary=users_to_groups, backref='groups')


class GroupSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        include_relationships = True
        load_instance = True


