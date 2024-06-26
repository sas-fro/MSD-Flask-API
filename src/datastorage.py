'''
Blub module doc string.
'''
import json
import idgenerator


class DataPoint:
    '''
    Blub class doc string.
    '''
    def __init__(self, patient_id, experiment_id, data):
        '''
        Blub function doc string.
        '''
        self.id = idgenerator.generate_unique_identifier()
        self.patient_id = patient_id
        self.experiment_id = experiment_id
        self.data = data


class DataStorage:
    '''
    Blub class doc string.
    '''
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataStorage, cls).__new__(cls)
            cls.instance.experiments = {}
            cls.instance.patients = {}
            cls.instance.data = []
        return cls.instance

    def create_patient(self, name):
        '''
        Blub function doc string.
        '''
        patient_id = len(self.patients)
        self.patients[patient_id] = name
        return patient_id

    def create_experiment(self, name):
        '''
        Blub function doc string.
        '''
        experiment_id = len(self.experiments)
        self.experiments[experiment_id] = name
        return experiment_id

    def get_patients(self):
        '''
        Blub function doc string.
        '''
        return self.patients

    def get_experiments(self):
        '''
        Blub function doc string.
        '''
        return self.experiments

    def add_data(self, dataobj):
        '''
        Blub function doc string.
        '''
        self.data.append(dataobj)

    def store_data(self, filename):
        '''
        Blub function doc string.
        '''
        # store data into file
        self.store(filename, self.data)
        self.data.clear()

    def store_patients(self, filename):
        '''
        Blub function doc string.
        '''
        self.store(filename, self.patients)

    def store_experiments(self, filename):
        '''
        Blub function doc string.
        '''
        self.store(filename, self.experiments)
    
    def store(self, filename, data):
        '''
        Blub function doc string.
        '''
        json_object = json.dumps(data, indent=4)
        with open(filename + ".json", "w") as outfile:
            outfile.write(json_object)
