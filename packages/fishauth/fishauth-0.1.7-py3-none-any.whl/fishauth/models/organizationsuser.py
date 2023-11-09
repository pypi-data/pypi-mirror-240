from sqlalchemy import Column, ForeignKey, Table, DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy.sql import func
from fishauth.models.base import Base

OrganizationsUser = Table(
    "organizationsuser",
    Base.metadata,
    Column("organization_id", ForeignKey("organization.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("time_created", DateTime(timezone=True), server_default=func.now()),
    Column("time_updated", DateTime(timezone=True), onupdate=func.now()),
    UniqueConstraint("organization_id", "user_id"),
)
