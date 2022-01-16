import pyodbc
import config_file


async def disconnected(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from disconnected where serverid = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def loops(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from loops where serverid = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def pause(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from pause where serverid = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def skip(guild):
    serverid = guild.id
    sql_connection = pyodbc.connect(config_file.sql_connection_string)
    sql_cursor = sql_connection.cursor()
    command = "delete from skipped where serverid = ?"
    sql_cursor.execute(command, serverid)
    sql_connection.commit()


async def turnonoff(guild):
    for what in config_file.functions:
        serverid = guild.id
        sql_connection = pyodbc.connect(config_file.sql_connection_string)
        sql_cursor = sql_connection.cursor()
        command = "delete from turnonoff where idserver = ? and what = ?"
        sql_cursor.execute(command, serverid, what)
        sql_connection.commit()