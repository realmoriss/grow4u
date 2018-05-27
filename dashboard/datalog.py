from flask import Blueprint, jsonify
from dashboard.db import get_db

bp = Blueprint('datalog', __name__, url_prefix='/datalog')

@bp.route("/lasthour", methods=["GET"])
def lasthour():
    db = get_db()
    sensor_data = {"date": [], "temp": [], "hum": [], "soil": []}
    try:
        with db.cursor() as cursor:
            select_cmd = "SELECT `date`, AVG(`temp`) AS `temp`, AVG(`hum`) AS `hum`, AVG(`soil`) AS `soil` FROM `sensor_log` WHERE `date` > NOW() - INTERVAL 1 HOUR GROUP BY YEAR(`date`), MONTH(`date`), DAY(`date`), HOUR(`date`), MINUTE(`date`)"
            cursor.execute(select_cmd)
            for point in cursor:
                sensor_data["date"].append(point["date"].isoformat())
                sensor_data["temp"].append(round(point["temp"], 2))
                sensor_data["hum"].append(round(point["hum"], 2))
                sensor_data["soil"].append(round(point["soil"], 2))
    except Exception as e:
        return "Error: " + str(e)
    return jsonify(sensor_data)


@bp.route("/hourly", methods=["GET"])
def hourly():
    db = get_db()
    sensor_data = {"date": [], "temp": [], "hum": [], "soil": []}
    try:
        with db.cursor() as cursor:
            select_cmd = "SELECT `date`, AVG(`temp`) AS `temp`, AVG(`hum`) AS `hum`, AVG(`soil`) AS `soil` FROM `sensor_log` WHERE `date` > NOW() - INTERVAL 1 DAY GROUP BY YEAR(`date`), MONTH(`date`), DAY(`date`), HOUR(`date`)"
            cursor.execute(select_cmd)
            for point in cursor:
                sensor_data["date"].append(point["date"].isoformat())
                sensor_data["temp"].append(round(point["temp"], 2))
                sensor_data["hum"].append(round(point["hum"], 2))
                sensor_data["soil"].append(round(point["soil"], 2))
    except Exception as e:
        return "Error: " + str(e)
    return jsonify(sensor_data)


@bp.route("/daily", methods=["GET"])
def daily():
    db = get_db()
    sensor_data = {"date": [], "temp": [], "hum": [], "soil": []}
    try:
        with db.cursor() as cursor:
            select_cmd = "SELECT `date`, AVG(`temp`) AS `temp`, AVG(`hum`) AS `hum`, AVG(`soil`) AS `soil` FROM `sensor_log` WHERE `date` > NOW() - INTERVAL 1 MONTH GROUP BY YEAR(`date`), MONTH(`date`), DAY(`date`)"
            cursor.execute(select_cmd)
            for point in cursor:
                sensor_data["date"].append(point["date"].isoformat())
                sensor_data["temp"].append(round(point["temp"], 2))
                sensor_data["hum"].append(round(point["hum"], 2))
                sensor_data["soil"].append(round(point["soil"], 2))
    except Exception as e:
        return "Error: " + str(e)
    return jsonify(sensor_data)
