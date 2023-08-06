# Copyright Toyota Research Institute 2022
from camd.campaigns.base import Campaign
from sklearn.neural_network import MLPRegressor
from camd.agent.stability import AgentStabilityAdaBoost
from camd.analysis import StabilityAnalyzer
from camd.experiment.base import Experiment
from camd.experiment.dft import get_mp_formation_energy_from_m3gnet
import pandas as pd
import os
import shutil
from m3gnet.models import Relaxer
from tqdm import tqdm

import warnings
warnings.filterwarnings('ignore')


if __name__ == "__main__":
    # We'll be using a cached dataset, but here's an example of how you
    # can fetch data from the materials project if needed
    # from pymatgen.ext.matproj import MPRester
    # from camd.utils.data import get_default_featurizer
    # with MPRester() as mpr:
    #    data = mpr.query({"nelements": {"$lte": 2}, "elements": "S"},
    #              ['structure', 'material_id',
    #               'pretty_formula', 'formation_energy_per_atom'])
    # data = {r['material_id']: r for r in data}
    # dataframe = pd.DataFrame.from_dict(data, orient='index')
    # featurizer = get_default_featurizer()
    # dataframe = featurizer.featurize_dataframe(dataframe, 'structure', ignore_errors=True)
    #  dataframe = dataframe.rename(columns={
    #      "formation_energy_per_atom": "delta_e",
    #      "pretty_formula": "Composition"
    #  })
    # dataframe.to_pickle("binary_sulfides_mp.pickle")


    # In[4]:


    dataframe = pd.read_pickle("binary_sulfides_mp.pickle")
    dataframe = dataframe.dropna()


    # In[5]:


    dataframe[['Composition', 'delta_e']].head()


    # In[6]:


    # CAMD generates structure using a structure generation algorithm
    # defined by Wyckoff-site enumerated prototypes, we'll also cache
    # these because featurization takes a little while, but here's the code
    use_cached = True
    if not use_cached:
        from camd.domain import StructureDomain, heuristic_setup
        chemsys = ["Mn", "S"]
        max_coeff, charge_balanced = heuristic_setup(chemsys)
        domain = StructureDomain.from_bounds(
            chemsys,
            charge_balanced=charge_balanced,
            n_max_atoms=20,
            grid=(1, max_coeff)
        )
        candidate_data = domain.candidates()
        candidate_data.to_pickle("mn_s_candidates.pickle")
    else:
        candidate_data = pd.read_pickle("mn_s_candidates.pickle")


    # In[ ]:





    # In[7]:


    # Define the experiment
    # Experiment classes in CAMD require 3 methods
    # - submit starts the calculation
    # - get_results returns a dataframe with results
    # - monitor is a method to wait until results are done, which ensures
    #   compatibility with CAMD logic
    class M3GNetExperiment(Experiment):
        def submit(self, data):
            """data is a pandas dataframe that must have a column called structure"""
            # Sometimes in this method you might submit to an external system,
            # e.g. AWS batch or a supercomputer, but in this case we just update
            # the data because we do the computation locally
            self.update_current_data(data)

        def monitor(self):
            relaxer = Relaxer()
            delta_es = []
            for index, row in tqdm(self.current_data.iterrows()):
                s = row['structure']
                t = relaxer.relax(s)["trajectory"]
                e = t.energies[-1].flatten()[0]
                delta_e = get_mp_formation_energy_from_m3gnet(
                    e, s
                )
                delta_es.append(delta_e)
            self.current_data['delta_e'] = delta_es

        def get_results(self):
            return self.current_data

        def save(self):
            return None


    # In[8]:


    ##########################################################
    # Binary stable material discovery 50:50 explore/exploit agent
    ##########################################################
    n_query = 5  # This many new candidates are "calculated with DFT"
    # (i.e. requested from Oracle -- DFT)
    agent = AgentStabilityAdaBoost(
        model=MLPRegressor(hidden_layer_sizes=(40, 20)),
        n_query=n_query,
        hull_distance=0.2,
        uncertainty=True,
        exploit_fraction=0.8, # Number of candidates chosen by the ML model, rest are random
        alpha=0.5, # Weighting of the estimated uncertainty from the AdaBoost ensemble
        n_estimators=10
    )
    analyzer = StabilityAnalyzer(hull_distance=0.2)
    experiment = M3GNetExperiment()
    candidate_data = dataframe

    # Usually takes ~10 minutes
    path = os.path.join(os.getcwd(), "m3gnet_structure_discovery")
    shutil.rmtree(path, ignore_errors=True)
    os.makedirs(path)
    new_loop = Campaign(
        candidate_data,
        agent,
        experiment,
        analyzer,
        seed_data=dataframe,
        path=path
    )
    new_loop.auto_loop(n_iterations=6, initialize=True)

    new_loop.history.plot.bar(y='total_discovery')