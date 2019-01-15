# -*- coding:utf-8 -*-
from sqlalchemy import text

db = None


class T_User(db.Model):
    __tablename__ = "t_user"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(32))
    status = db.Column(db.Enum("0", "1"), server_default="0", nullable=False, comment="0:正常，1:冻结")
    del_flg = db.Column(db.Enum("0", "9"), server_default="0", nullable=False, comment="0:有效, 9:删除")
    created_at = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           nullable=False)
    create_account_id = db.Column(db.Integer)
    update_account_id = db.Column(db.Integer)


class T_Role(db.Model):
    __tablename__ = "t_role"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    parent_id = db.Column(db.Integer, nullable=False, comment="self.id")  # 继承自关联
    role_group_id = db.Column(db.Integer, nullable=False, comment="role_group.id")  # 角色所属组
    name = db.Column(db.String(32))
    status = db.Column(db.Enum("0", "1"), server_default="0", nullable=False, comment="0:正常，1:冻结")
    del_flg = db.Column(db.Enum("0", "9"), server_default="0", nullable=False, comment="0:有效, 9:删除")
    created_at = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           nullable=False)
    create_account_id = db.Column(db.Integer)
    update_account_id = db.Column(db.Integer)


class T_Perm(db.Model):
    __tablename__ = "t_perm"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    perm_group_id = db.Column(db.Integer, nullable=False, comment="perm_group.id")  # 权限所属组
    name = db.Column(db.String(32))
    status = db.Column(db.Enum("0", "1"), server_default="0", nullable=False, comment="0:正常，1:冻结")
    del_flg = db.Column(db.Enum("0", "9"), server_default="0", nullable=False, comment="0:有效, 9:删除")
    created_at = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           nullable=False)
    create_account_id = db.Column(db.Integer)
    update_account_id = db.Column(db.Integer)


class T_Perm_Group(db.Model):
    __tablename__ = "t_perm_group"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(32))
    status = db.Column(db.Enum("0", "1"), server_default="0", nullable=False, comment="0:正常，1:冻结")
    del_flg = db.Column(db.Enum("0", "9"), server_default="0", nullable=False, comment="0:有效, 9:删除")
    created_at = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           nullable=False)
    create_account_id = db.Column(db.Integer)
    update_account_id = db.Column(db.Integer)


class T_Role_Group(db.Model):
    __tablename__ = "t_role_group"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(32))
    status = db.Column(db.Enum("0", "1"), server_default="0", nullable=False, comment="0:正常，1:冻结")
    del_flg = db.Column(db.Enum("0", "9"), server_default="0", nullable=False, comment="0:有效, 9:删除")
    created_at = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           nullable=False)
    create_account_id = db.Column(db.Integer)
    update_account_id = db.Column(db.Integer)


class R_Role_Perm_Extra_Relationship(db.Model):
    __tablename__ = "r_role_perm_extra_relationship"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    perm_id = db.Column(db.Integer, nullable=False, comment="perm.id")
    role_id = db.Column(db.Integer, nullable=False, comment="role.id")
    created_at = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)  # 创建时间
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           nullable=False)  # 更新时间
    create_account_id = db.Column(db.Integer)  # 创建人id
    update_account_id = db.Column(db.Integer)  # 更新人id


class R_Role_Perm_Relationship(db.Model):
    __tablename__ = "r_role_perm_relationship"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    perm_id = db.Column(db.Integer, nullable=False, comment="perm.id")
    role_id = db.Column(db.Integer, nullable=False, comment="role.id")
    created_at = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)  # 创建时间
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           nullable=False)  # 更新时间
    create_account_id = db.Column(db.Integer)  # 创建人id
    update_account_id = db.Column(db.Integer)  # 更新人id


class R_User_Role_Relationship(db.Model):
    __tablename__ = "r_user_role_relationship"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False, comment="user.id")
    role_id = db.Column(db.Integer, nullable=False, comment="role.id")
    created_at = db.Column(db.DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)  # 创建时间
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           nullable=False)  # 更新时间
    create_account_id = db.Column(db.Integer)  # 创建人id
    update_account_id = db.Column(db.Integer)  # 更新人id
