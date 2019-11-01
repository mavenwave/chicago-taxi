import json
import sys
import numpy as np

from trainer import model

PROJECT_ID = 'mwpmltr'
BUCKET_NAME = 'ross-keras'

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

if __name__=='__main__':
      # download the scaler
    if not path.exists('x_scaler'):
        logging.info('Downloading scaler')
        storage_client = storage.Client(project=project_id)
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob('scalers/x_scaler')
        blob.download_to_filename('x_scaler')
        logging.info('Downloaded scaler')

    x_scaler = joblib.load('x_scaler')

    gen = model.generator_input(['gs://ross-keras/data/full_test_results.csv'], chunk_size=5000, project_id=PROJECT_ID, bucket_name=BUCKET_NAME, x_scaler=x_scaler, batch_size=1)
    sample = gen.__next__()

    input_sample = {}

    input_sample['input'] = sample[0]
    
    print('Produced sample with label {} seconds.'.format(str(int(round(np.exp(sample[1][1]))))))

    with open('input_sample.json', 'w') as outfile:
        json.dump(input_sample, outfile, cls=NumpyEncoder)