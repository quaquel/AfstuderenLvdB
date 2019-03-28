#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import pysd
import pyNetLogo
# import time
from ema_workbench import (Model, RealParameter, IntegerParameter, ScalarOutcome, ema_logging,
                           perform_experiments, TimeSeriesOutcome, save_results, MultiprocessingEvaluator,
                          CategoricalParameter)
# from ema_workbench.em_framework.parameters import create_parameters
# import matplotlib.pyplot as plt
# from ema_workbench.analysis.plotting import lines, envelopes

# pd.set_option('display.max_columns', 30000)
# pd.set_option('display.max_rows', 30000)


# In[2]:
resultstosave = ['Available Gas',
                 'Available resources from stocks Oil',
                 'Available resources from stocks Coal',
                 'Extraction capacity installed Nuclear',
                 'Available resources from stocks Biofuels',
                 'Extraction capacity installed other Renewables',
                 'Energy Demand',
                 'Total Energy Supply',
                 'GDP',
                 'CO2 emissions',
                 'Russian Gas',
                 'EUgasimport',
                 'Gas Import Costs']

priceinputlist_E = ['Initial energy resource prices Oil',
                     'Initial energy resource prices Coal',
                     'Initial energy resource prices Biofuels',
                     'Initial energy resource prices Nuclear E',
                     'Initial energy resource prices other Renewables E',
                     'Initial energy resource prices Gas E']

energyprices_E = ['Energy resource prices Oil',
                   'Energy resource prices Coal',
                   'Energy resource prices Biofuels',
                   'Energy resource prices Nuclear E',
                   'Energy resource prices other Renewables E',
                   'Energy resource prices Gas E']

priceinputlist_NA = ['Initial energy resource prices Oil',
                     'Initial energy resource prices Coal',
                     'Initial energy resource prices Biofuels',
                     'Initial energy resource prices Nuclear NA',
                     'Initial energy resource prices other Renewables NA',
                     'Initial energy resource prices Gas NA']

energyprices_NA = ['Energy resource prices Oil',
                   'Energy resource prices Coal',
                   'Energy resource prices Biofuels',
                   'Energy resource prices Nuclear NA',
                   'Energy resource prices other Renewables NA',
                   'Energy resource prices Gas NA']

priceinputlist_SCA = ['Initial energy resource prices Oil',
                     'Initial energy resource prices Coal',
                     'Initial energy resource prices Biofuels',
                     'Initial energy resource prices Nuclear SCA',
                     'Initial energy resource prices other Renewables SCA',
                     'Initial energy resource prices Gas SCA']

energyprices_SCA = ['Energy resource prices Oil',
                   'Energy resource prices Coal',
                   'Energy resource prices Biofuels',
                   'Energy resource prices Nuclear SCA',
                   'Energy resource prices other Renewables SCA',
                   'Energy resource prices Gas SCA']

priceinputlist_CIS = ['Initial energy resource prices Oil',
                     'Initial energy resource prices Coal',
                     'Initial energy resource prices Biofuels',
                     'Initial energy resource prices Nuclear CIS',
                     'Initial energy resource prices other Renewables CIS',
                     'Initial energy resource prices Gas CIS']

energyprices_CIS = ['Energy resource prices Oil',
                    'Energy resource prices Coal',
                    'Energy resource prices Biofuels',
                    'Energy resource prices Nuclear CIS',
                    'Energy resource prices other Renewables CIS',
                    'Energy resource prices Gas CIS']

priceinputlist_ME = ['Initial energy resource prices Oil',
                     'Initial energy resource prices Coal',
                     'Initial energy resource prices Biofuels',
                     'Initial energy resource prices Nuclear ME',
                     'Initial energy resource prices other Renewables ME',
                     'Initial energy resource prices Gas ME']

energyprices_ME = ['Energy resource prices Oil',
                    'Energy resource prices Coal',
                    'Energy resource prices Biofuels',
                    'Energy resource prices Nuclear ME',
                    'Energy resource prices other Renewables ME',
                    'Energy resource prices Gas ME']

priceinputlist_AF = ['Initial energy resource prices Oil',
                     'Initial energy resource prices Coal',
                     'Initial energy resource prices Biofuels',
                     'Initial energy resource prices Nuclear AF',
                     'Initial energy resource prices other Renewables AF',
                     'Initial energy resource prices Gas AF']

energyprices_AF = ['Energy resource prices Oil',
                    'Energy resource prices Coal',
                    'Energy resource prices Biofuels',
                    'Energy resource prices Nuclear AF',
                    'Energy resource prices other Renewables AF',
                    'Energy resource prices Gas AF']

priceinputlist_AP = ['Initial energy resource prices Oil',
                     'Initial energy resource prices Coal',
                     'Initial energy resource prices Biofuels',
                     'Initial energy resource prices Nuclear AP',
                     'Initial energy resource prices other Renewables AP',
                     'Initial energy resource prices Gas AP']

energyprices_AP = ['Energy resource prices Oil',
                    'Energy resource prices Coal',
                    'Energy resource prices Biofuels',
                    'Energy resource prices Nuclear AP',
                    'Energy resource prices other Renewables AP',
                    'Energy resource prices Gas AP']

priceinputcountry = ['Energy Price Oil',
                     'Energy Price Coal',
                     'Energy Price Biofuels',
                     'Energy Price Nuclear',
                     'Energy Price other Renewables',
                     'Energy Price Gas']

priceinputlist = [priceinputlist_E,
                 priceinputlist_NA,
                 priceinputlist_SCA,
                 priceinputlist_CIS,
                 priceinputlist_ME,
                 priceinputlist_AF,
                 priceinputlist_AP]

energypriceslist = [energyprices_E,
                   energyprices_NA,
                   energyprices_SCA,
                   energyprices_CIS,
                   energyprices_ME,
                   energyprices_AF,
                   energyprices_AP]

listofcolumnsresults = ['Extraction capacity in preparation Gas', 
                        'Extraction capacity installed Gas',
                        'Mothballed capacity Gas',
                        'Undiscovered resources Gas',
                        'Discovered resources reserve base Gas',
                        'Extraction capacity in preparation Oil',
                        'Extraction capacity installed Oil',
                        'Mothballed capacity Oil',
                        'Energy stocks Oil',
                        'Undiscovered resources Oil',
                        'Discovered resources reserve base Oil',
                        'Extraction capacity in preparation Coal',
                        'Extraction capacity installed Coal',
                        'Mothballed capacity Coal',
                        'Energy stocks Coal',
                        'Undiscovered resources Coal',
                        'Discovered resources reserve base Coal',
                        'Extraction capacity in preparation Nuclear',
                        'Extraction capacity installed Nuclear',
                        'Mothballed capacity Nuclear',
                        'Extraction capacity in preparation Biofuels',
                        'Extraction capacity installed Biofuels',
                        'Mothballed capacity Biofuels',
                        'Energy stocks Biofuels',
                        'Extraction capacity in preparation other Renewables',
                        'Extraction capacity installed other Renewables',
                        'Mothballed capacity other Renewables',
                        'GDP',
                        'Energy Intensity GDP',
                        'Future Effect of Shortage on Decoupling',
                        'Effect of Supply Shortage on Decoupling',
                        'TIME',
                        'Region',
                        'Cumulative extracted fuel Gas',
                        'Unit costs Gas',
                        'Cumulative extracted fuel Oil',
                        'Unit costs Oil',
                        'Cumulative extracted fuel Coal',
                        'Unit costs Coal',
                        'Cumulative extracted fuel Nuclear',
                        'Normalised costs relative in relation to learning effects t1 Nuclear',
                        'Unit costs Nuclear',
                        'Cumulative extracted fuel Biofuels',
                        'Normalised costs relative in relation to learning effects t1 Biofuels',
                        'Unit costs Biofuels',
                        'EROEI Biofuels',
                        'Cumulative extracted fuel other Renewables',
                        'Normalised costs relative in relation to learning effects t1 other Renewables',
                        'Unit costs other Renewables',
                        'EROEI other Renewables',
                        'Long term normalized profits Gas',
                        'Long term normalized profits Oil',
                        'Long term normalized profits Coal',
                        'Long term normalized profits Nuclear',
                        'Long term normalized profits Biofuels',
                        'Long term normalized profits other Renewables',
                        'EROI resources Gas',
                        'EROI resources Oil',
                        'EROI resources Coal',
                        'Average normalised learning curve on costs Nuclear',
                        'Average normalised learning curve on costs Biofuels',
                        'Average normalised learning curve on costs other Renewables',
                        'Delay order new capacity Gas',
                        'Delay time new capacity Gas',
                        'Time for deteriation of unused capacity Gas',
                        'Initial relation between reserve base and resource size Gas',                        
                        'Average Rb over P gas',
                        'Gas Import',
                        'Gas Export',
                        'Delay order new capacity Oil',
                        'Delay time new capacity Oil',
                        'Time for deteriation of unused capacity Oil',
                        'Initial relation between reserve base and resource size Oil',
                        'Average Rb over P Oil',
                        'Total export Oil',
                        'Total import Oil',
                        'Average throughput time stocks Oil',
                        'Delay order new capacity Coal',
                        'Delay time new capacity Coal',
                        'Time for deteriation of unused capacity Coal',
                        'Initial relation between reserve base and resource size Coal','Average Rb over P Coal',
                        'Total export Coal',
                        'Total import Coal',
                        'Average throughput time stocks Coal',
                        'Delay order new capacity Nuclear',
                        'Delay time new capacity Nuclear',
                        'Time for deteriation of unused capacity Nuclear',
                        'Delay order new capacity Biofuels',
                        'Delay time new capacity Biofuels',
                        'Time for deteriation of unused capacity Biofuels',
                        'Total export Biofuels',
                        'Total import Biofuels',
                        'Average throughput time stocks Biofuels',
                        'Delay order new capacity other Renewables',
                        'Delay time new capacity other Renewables',
                        'Time for deteriation of unused capacity other Renewables',
                        'Factor limiting Economic Growth due to Energy Shortage',
                        'Effect of Energy Shortage on Future Decoupling',
                        'Delay Order Decoupling due to Shortage',
                        'Delay Time Decoupling due to Shortage',
                        'Autonomous Economic Growth Patern Switch',
                        'Autonomous Economic Growth Patern 1',
                        'One Year',
                        'Costs CO2 emissions',
                        'CO2 emissions of natural gas',
                        'CO2 emissions of Oil',
                        'CO2 emissions of coal',
                        'MATH Pi',
                        'Variance power',
                        'Average EROEI energy sources lognormal',
                        'Maximum EROEI',
                        'Minimum EROEI',
                        'Delay order forecasts',
                        'Short forecasting period',
                        'Experience curve parameter extraction',
                        'Initial normalised costs relative in relation to learning effects Nuclear2',
                        'Summed delay time new capacity',
                        'Initial normalised costs relative in relation to learning effects Biofuels2',
                        'Potential EROEI Biofuels',
                        'Initial normalised costs relative in relation to learning effects other Renewables2',
                        'Potential EROEI other Renewables',
                        'Maximum relative mothballing Gas',
                        'Long term profits energy supply period Gas',
                        'Supply elasticity Gas',
                        'Investment fraction normalized profits Gas',
                        'Maximum relative mothballing Oil',
                        'Long term profits energy supply period Oil',
                        'Supply elasticity Oil',
                        'Investment fraction normalized profits Oil',
                        'Maximum relative mothballing Coal',
                        'Long term profits energy supply period Coal',
                        'Supply elasticity Coal',
                        'Investment fraction normalized profits Coal',
                        'Maximum relative mothballing Nuclear',
                        'Long term profits energy supply period Nuclear',
                        'Supply elasticity Nuclear',
                        'Investment fraction normalized profits Nuclear',
                        'Maximum relative mothballing Biofuels',
                        'Long term profits energy supply period Biofuels',
                        'Supply elasticity Biofuels',
                        'Investment fraction normalized profits Biofuels',
                        'Maximum relative mothballing other Renewables',
                        'Long term profits energy supply period other Renewables',
                        'Supply elasticity other Renewables',
                        'Investment fraction normalized profits other Renewables',
                        'Russian Gas',
                        'Storage goal',
                        'Completing new extraction capacity Gas',
                        'Completing new extraction capacity Oil',
                        'Completing new extraction capacity Coal',
                        'Completing new extraction capacity Nuclear',
                        'Completing new extraction capacity Biofuels',
                        'Completing new extraction capacity other Renewables',
                        'Decoupling Effect Materializing',                       
                        'Normalised costs relative in relation to learning effects t1 Gas',
                        'Initial normalised costs relative in relation to learning effects Gas2',
                        'Average normalised learning curve on costs Gas',
                        'Normalised costs relative in relation to learning effects t1 Oil',
                        'Initial normalised costs relative in relation to learning effects Oil2',
                        'Average normalised learning curve on costs Oil',
                        'Normalised costs relative in relation to learning effects t1 Coal',
                        'Initial normalised costs relative in relation to learning effects Coal2',
                        'Average normalised learning curve on costs Coal',
                        'Gas Import Costs',
                        'Autonomous Energy Intensity Decrease',
                        'Previous Demand Factor',
                        'New Energy Demand Gas',
                        'New Energy Demand Oil',
                        'New Energy Demand Coal',
                        'New Energy Demand Nuclear',
                        'New Energy Demand Biofuels',
                        'New Energy Demand other Renewables']

listofcolumnsinput = ['Initial extraction capacity in preparation Gas', 
                        'Initial extraction capacity Gas',
                        'Initial mothballed capacity Gas',
                        'Initial Undiscovered resources Gas',
                        'Initial reserve base Gas',
                        'Initial extraction capacity in preparation Oil',
                        'Initial extraction capacity Oil',
                        'Initial mothballed capacity Oil',
                        'Initial Energy stocks Oil',
                        'Initial Undiscovered resources Oil',
                        'Initial reserve base Oil',
                        'Initial extraction capacity in preparation Coal',
                        'Initial extraction capacity Coal',
                        'Initial mothballed capacity Coal',
                        'Initial Energy stocks Coal',
                        'Initial Undiscovered resources Coal',
                        'Initial reserve base Coal',
                        'Initial extraction capacity in preparation Nuclear',
                        'Initial extraction capacity Nuclear',
                        'Initial mothballed capacity Nuclear',
                        'Initial extraction capacity in preparation Biofuels',
                        'Initial extraction capacity Biofuels',
                        'Initial mothballed capacity Biofuels',
                        'Initial Energy stocks Biofuels',
                        'Initial extraction capacity in preparation other Renewables',
                        'Initial extraction capacity other Renewables',
                        'Initial mothballed capacity other Renewables',
                        'Initial GDP',
                        'Initial Energy Intensity GDP',
                        'Initial Shortage Effect on Decoupling',
                        'Initial Effect of Supply Shortage on Decoupling',
                        'INITIAL TIME',
                        'Region',
                        'Initial cumulative extraction fuel Gas',
                        'Initial unit costs Gas',
                        'Initial cumulative extraction fuel Oil',
                        'Initial unit costs Oil',
                        'Initial cumulative extraction fuel Coal',
                        'Initial unit costs Coal',
                        'Initial cumulative extraction fuel Nuclear',
                        'Initial normalised costs relative in relation to learning effects Nuclear',
                        'Initial unit costs Nuclear',
                        'Initial cumulative extraction fuel Biofuels',
                        'Initial normalised costs relative in relation to learning effects Biofuels',
                        'Initial unit costs Biofuels',
                        'Initial EROEI Biofuels',
                        'Initial cumulative extraction fuel other Renewables',
                        'Initial normalised costs relative in relation to learning effects other Renewables',
                        'Initial unit costs other Renewables',
                        'Initial EROEI other Renewables',
                        'Initial long term normalized profits Gas',
                        'Initial long term normalized profits Oil',
                        'Initial long term normalized profits Coal',
                        'Initial long term normalized profits Nuclear',
                        'Initial long term normalized profits Biofuels',
                        'Initial long term normalized profits other Renewables',
                        'Initial EROI Gas',
                        'Initial EROI resources Oil',
                        'Initial EROI resources Coal',
                        'Initial average normalised learning curve on costs Nuclear',
                        'Initial average normalised learning curve on costs Biofuels',
                        'Initial average normalised learning curve on costs other Renewables',
                        'Delay order new capacity Gas',
                        'Delay time new capacity Gas',
                        'Time for deteriation of unused capacity Gas',
                        'Initial relation between reserve base and resource size Gas',
                        'Average Rb over P gas',
                        'Gas Import',
                        'Gas Export',
                        'Delay order new capacity Oil',
                        'Delay time new capacity Oil',
                        'Time for deteriation of unused capacity Oil',
                        'Initial relation between reserve base and resource size Oil',
                        'Average Rb over P Oil',
                        'Total export Oil',
                        'Total import Oil',
                        'Average throughput time stocks Oil',
                        'Delay order new capacity Coal',
                        'Delay time new capacity Coal',
                        'Time for deteriation of unused capacity Coal',
                        'Initial relation between reserve base and resource size Coal',
                        'Average Rb over P Coal',
                        'Total export Coal',
                        'Total import Coal',
                        'Average throughput time stocks Coal',
                        'Delay order new capacity Nuclear',
                        'Delay time new capacity Nuclear',
                        'Time for deteriation of unused capacity Nuclear',
                        'Delay order new capacity Biofuels',
                        'Delay time new capacity Biofuels',
                        'Time for deteriation of unused capacity Biofuels',
                        'Total export Biofuels',
                        'Total import Biofuels',
                        'Average throughput time stocks Biofuels',
                        'Delay order new capacity other Renewables',
                        'Delay time new capacity other Renewables',
                        'Time for deteriation of unused capacity other Renewables',
                        'Factor limiting Economic Growth due to Energy Shortage',
                        'Effect of Energy Shortage on Future Decoupling',
                        'Delay Order Decoupling due to Shortage',
                        'Delay Time Decoupling due to Shortage',
                        'Autonomous Economic Growth Patern Switch',
                        'Autonomous Economic Growth Patern 1',
                        'One Year',
                        'Costs CO2 emissions',
                        'CO2 emissions of natural gas',
                        'CO2 emissions of Oil',
                        'CO2 emissions of coal',
                        'MATH Pi',
                        'Variance power',
                        'Average EROEI energy sources lognormal',
                        'Maximum EROEI',
                        'Minimum EROEI',
                        'Delay order forecasts',
                        'Short forecasting period',
                        'Experience curve parameter extraction',
                        'Initial normalised costs relative in relation to learning effects Nuclear2',
                        'Summed delay time new capacity',
                        'Initial normalised costs relative in relation to learning effects Biofuels2',
                        'Potential EROEI Biofuels',
                        'Initial normalised costs relative in relation to learning effects other Renewables2',
                        'Potential EROEI other Renewables',
                        'Maximum relative mothballing Gas',
                        'Long term profits energy supply period Gas',
                        'Supply elasticity Gas',
                        'Investment fraction normalized profits Gas',
                        'Maximum relative mothballing Oil',
                        'Long term profits energy supply period Oil',
                        'Supply elasticity Oil',
                        'Investment fraction normalized profits Oil',
                        'Maximum relative mothballing Coal',
                        'Long term profits energy supply period Coal',
                        'Supply elasticity Coal',
                        'Investment fraction normalized profits Coal',
                        'Maximum relative mothballing Nuclear',
                        'Long term profits energy supply period Nuclear',
                        'Supply elasticity Nuclear',
                        'Investment fraction normalized profits Nuclear',
                        'Maximum relative mothballing Biofuels',
                        'Long term profits energy supply period Biofuels',
                        'Supply elasticity Biofuels',
                        'Investment fraction normalized profits Biofuels',
                        'Maximum relative mothballing other Renewables',
                        'Long term profits energy supply period other Renewables',
                        'Supply elasticity other Renewables',
                        'Investment fraction normalized profits other Renewables',
                        'Russian Gas',
                        'Storage goal',
                        'Initial completing new extraction capacity Gas',
                        'Initial completing new extraction capacity Oil',
                        'Initial completing new extraction capacity Coal',
                        'Initial completing new extraction capacity Nuclear',
                        'Initial completing new extraction capacity Biofuels',
                        'Initial completing new extraction capacity other Renewables',
                        'Initial Decoupling Effect Materializing',
                        'Initial normalised costs relative in relation to learning effects Gas',
                        'Initial normalised costs relative in relation to learning effects Gas2',
                        'Initial average normalised learning curve on costs Gas',
                        'Initial normalised costs relative in relation to learning effects Oil',
                        'Initial normalised costs relative in relation to learning effects Oil2',
                        'Initial average normalised learning curve on costs Oil',
                        'Initial normalised costs relative in relation to learning effects Coal',
                        'Initial normalised costs relative in relation to learning effects Coal2',
                        'Initial average normalised learning curve on costs Coal',
                        'Gas Import Costs',
                        'Autonomous Energy Intensity Decrease',
                        'Previous Demand Factor',
                        'Initial Demand Gas',
                        'Initial Demand Oil',
                        'Initial Demand Coal',
                        'Initial Demand Nuclear',
                        'Initial Demand Biofuels',
                        'Initial Demand other Renewables']

listofcolumnsresultsprices = ['Shadow fictional prices Oil',
                              'Energy resource prices Oil',
                              'Shadow fictional prices Coal',
                              'Energy resource prices Coal',
                              'Shadow fictional prices Biofuels',
                              'Energy resource prices Biofuels',
                              'Shadow fictional prices Nuclear E',
                              'Energy resource prices Nuclear E',
                              'Shadow fictional prices other Renewables E',
                              'Energy resource prices other Renewables E',
                              'Shadow fictional prices Gas E',
                              'Energy resource prices Gas E',
                              'Shadow fictional prices Nuclear NA',
                              'Energy resource prices Nuclear NA',
                              'Shadow fictional prices other Renewables NA',
                              'Energy resource prices other Renewables NA',
                              'Shadow fictional prices Gas NA',
                              'Energy resource prices Gas NA',
                              'Shadow fictional prices Nuclear SCA',
                              'Energy resource prices Nuclear SCA',
                              'Shadow fictional prices other Renewables SCA',
                              'Energy resource prices other Renewables SCA',
                              'Shadow fictional prices Gas SCA',
                              'Energy resource prices Gas SCA',
                              'Shadow fictional prices Nuclear CIS',
                              'Energy resource prices Nuclear CIS',
                              'Shadow fictional prices other Renewables CIS',
                              'Energy resource prices other Renewables CIS',
                              'Shadow fictional prices Gas CIS',
                              'Energy resource prices Gas CIS',
                              'Shadow fictional prices Nuclear ME',
                              'Energy resource prices Nuclear ME',
                              'Shadow fictional prices other Renewables ME',
                              'Energy resource prices other Renewables ME',
                              'Shadow fictional prices Gas ME',
                              'Energy resource prices Gas ME',
                              'Shadow fictional prices Nuclear AF',
                              'Energy resource prices Nuclear AF',
                              'Shadow fictional prices other Renewables AF',
                              'Energy resource prices other Renewables AF',
                              'Shadow fictional prices Gas AF',
                              'Energy resource prices Gas AF',
                              'Shadow fictional prices Nuclear AP',
                              'Energy resource prices Nuclear AP',
                              'Shadow fictional prices other Renewables AP',
                              'Energy resource prices other Renewables AP',
                              'Shadow fictional prices Gas AP',
                              'Energy resource prices Gas AP',
                              'TIME']
    
listofcolumnsinputprices = ['Initial shadow fictional prices Oil',
                            'Initial energy resource prices Oil',
                            'Initial shadow fictional prices Coal',
                            'Initial energy resource prices Coal',
                            'Initial shadow fictional prices Biofuels',
                            'Initial energy resource prices Biofuels',
                            'Initial shadow fictional prices Nuclear E',
                            'Initial energy resource prices Nuclear E',
                            'Initial shadow fictional prices other Renewables E',
                            'Initial energy resource prices other Renewables E',
                            'Initial shadow fictional prices Gas E',
                            'Initial energy resource prices Gas E',
                            'Initial shadow fictional prices Nuclear NA',
                            'Initial energy resource prices Nuclear NA',
                            'Initial shadow fictional prices other Renewables NA',
                            'Initial energy resource prices other Renewables NA',
                            'Initial shadow fictional prices Gas NA',
                            'Initial energy resource prices Gas NA',
                            'Initial shadow fictional prices Nuclear SCA',
                            'Initial energy resource prices Nuclear SCA',
                            'Initial shadow fictional prices other Renewables SCA',
                            'Initial energy resource prices other Renewables SCA',
                            'Initial shadow fictional prices Gas SCA',
                            'Initial energy resource prices Gas SCA',
                            'Initial shadow fictional prices Nuclear CIS',
                            'Initial energy resource prices Nuclear CIS',
                            'Initial shadow fictional prices other Renewables CIS',
                            'Initial energy resource prices other Renewables CIS',
                            'Initial shadow fictional prices Gas CIS',
                            'Initial energy resource prices Gas CIS',
                            'Initial shadow fictional prices Nuclear ME',
                            'Initial energy resource prices Nuclear ME',
                            'Initial shadow fictional prices other Renewables ME',
                            'Initial energy resource prices other Renewables ME',
                            'Initial shadow fictional prices Gas ME',
                            'Initial energy resource prices Gas ME',
                            'Initial shadow fictional prices Nuclear AF',
                            'Initial energy resource prices Nuclear AF',
                            'Initial shadow fictional prices other Renewables AF',
                            'Initial energy resource prices other Renewables AF',
                            'Initial shadow fictional prices Gas AF',
                            'Initial energy resource prices Gas AF',
                            'Initial shadow fictional prices Nuclear AP',
                            'Initial energy resource prices Nuclear AP',
                            'Initial shadow fictional prices other Renewables AP',
                            'Initial energy resource prices other Renewables AP',
                            'Initial shadow fictional prices Gas AP',
                            'Initial energy resource prices Gas AP',
                            'INITIAL TIME']

# In[3]:


def resultstodict (resultsnew, ncountries, initialrun, priceinputdict):    
    X = 4
    #Globals

    #Oil
    totaldemand_oil = 0
    totalstocked_oil = 0
    totalcosts_oil = 0
    totalextraction_oil = 0
    for i in range(ncountries):
        totaldemand_oil += resultsnew[i]['New Energy Demand Oil'].values[X]
        totalstocked_oil += resultsnew[i]['Available resources from stocks Oil'].values[X]
        totalcosts_oil += resultsnew[i]['Total costs energy supply Oil'].values[X]
        totalextraction_oil += resultsnew[i]['Extraction capacity installed Oil'].values[X]
    
    try:
        ficprice_oil = totaldemand_oil/totalstocked_oil*totalcosts_oil/totalextraction_oil
    except:
        try:
            ficprice_oil = totalcosts_oil/totalextraction_oil
        except:
            ficprice_oil = totalcosts_oil
                
    #Coal
    totaldemand_coal = 0
    totalstocked_coal = 0
    totalcosts_coal = 0
    totalextraction_coal = 0
    for i in range(ncountries):
        totaldemand_coal += resultsnew[i]['New Energy Demand Coal'].values[X]
        totalstocked_coal += resultsnew[i]['Available resources from stocks Coal'].values[X]
        totalcosts_coal += resultsnew[i]['Total costs energy supply Coal'].values[X]
        totalextraction_coal += resultsnew[i]['Extraction capacity installed Coal'].values[X]
        
    try:    
        ficprice_coal = totaldemand_coal/totalstocked_coal*totalcosts_coal/totalextraction_coal
    except:
        try:
            ficprice_coal = totalcosts_coal/totalextraction_coal
        except:
            ficprice_coal = totalcosts_coal
    
    #Biofuels
    totaldemand_biofuels = 0
    totalstocked_biofuels = 0
    totalcosts_biofuels = 0
    totalextraction_biofuels = 0
    for i in range(ncountries):
        totaldemand_biofuels += resultsnew[i]['New Energy Demand Biofuels'].values[X]
        totalstocked_biofuels += resultsnew[i]['Available resources from stocks Biofuels'].values[X]
        totalcosts_biofuels += resultsnew[i]['Total costs energy supply Biofuels'].values[X]
        totalextraction_biofuels += resultsnew[i]['Extraction capacity installed Biofuels'].values[X]
        
    try:
        ficprice_biofuels = totaldemand_biofuels/totalstocked_biofuels*totalcosts_biofuels/totalextraction_biofuels
    except:
        try: 
            ficprice_biofuels = totalcosts_biofuels/totalextraction_biofuels
        except:
            ficprice_biofuels = totalcosts_biofuels
    
    # Regional
    # E = 1, NA = 2, SCA = 3, CIS = 4, ME = 5, AF = 6, AP = 7
    
    #Nuclear
    costspercentage = 0.3
    totalcosts_nuclear_E = 0
    totalextraction_nuclear_E = 0
    totalcosts_nuclear_NA = 0
    totalextraction_nuclear_NA = 0
    totalcosts_nuclear_SCA = 0
    totalextraction_nuclear_SCA = 0
    totalcosts_nuclear_CIS = 0
    totalextraction_nuclear_CIS = 0
    totalcosts_nuclear_ME = 0
    totalextraction_nuclear_ME = 0
    totalcosts_nuclear_AF = 0
    totalextraction_nuclear_AF = 0
    totalcosts_nuclear_AP = 0
    totalextraction_nuclear_AP = 0
    for i in range(ncountries):
        if resultsnew[i]['Region'].values[X] == 1:
            totalcosts_nuclear_E += resultsnew[i]['Total costs energy supply Nuclear'].values[X]
            totalextraction_nuclear_E += resultsnew[i]['Extraction capacity installed Nuclear'].values[X]
        elif resultsnew[i]['Region'].values[X] == 2:
            totalcosts_nuclear_NA += resultsnew[i]['Total costs energy supply Nuclear'].values[X]
            totalextraction_nuclear_NA += resultsnew[i]['Extraction capacity installed Nuclear'].values[X]
        elif resultsnew[i]['Region'].values[X] == 3:
            totalcosts_nuclear_SCA += resultsnew[i]['Total costs energy supply Nuclear'].values[X]
            totalextraction_nuclear_SCA += resultsnew[i]['Extraction capacity installed Nuclear'].values[X]
        elif resultsnew[i]['Region'].values[X] == 4:
            totalcosts_nuclear_CIS += resultsnew[i]['Total costs energy supply Nuclear'].values[X]
            totalextraction_nuclear_CIS += resultsnew[i]['Extraction capacity installed Nuclear'].values[X]
        elif resultsnew[i]['Region'].values[X] == 5:
            totalcosts_nuclear_ME += resultsnew[i]['Total costs energy supply Nuclear'].values[X]
            totalextraction_nuclear_ME += resultsnew[i]['Extraction capacity installed Nuclear'].values[X]
        elif resultsnew[i]['Region'].values[X] == 6:
            totalcosts_nuclear_AF += resultsnew[i]['Total costs energy supply Nuclear'].values[X]
            totalextraction_nuclear_AF += resultsnew[i]['Extraction capacity installed Nuclear'].values[X]
        elif resultsnew[i]['Region'].values[X] == 7:
            totalcosts_nuclear_AP += resultsnew[i]['Total costs energy supply Nuclear'].values[X]
            totalextraction_nuclear_AP += resultsnew[i]['Extraction capacity installed Nuclear'].values[X]
        
    try:
        ficprice_nuclear_E = totalcosts_nuclear_E/totalextraction_nuclear_E*(1+costspercentage)
    except:
        ficprice_nuclear_E = totalcosts_nuclear_E
    try:
        ficprice_nuclear_NA = totalcosts_nuclear_NA/totalextraction_nuclear_NA*(1+costspercentage)
    except:
        ficprice_nuclear_NA = totalcosts_nuclear_NA
    try:
        ficprice_nuclear_SCA = totalcosts_nuclear_SCA/totalextraction_nuclear_SCA*(1+costspercentage)
    except:
        ficprice_nuclear_SCA = totalcosts_nuclear_SCA
    try:
        ficprice_nuclear_CIS = totalcosts_nuclear_CIS/totalextraction_nuclear_CIS*(1+costspercentage)
    except:
        ficprice_nuclear_CIS = totalcosts_nuclear_CIS
    try:
        ficprice_nuclear_ME = totalcosts_nuclear_ME/totalextraction_nuclear_ME*(1+costspercentage)
    except:
        ficprice_nuclear_ME = totalcosts_nuclear_ME
    try:
        ficprice_nuclear_AF = totalcosts_nuclear_AF/totalextraction_nuclear_AF*(1+costspercentage)
    except:
        ficprice_nuclear_AF = totalcosts_nuclear_AF
    try:
        ficprice_nuclear_AP = totalcosts_nuclear_AP/totalextraction_nuclear_AP*(1+costspercentage)
    except:
        ficprice_nuclear_AP = totalcosts_nuclear_AP
    
    #Other Renewables
    totalcosts_oR_E = 0
    totalextraction_oR_E = 0
    totalcosts_oR_NA = 0
    totalextraction_oR_NA = 0
    totalcosts_oR_SCA = 0
    totalextraction_oR_SCA = 0
    totalcosts_oR_CIS = 0
    totalextraction_oR_CIS = 0
    totalcosts_oR_ME = 0
    totalextraction_oR_ME = 0
    totalcosts_oR_AF = 0
    totalextraction_oR_AF = 0
    totalcosts_oR_AP = 0
    totalextraction_oR_AP = 0
    for i in range(ncountries):
        if resultsnew[i]['Region'].values[X] == 1:
            totalcosts_oR_E += resultsnew[i]['Total costs energy supply other Renewables'].values[X]
            totalextraction_oR_E += resultsnew[i]['Extraction capacity installed other Renewables'].values[X]
        elif resultsnew[i]['Region'].values[X] == 2:
            totalcosts_oR_NA += resultsnew[i]['Total costs energy supply other Renewables'].values[X]
            totalextraction_oR_NA += resultsnew[i]['Extraction capacity installed other Renewables'].values[X]
        elif resultsnew[i]['Region'].values[X] == 3:
            totalcosts_oR_SCA += resultsnew[i]['Total costs energy supply other Renewables'].values[X]
            totalextraction_oR_SCA += resultsnew[i]['Extraction capacity installed other Renewables'].values[X]
        elif resultsnew[i]['Region'].values[X] == 4:
            totalcosts_oR_CIS += resultsnew[i]['Total costs energy supply other Renewables'].values[X]
            totalextraction_oR_CIS += resultsnew[i]['Extraction capacity installed other Renewables'].values[X]
        elif resultsnew[i]['Region'].values[X] == 5:
            totalcosts_oR_ME += resultsnew[i]['Total costs energy supply other Renewables'].values[X]
            totalextraction_oR_ME += resultsnew[i]['Extraction capacity installed other Renewables'].values[X]
        elif resultsnew[i]['Region'].values[X] == 6:
            totalcosts_oR_AF += resultsnew[i]['Total costs energy supply other Renewables'].values[X]
            totalextraction_oR_AF += resultsnew[i]['Extraction capacity installed other Renewables'].values[X]
        elif resultsnew[i]['Region'].values[X] == 7:
            totalcosts_oR_AP += resultsnew[i]['Total costs energy supply other Renewables'].values[X]
            totalextraction_oR_AP += resultsnew[i]['Extraction capacity installed other Renewables'].values[X]
        
    try:
        ficprice_oR_E = totalcosts_oR_E/totalextraction_oR_E*(1+costspercentage)
    except:
        ficprice_oR_E = totalcosts_oR_E   
    try:
        ficprice_oR_NA = totalcosts_oR_NA/totalextraction_oR_NA*(1+costspercentage)
    except:
        ficprice_oR_NA = totalcosts_oR_NA
    try:
        ficprice_oR_SCA = totalcosts_oR_SCA/totalextraction_oR_SCA*(1+costspercentage)
    except:
        ficprice_oR_SCA = totalcosts_oR_SCA
    try:
        ficprice_oR_CIS = totalcosts_oR_CIS/totalextraction_oR_CIS*(1+costspercentage)
    except:
        ficprice_oR_CIS = totalcosts_oR_CIS
    try:
        ficprice_oR_ME = totalcosts_oR_ME/totalextraction_oR_ME*(1+costspercentage)
    except:
        ficprice_oR_ME = totalcosts_oR_ME 
    try:
        ficprice_oR_AF = totalcosts_oR_AF/totalextraction_oR_AF*(1+costspercentage)
    except:
        ficprice_oR_AF = totalcosts_oR_AF
    try:
        ficprice_oR_AP = totalcosts_oR_AP/totalextraction_oR_AP*(1+costspercentage)
    except:
        ficprice_oR_AP = totalcosts_oR_AP
    
    #Gas
    amplifier = 0.5
    totalcosts_gas_E = 0
    totalextraction_gas_E = 0
    totaldemand_gas_E = 0
    totalcosts_gas_NA = 0
    totalextraction_gas_NA = 0
    totaldemand_gas_NA = 0
    totalcosts_gas_SCA = 0
    totalextraction_gas_SCA = 0
    totaldemand_gas_SCA = 0
    totalcosts_gas_SCA = 0
    totalextraction_gas_SCA = 0
    totaldemand_gas_SCA = 0
    totalcosts_gas_CIS = 0
    totalextraction_gas_CIS = 0
    totaldemand_gas_CIS = 0
    totalcosts_gas_ME = 0
    totalextraction_gas_ME = 0
    totaldemand_gas_ME = 0
    totalcosts_gas_AF = 0
    totalextraction_gas_AF = 0
    totaldemand_gas_AF = 0
    totalcosts_gas_AP = 0
    totalextraction_gas_AP = 0
    totaldemand_gas_AP = 0
    for i in range(ncountries):
        if resultsnew[i]['Region'].values[X] == 1:
            totalcosts_gas_E += resultsnew[i]['Total costs energy supply Gas'].values[X]
            totalextraction_gas_E += resultsnew[i]['Extraction capacity installed Gas'].values[X]
            totaldemand_gas_E += resultsnew[i]['New Energy Demand Gas'].values[X]
        elif resultsnew[i]['Region'].values[X] == 2:
            totalcosts_gas_NA += resultsnew[i]['Total costs energy supply Gas'].values[X]
            totalextraction_gas_NA += resultsnew[i]['Extraction capacity installed Gas'].values[X]
            totaldemand_gas_NA += resultsnew[i]['New Energy Demand Gas'].values[X]
        elif resultsnew[i]['Region'].values[X] == 3:
            totalcosts_gas_SCA += resultsnew[i]['Total costs energy supply Gas'].values[X]
            totalextraction_gas_SCA += resultsnew[i]['Extraction capacity installed Gas'].values[X]
            totaldemand_gas_SCA += resultsnew[i]['New Energy Demand Gas'].values[X]
        elif resultsnew[i]['Region'].values[X] == 4:
            totalcosts_gas_CIS += resultsnew[i]['Total costs energy supply Gas'].values[X]
            totalextraction_gas_CIS += resultsnew[i]['Extraction capacity installed Gas'].values[X]
            totaldemand_gas_CIS += resultsnew[i]['New Energy Demand Gas'].values[X]
        elif resultsnew[i]['Region'].values[X] == 5:
            totalcosts_gas_ME += resultsnew[i]['Total costs energy supply Gas'].values[X]
            totalextraction_gas_ME += resultsnew[i]['Extraction capacity installed Gas'].values[X]
            totaldemand_gas_ME += resultsnew[i]['New Energy Demand Gas'].values[X]
        elif resultsnew[i]['Region'].values[X] == 6:
            totalcosts_gas_AF += resultsnew[i]['Total costs energy supply Gas'].values[X]
            totalextraction_gas_AF += resultsnew[i]['Extraction capacity installed Gas'].values[X]
            totaldemand_gas_AF += resultsnew[i]['New Energy Demand Gas'].values[X]
        elif resultsnew[i]['Region'].values[X] == 7:
            totalcosts_gas_AP += resultsnew[i]['Total costs energy supply Gas'].values[X]
            totalextraction_gas_AP += resultsnew[i]['Extraction capacity installed Gas'].values[X]
            totaldemand_gas_AP += resultsnew[i]['New Energy Demand Gas'].values[X]
            
    if totaldemand_gas_E > 0:
        try:
            ficprice_gas_E = totalcosts_gas_E/totalextraction_gas_E*(totaldemand_gas_E/totalextraction_gas_E)^amplifier
        except:
            try:
                ficprice_gas_E = totalcosts_gas_E/totalextraction_gas_E
            except:
                ficprice_gas_E = totalcosts_gas_E
    else:
        try:
            ficprice_gas_E = totalcosts_gas_E/totalextraction_gas_E
        except:
            ficprice_gas_E = totalcosts_gas_E
    if totaldemand_gas_NA > 0:
        try:
            ficprice_gas_NA = totalcosts_gas_NA/totalextraction_gas_NA*(totaldemand_gas_NA/totalextraction_gas_NA)^amplifier
        except:
            try: 
                ficprice_gas_NA = totalcosts_gas_NA/totalextraction_gas_NA
            except:
                ficprice_gas_NA = totalcosts_gas_NA
    else:
        try:
            ficprice_gas_NA = totalcosts_gas_NA/totalextraction_gas_NA
        except:
            ficprice_gas_NA = totalcosts_gas_NA
    if totaldemand_gas_SCA > 0:
        try:
            ficprice_gas_SCA = totalcosts_gas_SCA/totalextraction_gas_SCA*(totaldemand_gas_SCA/totalextraction_gas_SCA)^amplifier
        except:
            try:
                ficprice_gas_SCA = totalcosts_gas_SCA/totalextraction_gas_SCA
            except:
                ficprice_gas_SCA = totalcosts_gas_SCA
    else:
        try:
            ficprice_gas_SCA = totalcosts_gas_SCA/totalextraction_gas_SCA
        except:
            ficprice_gas_SCA = totalcosts_gas_SCA
    if totaldemand_gas_CIS > 0:
        try:
            ficprice_gas_CIS = totalcosts_gas_CIS/totalextraction_gas_CIS*(totaldemand_gas_CIS/totalextraction_gas_CIS)^amplifier
        except:
            try: 
                ficprice_gas_CIS = totalcosts_gas_CIS/totalextraction_gas_CIS
            except:
                ficprice_gas_CIS = totalcosts_gas_CIS
    else:
        try:
            ficprice_gas_CIS = totalcosts_gas_CIS/totalextraction_gas_CIS
        except:
            ficprice_gas_CIS = totalcosts_gas_CIS
    if totaldemand_gas_ME > 0:
        try:
            ficprice_gas_ME = totalcosts_gas_ME/totalextraction_gas_ME*(totaldemand_gas_ME/totalextraction_gas_ME)^amplifier
        except:
            try:
                ficprice_gas_ME = totalcosts_gas_ME/totalextraction_gas_ME
            except:
                ficprice_gas_ME = totalcosts_gas_ME
    else:
        try:
            ficprice_gas_ME = totalcosts_gas_ME/totalextraction_gas_ME
        except:
            ficprice_gas_ME = totalcosts_gas_ME
    if totaldemand_gas_AF > 0:
        try:
            ficprice_gas_AF = totalcosts_gas_AF/totalextraction_gas_AF*(totaldemand_gas_AF/totalextraction_gas_AF)^amplifier
        except:
            try:
                ficprice_gas_AF = totalcosts_gas_AF/totalextraction_gas_AF
            except:
                ficprice_gas_AF = totalcosts_gas_AF
    else:
        try:
            ficprice_gas_AF = totalcosts_gas_AF/totalextraction_gas_AF
        except:
            ficprice_gas_AF = totalcosts_gas_AF
    if totaldemand_gas_AP > 0:
        try:
            ficprice_gas_AP = totalcosts_gas_AP/totalextraction_gas_AP*(totaldemand_gas_AP/totalextraction_gas_AP)^amplifier
        except:
            try:
                ficprice_gas_AP = totalcosts_gas_AP/totalextraction_gas_AP
            except:
                ficprice_gas_AP = totalcosts_gas_AP
    else:
        try:
            ficprice_gas_AP = totalcosts_gas_AP/totalextraction_gas_AP
        except:
            ficprice_gas_AP = totalcosts_gas_AP
            
    if initialrun == 1:
        pricedict = {'Fictional prices Oil': ficprice_oil,
                 'Fictional prices Coal': ficprice_coal,
                 'Fictional prices Biofuels': ficprice_biofuels,
                 'Fictional prices Nuclear E': ficprice_nuclear_E,
                 'Fictional prices other Renewables E': ficprice_oR_E,
                 'Fictional prices Gas E': ficprice_gas_E,
                 'Fictional prices Nuclear NA': ficprice_nuclear_NA,
                 'Fictional prices other Renewables NA': ficprice_oR_NA,
                 'Fictional prices Gas NA': ficprice_gas_NA,
                 'Fictional prices Nuclear SCA': ficprice_nuclear_SCA,
                 'Fictional prices other Renewables SCA': ficprice_oR_SCA,
                 'Fictional prices Gas SCA': ficprice_gas_SCA,
                 'Fictional prices Nuclear CIS': ficprice_nuclear_CIS,
                 'Fictional prices other Renewables CIS': ficprice_oR_CIS,
                 'Fictional prices Gas CIS': ficprice_gas_CIS,
                 'Fictional prices Nuclear ME': ficprice_nuclear_ME,
                 'Fictional prices other Renewables ME': ficprice_oR_ME,
                 'Fictional prices Gas ME': ficprice_gas_ME,
                 'Fictional prices Nuclear AF': ficprice_nuclear_AF,
                 'Fictional prices other Renewables AF': ficprice_oR_AF,
                 'Fictional prices Gas AF': ficprice_gas_AF,
                 'Fictional prices Nuclear AP': ficprice_nuclear_AP,
                 'Fictional prices other Renewables AP': ficprice_oR_AP,
                 'Fictional prices Gas AP': ficprice_gas_AP,
                 'Initial shadow fictional prices Oil': ficprice_oil,
                 'Initial shadow fictional prices Coal': ficprice_coal,
                 'Initial shadow fictional prices Biofuels': ficprice_biofuels,
                 'Initial shadow fictional prices Nuclear E': ficprice_nuclear_E,
                 'Initial shadow fictional prices other Renewables E': ficprice_oR_E,
                 'Initial shadow fictional prices Gas E': ficprice_gas_E,
                 'Initial shadow fictional prices Nuclear NA': ficprice_nuclear_NA,
                 'Initial shadow fictional prices other Renewables NA': ficprice_oR_NA,
                 'Initial shadow fictional prices Gas NA': ficprice_gas_NA,
                 'Initial shadow fictional prices Nuclear SCA': ficprice_nuclear_SCA,
                 'Initial shadow fictional prices other Renewables SCA': ficprice_oR_SCA,
                 'Initial shadow fictional prices Gas SCA': ficprice_gas_SCA,
                 'Initial shadow fictional prices Nuclear CIS': ficprice_nuclear_CIS,
                 'Initial shadow fictional prices other Renewables CIS': ficprice_oR_CIS,
                 'Initial shadow fictional prices Gas CIS': ficprice_gas_CIS,
                 'Initial shadow fictional prices Nuclear ME': ficprice_nuclear_ME,
                 'Initial shadow fictional prices other Renewables ME': ficprice_oR_ME,
                 'Initial shadow fictional prices Gas ME': ficprice_gas_ME,
                 'Initial shadow fictional prices Nuclear AF': ficprice_nuclear_AF,
                 'Initial shadow fictional prices other Renewables AF': ficprice_oR_AF,
                 'Initial shadow fictional prices Gas AF': ficprice_gas_AF,
                 'Initial shadow fictional prices Nuclear AP': ficprice_nuclear_AP,
                 'Initial shadow fictional prices other Renewables AP': ficprice_oR_AP,
                 'Initial shadow fictional prices Gas AP': ficprice_gas_AP}
        pricedict.update(priceinputdict)
    else:
        pricedict = {'Fictional prices Oil': ficprice_oil,
                 'Fictional prices Coal': ficprice_coal,
                 'Fictional prices Biofuels': ficprice_biofuels,
                 'Fictional prices Nuclear E': ficprice_nuclear_E,
                 'Fictional prices other Renewables E': ficprice_oR_E,
                 'Fictional prices Gas E': ficprice_gas_E,
                 'Fictional prices Nuclear NA': ficprice_nuclear_NA,
                 'Fictional prices other Renewables NA': ficprice_oR_NA,
                 'Fictional prices Gas NA': ficprice_gas_NA,
                 'Fictional prices Nuclear SCA': ficprice_nuclear_SCA,
                 'Fictional prices other Renewables SCA': ficprice_oR_SCA,
                 'Fictional prices Gas SCA': ficprice_gas_SCA,
                 'Fictional prices Nuclear CIS': ficprice_nuclear_CIS,
                 'Fictional prices other Renewables CIS': ficprice_oR_CIS,
                 'Fictional prices Gas CIS': ficprice_gas_CIS,
                 'Fictional prices Nuclear ME': ficprice_nuclear_ME,
                 'Fictional prices other Renewables ME': ficprice_oR_ME,
                 'Fictional prices Gas ME': ficprice_gas_ME,
                 'Fictional prices Nuclear AF': ficprice_nuclear_AF,
                 'Fictional prices other Renewables AF': ficprice_oR_AF,
                 'Fictional prices Gas AF': ficprice_gas_AF,
                 'Fictional prices Nuclear AP': ficprice_nuclear_AP,
                 'Fictional prices other Renewables AP': ficprice_oR_AP,
                 'Fictional prices Gas AP': ficprice_gas_AP}
    
    return pricedict


# In[4]:


def runnetlogo(agent_gas, netlogo, ncountries, netlogoglobals):
    
    netlogo.write_NetLogo_attriblist(agent_gas[['who', 
                                                'GS', 
                                                'Coalsurplus', 
                                                'Oilsurplus', 
                                                'Biofuelsurplus']],
                                                 'country')
    netlogo.write_NetLogo_attriblist(netlogoglobals[['who', 
                                                     'inputpowerfactor',
                                                     'inputtransferprice',
                                                     'inputLNGprice',
                                                    'inputprice1',
                                                    'inputprice2',
                                                    'inputprice3',
                                                    'inputprice4',
                                                    'inputprice5',
                                                    'inputprice6',
                                                    'inputprice7',
                                                    'inputenergyunion',
                                                    'inputTime',
                                                    'inputCapincrease',
                                                    'inputCapincreasetime',
                                                    'inputLNGCapincrease',
                                                    'inputLNGCapincreasetime']], 'country')
    
    netlogo.command('repeat 1 [go]')
    
    gasimportlist = netlogo.report('gasimportlist')
    gasimportlist = np.split(gasimportlist, ncountries)
    gasexportlist = netlogo.report('gasexportlist')
    gasexportlist = np.split(gasexportlist, ncountries)
    
    Gasimport = []
    Gasexport = []
    for i in range(ncountries):
        Gasimport.append(gasimportlist[i][0])
        Gasexport.append(gasexportlist[i][0])
        
    coalimportlist = netlogo.report('coalimportlist')
    coalimportlist = np.split(coalimportlist, ncountries)
    coalexportlist = netlogo.report('coalexportlist')
    coalexportlist = np.split(coalexportlist, ncountries)
    
    Coalimport = []
    Coalexport = []
    for i in range(ncountries):
        Coalimport.append(coalimportlist[i][0])
        Coalexport.append(coalexportlist[i][0])
    
    oilimportlist = netlogo.report('oilimportlist')
    oilimportlist = np.split(oilimportlist, ncountries)
    oilexportlist = netlogo.report('oilexportlist')
    oilexportlist = np.split(oilexportlist, ncountries)
    
    Oilimport = []
    Oilexport = []
    for i in range(ncountries):
        Oilimport.append(oilimportlist[i][0])
        Oilexport.append(oilexportlist[i][0])
    
    biofuelimportlist = netlogo.report('biofuelimportlist')
    biofuelimportlist = np.split(biofuelimportlist, ncountries)
    biofuelexportlist = netlogo.report('biofuelexportlist')
    biofuelexportlist = np.split(biofuelexportlist, ncountries)
    
    Biofuelimport = []
    Biofuelexport = []
    for i in range(ncountries):
        Biofuelimport.append(biofuelimportlist[i][0])
        Biofuelexport.append(biofuelexportlist[i][0])
        
    russiangaslist = netlogo.report('russiangaslist')
    russiangaslist = np.split(russiangaslist, ncountries)
        
    Russiangasimport = []
    for i in range(ncountries):
        Russiangasimport.append(russiangaslist[i][0])
        
    gasimportcostslist = netlogo.report('gasimportcostslist')    
    gasimportcostslist = np.split(gasimportcostslist, ncountries)    
        
    Gasimportcosts = []
    for i in range(ncountries):
        Gasimportcosts.append(gasimportcostslist[i][0])
        
    eugasimportlist = netlogo.report('eugasimportlist')
    eugasimportlist = np.split(eugasimportlist, ncountries)
    
    EUgasimport = []
    for i in range(ncountries):
        EUgasimport.append(eugasimportlist[i][0])
        
    return Gasimport, Gasexport, Coalimport, Coalexport, Oilimport, Oilexport, Biofuelimport, Biofuelexport, Russiangasimport, Gasimportcosts, EUgasimport


# In[5]:

def hybridloop(inputpowerfactor, inputLNGprice, inputtransferprice, 
               DemandBalanceSupplyEnergyPrice, 
#                MaximumChangeinDemand,
               SupplyElasticityGas, 
               SupplyElasticityOil, SupplyElasticityCoal, Variancepower,
               SupplyElasticityNuclear, SupplyElasticityBiofuel, SupplyElasticityOR,
               inputCapincrease, inputCapincreasetime, inputLNGCapincrease,
               inputLNGCapincreasetime, EconomicGrowthScenario, EnergyIntensityScenario,
               CO2coal, CO2oil, EnergyUnion, CO2Cost,
               POil, PCoal, PBio, PNuc, POR, PGasE, PGasNA, PGasSCA, PGasCIS, PGasME,
               PGasAF, PGasAP, AutonomousEnergyIntensityDecrease):
    
    years = 40
    pricechecktime = 1
    dealtime = 5
    debug = 0
    
#     print("Policy Sum: ")
#     print(EnergyUnion+CO2Cost)    
    
#     print("Loading SD country model...")
#     sd_model = pysd.read_vensim("modelV42.mdl")
    sd_model = pysd.load("SDEnergyModel.py")
#     print("Loading SD price model...")
#     price_model = pysd.read_vensim("EnergyPriceModelV3.mdl")
    price_model = pysd.load("SDPriceModel.py")
    
    if EnergyUnion == 0:
        netlogo = pyNetLogo.NetLogoLink(gui=False)
        netlogo.load_model(r'GasMarketModel.nlogo')
        netlogo.command('setup')
        modelinput = pd.read_csv("CountryInput.csv")
        inputdict = modelinput.to_dict('index')
        ncountries = len(modelinput)
        scenarioinput = pd.read_csv("scenarioinput.csv")
        scenariodict = scenarioinput.to_dict('index')
    elif EnergyUnion == 1:
        netlogo = pyNetLogo.NetLogoLink(gui=False)
        netlogo.load_model(r'GasMarketModel-EU.nlogo')
        netlogo.command('setup')
        modelinput = pd.read_csv("CountryInput-EnU.csv")
        inputdict = modelinput.to_dict('index')
        ncountries = len(modelinput)
        scenarioinput = pd.read_csv("scenarioinput-EnUn.csv")
        scenariodict = scenarioinput.to_dict('index')
    
#     priceinput = pd.read_csv("startpricesonly3.csv")
#     priceinputdict = priceinput.to_dict('index')[0]
    priceinputdict = {'Initial energy resource prices Oil': POil,
                      'Initial energy resource prices Coal': PCoal,
                      'Initial energy resource prices Biofuels': PBio,
                      'Initial energy resource prices Nuclear E': PNuc,
                      'Initial energy resource prices other Renewables E': POR,
                      'Initial energy resource prices Gas E': PGasE,
                      'Initial energy resource prices Nuclear NA': PNuc,
                      'Initial energy resource prices other Renewables NA': POR,
                      'Initial energy resource prices Gas NA': PGasNA,
                      'Initial energy resource prices Nuclear SCA': PNuc,
                      'Initial energy resource prices other Renewables SCA': POR,
                      'Initial energy resource prices Gas SCA': PGasSCA,
                      'Initial energy resource prices Nuclear CIS': PNuc,
                      'Initial energy resource prices other Renewables CIS': POR,
                      'Initial energy resource prices Gas CIS': PGasCIS,
                      'Initial energy resource prices Nuclear ME': PNuc,
                      'Initial energy resource prices other Renewables ME': POR,
                      'Initial energy resource prices Gas ME': PGasME,
                      'Initial energy resource prices Nuclear AF': PNuc,
                      'Initial energy resource prices other Renewables AF': POR,
                      'Initial energy resource prices Gas AF': PGasAF,
                      'Initial energy resource prices Nuclear AP': PNuc,
                      'Initial energy resource prices other Renewables AP': POR,
                      'Initial energy resource prices Gas AP': PGasAP}
    
    priceinputdata = {'Initial energy resource prices Oil': [POil],
                      'Initial energy resource prices Coal': [PCoal],
                      'Initial energy resource prices Biofuels': [PBio],
                      'Initial energy resource prices Nuclear E': [PNuc],
                      'Initial energy resource prices other Renewables E': [POR],
                      'Initial energy resource prices Gas E': [PGasE],
                      'Initial energy resource prices Nuclear NA': [PNuc],
                      'Initial energy resource prices other Renewables NA': [POR],
                      'Initial energy resource prices Gas NA': [PGasNA],
                      'Initial energy resource prices Nuclear SCA': [PNuc],
                      'Initial energy resource prices other Renewables SCA': [POR],
                      'Initial energy resource prices Gas SCA': [PGasSCA],
                      'Initial energy resource prices Nuclear CIS': [PNuc],
                      'Initial energy resource prices other Renewables CIS': [POR],
                      'Initial energy resource prices Gas CIS': [PGasCIS],
                      'Initial energy resource prices Nuclear ME': [PNuc],
                      'Initial energy resource prices other Renewables ME': [POR],
                      'Initial energy resource prices Gas ME': [PGasME],
                      'Initial energy resource prices Nuclear AF': [PNuc],
                      'Initial energy resource prices other Renewables AF': [POR],
                      'Initial energy resource prices Gas AF': [PGasAF],
                      'Initial energy resource prices Nuclear AP': [PNuc],
                      'Initial energy resource prices other Renewables AP': [POR],
                      'Initial energy resource prices Gas AP': [PGasAP]}
    priceinput = pd.DataFrame(data=priceinputdata)
    
    
    netlogoglobals = pd.read_csv("netlogoglobals.csv")  
    
    initialtime = 2015
    
    pricedictlist = []
    for regionalinput in priceinputlist:
        pricedictlist.append(priceinput[regionalinput].to_dict('index')[0])
    
    for k_price, k_countryinput in zip(priceinputlist_E, priceinputcountry):
        priceinputE = pricedictlist[0]
        priceinputE[k_countryinput] = priceinputE.pop(k_price) 
    
    for k_price, k_countryinput in zip(priceinputlist_NA, priceinputcountry):
        priceinputNA = pricedictlist[1]
        priceinputNA[k_countryinput] = priceinputNA.pop(k_price)
    
    for k_price, k_countryinput in zip(priceinputlist_SCA, priceinputcountry):
        priceinputSCA = pricedictlist[2]
        priceinputSCA[k_countryinput] = priceinputSCA.pop(k_price) 
        
    for k_price, k_countryinput in zip(priceinputlist_CIS, priceinputcountry):
        priceinputCIS = pricedictlist[3]
        priceinputCIS[k_countryinput] = priceinputCIS.pop(k_price) 
        
    for k_price, k_countryinput in zip(priceinputlist_ME, priceinputcountry):
        priceinputME = pricedictlist[4]
        priceinputME[k_countryinput] = priceinputME.pop(k_price) 
    
    for k_price, k_countryinput in zip(priceinputlist_AF, priceinputcountry):
        priceinputAF = pricedictlist[5]
        priceinputAF[k_countryinput] = priceinputAF.pop(k_price) 
        
    for k_price, k_countryinput in zip(priceinputlist_AP, priceinputcountry):
        priceinputAP = pricedictlist[6]
        priceinputAP[k_countryinput] = priceinputAP.pop(k_price)
        
    for value in inputdict.values():
        value['FINAL TIME'] = 2016
        if value['Region'] == 1:
            value.update(priceinputE)
        elif value['Region'] == 2:
            value.update(priceinputNA)
        elif value['Region'] == 3:
            value.update(priceinputSCA)
        elif value['Region'] == 4:
            value.update(priceinputCIS)
        elif value['Region'] == 5:
            value.update(priceinputME)
        elif value['Region'] == 6:
            value.update(priceinputAF)
        elif value['Region'] == 7:
            value.update(priceinputAP)    
               
    for i in range(ncountries):
        inputdict[i]['Maximum Change in Demand'] = DemandBalanceSupplyEnergyPrice
        inputdict[i]['Supply elasticity Gas'] = SupplyElasticityGas
        inputdict[i]['Supply elasticity Oil'] = SupplyElasticityOil
        inputdict[i]['Supply elasticity Coal'] = SupplyElasticityCoal
        inputdict[i]['Supply elasticity Nuclear'] = SupplyElasticityNuclear
        inputdict[i]['Supply elasticity Biofuels'] = SupplyElasticityBiofuel
        inputdict[i]['Supply elasticity other Renewables'] = SupplyElasticityOR
        inputdict[i]['CO2 emissions of Oil'] = CO2oil
        inputdict[i]['CO2 emissions of coal'] = CO2coal
        inputdict[i]['Variance power'] = Variancepower 
        inputdict[i]['Previous Demand Factor'] = 0
        inputdict[i]['Autonomous Energy Intensity Decrease'] = AutonomousEnergyIntensityDecrease
        if EconomicGrowthScenario == 1:
            inputdict[i]['Autonomous Economic Growth Factor'] = scenariodict[i]['AEGFL']
        elif EconomicGrowthScenario == 2:
            inputdict[i]['Autonomous Economic Growth Factor'] = scenariodict[i]['AEGFM']
        elif EconomicGrowthScenario == 3:
            inputdict[i]['Autonomous Economic Growth Factor'] = scenariodict[i]['AEGFH']
        if EnergyIntensityScenario == 1:
            inputdict[i]['Initial Energy Intensity GDP'] = scenariodict[i]['IEIGDPL']
        elif EnergyIntensityScenario == 2:
            inputdict[i]['Initial Energy Intensity GDP'] = scenariodict[i]['IEIGDPM']
        elif EnergyIntensityScenario == 3:
            inputdict[i]['Initial Energy Intensity GDP'] = scenariodict[i]['IEIGDPH']
#         if EnergyUnion == 0 and i <28 and CO2Cost == 1: #change
#             inputdict[i]['Costs CO2 emissions'] = 100
#         elif EnergyUnion == 1 and i == 0 and CO2Cost == 1:
#             inputdict[i]['Costs CO2 emissions'] = 100

    dummyresults = []
    for value in inputdict.values():
        dummyresults.append(sd_model.run(params=value))
        
    initialrun = 1
    pricemodelinputdict = resultstodict(dummyresults, ncountries, initialrun, priceinputdict)
    initialrun = 0

    GS = []
    CS = []
    OS = []
    BO = []
            
    for country in dummyresults:
        GS.append(country['Gas to trade'].values[4])
        CS.append(country['Coal to trade'].values[4])
        OS.append(country['Oil to trade'].values[4])
        BO.append(country['Biofuels to trade'].values[4])    
    
    gasdata = {'who': list(range (ncountries)),
               'GS': GS,
               'Coalsurplus': CS,
               'Oilsurplus': OS,
               'Biofuelsurplus': BO}
    
    agent_gas = pd.DataFrame (gasdata, columns=['who', 'GS', 'Coalsurplus', 'Oilsurplus', 'Biofuelsurplus'])
    
    netlogoglobals['inputpowerfactor'] = inputpowerfactor
    netlogoglobals['inputLNGprice'] = inputLNGprice
    netlogoglobals['inputtransferprice'] = inputtransferprice
    netlogoglobals['inputTime'] = initialtime
    netlogoglobals['inputprice1'] = priceinput['Initial energy resource prices Gas E'].values[0]
    netlogoglobals['inputprice2'] = priceinput['Initial energy resource prices Gas NA'].values[0]
    netlogoglobals['inputprice3'] = priceinput['Initial energy resource prices Gas SCA'].values[0]
    netlogoglobals['inputprice4'] = priceinput['Initial energy resource prices Gas CIS'].values[0]
    netlogoglobals['inputprice5'] = priceinput['Initial energy resource prices Gas ME'].values[0]
    netlogoglobals['inputprice6'] = priceinput['Initial energy resource prices Gas AF'].values[0]
    netlogoglobals['inputprice7'] = priceinput['Initial energy resource prices Gas AP'].values[0]
    netlogoglobals['inputenergyunion'] = EnergyUnion
    netlogoglobals['inputCapincrease'] = inputCapincrease
    if inputCapincreasetime == 1:
        netlogoglobals['inputCapincreasetime'] = 3
    elif inputCapincreasetime == 2:
        netlogoglobals['inputCapincreasetime'] = 7
    netlogoglobals['inputLNGCapincrease'] = inputLNGCapincrease
    if inputLNGCapincreasetime == 1:
        netlogoglobals['inputLNGCapincreasetime'] = 3
    elif inputLNGCapincreasetime == 2:
        netlogoglobals['inputLNGCapincreasetime'] = 7

    Gasimport, Gasexport, Coalimport, Coalexport, Oilimport, Oilexport, Biofuelimport, Biofuelexport, Russiangasimport, Gasimportcosts, EUgasimport = runnetlogo(agent_gas, netlogo, ncountries,netlogoglobals)
    
        
#     print("Running models...")
    pricemodelinputdict.update({'INITIAL TIME': initialtime}) 
    pricemodelinputdict.update({'FINAL TIME': initialtime+pricechecktime}) 
    priceresults = price_model.run(params=pricemodelinputdict)
        
    countryresults = []
    countryresultstosave = []
    for value, gi, ge, ci, ce, oi, oe, bi, be, rg, gic, eugi in zip(inputdict.values(), Gasimport, Gasexport, Coalimport, Coalexport, Oilimport, Oilexport, Biofuelimport, Biofuelexport, Russiangasimport, Gasimportcosts, EUgasimport):
        value['INITIAL TIME'] = initialtime
        value['FINAL TIME'] = initialtime+pricechecktime
        value['Gas Import'] = gi
        value['Gas Export'] = ge
        value['Total import Coal'] = ci
        value['Total export Coal'] = ce
        value['Total import Oil'] = oi
        value['Total export Oil'] = oe
        value['Total import Biofuels'] = bi
        value['Total export Biofuels'] = be
        value['Russian Gas'] = rg
        value['Gas Import Costs'] = gic
        value['EUgasimport'] = eugi
        singleregionresults = sd_model.run(params=value)
        countryresults.append(singleregionresults)
        singleregionresultstosave = []  
        singleregionresultstosave.append(singleregionresults[resultstosave])
        countryresultstosave.append(singleregionresultstosave)
        
    combresults = [countryresultstosave]
    combprices = [priceresults]
    
    for n in range(pricechecktime, years, pricechecktime):
#         print("Year: ", n)
        finalvalues = []
        for singleresult in countryresults:
            finalvalues.append(singleresult.ix[[4], listofcolumnsresults])
    
        dictlist = []
        for valueset in finalvalues:
            newdict = valueset.to_dict('records')[0]
            for k_results, k_input in zip(listofcolumnsresults, listofcolumnsinput):
                newdict[k_input] = newdict.pop(k_results)
            dictlist.append(newdict)
            
        dictdict = {}
        for i in range(ncountries):
            dictdict.update({i:{}})
        dictdict = {key:dictlist[i] for (key, value), i in zip(dictdict.items(), range(ncountries))}
            
        updatedprices = priceresults.iloc[4]
        pricedictlist = []
        for regionalinput in energypriceslist:
            pricedictlist.append(updatedprices[regionalinput].to_dict())
    
        for k_price, k_countryinput in zip(energyprices_E, priceinputcountry):
            priceinputE = pricedictlist[0]
            priceinputE[k_countryinput] = priceinputE.pop(k_price) 
    
        for k_price, k_countryinput in zip(energyprices_NA, priceinputcountry):
            priceinputNA = pricedictlist[1]
            priceinputNA[k_countryinput] = priceinputNA.pop(k_price)
    
        for k_price, k_countryinput in zip(energyprices_SCA, priceinputcountry):
            priceinputSCA = pricedictlist[2]
            priceinputSCA[k_countryinput] = priceinputSCA.pop(k_price) 
    
        for k_price, k_countryinput in zip(energyprices_CIS, priceinputcountry):
            priceinputCIS = pricedictlist[3]
            priceinputCIS[k_countryinput] = priceinputCIS.pop(k_price) 
            
        for k_price, k_countryinput in zip(energyprices_ME, priceinputcountry):
            priceinputME = pricedictlist[4]
            priceinputME[k_countryinput] = priceinputME.pop(k_price)
            
        for k_price, k_countryinput in zip(energyprices_AF, priceinputcountry):
            priceinputAF = pricedictlist[5]
            priceinputAF[k_countryinput] = priceinputAF.pop(k_price)       
        
        for k_price, k_countryinput in zip(energyprices_AP, priceinputcountry):
            priceinputAP = pricedictlist[6]
            priceinputAP[k_countryinput] = priceinputAP.pop(k_price) 
    
        for value,i in zip(dictdict.values(), range(ncountries)):
            if value['Region'] == 1:
                value.update(priceinputE)
            elif value['Region'] == 2:
                value.update(priceinputNA)
            elif value['Region'] == 3:
                value.update(priceinputSCA)
            elif value['Region'] == 4:
                value.update(priceinputCIS)
            elif value['Region'] == 5:
                value.update(priceinputME)
            elif value['Region'] == 6:
                value.update(priceinputAF)
            elif value['Region'] == 7:
                value.update(priceinputAP) 
            if CO2Cost == 1:
                if EnergyUnion == 0 and i <28: #change
                    value['Costs CO2 emissions'] = 10 + n
                elif EnergyUnion == 1 and i == 0:
                    value['Costs CO2 emissions'] = 10 + n
            elif CO2Cost == 2:
                if EnergyUnion == 0 and i <28: #change
                    value['Costs CO2 emissions'] = 10 + 2*n
                elif EnergyUnion == 1 and i == 0:
                    value['Costs CO2 emissions'] = 10 + 2*n
    
        pricemodelinputdict = resultstodict(countryresults, ncountries, initialrun, priceinputdict)
    
        finalpricevalues = priceresults.ix[[4], listofcolumnsresultsprices]
    
        stockdictprices = finalpricevalues.to_dict('index')[4]
        for k_results, k_input in zip(listofcolumnsresultsprices, listofcolumnsinputprices):
            stockdictprices[k_input] = stockdictprices.pop(k_results)
        pricemodelinputdict.update(stockdictprices)
        pricemodelinputdict.update({'FINAL TIME': initialtime+pricechecktime+n})
        
        priceresults = price_model.run(params=pricemodelinputdict)
        
        countryresults = []
        countryresultstosave = []

        for value, gi, ge, ci, ce, oi, oe, bi, be, rg, gic, eugi in zip(dictdict.values(), Gasimport, Gasexport, Coalimport, Coalexport, Oilimport, Oilexport, Biofuelimport, Biofuelexport, Russiangasimport, Gasimportcosts, EUgasimport):
            value['FINAL TIME'] = value['INITIAL TIME'] + pricechecktime
            value['Gas Import'] = gi
            value['Gas Export'] = ge
            value['Total import Coal'] = ci
            value['Total export Coal'] = ce
            value['Total import Oil'] = oi
            value['Total export Oil'] = oe
            value['Total import Biofuels'] = bi
            value['Total export Biofuels'] = be
            value['Russian Gas'] = rg
            value['Gas Import Costs'] = gic
            value['EUgasimport'] = eugi
            singleregionresults = sd_model.run(params=value)
            countryresults.append(singleregionresults)
            singleregionresultstosave = []
            singleregionresultstosave.append(singleregionresults[resultstosave])
            countryresultstosave.append(singleregionresultstosave)
        
        combresults.append(countryresultstosave)
        combprices.append(priceresults)
        
        if n%dealtime == 0:
            GS = []
            CS = []
            OS = []
            BO = []
            
            for country in countryresults:
                GS.append(country['Gas to trade'].values[4])
                CS.append(country['Coal to trade'].values[4])
                OS.append(country['Oil to trade'].values[4])
                BO.append(country['Biofuels to trade'].values[4])   
                
            gasdata = {'who': list(range (ncountries)),
                       'GS': GS,
                       'Coalsurplus': CS,
                       'Oilsurplus': OS,
                       'Biofuelsurplus': BO}
            
            agent_gas = pd.DataFrame (gasdata, columns=['who', 'GS', 'Coalsurplus', 'Oilsurplus', 'Biofuelsurplus'])
            
            netlogoglobals['inputTime'] = countryresults[0]['FINAL TIME'].values[4]
            netlogoglobals['inputprice1'] = finalpricevalues['Energy resource prices Gas E'].values
            netlogoglobals['inputprice2'] = finalpricevalues['Energy resource prices Gas NA'].values
            netlogoglobals['inputprice3'] = finalpricevalues['Energy resource prices Gas SCA'].values
            netlogoglobals['inputprice4'] = finalpricevalues['Energy resource prices Gas CIS'].values
            netlogoglobals['inputprice5'] = finalpricevalues['Energy resource prices Gas ME'].values
            netlogoglobals['inputprice6'] = finalpricevalues['Energy resource prices Gas AF'].values
            netlogoglobals['inputprice7'] = finalpricevalues['Energy resource prices Gas AP'].values
            
            Gasimport, Gasexport, Coalimport, Coalexport, Oilimport, Oilexport, Biofuelimport, Biofuelexport, Russiangasimport, Gasimportcosts, EUgasimport = runnetlogo(agent_gas, netlogo, ncountries,netlogoglobals)
                    
    prices = pd.concat(combprices)
    results = [pd.concat([entry[n][0] for entry in combresults]) for n in range(ncountries)]        

    Oil_Price = prices['Energy resource prices Oil']
    Coal_Price = prices['Energy resource prices Coal']
    Bio_Price = prices['Energy resource prices Biofuels']
    Gas_PriceE = prices['Energy resource prices Nuclear E']
    Nuc_PriceE = prices['Energy resource prices other Renewables E']
    OR_PriceE = prices['Energy resource prices Gas E']
    Gas_PriceCIS = prices['Energy resource prices Nuclear CIS']
    
    if EnergyUnion == 0:  
        EU_GasSup = results[27]['Available Gas']
#         EU_GasDem = results[27]['New Energy Demand Gas']
#         EU_GasCon = results[27]['Resource consumption Gas']
        EU_OilSup = results[27]['Available resources from stocks Oil']
#         EU_OilDem = results[27]['New Energy Demand Oil']
#         EU_OilCon = results[27]['Resource consumption Oil']
        EU_CoalSup = results[27]['Available resources from stocks Coal']
#         EU_CoalDem = results[27]['New Energy Demand Coal']
#         EU_CoalCon = results[27]['Resource consumption Coal']
        EU_NucSup = results[27]['Extraction capacity installed Nuclear']
#         EU_NucDem = results[27]['New Energy Demand Nuclear']
#         EU_NucCon = results[27]['Extraction capacity installed Nuclear']
        EU_BioSup = results[27]['Available resources from stocks Biofuels']
#         EU_BioDem = results[27]['New Energy Demand Biofuels']
#         EU_BioCon = results[27]['Resource consumption Biofuels']
        EU_ORSup = results[27]['Extraction capacity installed other Renewables']
#         EU_ORDem = results[27]['New Energy Demand other Renewables']
#         EU_ORCon = results[27]['Extraction capacity installed other Renewables']
        
        EU_EDem = results[27]['Energy Demand']
        EU_ESup = results[27]['Total Energy Supply']
        EU_GDP = results[27]['GDP']
        
        EU_CO2 = results[27]['CO2 emissions']
        EU_RusGas = results[27]['Russian Gas']
        EU_EUGI = results[27]['EUgasimport']
        EU_GIC = results[27]['Gas Import Costs']
        
        for i in range(27):
            EU_GasSup += results[i]['Available Gas']
#             EU_GasDem += results[i]['New Energy Demand Gas']
#             EU_GasCon += results[i]['Resource consumption Gas']
            EU_OilSup += results[i]['Available resources from stocks Oil']
#             EU_OilDem += results[i]['New Energy Demand Oil']
#             EU_OilCon += results[i]['Resource consumption Oil']
            EU_CoalSup += results[i]['Available resources from stocks Coal']
#             EU_CoalDem += results[i]['New Energy Demand Coal']
#             EU_CoalCon += results[i]['Resource consumption Coal']
            EU_NucSup += results[i]['Extraction capacity installed Nuclear']
#             EU_NucDem += results[i]['New Energy Demand Nuclear']
    #         EU_NucCon += results[i]['Extraction capacity installed Nuclear']
            EU_BioSup += results[i]['Available resources from stocks Biofuels']
#             EU_BioDem += results[i]['New Energy Demand Biofuels']
#             EU_BioCon += results[i]['Resource consumption Biofuels']
            EU_ORSup += results[i]['Extraction capacity installed other Renewables']
#             EU_ORDem += results[i]['New Energy Demand other Renewables']
    #         EU_ORCon += results[i]['Extraction capacity installed other Renewables']
        
            EU_EDem += results[i]['Energy Demand']
            EU_ESup += results[i]['Total Energy Supply']
            EU_GDP += results[i]['GDP']
        
            EU_CO2 += results[i]['CO2 emissions']
            EU_RusGas += results[i]['Russian Gas']
            EU_EUGI += results[i]['EUgasimport']
            EU_GIC += results[i]['Gas Import Costs']
        
    elif EnergyUnion == 1:
        EU_GasSup = results[0]['Available Gas']
#         EU_GasDem = results[0]['New Energy Demand Gas']
#         EU_GasCon = results[0]['Resource consumption Gas']
        EU_OilSup = results[0]['Available resources from stocks Oil']
#         EU_OilDem = results[0]['New Energy Demand Oil']
#         EU_OilCon = results[0]['Resource consumption Oil']
        EU_CoalSup = results[0]['Available resources from stocks Coal']
#         EU_CoalDem = results[0]['New Energy Demand Coal']
#         EU_CoalCon = results[0]['Resource consumption Coal']
        EU_NucSup = results[0]['Extraction capacity installed Nuclear']
#         EU_NucDem = results[0]['New Energy Demand Nuclear']
#         EU_NucCon = results[0]['Extraction capacity installed Nuclear']
        EU_BioSup = results[0]['Available resources from stocks Biofuels']
#         EU_BioDem = results[0]['New Energy Demand Biofuels']
#         EU_BioCon = results[0]['Resource consumption Biofuels']
        EU_ORSup = results[0]['Extraction capacity installed other Renewables']
#         EU_ORDem = results[0]['New Energy Demand other Renewables']
#         EU_ORCon = results[0]['Extraction capacity installed other Renewables']
        
        EU_EDem = results[0]['Energy Demand']
        EU_ESup = results[0]['Total Energy Supply']
        EU_GDP = results[0]['GDP']
        
        EU_CO2 = results[0]['CO2 emissions']
        EU_RusGas = results[0]['Russian Gas']
        EU_EUGI = results[0]['EUgasimport']
        EU_GIC = results[0]['Gas Import Costs']
        
#     EU_RGperAG = EU_RusGas/EU_GasSup
#     EU_RGperTES = EU_RusGas/EU_ESup
#     EU_RGperGC = EU_RusGas/EU_GasCon
    
#     EU_GICperBBTU = EU_GIC/EU_EUGI   
    
#     FuncpriceGas = results[0]['Functional Energy Price Gas']
#     FuncpriceOil = results[0]['Functional Energy Price Oil']
#     FuncpriceCoal = results[0]['Functional Energy Price Coal']
    
    return {
#         'FuncpriceGas': FuncpriceGas,
#         'FuncpriceOil': FuncpriceOil,
#         'FuncpriceCoal': FuncpriceCoal,
        'EU_GasSup': EU_GasSup,
#         'EU_GasDem': EU_GasDem, 
#         'EU_GasCon': EU_GasCon, 
        'EU_OilSup': EU_OilSup, 
#         'EU_OilDem': EU_OilDem, 
#         'EU_OilCon': EU_OilCon, 
        'EU_CoalSup': EU_CoalSup, 
#         'EU_CoalDem': EU_CoalDem, 
#         'EU_CoalCon': EU_CoalCon,
        'EU_NucSup': EU_NucSup, 
#         'EU_NucDem': EU_NucDem, 
#         'EU_NucCon': EU_NucCon,  
        'EU_BioSup': EU_BioSup, 
#         'EU_BioDem': EU_BioDem, 
#         'EU_BioCon': EU_BioCon,  
        'EU_ORSup': EU_ORSup, 
#         'EU_ORDem': EU_ORDem, 
#         'EU_ORCon': EU_ORCon,  
       
        'EU_EDem': EU_EDem,
        'EU_ESup': EU_ESup,
        'EU_GDP': EU_GDP,
        
        'EU_CO2': EU_CO2,
        'EU_RusGas': EU_RusGas,
        'EU_EUGI': EU_EUGI,
        'EU_GIC':  EU_GIC,
        
#         'EU_RGperAG': EU_RGperAG,
#         'EU_RGperTES': EU_RGperTES,
#         'EU_RGperGC': EU_RGperGC,
#         'EU_GICperBBTU': EU_GICperBBTU,
        
        'Oil_Price': Oil_Price,
        'Coal_Price': Coal_Price,
        'Bio_Price': Bio_Price,
        'Gas_PriceE': Gas_PriceE,
        'Nuc_PriceE': Nuc_PriceE,
        'OR_PriceE': OR_PriceE,
        'Gas_PriceCIS': Gas_PriceCIS}
