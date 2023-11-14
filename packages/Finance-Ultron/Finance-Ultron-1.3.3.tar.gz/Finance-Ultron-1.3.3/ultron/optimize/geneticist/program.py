# -*- coding: utf-8 -*-
import numpy as np
import datetime, time, hashlib, json, copy, pdb, itertools, random
from ultron.utilities.logger import kd_logger
from ultron.optimize.model.modelbase import load_module
from ultron.optimize.geneticist.fitness import model_fitness
from ultron.utilities.utils import NumpyEncoder
from ultron.kdutils.create_id import create_id

import warnings

warnings.filterwarnings("ignore")


class Program(object):

    def __init__(self,
                 params_sets,
                 model_sets,
                 method,
                 random_state,
                 p_point_replace,
                 gen,
                 fitness,
                 model_name=None,
                 program=None,
                 parents=None):
        self._id = str(
            int(time.time() * 1000000 + datetime.datetime.now().microsecond))
        self._init_method = method
        self._random_state = random_state
        self._p_point_replace = p_point_replace
        self._gen = gen
        self._fitness = fitness
        self._program = program
        self._parents = parents
        self._raw_fitness = None
        self._create_time = datetime.datetime.now()
        if self._program is None:
            self._program = self.build_program(random_state, params_sets,
                                               model_sets, model_name)
        else:
            self._program = self.reset_program(program)
        self._params = self._program['params']
        self._model_name = self._program['model_name']
        self._params_sets = params_sets[self._model_name]
        self._name = self._model_name + '_' + self._id
        self._short_name = create_id(self._model_name + self._id)
        self._desc = {}
        self.create_identification()
        self._is_valid = True

    def reset_program(self, program):
        kd_logger.info("{0}:model_name:{1},params:{2},".format(
            'reset'.ljust(6), program['model_name'].ljust(20),
            str(program['params']).ljust(30)))
        return program

    def build_program(self, random_state, params_sets, model_sets, model_name):
        ### 选择模型
        if model_name is None:
            #model_name = model_sets[random_state.randint(len(model_sets))]
            copy_model_sets = list(
                itertools.chain.from_iterable(
                    [model_sets for i in range(0, 50)]))
            random.shuffle(copy_model_sets)
            model_name = copy_model_sets[random_state.randint(
                len(copy_model_sets))]
        ##获取模型对应参数集
        model_params_sets = params_sets[model_name]
        params = {}
        for key in model_params_sets.keys():
            copy_params_sets = list(
                itertools.chain.from_iterable(
                    [model_params_sets[key] for i in range(0, 50)]))
            random.shuffle(copy_params_sets)
            params[key] = random_state.choice(copy_params_sets)
        #self._model = load_module(self._model_name)(**params)
        #kd_logger.info("%06s:model_name:%010s, params:%030s" %
        #               ('init', model_name, params))
        kd_logger.info("{0}:model_name:{1},params:{2},".format(
            'init'.ljust(6), model_name.ljust(20),
            str(params).ljust(30)))
        return {'model_name': model_name, 'params': params}

    def log(self):
        print("name:{0},gen:{1},params:{2},fitness:{3},method:{4},token:{5}".
              format(self._name, self._gen, self._params, self._raw_fitness,
                     self._init_method, self._identification))

    def output(self):
        parents = {'method': 'Gen'} if self._parents is None else self._parents
        return {
            'name': self._name,
            'short_name': self._short_name,
            'model_params': self._params,
            'model_name': self._model_name,
            'fitness': self._raw_fitness,
            'gen': self._gen,
            'desc': self._desc,
            'update_time': self._create_time
        }

    def create_identification(self):
        m = hashlib.md5()
        try:
            token = self.transform()
        except Exception as e:
            #ID为key
            token = self._name
        if token is None:
            token = self._name
        m.update(bytes(token, encoding='UTF-8'))
        self._identification = m.hexdigest()

    def transform(self):
        return json.dumps(self._program, cls=NumpyEncoder)

    def get_subtree(self, random_state, program=None):
        if program is None:
            program = self._program
        params = program['params']
        # Choice of crossover points follows Koza's (1992) widely used approach
        # of choosing functions 90% of the time and leaves 10% of the time.
        probs = np.array([
            0.9 if params[node] in self._params_sets[node] else 0.1
            for node in params.keys()
        ])
        probs = np.cumsum(probs / probs.sum())
        start = np.searchsorted(probs, random_state.uniform())
        end = start
        while len(list(params.keys())[start:]) > end - start:
            end += 1
        return start, end

    def reproduce(self):
        return copy.deepcopy(self._program)

    def point_mutation(self, random_state):
        program = copy.deepcopy(self._program)
        mutate = np.where(
            random_state.uniform(
                size=len(program['params'])) < self._p_point_replace)[0]
        removed = [
            list(self._program['params'].keys())[node] for node in mutate
        ]
        remain = list(set(self._program['params'].keys()) - set(removed))
        for key in removed:
            program['params'][key] = random_state.choice(
                self._params_sets[key])
        return program, removed, remain

    def crossover(self, donor, random_state):
        start, end = self.get_subtree(random_state)
        removed = list(self._program['params'].keys())[start:end]
        remain = list(set(self._program['params'].keys()) - set(removed))
        program = copy.deepcopy(self._program)
        for key in removed:
            program['params'][key] = donor['params'][key]
        return program, removed, remain

    def fit(self, features, X, Y):
        model = load_module(self._model_name)(features=features,
                                              **self._params)
        model.fit(X, Y.values)
        self._desc = model.save()

    def raw_fitness(self, features, X, Y, mode, default_value, custom_params,
                    n_splits):
        if self._fitness is None:
            raw_fitness = model_fitness(features=features,
                                        model_name=self._model_name,
                                        X=X,
                                        Y=Y,
                                        mode=mode,
                                        default_value=default_value,
                                        n_splits=n_splits,
                                        params=self._params)
        else:
            raw_fitness = self._fitness(features=features,
                                        model_name=self._model_name,
                                        X=X,
                                        Y=Y,
                                        default_value=default_value,
                                        custom_params=custom_params,
                                        params=self._params)

        self._raw_fitness = raw_fitness
        self.fit(features=features, X=X, Y=Y)
