from FundNotify.extensions import db
from FundNotify.models.relationships import tags_posts
from FundNotify.database import (
    Model,
    SurrogatePK,
)


class Tag(SurrogatePK, Model):

    __tablename__ = 'tags'

    tag = db.Column(db.Text)
    posts = db.relationship('Post', secondary=tags_posts, backref=db.backref('tags_br', lazy='dynamic'))

    def __init__(self, tag, **kwargs):
        db.Model.__init__(self, tag=tag, **kwargs)