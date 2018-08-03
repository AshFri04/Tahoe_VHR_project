
""" Models for Tahoe VHR Project. """


from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()

###########################################################################

# Model definitions


class ResidentialDetails(db.Model):
    """ Table containing residential information about each VHR ownwer. """

    __tablename__ = "residential_details"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    APN = db.Column(db.String(255))
    vr_address = db.Column(db.String(255))
    vr_address_city = db.Column(db.String(255))
    vr_address_state = db.Column(db.String(255))
    vr_address_zip = db.Column(db.String(255))
    vr_address_county = db.Column(db.String(255))
    owner = db.Column(db.String(255))

    owner_first_name = db.Column(db.String(100))
    owner_last_name = db.Column(db.String(100))
    owner_address = db.Column(db.String(255))
    owner_address_city = db.Column(db.String(255))
    owner_address_state = db.Column(db.String(255))
    owner_address_zip = db.Column(db.String(255))
   
    def __repr__(self):
        """ Provide helpful representation when printed. """

        return "<residentialDetails user_id={} owner_first_name={} owner_last_name={} owner_address={} vhr_address={}>".format(self.user_id, self.owner_first_name, self.owner_last_name, self.owner_address, self.vhr_address)

###########################################################################

# Helper Functions

def connect_to_db(app, db_uri="postgresql:///tahoe_vr"):
    """ Connect the database to my Flask app. """

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tahoe_vr'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to Database."

