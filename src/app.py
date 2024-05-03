'''
Blub module doc string.
'''
import datastorage

import json
from flask import request, Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s: %(message)s')

@app.route('/', methods=['GET'])
def index():
    '''
    Blub function doc string.
    '''
    return json.dumps({'name': 'David',
                       'mail': 'david.herzig@roche.com'})


@app.route('/experiment', methods=['POST', 'GET'])
def create_experiment():
    '''
    Blub function doc string.
    '''
    ds = datastorage.DataStorage()
    if request.method == 'POST':
        form_data = request.data
        data = json.loads(form_data)
        id = ds.create_experiment(data['name'])
        return json.dumps({'result': id})
    elif request.method == 'GET':
        return ds.get_experiments()


@app.route('/patient', methods=['POST', 'GET'])
def create_patient():
    '''
    Blub function doc string.
    '''
    ds = datastorage.DataStorage()
    if request.method == 'POST':
        name = request.args.get('name')
        ds = datastorage.DataStorage()
        id = ds.create_patient(name)
        return json.dumps({'result': id})
    elif request.method == 'GET':
        return ds.get_patients()


@app.route('/store', methods=['POST'])
def store_data():
    '''
    Blub function doc string.
    '''
    pass


@app.route('/upload', methods=['POST'])
def upload_data(data):
    '''
    Blub function doc string.
    '''
    pass


if __name__ == '__main__':
    print('Hello World')

    ds1 = datastorage.DataStorage()
    print(ds1.create_experiment('Experiment'))
    print(ds1.get_experiments())

    ds2 = datastorage.DataStorage()
    print(ds2.create_experiment('Experiment2'))
    print(ds2.get_experiments())
