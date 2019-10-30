import json
import sys
import numpy as np

from trainer import model

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

if __name__=='__main__':
    gen = model.generator_input(['gs://ross-keras/data/full_test_results.csv'], chunk_size=5000)
    sample = gen.__next__()

    input_sample = {}

    input_arrs = []
    for i in range(0, len(sample[0])):
        input_arrs.append(sample[0][i][0])

    input_sample['input'] = input_arrs
    
    print('Produced sample with label {}'.format(str(sample[1][1])))

    with open('input_sample.json', 'w') as outfile:
        json.dump(input_sample, outfile, cls=NumpyEncoder)