from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import random

app = Flask(__name__)


def favorite_rank() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'user_data'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    animal = str(random.choice(['dog','cat','python','panda']))
    cursor.execute(f"""insert into user_data.animals_rank (name, value)
                       values ('{animal}',{str(random.randint(1, 10))})""")
    connection.commit()
    cursor.execute('SELECT lower(name), count(value) rank FROM animals_rank group by lower(name)')
    results = [{name: value} for (name, value) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'favorite_rank': favorite_rank()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
