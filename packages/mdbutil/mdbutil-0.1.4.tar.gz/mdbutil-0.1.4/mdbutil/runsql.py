#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import pymysql
import os


@click.command
@click.option("-p", "--password", help="password to use", required="True")
@click.option("-u", "--user", help="user to use", required="True")
@click.option("-h", "--host", help="database host", required="True")
@click.option("-d", "--database", help="database to use")
@click.option("-s", "--sql", help="input SQL command or filename containing the statements to be executed", required="True")
def run_sql(host: str, user: str, password: str, database: str, sql: str):
    """Run a given SQL script file"""
    if os.path.exists(sql):
        with open(sql, 'rt') as inf:
            statements = inf.read().split(";")
    else:
        statements = [ sql ]
    with pymysql.connect(host=host, user=user, password=password, charset='utf8mb4', local_infile=True,
                         autocommit=True, database=database) as con, con.cursor() as cur:
        for statement in statements:
            if len(statement.strip()) > 0:
                print(f"Running statement:\n{statement}")
                cur.execute(statement)
                warnings = cur.fetchall()
                if len(warnings) > 0:
                    print(f"Errors and warnings encountered: {warnings} while running {statement}.")


if __name__ == '__main__':
    run_sql()
