from __future__ import annotations

import pytest
import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.orm
from quart import Quart
from sqlalchemy.orm import Mapped

from quart_sqlalchemy import SQLAlchemy
from quart_sqlalchemy.model import DefaultMeta
from quart_sqlalchemy.model import Model


sa = sqlalchemy


def test_default_metadata(db: SQLAlchemy) -> None:
    assert db.metadata is db.metadatas[None]
    assert db.metadata.info["bind_key"] is None
    assert db.Model.metadata is db.metadata


def test_custom_metadata() -> None:
    metadata = sa.MetaData()
    db = SQLAlchemy(metadata=metadata)
    assert db.metadata is metadata
    assert db.metadata.info["bind_key"] is None
    assert db.Model.metadata is db.metadata


def test_metadata_from_custom_model() -> None:
    base = sa.orm.declarative_base(cls=Model, metaclass=DefaultMeta)
    metadata = base.metadata
    db = SQLAlchemy(model_class=base)
    assert db.Model.metadata is metadata
    assert db.Model.metadata is db.metadata


def test_custom_metadata_overrides_custom_model() -> None:
    base = sa.orm.declarative_base(cls=Model, metaclass=DefaultMeta)
    metadata = sa.MetaData()
    db = SQLAlchemy(model_class=base, metadata=metadata)
    assert db.Model.metadata is metadata
    assert db.Model.metadata is db.metadata


def test_metadata_per_bind(app: Quart) -> None:
    app.config["SQLALCHEMY_BINDS"] = {"a": "sqlite://"}
    db = SQLAlchemy(app)
    assert db.metadatas["a"] is not db.metadata
    assert db.metadatas["a"].info["bind_key"] == "a"


def test_copy_naming_convention(app: Quart) -> None:
    app.config["SQLALCHEMY_BINDS"] = {"a": "sqlite://"}
    db = SQLAlchemy(app, metadata=sa.MetaData(naming_convention={"pk": "spk_%(table_name)s"}))
    assert db.metadata.naming_convention["pk"] == "spk_%(table_name)s"
    assert db.metadatas["a"].naming_convention == db.metadata.naming_convention


async def test_create_drop_all(app: Quart) -> None:
    async with app.app_context():
        app.config["SQLALCHEMY_BINDS"] = {"a": "sqlite://"}
        db = SQLAlchemy(app)

        class User(db.Model):
            id: Mapped[int] = sa.orm.mapped_column(primary_key=True)

        class Post(db.Model):
            __bind_key__ = "a"
            id: Mapped[int] = sa.orm.mapped_column(primary_key=True)

        with pytest.raises(sa.exc.OperationalError):
            db.session.execute(sa.select(User)).scalars()

        with pytest.raises(sa.exc.OperationalError):
            db.session.execute(sa.select(Post)).scalars()

        db.create_all()
        db.session.execute(sa.select(User)).scalars()
        db.session.execute(sa.select(Post)).scalars()
        db.drop_all()

        with pytest.raises(sa.exc.OperationalError):
            db.session.execute(sa.select(User)).scalars()

        with pytest.raises(sa.exc.OperationalError):
            db.session.execute(sa.select(Post)).scalars()


@pytest.mark.parametrize("bind_key", ["a", ["a"]])
async def test_create_key_spec(app: Quart, bind_key: str | list[str | None]) -> None:
    async with app.app_context():
        app.config["SQLALCHEMY_BINDS"] = {"a": "sqlite://"}
        db = SQLAlchemy(app)

        class User(db.Model):
            id: Mapped[int] = sa.orm.mapped_column(primary_key=True)

        class Post(db.Model):
            __bind_key__ = "a"
            id: Mapped[int] = sa.orm.mapped_column(primary_key=True)

        db.create_all(bind_key=bind_key)
        db.session.execute(sa.select(Post)).scalars()

        with pytest.raises(sa.exc.OperationalError):
            db.session.execute(sa.select(User)).scalars()


async def test_reflect(app: Quart) -> None:
    async with app.app_context():
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
        app.config["SQLALCHEMY_BINDS"] = {"post": "sqlite:///post.db"}
        db = SQLAlchemy(app)
        db.Table("user", sa.Column("id", sa.Integer, primary_key=True))
        db.Table("post", sa.Column("id", sa.Integer, primary_key=True), bind_key="post")
        db.create_all()

        del app.extensions["sqlalchemy"]
        db = SQLAlchemy(app)
        assert not db.metadata.tables
        db.reflect()
        assert "user" in db.metadata.tables
        assert "post" in db.metadatas["post"].tables
