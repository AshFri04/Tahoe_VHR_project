import csv

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from model import connect_to_db, db, ResidentialDetails
from server import app

###########################################################################

# Functions associated with seeding the database


def set_values_for_residential_data():
    # Reading csv file
    with open('residentialPropertyDetails.csv', 'r') as my_file:
        csv_reader = csv.reader(my_file)

        # this will just create an object in memory of the file (need to loop over data)
        # print csv_reader

        # Loops over the first value (which is data we don't need for parsing)
        next(csv_reader)

        for line in csv_reader:
            APN = line[1]
            vr_address = line[3]
            vr_address_city = line[4]
            vr_address_state = line[5]
            vr_address_zip = line[6]
            vr_address_county = line[2]
            owner = line[9]

            owner_first_name = line[10]
            owner_last_name = line[11]
            owner_address = line[14]
            owner_address_city = line[15]
            owner_address_state = line[16]
            owner_address_zip = line[17]

            # For debugging purposes
            # print APN, vr_address, vr_address_city, vr_address_state, vr_address_zip, vr_address_county, owner, owner_first_name, owner_last_name, owner_address, owner_address_city, owner_address_state, owner_address_zip

            residential_info = ResidentialDetails(APN=APN, vr_address=vr_address, vr_address_city=vr_address_city, vr_address_state=vr_address_state, vr_address_zip=vr_address_zip, vr_address_county=vr_address_county, owner=owner, owner_first_name=owner_first_name, owner_last_name=owner_last_name, owner_address=owner_address, owner_address_city=owner_address_city, owner_address_state=owner_address_state, owner_address_zip=owner_address_zip)

            #Add residential data to the database
            db.session.add(residential_info)

        db.session.commit()


if __name__ == "__main__":

    connect_to_db(app)

    set_values_for_residential_data()
        
