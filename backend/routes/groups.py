from flask import Blueprint, jsonify
from backend.entities.group import Group, GroupSchema
from sqlalchemy import select
from backend import db


group_bp = Blueprint("group", __name__)
group_schema = GroupSchema()

@group_bp.route("/get", methods=["GET"])
def get_all_groups():
    # 1
    # groups = Group.query.all()
    
    # 2
    groups = db.session.scalars(select(Group).all())

    return jsonify(group_schema.dump(groups, many=True))
