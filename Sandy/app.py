# import dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect, jsonify

#database setup
connection_string = "postgres:applepie28@localhost:5432/ustravelapp_db"
engine = create_engine(f'postgresql://{connection_string}')
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
combined_table = Base.classes.usetravelapp
amusement_table = Base.classes.amusementpark
aquarium_table = Base.classes.aquarium
beach_table = Base.classes.beaches
campsite_table = Base.classes.campsite
casino_table = Base.classes.casinos
festival_table = Base.classes.festival
mall_table = Base.classes.malls
park_table = Base.classes.nationalpark
zoo_table = Base.classes.zoo

# Flask Setup
app = Flask(__name__)

# Flask Routes

# home page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rank")
def rank():
    session = Session(engine)

    ranking = session.query(combined_table.state, combined_table.rank_number).all()
    session.close()

    rank_list = []
    for state_name, rank in ranking:
        rank_list_dict = {}
        rank_list_dict["name"] = state_name
        rank_list_dict["rank"] = rank
        rank_list.append(rank_list_dict)
    
    return jsonify(rank_list)


# dynamic state page
@app.route("/<state>")
def dynamic(state):
    # Create a session
    session = Session(engine)

    travel_num = session.query(combined_table.state, combined_table.abbr, combined_table.states_value, combined_table.count_amusement_park, combined_table.count_aquarium, combined_table.count_beach, combined_table.count_casino, combined_table.count_festival, combined_table.count_hotelratings, combined_table.count_malls, combined_table.count_parks, combined_table.count_campsite, combined_table.count_zoo, combined_table.airfare_rank, combined_table.passenger_rank, combined_table.rank_number).\
        filter(combined_table.state == state).all()
    # session.close()

    amusement_query = session.query(amusement_table.amusementpark_name).\
        filter(amusement_table.state == state).all()
    # session.close()

    aquarium_query = session.query(aquarium_table.aquarium_name).\
        filter(aquarium_table.state == state).all()
    # session.close()

    beach_query = session.query(beach_table.beach_name).\
        filter(beach_table.state == state).all()
    # session.close()

    campsite_query = session.query(campsite_table.name).\
        filter(campsite_table.state == state).all()
    # session.close()

    casino_query = session.query(casino_table.casino).\
        filter(casino_table.state == state).all()
    # session.close()

    festival_query = session.query(festival_table.festival_name).\
        filter(festival_table.state == state).all()
    # session.close()

    mall_query = session.query(mall_table.shoppingmall_name).\
        filter(mall_table.state == state).all()
    # session.close()

    park_query = session.query(park_table.national_park_name).\
        filter(park_table.state == state).all()
    # session.close()

    zoo_query = session.query(zoo_table.zoo_name).\
        filter(zoo_table.state == state).all()
    # session.close()


     # add all data into a list to be jsonified
    start_list = []
    for state, abbr, dollar, amusement_num, aquarium_num, beach_num, casino_num, festival_num, hotel, mall_num, park_num, campsite_num, zoo_num, airfare, passenger, rank in travel_num:
        start_list_dict = {}
        start_list_dict["state"] = state
        start_list_dict["abbreviation"] = abbr
        start_list_dict["dollar_value"] = dollar
        start_list_dict["amusement_park_num"] = amusement_num
        start_list_dict["aquarium_num"] = aquarium_num
        start_list_dict["beach_num"] = beach_num
        start_list_dict["casino_num"] = casino_num
        start_list_dict["festival_num"] = festival_num
        start_list_dict["hotel_ratings"] = hotel
        start_list_dict["mall_num"] = mall_num
        start_list_dict["national_park_num"] = park_num
        start_list_dict["campsite_num"] = campsite_num
        start_list_dict["zoo_num"] = zoo_num
        start_list_dict["airfare_rank"] = airfare
        start_list_dict["passenger_rank"] = passenger
        start_list_dict["overall_rank"] = rank
        start_list.append(start_list_dict)
    
    amusement_list = []
    aquarium_list = []
    beach_list = []
    campsite_list = []
    casino_list = []
    festival_list = []
    mall_list = []
    park_list = []
    zoo_list = []

    attraction_dict = {}

    if amusement_query:
        for amusement in amusement_query:
            for item in amusement:
                amusement_list.append(item)
            attraction_dict["amusement_park_list"] = amusement_list

    if aquarium_query:
        for aquarium in aquarium_query:
            for item in aquarium:
                aquarium_list.append(item)
            attraction_dict["aquarium_list"] = aquarium_list

    if beach_query:
        for beach in beach_query:
            for item in beach:
                beach_list.append(item)
            attraction_dict["beach_list"] = beach_list

    if campsite_query:
        for campsite in campsite_query:
            for item in campsite:
                campsite_list.append(item)
            attraction_dict["campsite_list"] = campsite_list

    if casino_query:
        for casino in casino_query:
            for item in casino:
                casino_list.append(item)
            attraction_dict["casino_list"] = casino_list

    if festival_query:
        for festival in festival_query:
            for item in festival:
                festival_list.append(item)
            attraction_dict["festival_list"] = festival_list

    if mall_query:
        for mall in mall_query:
            for item in mall:
                mall_list.append(item)
            attraction_dict["mall_list"] = mall_list

    if park_query:
        for park in park_query:
            for item in park:
                park_list.append(item)
            attraction_dict["national_park_list"] = park_list

    if zoo_query:
        for zoo in zoo_query:
            for item in zoo:
                zoo_list.append(item)
            attraction_dict["zoo_list"] = zoo_list
    start_list.append(attraction_dict)

    return jsonify(start_list)

if __name__ == "__main__":
    app.run(debug=True)