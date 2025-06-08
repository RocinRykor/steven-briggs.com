from .db import data_base as db


class Project(db.Model):
    """
    | id:                       The primary key for the project
    | title:                    A string for the name of the project
    | repo_link:                URL to the GitHub repository for the project
    | repo_link_description:    Text to accompany the repo link to allow customization
    | live_link:                URL to the active page for the project (such as GitHub Pages)
    | live_link_description:    Text to accompany the live link to allow customization
    | short_description:        Short text description for the project, shows on initial project card
    | description:              Large text description for the project, shows on full project page
    | img_filename:             Filename for an image representing the project
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    repo_link = db.Column(db.String(256))
    repo_link_description = db.Column(db.String(256))
    live_link = db.Column(db.String(256))
    live_link_description = db.Column(db.String(256))
    short_description = db.Column(db.String(1024))
    description = db.Column(db.String(8192))
    img_filename = db.Column(db.String(128))

    def jsonify(self):
        """
        Returns the Project as a JSON object

        -> JSON Object
        """

        output = {
            "id": self.id,
            "title": self.title,
            "repo_link": self.repo_link,
            "repo_link_description": self.repo_link_description,
            "live_link": self.live_link,
            "live_link_description": self.live_link_description,
            "short_description": self.short_description,
            "description": self.description,
            "img_filename": self.img_filename,
        }

        print(output)

        return output