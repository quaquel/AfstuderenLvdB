#!/usr/bin/env python
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pysd
import pyNetLogo
import time
import csv
from ema_workbench import (Model, RealParameter, IntegerParameter, ScalarOutcome, ema_logging,
                           perform_experiments, TimeSeriesOutcome, save_results, MultiprocessingEvaluator,
                          CategoricalParameter)
from ema_workbench.em_framework.parameters import create_parameters
import matplotlib.pyplot as plt
from ema_workbench.analysis.plotting import lines, envelopes

from HybridmodelFunctions22Feb import hybridloop


# In[3]:

def main():

    hybridmodel = Model('hybridmodel', function=hybridloop)

    hybridmodel.uncertainties = [IntegerParameter("inputpowerfactor", 15, 25), #7 13
                            IntegerParameter("inputLNGprice", 200, 1000),
                            IntegerParameter("inputtransferprice", 50, 300),
                            IntegerParameter("inputCapincrease", 1000, 3000),
                            IntegerParameter("inputCapincreasetime", 1, 2),
                            IntegerParameter("inputLNGCapincrease", 1000, 3000),
                            IntegerParameter("inputLNGCapincreasetime", 1, 2),
                            RealParameter("DemandBalanceSupplyEnergyPrice", 0.4, 0.7),
                            RealParameter("SupplyElasticityGas", 0.06, 0.07),
                            RealParameter("SupplyElasticityOil", 0.1, 0.2),
                            RealParameter("SupplyElasticityCoal", 0.1, 0.2),
                            RealParameter("SupplyElasticityNuclear", 0.007, 0.017),
                            RealParameter("SupplyElasticityBiofuel", 0.1, 0.2),
                            RealParameter("SupplyElasticityOR", 0.15, 0.3),
                            IntegerParameter("EconomicGrowthScenario", 1, 3),
                            IntegerParameter("EnergyIntensityScenario", 1, 3),
                            RealParameter("CO2coal", 95, 105),
                            RealParameter("CO2oil", 65, 95),
                            RealParameter("Variancepower", -5.0, -0.1),
                            RealParameter("AutonomousEnergyIntensityDecrease", 0, 0.02),
                             
                            IntegerParameter("POil", 8900, 9100),
                            IntegerParameter("PCoal", 2800, 3100),
                            IntegerParameter("PBio", 29000, 32000),
                            IntegerParameter("PNuc", 16000, 17000),
                            IntegerParameter("POR", 19000, 22000),
                            IntegerParameter("PGasE", 6500, 7000),
                            IntegerParameter("PGasNA", 2500, 2700),
                            IntegerParameter("PGasSCA", 2500, 2700),
                            IntegerParameter("PGasCIS", 6500, 7000),
                            IntegerParameter("PGasME", 7000, 8000),
                            IntegerParameter("PGasAF", 7000, 8000),
                            IntegerParameter("PGasAP", 7000, 8000)]

    hybridmodel.outcomes = [TimeSeriesOutcome("EU_GasSup"),
#                         TimeSeriesOutcome("EU_GasDem"),
#                         TimeSeriesOutcome("EU_GasCon"),
                        TimeSeriesOutcome("EU_OilSup"),
#                         TimeSeriesOutcome("EU_OilDem"),
#                         TimeSeriesOutcome("EU_OilCon"),
                        TimeSeriesOutcome("EU_CoalSup"),
#                         TimeSeriesOutcome("EU_CoalDem"),
#                         TimeSeriesOutcome("EU_CoalCon"),
                        TimeSeriesOutcome("EU_NucSup"),
#                         TimeSeriesOutcome("EU_NucDem"),
#                         TimeSeriesOutcome("EU_NucCon"),
                        TimeSeriesOutcome("EU_BioSup"),
#                         TimeSeriesOutcome("EU_BioDem"),
#                         TimeSeriesOutcome("EU_BioCon"),
                        TimeSeriesOutcome("EU_ORSup"),
#                         TimeSeriesOutcome("EU_ORDem"),
#                         TimeSeriesOutcome("EU_ORCon"),
                        TimeSeriesOutcome("EU_EDem"),
                        TimeSeriesOutcome("EU_ESup"),
                        TimeSeriesOutcome("EU_GDP"),
                        TimeSeriesOutcome("EU_CO2"),
                        TimeSeriesOutcome("EU_RusGas"),
                        TimeSeriesOutcome("EU_EUGI"),
                        TimeSeriesOutcome("EU_GIC"),
#                         TimeSeriesOutcome("EU_RGperAG"),
#                         TimeSeriesOutcome("EU_RGperTES"),
#                         TimeSeriesOutcome("EU_RGperGC"),
#                         TimeSeriesOutcome("EU_GICperBBTU"), 
                        TimeSeriesOutcome("Oil_Price"),
                        TimeSeriesOutcome("Coal_Price"),
                        TimeSeriesOutcome("Bio_Price"),
                        TimeSeriesOutcome("Gas_PriceE"),
                        TimeSeriesOutcome("Nuc_PriceE"),
                        TimeSeriesOutcome("OR_PriceE"),
#                         TimeSeriesOutcome("FuncpriceGas"),
#                         TimeSeriesOutcome("FuncpriceOil"),
#                         TimeSeriesOutcome("FuncpriceCoal"),
                        TimeSeriesOutcome("Gas_PriceCIS")]
                        

    hybridmodel.levers = [IntegerParameter("EnergyUnion", 0, 1),
                          IntegerParameter("CO2Cost", 0, 2)]

    ema_logging.log_to_stderr(ema_logging.INFO)
    with MultiprocessingEvaluator(hybridmodel, n_processes=24) as evaluator:
        results = evaluator.perform_experiments(scenarios=200,
                                                policies=6,
                                                levers_sampling='ff')

    save_results(results, './results/1200 runs V30.tar.gz')


if __name__ == "__main__":
    main()
