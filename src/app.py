'''
Blub module doc string.
'''
import logging
import tracemalloc
import json

from flask import request, Flask

import datastorage

app = Flask(__name__)

logging.basicConfig(filename='app.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)

class Experiment:
    '''
    Blub module doc string.
    '''
    def __init__(self, id, name):
        self.id = id
        self.name = name


def to_json(obj):
    '''
    Blub module doc string.
    '''
    return json.dumps(obj, default=lambda obj: obj.__dict__)


def log_malloc():
    '''
    Prints malloc into log.
    '''
    current, peak = tracemalloc.get_traced_memory()
    logger.info(f'Current and peak memory usage: {current}, {peak}')


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
        logger.info(form_data)
        data = json.loads(form_data)
        id = ds.create_experiment(data['name'])
        log_malloc()
        return json.dumps({'result' : id})
    if request.method == 'GET':
        exps = ds.get_experiments()
        exps_array = []
        for key, value in exps.items():
            exp = Experiment(key, value)
            exps_array.append(exp)
        log_malloc()
        return to_json(exps_array)


@app.route('/patient', methods=['POST', 'GET'])
def create_patient():
    '''
    Blub function doc string.
    '''
    ds = datastorage.DataStorage()
    if request.method == 'POST':
        form_data = request.data
        logger.info(form_data)
        data = json.loads(form_data)
        id = ds.create_patient(data['name'])
        log_malloc()
        return json.dumps({'result' : id})
    if request.method == 'GET':
        log_malloc()
        return ds.get_patients()


@app.route('/store', methods=['POST'])
def store_data():
    ds = datastorage.DataStorage()
    form_data = request.data
    logger.info(form_data)
    data = json.loads(form_data)
    filename = data['filename']
    type = data['type']

    if type == 'experiments':
        ds.store_experiments(filename)
    elif type == 'patients':
        ds.store_patients(filename)
    elif type == 'data':
        ds.store_data(filename)
    else:
        logger.warning('invalid data type: ' + type)
    log_malloc()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route('/data', methods=['POST'])
def upload_data():
    form_data = request.data
    logger.info(form_data)
    data = json.loads(form_data)
    ds = datastorage.DataStorage()
    ds.add_data(data)
    log_malloc()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


if __name__ == '__main__':
    tracemalloc.start()
    app.run(debug=True, host="0.0.0.0", port=8080)