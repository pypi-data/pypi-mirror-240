from __future__ import annotations

import typing as t
import warnings

import pytest
import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.orm
from quart import Quart
from sqlalchemy.orm import Mapped
from werkzeug.exceptions import NotFound

from quart_sqlalchemy import SQLAlchemy
from quart_sqlalchemy.query import Query


sa = sqlalchemy


@pytest.fixture(autouse=True)
def ignore_query_warning() -> t.Generator[None, None, None]:
    if hasattr(sa.exc, "LegacyAPIWarning"):
        with warnings.catch_warnings():
            exc = sa.exc.LegacyAPIWarning
            warnings.simplefilter("ignore", exc)
            yield
    else:
        yield


async def test_get_or_404(app: Quart, db: SQLAlchemy, Todo: t.Any) -> None:
    async with app.app_context():
        item = Todo()
        db.session.add(item)
        db.session.commit()
        assert Todo.query.get_or_404(1) is item

        with pytest.raises(NotFound):
            Todo.query.get_or_404(2)


async def test_first_or_404(app: Quart, db: SQLAlchemy, Todo: t.Any) -> None:
    async with app.app_context():
        db.session.add(Todo(title="a"))
        db.session.commit()
        assert Todo.query.filter_by(title="a").first_or_404().title == "a"

        with pytest.raises(NotFound):
            Todo.query.filter_by(title="b").first_or_404()


async def test_one_or_404(app: Quart, db: SQLAlchemy, Todo: t.Any) -> None:
    async with app.app_context():
        db.session.add(Todo(title="a"))
        db.session.add(Todo(title="b"))
        db.session.add(Todo(title="b"))
        db.session.commit()
        assert Todo.query.filter_by(title="a").one_or_404().title == "a"

        with pytest.raises(NotFound):
            # MultipleResultsFound
            Todo.query.filter_by(title="b").one_or_404()

        with pytest.raises(NotFound):
            # NoResultFound
            Todo.query.filter_by(title="c").one_or_404()


async def test_paginate(app: Quart, db: SQLAlchemy, Todo: t.Any) -> None:
    async with app.app_context():
        db.session.add_all(Todo() for _ in range(150))
        db.session.commit()
        p = Todo.query.paginate()
        assert p.total == 150
        assert len(p.items) == 20
        p2 = p.next()
        assert p2.page == 2
        assert p2.total == 150


# The Query interface is legacy and in order to preserve the custom functionality added to Query,
# we need to use db.relationship rather than sa.orm.relationship.


async def test_default_query_class(app: Quart, db: SQLAlchemy) -> None:
    class Parent(db.Model):
        id: Mapped[int] = sa.orm.mapped_column(primary_key=True)
        children1: Mapped[t.List["Child"]] = db.relationship(
            "Child", backref="parent1", lazy="dynamic"
        )

    class Child(db.Model):
        id: Mapped[int] = sa.orm.mapped_column(primary_key=True)
        parent_id: Mapped[int] = sa.orm.mapped_column(sa.ForeignKey(Parent.id))
        parent2: Mapped[Parent] = db.relationship(
            Parent,
            backref=db.backref("children2", lazy="dynamic", viewonly=True),
            viewonly=True,
        )

    async with app.app_context():
        p = Parent()
        assert type(Parent.query) is Query
        assert isinstance(p.children1, Query)
        assert isinstance(p.children2, Query)
        assert isinstance(db.session.query(Child), Query)


async def test_custom_query_class(app: Quart) -> None:
    class CustomQuery(Query):
        pass

    async with app.app_context():
        db = SQLAlchemy(app, query_class=CustomQuery)

        class Parent(db.Model):
            id: Mapped[int] = sa.orm.mapped_column(primary_key=True)
            children1: Mapped[t.List["Child"]] = db.relationship(
                "Child", backref="parent1", lazy="dynamic"
            )

        class Child(db.Model):
            id: Mapped[int] = sa.orm.mapped_column(primary_key=True)
            parent_id: Mapped[int] = sa.orm.mapped_column(sa.ForeignKey(Parent.id))
            parent2: Mapped[Parent] = db.relationship(
                Parent,
                backref=db.backref("children2", lazy="dynamic", viewonly=True),
                viewonly=True,
            )

        p = Parent()
        assert type(Parent.query) is CustomQuery
        assert isinstance(p.children1, CustomQuery)
        assert isinstance(p.children2, CustomQuery)
        assert isinstance(db.session.query(Child), CustomQuery)
