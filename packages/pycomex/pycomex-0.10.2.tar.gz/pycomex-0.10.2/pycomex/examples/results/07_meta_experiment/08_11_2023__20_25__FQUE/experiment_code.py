import os
import pathlib
import typing as t

from pycomex.functional.experiment import Experiment, get_experiment
from pycomex.utils import file_namespace, folder_path, random_string

PATH = pathlib.Path(__file__).parent.absolute()

# :param REPETITIONS:
#       pass
REPETITIONS: int = 3

# :param NUM_WORDS_SWEEP:
#       pass
NUM_WORDS_SWEEP: t.List[int] = [10, 100, 1000]


@Experiment(
    base_path=folder_path(__file__),
    namespace=file_namespace(__file__),
    glob=globals()    
)
def experiment(e: Experiment):
    
    e.log('starting meta experiment...')
    
    for num_words in e.NUM_WORDS_SWEEP:
        
        e.log(f'running experiment with {num_words} number of words')
        exp: Experiment = get_experiment(os.path.join(PATH, '03_analysing.py'))
        exp.NUM_WORDS = num_words
        exp.logger = e.logger
        exp.name = 'meta_' + random_string()
        exp.run()

        e[f'metrics/length/{num_words}'] = sum(exp['metrics/length'].values())


experiment.run_if_main()