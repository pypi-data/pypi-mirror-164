#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gzip
import os
import shutil
from multiprocessing import Process

import click
import pymysql
import tqdm


def gunzip(input: str, output: str):
    pbar = tqdm.tqdm(total=os.path.getsize(input), unit='b', unit_scale=True, unit_divisor=1024)
    with open(input, 'rb') as inf, gzip.open(inf, "rb") as rf, open(output, 'wb') as of:
        while True:
            buf = rf.read(shutil.COPY_BUFSIZE)
            if not buf:
                break
            of.write(buf)
            pbar.n = inf.tell()
            pbar.update(0)


@click.command
@click.option("-p", "--password", help="password to use", required="True")
@click.option("-u", "--user", help="user to use", required="True")
@click.option("-h", "--host", help="database host", required="True")
@click.option("-d", "--database", help="database to use", required="True")
@click.option("-t", "--table", help="table name", required="True")
@click.option("-i", "--input", help="input CSV/TSV (gz) filename", required="True", type=click.Path(exists=True))
@click.option("-f", "--format" , help="SQL CSV/TSV format definition (default \"LINES TERMINATED BY '\\r\\n' IGNORE 1 ROWS\")", default="LINES TERMINATED BY '\\r\\n' IGNORE 1 ROWS")
def load_db(host: str, user: str, password: str, database: str, table: str, input: str, format: str):
    """Load a CSV/TSV (gz) file into MariaDB using LOAD DATA LOCAL INFILE"""
    with pymysql.connect(host=host, user=user, password=password, database=database, charset='utf8mb4', local_infile=True,
                         autocommit=True) as con, con.cursor() as cur:
        if input.endswith(".gz"):
            os.mkfifo("pipe.tsv", 0o600)
            p = Process(target=gunzip, args=(input, "pipe.tsv"))
            p.start()
            try:
                cur.execute(f"LOAD DATA LOCAL INFILE 'pipe.tsv' INTO TABLE {table} {format}")
                print(f"Ingested {cur.rowcount} rows.")
                cur.execute("SHOW WARNINGS")
                print(f"Errors and warnings encountered: {cur.fetchall()}")
                p.join()
            finally:
                p.terminate()
                os.remove("pipe.tsv")
        else:
            cur.execute(f"LOAD DATA LOCAL INFILE '{input}' INTO TABLE {table} {format}")
            print(f"Ingested {cur.rowcount} rows.")
            cur.execute("SHOW WARNINGS")
            print(f"Errors and warnings encountered: {cur.fetchall()}")


if __name__ == '__main__':
    load_db()


