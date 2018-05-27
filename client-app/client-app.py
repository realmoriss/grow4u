#!/usr/bin/env python3

import sys
import serial
import io
import datetime
import time
import pymysql

def readCmd(sio: io.TextIOWrapper, cmd: str):
    dt_out = sio.write(cmd + "\n")
    sio.flush()
    if dt_out==0:
        raise Exception("Unable to write to device.")
    if sio.readline().strip()!=cmd:
        raise Exception("Device is not responding.")
    return sio.readline().strip()

def main():
    db_host = ""
    db_user = ""
    db_pass = ""
    db_name = ""
    db_charset = "utf8mb4"
    db = pymysql.connect(host=db_host, user=db_user, password=db_pass,
                         db=db_name, charset=db_charset, cursorclass=pymysql.cursors.DictCursor)

    try:
        ser = serial.Serial(port="/dev/ttyACM0", baudrate=38400, timeout=1)
    except Exception as e:
        print("Unable to connect to serial port: " + str(e))
        sys.exit(1)

    ser.flushInput()
    ser.flushOutput()

    try:
        # The buffer size should be set to 1 for both BufferedRWPair and TextIOWrapper
        # see issue: https://stackoverflow.com/a/27894482
        sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding="ascii")
        sio._CHUNK_SIZE = 1
        print("Started logging...")

        with db.cursor() as cursor:
            create_table_cmd = "CREATE TABLE IF NOT EXISTS `sensor_log` (`id` INT NOT NULL AUTO_INCREMENT, `date` DATETIME, `temp` FLOAT, `hum` FLOAT, `soil` FLOAT, PRIMARY KEY (`id`))"
            cursor.execute(create_table_cmd)
            db.commit()

        with db.cursor() as cursor:
            insert_cmd = "INSERT INTO `sensor_log` (`date`, `temp`, `hum`, `soil`) VALUES (%s, %s, %s, %s)"
            while True:
                cursor.execute(insert_cmd, (datetime.datetime.now().isoformat(), readCmd(sio, "temp"), readCmd(sio, "hum"), readCmd(sio, "soil")))
                db.commit()
                time.sleep(10)

    except Exception as e:
        print("Error while communicating: " + str(e))
    except KeyboardInterrupt:
        print("Bye.")
    finally:
        db.close()

if __name__ == "__main__":
    main()

