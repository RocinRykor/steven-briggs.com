from .db import data_base as db


class JournalEntry(db.Model):
    """
    A model representing a blog post.
    | id:            The primary key for the blog post
    | title:         A string containing the title of the blog post
    | content:       A string containing the content of the blog post
    | author_id:     An integer representing the user who wrote the blog post
    | author:        A relationship to the user who wrote the blog post
    | created_at:    A datetime object representing the date and time the blog post was created
    | updated_at:    A datetime object representing the date and time the blog post was last updated
    | is_private:    Whether the blog post will be marked as private (won't be viewable anyone not logged in)
    | is_super_private: Whether the blog post will be marked as super private (won't be viewable anyone not logged in as the original author)
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', back_populates='blog_posts')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    is_private = db.Column(db.Boolean)
    is_super_private = db.Column(db.Boolean)

    def jsonify(self):
        """
        Returns the blog post as a JSON object.

        -> JSON object
        """
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
