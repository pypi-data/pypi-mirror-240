import os
import pathlib

from pycomex.functional.experiment import Experiment, get_experiment
from pycomex.utils import file_namespace, folder_path

PATH = pathlib.Path(__file__).parent.absolute()


@Experiment(
    base_path=folder_path(__file__),
    namespace=file_namespace(__file__),
    glob=globals()    
)
def experiment(e: Experiment):
    
    e.log('starting meta experiment...')
    
    exp: Experiment = get_experiment(os.path.join(PATH, '03_analysing.py'))
    exp.REPETITIONS = 3
    exp.logger = e.logger
    exp.name = 'test'
    exp.run()

    print(exp.data)


experiment.run_if_main()