"""
Python model "modelV42.py"
Translated using PySD version 0.9.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME':
    'time',
    'Time':
    'time',
    'Previous Energy Demand Nuclear':
    'previous_energy_demand_nuclear',
    'Previous Energy Demand Oil':
    'previous_energy_demand_oil',
    'Previous Energy Demand other Renewables':
    'previous_energy_demand_other_renewables',
    'Normalized Previous Demand Biofuels':
    'normalized_previous_demand_biofuels',
    'Normalized Previous Demand Coal':
    'normalized_previous_demand_coal',
    'Normalized Previous Demand Gas':
    'normalized_previous_demand_gas',
    'Normalized Previous Demand Nuclear':
    'normalized_previous_demand_nuclear',
    'Normalized Previous Demand Oil':
    'normalized_previous_demand_oil',
    'Normalized Previous Demand other Renewables':
    'normalized_previous_demand_other_renewables',
    'Initial Demand Nuclear':
    'initial_demand_nuclear',
    'Initial Demand Oil':
    'initial_demand_oil',
    'Initial Demand other Renewables':
    'initial_demand_other_renewables',
    'Previous Demand Factor':
    'previous_demand_factor',
    'Previous Energy Demand Biofuels':
    'previous_energy_demand_biofuels',
    'Previous Energy Demand Coal':
    'previous_energy_demand_coal',
    'EUgasimport':
    'eugasimport',
    'Initial Demand Gas':
    'initial_demand_gas',
    'Previous Energy Demand Gas':
    'previous_energy_demand_gas',
    'Initial Demand Biofuels':
    'initial_demand_biofuels',
    'Initial Demand Coal':
    'initial_demand_coal',
    'Total Previous Energy Demand':
    'total_previous_energy_demand',
    'Gas Import Costs':
    'gas_import_costs',
    'decrease factor':
    'decrease_factor',
    'Autonomous Energy Intensity Decrease':
    'autonomous_energy_intensity_decrease',
    'Increase in discovered and technically recoverable resources Oil':
    'increase_in_discovered_and_technically_recoverable_resources_oil',
    'Normalised costs relative in relation to learning t1 Coal':
    'normalised_costs_relative_in_relation_to_learning_t1_coal',
    'Normalised costs relative in relation to learning t1 Gas':
    'normalised_costs_relative_in_relation_to_learning_t1_gas',
    'Initial average normalised learning curve on costs Gas':
    'initial_average_normalised_learning_curve_on_costs_gas',
    'Normalised costs relative in relation to learning t1 Oil':
    'normalised_costs_relative_in_relation_to_learning_t1_oil',
    'Cumulative extracted fuel t1 Gas':
    'cumulative_extracted_fuel_t1_gas',
    'Cost development learning curve Coal':
    'cost_development_learning_curve_coal',
    'Cost development learning curve Gas':
    'cost_development_learning_curve_gas',
    'Normalised costs relative in relation to learning effects Oil':
    'normalised_costs_relative_in_relation_to_learning_effects_oil',
    'Cost development learning curve Oil':
    'cost_development_learning_curve_oil',
    'Initial normalised costs relative in relation to learning effects Coal':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_coal',
    'Average normalised learning curve on costs Coal':
    'average_normalised_learning_curve_on_costs_coal',
    'Average normalised learning curve on costs Gas':
    'average_normalised_learning_curve_on_costs_gas',
    'Initial normalised costs relative in relation to learning effects Gas2':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_gas2',
    'Average normalised learning curve on costs Oil':
    'average_normalised_learning_curve_on_costs_oil',
    'Increase in discovered and technically recoverable resources Coal':
    'increase_in_discovered_and_technically_recoverable_resources_coal',
    'Initial normalised costs relative in relation to learning effects Oil':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_oil',
    'Initial normalised costs relative in relation to learning effects Oil2':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_oil2',
    'Initial average normalised learning curve on costs Coal':
    'initial_average_normalised_learning_curve_on_costs_coal',
    'Cumulative extracted fuel t1 Coal':
    'cumulative_extracted_fuel_t1_coal',
    'Normalised costs relative in relation to learning effects t1 Gas':
    'normalised_costs_relative_in_relation_to_learning_effects_t1_gas',
    'Normalised costs relative in relation to learning effects Gas':
    'normalised_costs_relative_in_relation_to_learning_effects_gas',
    'Cumulative extracted fuel t1 Oil':
    'cumulative_extracted_fuel_t1_oil',
    'Initial average normalised learning curve on costs Oil':
    'initial_average_normalised_learning_curve_on_costs_oil',
    'Initial normalised costs relative in relation to learning effects Gas':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_gas',
    'Change in average learning curve parameter Coal':
    'change_in_average_learning_curve_parameter_coal',
    'Change in average learning curve parameter Gas':
    'change_in_average_learning_curve_parameter_gas',
    'Relative change in costs due to learning Coal':
    'relative_change_in_costs_due_to_learning_coal',
    'Change in average learning curve parameter Oil':
    'change_in_average_learning_curve_parameter_oil',
    'Normalised costs relative in relation to learning effects t1 Oil':
    'normalised_costs_relative_in_relation_to_learning_effects_t1_oil',
    'Relative change in costs due to learning Oil':
    'relative_change_in_costs_due_to_learning_oil',
    'Initial normalised costs relative in relation to learning effects Coal2':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_coal2',
    'Relative change in costs due to learning Gas':
    'relative_change_in_costs_due_to_learning_gas',
    'Normalised costs relative in relation to learning effects Coal':
    'normalised_costs_relative_in_relation_to_learning_effects_coal',
    'Increase in discovered and technically recoverable gas':
    'increase_in_discovered_and_technically_recoverable_gas',
    'Normalised costs relative in relation to learning effects t1 Coal':
    'normalised_costs_relative_in_relation_to_learning_effects_t1_coal',
    'Coal to trade from storage':
    'coal_to_trade_from_storage',
    'Biofuels to trade from stocks':
    'biofuels_to_trade_from_stocks',
    'Oil to trade from storage':
    'oil_to_trade_from_storage',
    'Decoupling Effect Materializing':
    'decoupling_effect_materializing',
    'Initial Decoupling Effect Materializing':
    'initial_decoupling_effect_materializing',
    'Total income energy supply Biofuels':
    'total_income_energy_supply_biofuels',
    'Total income energy supply Coal':
    'total_income_energy_supply_coal',
    'Available Gas':
    'available_gas',
    'Total income energy supply Oil':
    'total_income_energy_supply_oil',
    'Completing new extraction capacity Nuclear':
    'completing_new_extraction_capacity_nuclear',
    'Completing new extraction capacity Oil':
    'completing_new_extraction_capacity_oil',
    'Completing new extraction capacity other Renewables':
    'completing_new_extraction_capacity_other_renewables',
    'Initial completing new extraction capacity Biofuels':
    'initial_completing_new_extraction_capacity_biofuels',
    'Biofuels to trade':
    'biofuels_to_trade',
    'Initial completing new extraction capacity Nuclear':
    'initial_completing_new_extraction_capacity_nuclear',
    'Initial completing new extraction capacity Oil':
    'initial_completing_new_extraction_capacity_oil',
    'Oil to trade':
    'oil_to_trade',
    'Coal to trade':
    'coal_to_trade',
    'Total income energy supply Gas':
    'total_income_energy_supply_gas',
    'Completing new extraction capacity Biofuels':
    'completing_new_extraction_capacity_biofuels',
    'Completing new extraction capacity Gas':
    'completing_new_extraction_capacity_gas',
    'Initial completing new extraction capacity other Renewables':
    'initial_completing_new_extraction_capacity_other_renewables',
    'Initial completing new extraction capacity Gas':
    'initial_completing_new_extraction_capacity_gas',
    'Initial completing new extraction capacity Coal':
    'initial_completing_new_extraction_capacity_coal',
    'Completing new extraction capacity Coal':
    'completing_new_extraction_capacity_coal',
    'Storage goal':
    'storage_goal',
    'Average throughput time stocks Oil':
    'average_throughput_time_stocks_oil',
    'Current Energy Supply Distribution Oil':
    'current_energy_supply_distribution_oil',
    'Russian Gas':
    'russian_gas',
    'Total Energy Supply':
    'total_energy_supply',
    'Current Energy Supply Distribution Biofuels':
    'current_energy_supply_distribution_biofuels',
    'Current Energy Supply Distribution Coal':
    'current_energy_supply_distribution_coal',
    'Current Energy Supply Distribution Gas':
    'current_energy_supply_distribution_gas',
    'Energy export Biofuels':
    'energy_export_biofuels',
    'Energy export Coal':
    'energy_export_coal',
    'Energy export Oil':
    'energy_export_oil',
    'Initial EROI resources Coal':
    'initial_eroi_resources_coal',
    'EROI resources Coal':
    'eroi_resources_coal',
    'EROI resources Gas':
    'eroi_resources_gas',
    'EROI resources Oil':
    'eroi_resources_oil',
    'Initial average normalised learning curve on costs Biofuels':
    'initial_average_normalised_learning_curve_on_costs_biofuels',
    'Initial average normalised learning curve on costs Nuclear':
    'initial_average_normalised_learning_curve_on_costs_nuclear',
    'Initial EROI Gas':
    'initial_eroi_gas',
    'Average normalised learning curve on costs Biofuels':
    'average_normalised_learning_curve_on_costs_biofuels',
    'Initial EROI resources Oil':
    'initial_eroi_resources_oil',
    'Average normalised learning curve on costs other Renewables':
    'average_normalised_learning_curve_on_costs_other_renewables',
    'Initial average normalised learning curve on costs other Renewables':
    'initial_average_normalised_learning_curve_on_costs_other_renewables',
    'Average normalised learning curve on costs Nuclear':
    'average_normalised_learning_curve_on_costs_nuclear',
    'Region':
    'region',
    'Autonomous Economic Growth':
    'autonomous_economic_growth',
    'Autonomous Economic Growth Factor':
    'autonomous_economic_growth_factor',
    'Autonomous Economic Growth Patern 1':
    'autonomous_economic_growth_patern_1',
    'Autonomous Economic Growth Patern 2':
    'autonomous_economic_growth_patern_2',
    'Autonomous Economic Growth Patern Switch':
    'autonomous_economic_growth_patern_switch',
    'Increase in GDP':
    'increase_in_gdp',
    'Initial normalised costs relative in relation to learning effects Biofuels2':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_biofuels2',
    'Cost development learning curve Nuclear':
    'cost_development_learning_curve_nuclear',
    'Initial normalised costs relative in relation to learning effects other Renewables2':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_other_renewables2',
    'Initial normalised costs relative in relation to learning effects Nuclear2':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_nuclear2',
    'Variance power':
    'variance_power',
    'Initial normalised costs relative in relation to learning effects Biofuels':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_biofuels',
    'Initial normalised costs relative in relation to learning effects other Renewables':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_other_renewables',
    'Initial normalised costs relative in relation to learning effects Nuclear':
    'initial_normalised_costs_relative_in_relation_to_learning_effects_nuclear',
    'Normalized relation between costs and income other Renewables':
    'normalized_relation_between_costs_and_income_other_renewables',
    'Average EROEI energy sources lognormal':
    'average_eroei_energy_sources_lognormal',
    'Cumulative extracted fuel t1 Biofuels':
    'cumulative_extracted_fuel_t1_biofuels',
    'Potential EROEI Biofuels':
    'potential_eroei_biofuels',
    'Potential EROEI other Renewables':
    'potential_eroei_other_renewables',
    'Cumulative extracted fuel Nuclear':
    'cumulative_extracted_fuel_nuclear',
    'Supply elasticity Nuclear':
    'supply_elasticity_nuclear',
    'Initial unit costs Biofuels':
    'initial_unit_costs_biofuels',
    'Initial unit costs Coal':
    'initial_unit_costs_coal',
    'Change in average learning curve parameter Biofuels':
    'change_in_average_learning_curve_parameter_biofuels',
    'Change in average learning curve parameter other Renewables':
    'change_in_average_learning_curve_parameter_other_renewables',
    'Change in average learning curve parameter Nuclear':
    'change_in_average_learning_curve_parameter_nuclear',
    'Change in cumulative extracted fuel Biofuels':
    'change_in_cumulative_extracted_fuel_biofuels',
    'Change in cumulative extracted fuel other Renewables':
    'change_in_cumulative_extracted_fuel_other_renewables',
    'Change in EROEI Biofuels':
    'change_in_eroei_biofuels',
    'Change in EROEI other Renewables':
    'change_in_eroei_other_renewables',
    'Change in EROI due to reserve depletion Coal':
    'change_in_eroi_due_to_reserve_depletion_coal',
    'Change in EROI due to reserve depletion Gas':
    'change_in_eroi_due_to_reserve_depletion_gas',
    'Change in EROI due to reserve depletion Oil':
    'change_in_eroi_due_to_reserve_depletion_oil',
    'Change in normalized relative profits Biofuels':
    'change_in_normalized_relative_profits_biofuels',
    'Change in normalized relative profits Coal':
    'change_in_normalized_relative_profits_coal',
    'Change in normalized relative profits Gas':
    'change_in_normalized_relative_profits_gas',
    'Change in normalized relative profits Oil':
    'change_in_normalized_relative_profits_oil',
    'Change in normalized relative profits other Renewables':
    'change_in_normalized_relative_profits_other_renewables',
    'Change in normalized relative profits Nuclear':
    'change_in_normalized_relative_profits_nuclear',
    'Change in short term supply Biofuels':
    'change_in_short_term_supply_biofuels',
    'Change in short term supply Coal':
    'change_in_short_term_supply_coal',
    'Change in short term supply Gas':
    'change_in_short_term_supply_gas',
    'Change in short term supply Oil':
    'change_in_short_term_supply_oil',
    'Change in short term supply other Renewables':
    'change_in_short_term_supply_other_renewables',
    'Change in short term supply Nuclear':
    'change_in_short_term_supply_nuclear',
    'Change in unit costs Biofuels':
    'change_in_unit_costs_biofuels',
    'Change in unit costs Coal':
    'change_in_unit_costs_coal',
    'Change in unit costs Gas':
    'change_in_unit_costs_gas',
    'Change in unit costs Oil':
    'change_in_unit_costs_oil',
    'Change in unit costs other Renewables':
    'change_in_unit_costs_other_renewables',
    'Change in unit costs Nuclear':
    'change_in_unit_costs_nuclear',
    'MATH erf inv Coal':
    'math_erf_inv_coal',
    'MATH erf inv Gas':
    'math_erf_inv_gas',
    'MATH erf inv Oil':
    'math_erf_inv_oil',
    'MATH LN 1 minus x squared Coal':
    'math_ln_1_minus_x_squared_coal',
    'MATH LN 1 minus x squared Gas':
    'math_ln_1_minus_x_squared_gas',
    'MATH LN 1 minus x squared Oil':
    'math_ln_1_minus_x_squared_oil',
    'MATH mu fossil fuels':
    'math_mu_fossil_fuels',
    'MATH Pi':
    'math_pi',
    'MATH sgn erf input Coal':
    'math_sgn_erf_input_coal',
    'MATH sgn erf input Gas':
    'math_sgn_erf_input_gas',
    'MATH sgn erf input Oil':
    'math_sgn_erf_input_oil',
    'Cost development learning curve Biofuels':
    'cost_development_learning_curve_biofuels',
    'Cost development learning curve other Renewables':
    'cost_development_learning_curve_other_renewables',
    'Maximum relative mothballing Biofuels':
    'maximum_relative_mothballing_biofuels',
    'Cumulative extracted fuel other Renewables':
    'cumulative_extracted_fuel_other_renewables',
    'Cumulative extracted fuel Biofuels':
    'cumulative_extracted_fuel_biofuels',
    'Cumulative extracted fuel Coal':
    'cumulative_extracted_fuel_coal',
    'Cumulative extracted fuel Gas':
    'cumulative_extracted_fuel_gas',
    'Cumulative extracted fuel Oil':
    'cumulative_extracted_fuel_oil',
    'Supply elasticity Biofuels':
    'supply_elasticity_biofuels',
    'Cumulative extracted fuel t1 other Renewables':
    'cumulative_extracted_fuel_t1_other_renewables',
    'Cumulative extracted fuel t1 Nuclear':
    'cumulative_extracted_fuel_t1_nuclear',
    'Supply elasticity Oil':
    'supply_elasticity_oil',
    'Supply elasticity other Renewables':
    'supply_elasticity_other_renewables',
    'Normalised costs relative in relation to learning effects Biofuels':
    'normalised_costs_relative_in_relation_to_learning_effects_biofuels',
    'Normalised costs relative in relation to learning effects other Renewables':
    'normalised_costs_relative_in_relation_to_learning_effects_other_renewables',
    'Mothballing of capacity Biofuels':
    'mothballing_of_capacity_biofuels',
    'Mothballing of capacity Coal':
    'mothballing_of_capacity_coal',
    'Mothballing of capacity Gas':
    'mothballing_of_capacity_gas',
    'Mothballing of capacity Oil':
    'mothballing_of_capacity_oil',
    'Mothballing of capacity other Renewables':
    'mothballing_of_capacity_other_renewables',
    'Mothballing of capacity Nuclear':
    'mothballing_of_capacity_nuclear',
    'Initial cumulative extraction fuel Oil':
    'initial_cumulative_extraction_fuel_oil',
    'Initial cumulative extraction fuel other Renewables':
    'initial_cumulative_extraction_fuel_other_renewables',
    'Initial cumulative extraction fuel Nuclear':
    'initial_cumulative_extraction_fuel_nuclear',
    'Total costs energy supply Gas':
    'total_costs_energy_supply_gas',
    'Total costs energy supply Oil':
    'total_costs_energy_supply_oil',
    'Total costs energy supply other Renewables':
    'total_costs_energy_supply_other_renewables',
    'New extraction capacity proposed Biofuels':
    'new_extraction_capacity_proposed_biofuels',
    'New extraction capacity proposed Coal':
    'new_extraction_capacity_proposed_coal',
    'Delay order forecasts':
    'delay_order_forecasts',
    'New extraction capacity proposed Oil':
    'new_extraction_capacity_proposed_oil',
    'New extraction capacity proposed other Renewables':
    'new_extraction_capacity_proposed_other_renewables',
    'New extraction capacity proposed Nuclear':
    'new_extraction_capacity_proposed_nuclear',
    'new long term supply Biofuels':
    'new_long_term_supply_biofuels',
    'new long term supply Coal':
    'new_long_term_supply_coal',
    'new long term supply Gas':
    'new_long_term_supply_gas',
    'new long term supply Oil':
    'new_long_term_supply_oil',
    'new long term supply other Renewables':
    'new_long_term_supply_other_renewables',
    'new long term supply Nuclear':
    'new_long_term_supply_nuclear',
    'Normalised costs relative in relation to learning effects t1 other Renewables':
    'normalised_costs_relative_in_relation_to_learning_effects_t1_other_renewables',
    'Normalised costs relative in relation to learning effects t1 Biofuels':
    'normalised_costs_relative_in_relation_to_learning_effects_t1_biofuels',
    'Normalised costs relative in relation to learning effects t1 Nuclear':
    'normalised_costs_relative_in_relation_to_learning_effects_t1_nuclear',
    'Normalised costs relative in relation to learning effects Nuclear':
    'normalised_costs_relative_in_relation_to_learning_effects_nuclear',
    'Normalised costs relative in relation to learning t1 Biofuels':
    'normalised_costs_relative_in_relation_to_learning_t1_biofuels',
    'Normalised costs relative in relation to learning t1 other Renewables':
    'normalised_costs_relative_in_relation_to_learning_t1_other_renewables',
    'Normalised costs relative in relation to learning t1 Nuclear':
    'normalised_costs_relative_in_relation_to_learning_t1_nuclear',
    'Initial long term normalized profits Nuclear':
    'initial_long_term_normalized_profits_nuclear',
    'Unit costs Gas':
    'unit_costs_gas',
    'Unit costs Oil':
    'unit_costs_oil',
    'Unit costs other Renewables':
    'unit_costs_other_renewables',
    'Unit costs Nuclear':
    'unit_costs_nuclear',
    'Variance in EROEI distribution':
    'variance_in_eroei_distribution',
    'Normalized relation between costs and income Biofuels':
    'normalized_relation_between_costs_and_income_biofuels',
    'Normalized relation between costs and income Coal':
    'normalized_relation_between_costs_and_income_coal',
    'Normalized relation between costs and income Gas':
    'normalized_relation_between_costs_and_income_gas',
    'Normalized relation between costs and income Oil':
    'normalized_relation_between_costs_and_income_oil',
    'Maximum relative mothballing Coal':
    'maximum_relative_mothballing_coal',
    'Normalized relation between costs and income Nuclear':
    'normalized_relation_between_costs_and_income_nuclear',
    'Short forecasting period':
    'short_forecasting_period',
    'Summed delay time new capacity':
    'summed_delay_time_new_capacity',
    'Maximum relative mothballing other Renewables':
    'maximum_relative_mothballing_other_renewables',
    'Supply elasticity Coal':
    'supply_elasticity_coal',
    'Supply elasticity Gas':
    'supply_elasticity_gas',
    'Relative crustal abundance fossil fuels':
    'relative_crustal_abundance_fossil_fuels',
    'Relative EROI Coal':
    'relative_eroi_coal',
    'Relative EROI Gas':
    'relative_eroi_gas',
    'Initial unit costs Gas':
    'initial_unit_costs_gas',
    'Initial unit costs Oil':
    'initial_unit_costs_oil',
    'Initial unit costs other Renewables':
    'initial_unit_costs_other_renewables',
    'Recommissioning of capacity Biofuels':
    'recommissioning_of_capacity_biofuels',
    'Recommissioning of capacity Coal':
    'recommissioning_of_capacity_coal',
    'Recommissioning of capacity Gas':
    'recommissioning_of_capacity_gas',
    'Recommissioning of capacity Oil':
    'recommissioning_of_capacity_oil',
    'EROEI Biofuels':
    'eroei_biofuels',
    'EROEI Coal':
    'eroei_coal',
    'EROEI Gas':
    'eroei_gas',
    'EROEI Oil':
    'eroei_oil',
    'EROEI other Renewables':
    'eroei_other_renewables',
    'Experience curve parameter extraction':
    'experience_curve_parameter_extraction',
    'Relative change in EROEI Coal':
    'relative_change_in_eroei_coal',
    'Relative change in EROEI Gas':
    'relative_change_in_eroei_gas',
    'Relative change in EROEI Oil':
    'relative_change_in_eroei_oil',
    'Relative change in EROI Biofuels':
    'relative_change_in_eroi_biofuels',
    'Relative change in EROI other Renewables':
    'relative_change_in_eroi_other_renewables',
    'Long term profits energy supply period other Renewables':
    'long_term_profits_energy_supply_period_other_renewables',
    'Minimum EROEI':
    'minimum_eroei',
    'Total costs energy supply Coal':
    'total_costs_energy_supply_coal',
    'Investment fraction normalized profits other Renewables':
    'investment_fraction_normalized_profits_other_renewables',
    'MATH 2 over Pi times a':
    'math_2_over_pi_times_a',
    'Relative EROI Oil':
    'relative_eroi_oil',
    'MATH erf input Oil':
    'math_erf_input_oil',
    'Relative potential EROEI Biofuels':
    'relative_potential_eroei_biofuels',
    'Relative potential EROEI other Renewables':
    'relative_potential_eroei_other_renewables',
    'Initial long term normalized profits Gas':
    'initial_long_term_normalized_profits_gas',
    'Initial long term normalized profits Oil':
    'initial_long_term_normalized_profits_oil',
    'Initial long term normalized profits other Renewables':
    'initial_long_term_normalized_profits_other_renewables',
    'Unit costs Coal':
    'unit_costs_coal',
    'Relative variance in EROEI distribution':
    'relative_variance_in_eroei_distribution',
    'Long term profits energy supply period Oil':
    'long_term_profits_energy_supply_period_oil',
    'Investment fraction normalized profits Gas':
    'investment_fraction_normalized_profits_gas',
    'Investment fraction normalized profits Nuclear':
    'investment_fraction_normalized_profits_nuclear',
    'MATH sigma fossil fuels':
    'math_sigma_fossil_fuels',
    'Total costs energy supply Nuclear':
    'total_costs_energy_supply_nuclear',
    'Maximum EROEI':
    'maximum_eroei',
    'Initial EROEI Biofuels':
    'initial_eroei_biofuels',
    'Initial EROEI other Renewables':
    'initial_eroei_other_renewables',
    'Maximum relative mothballing Gas':
    'maximum_relative_mothballing_gas',
    'Long term normalized profits Nuclear':
    'long_term_normalized_profits_nuclear',
    'Maximum relative mothballing Oil':
    'maximum_relative_mothballing_oil',
    'Long term profits energy supply period Coal':
    'long_term_profits_energy_supply_period_coal',
    'Maximum relative mothballing Nuclear':
    'maximum_relative_mothballing_nuclear',
    'Total costs energy supply Biofuels':
    'total_costs_energy_supply_biofuels',
    'Unit costs Biofuels':
    'unit_costs_biofuels',
    'Investment fraction normalized profits Oil':
    'investment_fraction_normalized_profits_oil',
    'Long term profits energy supply period Nuclear':
    'long_term_profits_energy_supply_period_nuclear',
    'Relative change in costs due to learning Biofuels':
    'relative_change_in_costs_due_to_learning_biofuels',
    'Total income energy supply other Renewables':
    'total_income_energy_supply_other_renewables',
    'Total income energy supply Nuclear':
    'total_income_energy_supply_nuclear',
    'MATH erf input Gas':
    'math_erf_input_gas',
    'Initial long term normalized profits Biofuels':
    'initial_long_term_normalized_profits_biofuels',
    'Initial cumulative extraction fuel Biofuels':
    'initial_cumulative_extraction_fuel_biofuels',
    'Initial cumulative extraction fuel Coal':
    'initial_cumulative_extraction_fuel_coal',
    'Initial cumulative extraction fuel Gas':
    'initial_cumulative_extraction_fuel_gas',
    'Total available resources Oil':
    'total_available_resources_oil',
    'Long term profits energy supply period Gas':
    'long_term_profits_energy_supply_period_gas',
    'MATH erf input Coal':
    'math_erf_input_coal',
    'Total available resources Gas':
    'total_available_resources_gas',
    'Recommissioning of capacity other Renewables':
    'recommissioning_of_capacity_other_renewables',
    'Relative change in costs due to learning other Renewables':
    'relative_change_in_costs_due_to_learning_other_renewables',
    'Recommissioning of capacity Nuclear':
    'recommissioning_of_capacity_nuclear',
    'Long term normalized profits Coal':
    'long_term_normalized_profits_coal',
    'Investment fraction normalized profits Biofuels':
    'investment_fraction_normalized_profits_biofuels',
    'Long term normalized profits Gas':
    'long_term_normalized_profits_gas',
    'Long term normalized profits other Renewables':
    'long_term_normalized_profits_other_renewables',
    'Total available resources Coal':
    'total_available_resources_coal',
    'Long term profits energy supply period Biofuels':
    'long_term_profits_energy_supply_period_biofuels',
    'Initial unit costs Nuclear':
    'initial_unit_costs_nuclear',
    'MATH a':
    'math_a',
    'Long term normalized profits Biofuels':
    'long_term_normalized_profits_biofuels',
    'Investment fraction normalized profits Coal':
    'investment_fraction_normalized_profits_coal',
    'Relative change in costs due to learning Nuclear':
    'relative_change_in_costs_due_to_learning_nuclear',
    'Initial long term normalized profits Coal':
    'initial_long_term_normalized_profits_coal',
    'New extraction capacity proposed Gas':
    'new_extraction_capacity_proposed_gas',
    'Long term normalized profits Oil':
    'long_term_normalized_profits_oil',
    'CO2 emissions of Oil':
    'co2_emissions_of_oil',
    'CO2 emissions of coal':
    'co2_emissions_of_coal',
    'CO2 emissions':
    'co2_emissions',
    'CO2 emissions of natural gas':
    'co2_emissions_of_natural_gas',
    'Functional Energy Price Coal':
    'functional_energy_price_coal',
    'Functional Energy Price Oil':
    'functional_energy_price_oil',
    'Resource consumption Gas':
    'resource_consumption_gas',
    'Costs CO2 emissions':
    'costs_co2_emissions',
    'Functional Energy Price Gas':
    'functional_energy_price_gas',
    'Undiscovered resources Oil':
    'undiscovered_resources_oil',
    'Initial Undiscovered resources Coal':
    'initial_undiscovered_resources_coal',
    'Initial Undiscovered resources Gas':
    'initial_undiscovered_resources_gas',
    'Initial Undiscovered resources Oil':
    'initial_undiscovered_resources_oil',
    'Discovered resources reserve base Gas':
    'discovered_resources_reserve_base_gas',
    'Undiscovered resources Gas':
    'undiscovered_resources_gas',
    'Undiscovered resources Coal':
    'undiscovered_resources_coal',
    'Preference for Gas':
    'preference_for_gas',
    'Effect of Supply Shortage on Decoupling':
    'effect_of_supply_shortage_on_decoupling',
    'Extraction capacity installed Gas':
    'extraction_capacity_installed_gas',
    'Preference for other Renewables':
    'preference_for_other_renewables',
    'Initial Effect of Supply Shortage on Decoupling':
    'initial_effect_of_supply_shortage_on_decoupling',
    'Normalized Preference Coal':
    'normalized_preference_coal',
    'Initial Energy stocks Biofuels':
    'initial_energy_stocks_biofuels',
    'Initial Energy stocks Coal':
    'initial_energy_stocks_coal',
    'Initial Energy stocks Oil':
    'initial_energy_stocks_oil',
    'Normalized Preferenced other Renewables':
    'normalized_preferenced_other_renewables',
    'Functional Energy Price Nuclear':
    'functional_energy_price_nuclear',
    'Functional Energy Price other Renewables':
    'functional_energy_price_other_renewables',
    'Ideal Energy Demand Distribution Nuclear':
    'ideal_energy_demand_distribution_nuclear',
    'Preference for Biofuels':
    'preference_for_biofuels',
    'Preference for Coal':
    'preference_for_coal',
    'Initial mothballed capacity Gas':
    'initial_mothballed_capacity_gas',
    'Preference for Nuclear':
    'preference_for_nuclear',
    'Preference for Oil':
    'preference_for_oil',
    'Ideal Energy Demand Distribution Coal':
    'ideal_energy_demand_distribution_coal',
    'Normalized Preference Biofuels':
    'normalized_preference_biofuels',
    'total preferences':
    'total_preferences',
    'Mothballed capacity Coal':
    'mothballed_capacity_coal',
    'Initial mothballed capacity Coal':
    'initial_mothballed_capacity_coal',
    'Mothballed capacity Oil':
    'mothballed_capacity_oil',
    'Initial mothballed capacity Oil':
    'initial_mothballed_capacity_oil',
    'Ideal Energy Demand Distribution Biofuels':
    'ideal_energy_demand_distribution_biofuels',
    'Ideal Energy Demand Distribution other Renewables':
    'ideal_energy_demand_distribution_other_renewables',
    'Ideal Energy Demand Distribution Gas':
    'ideal_energy_demand_distribution_gas',
    'Ideal Energy Demand Distribution Oil':
    'ideal_energy_demand_distribution_oil',
    'Mothballed capacity Gas':
    'mothballed_capacity_gas',
    'Energy stocks Coal':
    'energy_stocks_coal',
    'Energy stocks Oil':
    'energy_stocks_oil',
    'Normalized Preference Gas':
    'normalized_preference_gas',
    'Energy stocks Biofuels':
    'energy_stocks_biofuels',
    'Normalized Preference Oil':
    'normalized_preference_oil',
    'Normalized Preference Nuclear':
    'normalized_preference_nuclear',
    'Functional Energy Price Biofuels':
    'functional_energy_price_biofuels',
    'Gas to trade':
    'gas_to_trade',
    'Energy Price Biofuels':
    'energy_price_biofuels',
    'Energy Price Coal':
    'energy_price_coal',
    'Energy Price Gas':
    'energy_price_gas',
    'Energy Price Nuclear':
    'energy_price_nuclear',
    'Energy Price Oil':
    'energy_price_oil',
    'Energy Price other Renewables':
    'energy_price_other_renewables',
    'total ideal demand distribution':
    'total_ideal_demand_distribution',
    'Current Energy Demand Oil':
    'current_energy_demand_oil',
    'Current Energy Demand other Renewables':
    'current_energy_demand_other_renewables',
    'Energy Demand Biofuels':
    'energy_demand_biofuels',
    'Energy Demand Coal':
    'energy_demand_coal',
    'Energy Demand Gas':
    'energy_demand_gas',
    'Energy Demand Nuclear':
    'energy_demand_nuclear',
    'Energy Demand Oil':
    'energy_demand_oil',
    'New Energy Demand Biofuels':
    'new_energy_demand_biofuels',
    'Maximum Change in Demand':
    'maximum_change_in_demand',
    'Current Energy Demand Biofuels':
    'current_energy_demand_biofuels',
    'Current Energy Demand Coal':
    'current_energy_demand_coal',
    'Current Energy Demand Gas':
    'current_energy_demand_gas',
    'Energy Demand other Renewables':
    'energy_demand_other_renewables',
    'New Energy Demand Coal':
    'new_energy_demand_coal',
    'New Energy Demand Gas':
    'new_energy_demand_gas',
    'New Energy Demand Nuclear':
    'new_energy_demand_nuclear',
    'New Energy Demand Oil':
    'new_energy_demand_oil',
    'New Energy Demand other Renewables':
    'new_energy_demand_other_renewables',
    'Current Energy Demand Nuclear':
    'current_energy_demand_nuclear',
    'Ideal Energy Demand Gas':
    'ideal_energy_demand_gas',
    'Ideal Energy Demand Biofuels':
    'ideal_energy_demand_biofuels',
    'Ideal Energy Demand Coal':
    'ideal_energy_demand_coal',
    'Ideal Energy Demand Oil':
    'ideal_energy_demand_oil',
    'Ideal Energy Demand other Renewables':
    'ideal_energy_demand_other_renewables',
    'Total New Energy Demand':
    'total_new_energy_demand',
    'Ideal Energy Demand Nuclear':
    'ideal_energy_demand_nuclear',
    'Current Energy Supply Distribution Nuclear':
    'current_energy_supply_distribution_nuclear',
    'Available resources from stocks Biofuels':
    'available_resources_from_stocks_biofuels',
    'Available resources from stocks Coal':
    'available_resources_from_stocks_coal',
    'Available resources from stocks Oil':
    'available_resources_from_stocks_oil',
    'Relative Biofuels Shortage':
    'relative_biofuels_shortage',
    'Relative Coal Shortage':
    'relative_coal_shortage',
    'Relative other Renewables Shortage':
    'relative_other_renewables_shortage',
    'Relative Shortages Oil':
    'relative_shortages_oil',
    'Current Energy Supply Distribution other Renewables':
    'current_energy_supply_distribution_other_renewables',
    'Resource consumption reduction factor Biofuels':
    'resource_consumption_reduction_factor_biofuels',
    'Decrease in Shortage Effect':
    'decrease_in_shortage_effect',
    'Delay Order Decoupling due to Shortage':
    'delay_order_decoupling_due_to_shortage',
    'Nuclear Shortage':
    'nuclear_shortage',
    'Factor limiting Economic Growth due to Energy Shortage':
    'factor_limiting_economic_growth_due_to_energy_shortage',
    'Delay Time Decoupling due to Shortage':
    'delay_time_decoupling_due_to_shortage',
    'Future Shortage Effect':
    'future_shortage_effect',
    'Total Energy Supply Distribution':
    'total_energy_supply_distribution',
    'Relative Supply Shortage':
    'relative_supply_shortage',
    'Resource consumption reduction factor Oil':
    'resource_consumption_reduction_factor_oil',
    'Effect of Energy Shortage on Future Decoupling':
    'effect_of_energy_shortage_on_future_decoupling',
    'Resource consumption Oil':
    'resource_consumption_oil',
    'Resource consumption reduction factor Coal':
    'resource_consumption_reduction_factor_coal',
    'other Renewables Shortage':
    'other_renewables_shortage',
    'Relative Shortage Nuclear':
    'relative_shortage_nuclear',
    'Limitations Economic Growth due to Energy Shortage':
    'limitations_economic_growth_due_to_energy_shortage',
    'Resource consumption Coal':
    'resource_consumption_coal',
    'Resource consumption Biofuels':
    'resource_consumption_biofuels',
    'Future Effect of Shortage on Decoupling':
    'future_effect_of_shortage_on_decoupling',
    'Energy Shortage':
    'energy_shortage',
    'Initial Shortage Effect on Decoupling':
    'initial_shortage_effect_on_decoupling',
    'Initial Energy Intensity GDP':
    'initial_energy_intensity_gdp',
    'Energy Demand':
    'energy_demand',
    'Gas Export':
    'gas_export',
    'Initial GDP':
    'initial_gdp',
    'GDP':
    'gdp',
    'One Year':
    'one_year',
    'Energy Intensity GDP':
    'energy_intensity_gdp',
    'Gas Import':
    'gas_import',
    'Decrease Energy Intensity GDP':
    'decrease_energy_intensity_gdp',
    'Average Rb over P Coal':
    'average_rb_over_p_coal',
    'Average Rb over P Oil':
    'average_rb_over_p_oil',
    'Average Rb over P gas':
    'average_rb_over_p_gas',
    'Average throughput time stocks Biofuels':
    'average_throughput_time_stocks_biofuels',
    'Average throughput time stocks Coal':
    'average_throughput_time_stocks_coal',
    'Delay order new capacity Biofuels':
    'delay_order_new_capacity_biofuels',
    'Delay order new capacity Coal':
    'delay_order_new_capacity_coal',
    'Delay order new capacity Gas':
    'delay_order_new_capacity_gas',
    'Delay order new capacity Oil':
    'delay_order_new_capacity_oil',
    'Delay order new capacity other Renewables':
    'delay_order_new_capacity_other_renewables',
    'Delay order new capacity Nuclear':
    'delay_order_new_capacity_nuclear',
    'Delay time new capacity Biofuels':
    'delay_time_new_capacity_biofuels',
    'Delay time new capacity Coal':
    'delay_time_new_capacity_coal',
    'Delay time new capacity Gas':
    'delay_time_new_capacity_gas',
    'Delay time new capacity Oil':
    'delay_time_new_capacity_oil',
    'Delay time new capacity other Renewables':
    'delay_time_new_capacity_other_renewables',
    'Delay time new capacity Nuclear':
    'delay_time_new_capacity_nuclear',
    'Deterioration of unused capacity Biofuels':
    'deterioration_of_unused_capacity_biofuels',
    'Deterioration of unused capacity Coal':
    'deterioration_of_unused_capacity_coal',
    'Deterioration of unused capacity Gas':
    'deterioration_of_unused_capacity_gas',
    'Deterioration of unused capacity Oil':
    'deterioration_of_unused_capacity_oil',
    'Deterioration of unused capacity other Renewables':
    'deterioration_of_unused_capacity_other_renewables',
    'Deterioration of unused capacity Nuclear':
    'deterioration_of_unused_capacity_nuclear',
    'Discovered resources reserve base Coal':
    'discovered_resources_reserve_base_coal',
    'Discovered resources reserve base Oil':
    'discovered_resources_reserve_base_oil',
    'Energy import Biofuels':
    'energy_import_biofuels',
    'Energy import Coal':
    'energy_import_coal',
    'Energy import Oil':
    'energy_import_oil',
    'Extraction capacity in preparation Biofuels':
    'extraction_capacity_in_preparation_biofuels',
    'Extraction capacity in preparation Coal':
    'extraction_capacity_in_preparation_coal',
    'Extraction capacity in preparation Gas':
    'extraction_capacity_in_preparation_gas',
    'Extraction capacity in preparation Oil':
    'extraction_capacity_in_preparation_oil',
    'Extraction capacity in preparation other Renewables':
    'extraction_capacity_in_preparation_other_renewables',
    'Extraction capacity in preparation Nuclear':
    'extraction_capacity_in_preparation_nuclear',
    'Extraction capacity installed Biofuels':
    'extraction_capacity_installed_biofuels',
    'Extraction capacity installed Coal':
    'extraction_capacity_installed_coal',
    'Extraction capacity installed Oil':
    'extraction_capacity_installed_oil',
    'Extraction capacity installed other Renewables':
    'extraction_capacity_installed_other_renewables',
    'Extraction capacity installed Nuclear':
    'extraction_capacity_installed_nuclear',
    'Initial mothballed capacity Biofuels':
    'initial_mothballed_capacity_biofuels',
    'Initial mothballed capacity other Renewables':
    'initial_mothballed_capacity_other_renewables',
    'Initial mothballed capacity Nuclear':
    'initial_mothballed_capacity_nuclear',
    'Initial extraction capacity Biofuels':
    'initial_extraction_capacity_biofuels',
    'Initial extraction capacity Coal':
    'initial_extraction_capacity_coal',
    'Initial extraction capacity Gas':
    'initial_extraction_capacity_gas',
    'Initial extraction capacity Oil':
    'initial_extraction_capacity_oil',
    'Initial extraction capacity other Renewables':
    'initial_extraction_capacity_other_renewables',
    'Initial extraction capacity in preparation Biofuels':
    'initial_extraction_capacity_in_preparation_biofuels',
    'Initial extraction capacity in preparation Coal':
    'initial_extraction_capacity_in_preparation_coal',
    'Initial extraction capacity in preparation Gas':
    'initial_extraction_capacity_in_preparation_gas',
    'Initial extraction capacity in preparation Oil':
    'initial_extraction_capacity_in_preparation_oil',
    'Initial extraction capacity in preparation other Renewables':
    'initial_extraction_capacity_in_preparation_other_renewables',
    'Initial extraction capacity in preparation Nuclear':
    'initial_extraction_capacity_in_preparation_nuclear',
    'Initial extraction capacity Nuclear':
    'initial_extraction_capacity_nuclear',
    'Initial relation between reserve base and resource size Coal':
    'initial_relation_between_reserve_base_and_resource_size_coal',
    'Initial relation between reserve base and resource size Gas':
    'initial_relation_between_reserve_base_and_resource_size_gas',
    'Initial relation between reserve base and resource size Oil':
    'initial_relation_between_reserve_base_and_resource_size_oil',
    'Initial reserve base Coal':
    'initial_reserve_base_coal',
    'Initial reserve base Gas':
    'initial_reserve_base_gas',
    'Initial reserve base Oil':
    'initial_reserve_base_oil',
    'Mothballed capacity Biofuels':
    'mothballed_capacity_biofuels',
    'Mothballed capacity other Renewables':
    'mothballed_capacity_other_renewables',
    'Mothballed capacity Nuclear':
    'mothballed_capacity_nuclear',
    'Non stockpiled gas extraction':
    'non_stockpiled_gas_extraction',
    'Production of biofuels':
    'production_of_biofuels',
    'Resource extraction Coal':
    'resource_extraction_coal',
    'Resource extraction Oil':
    'resource_extraction_oil',
    'Time for deteriation of unused capacity Biofuels':
    'time_for_deteriation_of_unused_capacity_biofuels',
    'Time for deteriation of unused capacity Coal':
    'time_for_deteriation_of_unused_capacity_coal',
    'Time for deteriation of unused capacity Gas':
    'time_for_deteriation_of_unused_capacity_gas',
    'Time for deteriation of unused capacity Oil':
    'time_for_deteriation_of_unused_capacity_oil',
    'Time for deteriation of unused capacity other Renewables':
    'time_for_deteriation_of_unused_capacity_other_renewables',
    'Time for deteriation of unused capacity Nuclear':
    'time_for_deteriation_of_unused_capacity_nuclear',
    'Total export Biofuels':
    'total_export_biofuels',
    'Total export Coal':
    'total_export_coal',
    'Total export Oil':
    'total_export_oil',
    'Total import Biofuels':
    'total_import_biofuels',
    'Total import Coal':
    'total_import_coal',
    'Total import Oil':
    'total_import_oil',
    'FINAL TIME':
    'final_time',
    'INITIAL TIME':
    'initial_time',
    'SAVEPER':
    'saveper',
    'TIME STEP':
    'time_step'
}

__pysd_version__ = "0.9.0"


@cache('step')
def previous_energy_demand_nuclear():
    """
    Real Name: Previous Energy Demand Nuclear
    Original Eqn: Initial Demand Nuclear
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return initial_demand_nuclear()


@cache('step')
def previous_energy_demand_oil():
    """
    Real Name: Previous Energy Demand Oil
    Original Eqn: Initial Demand Oil
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return initial_demand_oil()


@cache('step')
def previous_energy_demand_other_renewables():
    """
    Real Name: Previous Energy Demand other Renewables
    Original Eqn: Initial Demand other Renewables
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return initial_demand_other_renewables()


@cache('step')
def normalized_previous_demand_biofuels():
    """
    Real Name: Normalized Previous Demand Biofuels
    Original Eqn: ZIDZ(Previous Energy Demand Biofuels, Total Previous Energy Demand)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(previous_energy_demand_biofuels(), total_previous_energy_demand())


@cache('step')
def normalized_previous_demand_coal():
    """
    Real Name: Normalized Previous Demand Coal
    Original Eqn: ZIDZ(Previous Energy Demand Coal, Total Previous Energy Demand)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(previous_energy_demand_coal(), total_previous_energy_demand())


@cache('step')
def normalized_previous_demand_gas():
    """
    Real Name: Normalized Previous Demand Gas
    Original Eqn: ZIDZ(Previous Energy Demand Gas, Total Previous Energy Demand)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(previous_energy_demand_gas(), total_previous_energy_demand())


@cache('step')
def normalized_previous_demand_nuclear():
    """
    Real Name: Normalized Previous Demand Nuclear
    Original Eqn: ZIDZ(Previous Energy Demand Nuclear, Total Previous Energy Demand)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(previous_energy_demand_nuclear(), total_previous_energy_demand())


@cache('step')
def normalized_previous_demand_oil():
    """
    Real Name: Normalized Previous Demand Oil
    Original Eqn: ZIDZ(Previous Energy Demand Oil, Total Previous Energy Demand)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(previous_energy_demand_oil(), total_previous_energy_demand())


@cache('step')
def normalized_previous_demand_other_renewables():
    """
    Real Name: Normalized Previous Demand other Renewables
    Original Eqn: ZIDZ(Previous Energy Demand other Renewables, Total Previous Energy Demand)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(previous_energy_demand_other_renewables(),
                          total_previous_energy_demand())


@cache('run')
def initial_demand_nuclear():
    """
    Real Name: Initial Demand Nuclear
    Original Eqn: 1.27531e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 1.27531e+06


@cache('run')
def initial_demand_oil():
    """
    Real Name: Initial Demand Oil
    Original Eqn: 3.21823e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 3.21823e+06


@cache('run')
def initial_demand_other_renewables():
    """
    Real Name: Initial Demand other Renewables
    Original Eqn: 1.4764e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 1.4764e+06


@cache('run')
def previous_demand_factor():
    """
    Real Name: Previous Demand Factor
    Original Eqn: 0.99
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.99


@cache('step')
def previous_energy_demand_biofuels():
    """
    Real Name: Previous Energy Demand Biofuels
    Original Eqn: Initial Demand Biofuels
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return initial_demand_biofuels()


@cache('step')
def previous_energy_demand_coal():
    """
    Real Name: Previous Energy Demand Coal
    Original Eqn: Initial Demand Coal
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return initial_demand_coal()


@cache('run')
def eugasimport():
    """
    Real Name: EUgasimport
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def initial_demand_gas():
    """
    Real Name: Initial Demand Gas
    Original Eqn: 2.73897e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 2.73897e+06


@cache('step')
def previous_energy_demand_gas():
    """
    Real Name: Previous Energy Demand Gas
    Original Eqn: Initial Demand Gas
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return initial_demand_gas()


@cache('run')
def initial_demand_biofuels():
    """
    Real Name: Initial Demand Biofuels
    Original Eqn: 363653
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 363653


@cache('run')
def initial_demand_coal():
    """
    Real Name: Initial Demand Coal
    Original Eqn: 3.76404e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 3.76404e+06


@cache('step')
def total_previous_energy_demand():
    """
    Real Name: Total Previous Energy Demand
    Original Eqn: Previous Energy Demand Biofuels+Previous Energy Demand Coal+Previous Energy Demand Gas\ +Previous Energy Demand Nuclear+Previous Energy Demand Oil+Previous Energy Demand other Renewables
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return previous_energy_demand_biofuels() + previous_energy_demand_coal(
    ) + previous_energy_demand_gas() + previous_energy_demand_nuclear(
    ) + previous_energy_demand_oil() + previous_energy_demand_other_renewables()


@cache('run')
def gas_import_costs():
    """
    Real Name: Gas Import Costs
    Original Eqn: 0
    Units: Dollar
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def decrease_factor():
    """
    Real Name: decrease factor
    Original Eqn: Effect of Supply Shortage on Decoupling+Autonomous Energy Intensity Decrease
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return effect_of_supply_shortage_on_decoupling() + autonomous_energy_intensity_decrease()


@cache('run')
def autonomous_energy_intensity_decrease():
    """
    Real Name: Autonomous Energy Intensity Decrease
    Original Eqn: 0.01
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.01


@cache('step')
def increase_in_discovered_and_technically_recoverable_resources_oil():
    """
    Real Name: Increase in discovered and technically recoverable resources Oil
    Original Eqn: -Relative change in costs due to learning Oil*Initial relation between reserve base and resource size Oil\ *Undiscovered resources Oil
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return -relative_change_in_costs_due_to_learning_oil(
    ) * initial_relation_between_reserve_base_and_resource_size_oil() * undiscovered_resources_oil(
    )


@cache('step')
def normalised_costs_relative_in_relation_to_learning_t1_coal():
    """
    Real Name: Normalised costs relative in relation to learning t1 Coal
    Original Eqn: Normalised costs relative in relation to learning effects t1 Coal/Summed delay time new capacity
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_coal(
    ) / summed_delay_time_new_capacity()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_t1_gas():
    """
    Real Name: Normalised costs relative in relation to learning t1 Gas
    Original Eqn: Normalised costs relative in relation to learning effects t1 Gas/Summed delay time new capacity
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_gas(
    ) / summed_delay_time_new_capacity()


@cache('run')
def initial_average_normalised_learning_curve_on_costs_gas():
    """
    Real Name: Initial average normalised learning curve on costs Gas
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def normalised_costs_relative_in_relation_to_learning_t1_oil():
    """
    Real Name: Normalised costs relative in relation to learning t1 Oil
    Original Eqn: Normalised costs relative in relation to learning effects t1 Oil/Summed delay time new capacity
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_oil(
    ) / summed_delay_time_new_capacity()


@cache('step')
def cumulative_extracted_fuel_t1_gas():
    """
    Real Name: Cumulative extracted fuel t1 Gas
    Original Eqn: DELAY N(Cumulative extracted fuel Gas, Short forecasting period, Initial cumulative extraction fuel Gas\ , Delay order forecasts)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return delay_cumulative_extracted_fuel_gas_short_forecasting_period_initial_cumulative_extraction_fuel_gas_delay_order_forecasts(
    )


@cache('step')
def cost_development_learning_curve_coal():
    """
    Real Name: Cost development learning curve Coal
    Original Eqn: Normalised costs relative in relation to learning effects t1 Coal/Initial normalised costs relative in relation to learning effects Coal2
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_coal(
    ) / initial_normalised_costs_relative_in_relation_to_learning_effects_coal2()


@cache('step')
def cost_development_learning_curve_gas():
    """
    Real Name: Cost development learning curve Gas
    Original Eqn: Normalised costs relative in relation to learning effects t1 Gas/Initial normalised costs relative in relation to learning effects Gas2
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_gas(
    ) / initial_normalised_costs_relative_in_relation_to_learning_effects_gas2()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_oil():
    """
    Real Name: Normalised costs relative in relation to learning effects Oil
    Original Eqn: Normalised costs relative in relation to learning t1 Oil*XIDZ( Cumulative extracted fuel Oil\ , Cumulative extracted fuel t1 Oil, 1)^Experience curve parameter extraction
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Normalised costs relative in relation to learning t1 other 
        Renewables*ZIDZ(Cumulative extracted fuel other Renewables, Cumulative 
        extracted fuel t1 other Renewables)^Experience curve parameter extraction
    """
    return normalised_costs_relative_in_relation_to_learning_t1_oil() * functions.xidz(
        cumulative_extracted_fuel_oil(), cumulative_extracted_fuel_t1_oil(),
        1)**experience_curve_parameter_extraction()


@cache('step')
def cost_development_learning_curve_oil():
    """
    Real Name: Cost development learning curve Oil
    Original Eqn: Normalised costs relative in relation to learning effects t1 Oil/Initial normalised costs relative in relation to learning effects Oil2
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_oil(
    ) / initial_normalised_costs_relative_in_relation_to_learning_effects_oil2()


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_coal():
    """
    Real Name: Initial normalised costs relative in relation to learning effects Coal
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('step')
def average_normalised_learning_curve_on_costs_coal():
    """
    Real Name: Average normalised learning curve on costs Coal
    Original Eqn: INTEG ( Change in average learning curve parameter Coal, Initial average normalised learning curve on costs Coal)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_average_normalised_learning_curve_on_costs_coal()


@cache('step')
def average_normalised_learning_curve_on_costs_gas():
    """
    Real Name: Average normalised learning curve on costs Gas
    Original Eqn: INTEG ( Change in average learning curve parameter Gas, Initial average normalised learning curve on costs Gas)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_average_normalised_learning_curve_on_costs_gas()


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_gas2():
    """
    Real Name: Initial normalised costs relative in relation to learning effects Gas2
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('step')
def average_normalised_learning_curve_on_costs_oil():
    """
    Real Name: Average normalised learning curve on costs Oil
    Original Eqn: INTEG ( Change in average learning curve parameter Oil, Initial average normalised learning curve on costs Oil)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_average_normalised_learning_curve_on_costs_oil()


@cache('step')
def increase_in_discovered_and_technically_recoverable_resources_coal():
    """
    Real Name: Increase in discovered and technically recoverable resources Coal
    Original Eqn: -Relative change in costs due to learning Coal*Initial relation between reserve base and resource size Coal\ *Undiscovered resources Coal
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return -relative_change_in_costs_due_to_learning_coal(
    ) * initial_relation_between_reserve_base_and_resource_size_coal(
    ) * undiscovered_resources_coal()


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_oil():
    """
    Real Name: Initial normalised costs relative in relation to learning effects Oil
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_oil2():
    """
    Real Name: Initial normalised costs relative in relation to learning effects Oil2
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('run')
def initial_average_normalised_learning_curve_on_costs_coal():
    """
    Real Name: Initial average normalised learning curve on costs Coal
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def cumulative_extracted_fuel_t1_coal():
    """
    Real Name: Cumulative extracted fuel t1 Coal
    Original Eqn: DELAY N(Cumulative extracted fuel Coal, Short forecasting period, Initial cumulative extraction fuel Coal\ , Delay order forecasts)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return delay_cumulative_extracted_fuel_coal_short_forecasting_period_initial_cumulative_extraction_fuel_coal_delay_order_forecasts(
    )


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_t1_gas():
    """
    Real Name: Normalised costs relative in relation to learning effects t1 Gas
    Original Eqn: INTEG ( Normalised costs relative in relation to learning effects Gas-Normalised costs relative in relation to learning t1 Gas\ , Initial normalised costs relative in relation to learning effects Gas)
    Units: year
    Limits: (None, None)
    Type: component


    """
    return integ_normalised_costs_relative_in_relation_to_learning_effects_t1_gas()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_gas():
    """
    Real Name: Normalised costs relative in relation to learning effects Gas
    Original Eqn: Normalised costs relative in relation to learning t1 Gas*XIDZ( Cumulative extracted fuel Gas\ , Cumulative extracted fuel t1 Gas, 1)^Experience curve parameter extraction
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Normalised costs relative in relation to learning t1 other 
        Renewables*ZIDZ(Cumulative extracted fuel other Renewables, Cumulative 
        extracted fuel t1 other Renewables)^Experience curve parameter extraction
    """
    return normalised_costs_relative_in_relation_to_learning_t1_gas() * functions.xidz(
        cumulative_extracted_fuel_gas(), cumulative_extracted_fuel_t1_gas(),
        1)**experience_curve_parameter_extraction()


@cache('step')
def cumulative_extracted_fuel_t1_oil():
    """
    Real Name: Cumulative extracted fuel t1 Oil
    Original Eqn: DELAY N(Cumulative extracted fuel Oil, Short forecasting period, Initial cumulative extraction fuel Oil\ , Delay order forecasts)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return delay_cumulative_extracted_fuel_oil_short_forecasting_period_initial_cumulative_extraction_fuel_oil_delay_order_forecasts(
    )


@cache('run')
def initial_average_normalised_learning_curve_on_costs_oil():
    """
    Real Name: Initial average normalised learning curve on costs Oil
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_gas():
    """
    Real Name: Initial normalised costs relative in relation to learning effects Gas
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('step')
def change_in_average_learning_curve_parameter_coal():
    """
    Real Name: Change in average learning curve parameter Coal
    Original Eqn: (Cost development learning curve Coal-Average normalised learning curve on costs Coal\ )/One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (cost_development_learning_curve_coal() -
            average_normalised_learning_curve_on_costs_coal()) / one_year()


@cache('step')
def change_in_average_learning_curve_parameter_gas():
    """
    Real Name: Change in average learning curve parameter Gas
    Original Eqn: (Cost development learning curve Gas-Average normalised learning curve on costs Gas)\ /One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (cost_development_learning_curve_gas() -
            average_normalised_learning_curve_on_costs_gas()) / one_year()


@cache('step')
def relative_change_in_costs_due_to_learning_coal():
    """
    Real Name: Relative change in costs due to learning Coal
    Original Eqn: ZIDZ(Change in average learning curve parameter Coal, Average normalised learning curve on costs Coal\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_average_learning_curve_parameter_coal(),
                          average_normalised_learning_curve_on_costs_coal())


@cache('step')
def change_in_average_learning_curve_parameter_oil():
    """
    Real Name: Change in average learning curve parameter Oil
    Original Eqn: (Cost development learning curve Oil-Average normalised learning curve on costs Oil)\ /One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (cost_development_learning_curve_oil() -
            average_normalised_learning_curve_on_costs_oil()) / one_year()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_t1_oil():
    """
    Real Name: Normalised costs relative in relation to learning effects t1 Oil
    Original Eqn: INTEG ( Normalised costs relative in relation to learning effects Oil-Normalised costs relative in relation to learning t1 Oil\ , Initial normalised costs relative in relation to learning effects Oil)
    Units: year
    Limits: (None, None)
    Type: component


    """
    return integ_normalised_costs_relative_in_relation_to_learning_effects_t1_oil()


@cache('step')
def relative_change_in_costs_due_to_learning_oil():
    """
    Real Name: Relative change in costs due to learning Oil
    Original Eqn: ZIDZ(Change in average learning curve parameter Oil, Average normalised learning curve on costs Oil\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_average_learning_curve_parameter_oil(),
                          average_normalised_learning_curve_on_costs_oil())


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_coal2():
    """
    Real Name: Initial normalised costs relative in relation to learning effects Coal2
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('step')
def relative_change_in_costs_due_to_learning_gas():
    """
    Real Name: Relative change in costs due to learning Gas
    Original Eqn: ZIDZ(Change in average learning curve parameter Gas, Average normalised learning curve on costs Gas\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_average_learning_curve_parameter_gas(),
                          average_normalised_learning_curve_on_costs_gas())


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_coal():
    """
    Real Name: Normalised costs relative in relation to learning effects Coal
    Original Eqn: Normalised costs relative in relation to learning t1 Coal*XIDZ( Cumulative extracted fuel Coal\ , Cumulative extracted fuel t1 Coal, 1)^Experience curve parameter extraction
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Normalised costs relative in relation to learning t1 other 
        Renewables*ZIDZ(Cumulative extracted fuel other Renewables, Cumulative 
        extracted fuel t1 other Renewables)^Experience curve parameter extraction
    """
    return normalised_costs_relative_in_relation_to_learning_t1_coal() * functions.xidz(
        cumulative_extracted_fuel_coal(), cumulative_extracted_fuel_t1_coal(),
        1)**experience_curve_parameter_extraction()


@cache('step')
def increase_in_discovered_and_technically_recoverable_gas():
    """
    Real Name: Increase in discovered and technically recoverable gas
    Original Eqn: -Relative change in costs due to learning Gas*Initial relation between reserve base and resource size Gas\ *Undiscovered resources Gas
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return -relative_change_in_costs_due_to_learning_gas(
    ) * initial_relation_between_reserve_base_and_resource_size_gas() * undiscovered_resources_gas(
    )


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_t1_coal():
    """
    Real Name: Normalised costs relative in relation to learning effects t1 Coal
    Original Eqn: INTEG ( Normalised costs relative in relation to learning effects Coal-Normalised costs relative in relation to learning t1 Coal\ , Initial normalised costs relative in relation to learning effects Coal)
    Units: year
    Limits: (None, None)
    Type: component


    """
    return integ_normalised_costs_relative_in_relation_to_learning_effects_t1_coal()


@cache('step')
def coal_to_trade_from_storage():
    """
    Real Name: Coal to trade from storage
    Original Eqn: IF THEN ELSE(Extraction capacity installed Coal>Energy Demand Coal, MAX(0, Available resources from stocks Coal\ -Energy Demand Coal*Storage goal) , 0)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        extraction_capacity_installed_coal() > energy_demand_coal(),
        np.maximum(0,
                   available_resources_from_stocks_coal() - energy_demand_coal() * storage_goal()),
        0)


@cache('step')
def biofuels_to_trade_from_stocks():
    """
    Real Name: Biofuels to trade from stocks
    Original Eqn: IF THEN ELSE(Extraction capacity installed Biofuels>Energy Demand Biofuels, MAX(0, Available resources from stocks Biofuels\ -Energy Demand Biofuels*Storage goal) , 0)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        extraction_capacity_installed_biofuels() > energy_demand_biofuels(),
        np.maximum(
            0,
            available_resources_from_stocks_biofuels() -
            energy_demand_biofuels() * storage_goal()), 0)


@cache('step')
def oil_to_trade_from_storage():
    """
    Real Name: Oil to trade from storage
    Original Eqn: IF THEN ELSE(Extraction capacity installed Oil>Energy Demand Oil, MAX(0 , Available resources from stocks Oil\ -Energy Demand Oil*Storage goal),0)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        extraction_capacity_installed_oil() > energy_demand_oil(),
        np.maximum(0,
                   available_resources_from_stocks_oil() - energy_demand_oil() * storage_goal()),
        0)


@cache('step')
def decoupling_effect_materializing():
    """
    Real Name: Decoupling Effect Materializing
    Original Eqn: DELAY N(MAX(0,Future Shortage Effect), Delay Time Decoupling due to Shortage, Initial Decoupling Effect Materializing\ , Delay Order Decoupling due to Shortage)
    Units: 1/(year*year)
    Limits: (None, None)
    Type: component


    """
    return delay_npmaximum0future_shortage_effect_delay_time_decoupling_due_to_shortage_initial_decoupling_effect_materializing_delay_order_decoupling_due_to_shortage(
    )


@cache('run')
def initial_decoupling_effect_materializing():
    """
    Real Name: Initial Decoupling Effect Materializing
    Original Eqn: 0
    Units: 1/(year*year)
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def total_income_energy_supply_biofuels():
    """
    Real Name: Total income energy supply Biofuels
    Original Eqn: Energy Price Biofuels*(New Energy Demand Biofuels+Energy export Biofuels)
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return energy_price_biofuels() * (new_energy_demand_biofuels() + energy_export_biofuels())


@cache('step')
def total_income_energy_supply_coal():
    """
    Real Name: Total income energy supply Coal
    Original Eqn: Energy Price Coal*(New Energy Demand Coal+Energy export Coal)
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return energy_price_coal() * (new_energy_demand_coal() + energy_export_coal())


@cache('step')
def available_gas():
    """
    Real Name: Available Gas
    Original Eqn: MAX(0,Non stockpiled gas extraction+Gas Import-Gas Export)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.maximum(0, non_stockpiled_gas_extraction() + gas_import() - gas_export())


@cache('step')
def total_income_energy_supply_oil():
    """
    Real Name: Total income energy supply Oil
    Original Eqn: Energy Price Oil*(New Energy Demand Oil+Energy export Oil)
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return energy_price_oil() * (new_energy_demand_oil() + energy_export_oil())


@cache('step')
def completing_new_extraction_capacity_nuclear():
    """
    Real Name: Completing new extraction capacity Nuclear
    Original Eqn: DELAY N(MAX(0,New extraction capacity proposed Nuclear), Delay time new capacity Nuclear\ , Initial completing new extraction capacity Nuclear, Delay order new capacity Nuclear\ )
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return delay_npmaximum0new_extraction_capacity_proposed_nuclear_delay_time_new_capacity_nuclear_initial_completing_new_extraction_capacity_nuclear_delay_order_new_capacity_nuclear(
    )


@cache('step')
def completing_new_extraction_capacity_oil():
    """
    Real Name: Completing new extraction capacity Oil
    Original Eqn: DELAY N(MAX(0,New extraction capacity proposed Oil), Delay time new capacity Oil, Initial completing new extraction capacity Oil\ , Delay order new capacity Oil)
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return delay_npmaximum0new_extraction_capacity_proposed_oil_delay_time_new_capacity_oil_initial_completing_new_extraction_capacity_oil_delay_order_new_capacity_oil(
    )


@cache('step')
def completing_new_extraction_capacity_other_renewables():
    """
    Real Name: Completing new extraction capacity other Renewables
    Original Eqn: DELAY N(MAX(0,New extraction capacity proposed other Renewables), Delay time new capacity other Renewables\ , Initial completing new extraction capacity other Renewables , Delay order new capacity other Renewables)
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return delay_npmaximum0new_extraction_capacity_proposed_other_renewables_delay_time_new_capacity_other_renewables_initial_completing_new_extraction_capacity_other_renewables_delay_order_new_capacity_other_renewables(
    )


@cache('run')
def initial_completing_new_extraction_capacity_biofuels():
    """
    Real Name: Initial completing new extraction capacity Biofuels
    Original Eqn: 689.952
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: constant


    """
    return 689.952


@cache('step')
def biofuels_to_trade():
    """
    Real Name: Biofuels to trade
    Original Eqn: Production of biofuels-Energy Demand Biofuels+Biofuels to trade from stocks
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return production_of_biofuels() - energy_demand_biofuels() + biofuels_to_trade_from_stocks()


@cache('run')
def initial_completing_new_extraction_capacity_nuclear():
    """
    Real Name: Initial completing new extraction capacity Nuclear
    Original Eqn: 0
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def initial_completing_new_extraction_capacity_oil():
    """
    Real Name: Initial completing new extraction capacity Oil
    Original Eqn: 0
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def oil_to_trade():
    """
    Real Name: Oil to trade
    Original Eqn: Resource extraction Oil-Energy Demand Oil + Oil to trade from storage
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return resource_extraction_oil() - energy_demand_oil() + oil_to_trade_from_storage()


@cache('step')
def coal_to_trade():
    """
    Real Name: Coal to trade
    Original Eqn: Resource extraction Coal-Energy Demand Coal+Coal to trade from storage
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return resource_extraction_coal() - energy_demand_coal() + coal_to_trade_from_storage()


@cache('step')
def total_income_energy_supply_gas():
    """
    Real Name: Total income energy supply Gas
    Original Eqn: Energy Price Gas*(Gas Export+New Energy Demand Gas)
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return energy_price_gas() * (gas_export() + new_energy_demand_gas())


@cache('step')
def completing_new_extraction_capacity_biofuels():
    """
    Real Name: Completing new extraction capacity Biofuels
    Original Eqn: DELAY N(MAX(0,New extraction capacity proposed Biofuels), Delay time new capacity Biofuels\ , Initial completing new extraction capacity Biofuels, Delay order new capacity Biofuels\ )
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return delay_npmaximum0new_extraction_capacity_proposed_biofuels_delay_time_new_capacity_biofuels_initial_completing_new_extraction_capacity_biofuels_delay_order_new_capacity_biofuels(
    )


@cache('step')
def completing_new_extraction_capacity_gas():
    """
    Real Name: Completing new extraction capacity Gas
    Original Eqn: DELAY N(MAX(0,New extraction capacity proposed Gas), Delay time new capacity Gas, Initial completing new extraction capacity Gas\ , Delay order new capacity Gas)
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return delay_npmaximum0new_extraction_capacity_proposed_gas_delay_time_new_capacity_gas_initial_completing_new_extraction_capacity_gas_delay_order_new_capacity_gas(
    )


@cache('run')
def initial_completing_new_extraction_capacity_other_renewables():
    """
    Real Name: Initial completing new extraction capacity other Renewables
    Original Eqn: 64231.8
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: constant


    """
    return 64231.8


@cache('run')
def initial_completing_new_extraction_capacity_gas():
    """
    Real Name: Initial completing new extraction capacity Gas
    Original Eqn: 0
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def initial_completing_new_extraction_capacity_coal():
    """
    Real Name: Initial completing new extraction capacity Coal
    Original Eqn: 0
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def completing_new_extraction_capacity_coal():
    """
    Real Name: Completing new extraction capacity Coal
    Original Eqn: DELAY N(MAX(0,New extraction capacity proposed Coal), Delay time new capacity Coal, \ Initial completing new extraction capacity Coal, Delay order new capacity Coal)
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return delay_npmaximum0new_extraction_capacity_proposed_coal_delay_time_new_capacity_coal_initial_completing_new_extraction_capacity_coal_delay_order_new_capacity_coal(
    )


@cache('run')
def storage_goal():
    """
    Real Name: Storage goal
    Original Eqn: 0
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def average_throughput_time_stocks_oil():
    """
    Real Name: Average throughput time stocks Oil
    Original Eqn: 0.1
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 0.1


@cache('step')
def current_energy_supply_distribution_oil():
    """
    Real Name: Current Energy Supply Distribution Oil
    Original Eqn: ZIDZ(Available resources from stocks Oil, Total Energy Supply)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(available_resources_from_stocks_oil(), total_energy_supply())


@cache('run')
def russian_gas():
    """
    Real Name: Russian Gas
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def total_energy_supply():
    """
    Real Name: Total Energy Supply
    Original Eqn: Available Gas+Available resources from stocks Biofuels+Available resources from stocks Coal\ +Available resources from stocks Oil +Extraction capacity installed other Renewables+Extraction capacity installed Nuclear
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return available_gas() + available_resources_from_stocks_biofuels(
    ) + available_resources_from_stocks_coal() + available_resources_from_stocks_oil(
    ) + extraction_capacity_installed_other_renewables() + extraction_capacity_installed_nuclear()


@cache('step')
def current_energy_supply_distribution_biofuels():
    """
    Real Name: Current Energy Supply Distribution Biofuels
    Original Eqn: ZIDZ(Available resources from stocks Biofuels, Total Energy Supply )
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(available_resources_from_stocks_biofuels(), total_energy_supply())


@cache('step')
def current_energy_supply_distribution_coal():
    """
    Real Name: Current Energy Supply Distribution Coal
    Original Eqn: ZIDZ(Available resources from stocks Coal, Total Energy Supply)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(available_resources_from_stocks_coal(), total_energy_supply())


@cache('step')
def current_energy_supply_distribution_gas():
    """
    Real Name: Current Energy Supply Distribution Gas
    Original Eqn: ZIDZ(Available Gas, Total Energy Supply)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(available_gas(), total_energy_supply())


@cache('step')
def energy_export_biofuels():
    """
    Real Name: Energy export Biofuels
    Original Eqn: MIN(Total export Biofuels,Available resources from stocks Biofuels)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.minimum(total_export_biofuels(), available_resources_from_stocks_biofuels())


@cache('step')
def energy_export_coal():
    """
    Real Name: Energy export Coal
    Original Eqn: MIN(Total export Coal,Available resources from stocks Coal)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.minimum(total_export_coal(), available_resources_from_stocks_coal())


@cache('step')
def energy_export_oil():
    """
    Real Name: Energy export Oil
    Original Eqn: MIN(Available resources from stocks Oil, Total export Oil)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.minimum(available_resources_from_stocks_oil(), total_export_oil())


@cache('run')
def initial_eroi_resources_coal():
    """
    Real Name: Initial EROI resources Coal
    Original Eqn: 21.8043
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 21.8043


@cache('step')
def eroi_resources_coal():
    """
    Real Name: EROI resources Coal
    Original Eqn: INTEG ( Change in EROI due to reserve depletion Coal, Initial EROI resources Coal)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_eroi_resources_coal()


@cache('step')
def eroi_resources_gas():
    """
    Real Name: EROI resources Gas
    Original Eqn: INTEG ( Change in EROI due to reserve depletion Gas, Initial EROI Gas)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_eroi_resources_gas()


@cache('step')
def eroi_resources_oil():
    """
    Real Name: EROI resources Oil
    Original Eqn: INTEG ( Change in EROI due to reserve depletion Oil, Initial EROI resources Oil)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_eroi_resources_oil()


@cache('run')
def initial_average_normalised_learning_curve_on_costs_biofuels():
    """
    Real Name: Initial average normalised learning curve on costs Biofuels
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('run')
def initial_average_normalised_learning_curve_on_costs_nuclear():
    """
    Real Name: Initial average normalised learning curve on costs Nuclear
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('run')
def initial_eroi_gas():
    """
    Real Name: Initial EROI Gas
    Original Eqn: 35.9938
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 35.9938


@cache('step')
def average_normalised_learning_curve_on_costs_biofuels():
    """
    Real Name: Average normalised learning curve on costs Biofuels
    Original Eqn: INTEG ( Change in average learning curve parameter Biofuels, Initial average normalised learning curve on costs Biofuels)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_average_normalised_learning_curve_on_costs_biofuels()


@cache('run')
def initial_eroi_resources_oil():
    """
    Real Name: Initial EROI resources Oil
    Original Eqn: 34.8648
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 34.8648


@cache('step')
def average_normalised_learning_curve_on_costs_other_renewables():
    """
    Real Name: Average normalised learning curve on costs other Renewables
    Original Eqn: INTEG ( Change in average learning curve parameter other Renewables, Initial average normalised learning curve on costs other Renewables)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_average_normalised_learning_curve_on_costs_other_renewables()


@cache('run')
def initial_average_normalised_learning_curve_on_costs_other_renewables():
    """
    Real Name: Initial average normalised learning curve on costs other Renewables
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def average_normalised_learning_curve_on_costs_nuclear():
    """
    Real Name: Average normalised learning curve on costs Nuclear
    Original Eqn: INTEG ( Change in average learning curve parameter Nuclear, Initial average normalised learning curve on costs Nuclear)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_average_normalised_learning_curve_on_costs_nuclear()


@cache('run')
def region():
    """
    Real Name: Region
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def autonomous_economic_growth():
    """
    Real Name: Autonomous Economic Growth
    Original Eqn: Autonomous Economic Growth Factor*IF THEN ELSE(Autonomous Economic Growth Patern Switch\ = 1, Autonomous Economic Growth Patern 1, Autonomous Economic Growth Patern 2)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return autonomous_economic_growth_factor() * functions.if_then_else(
        autonomous_economic_growth_patern_switch() == 1, autonomous_economic_growth_patern_1(),
        autonomous_economic_growth_patern_2())


@cache('run')
def autonomous_economic_growth_factor():
    """
    Real Name: Autonomous Economic Growth Factor
    Original Eqn: 0.016
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.016


@cache('run')
def autonomous_economic_growth_patern_1():
    """
    Real Name: Autonomous Economic Growth Patern 1
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def autonomous_economic_growth_patern_2():
    """
    Real Name: Autonomous Economic Growth Patern 2
    Original Eqn: 0.3+SIN(Time/One Year)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return 0.3 + np.sin(time() / one_year())


@cache('run')
def autonomous_economic_growth_patern_switch():
    """
    Real Name: Autonomous Economic Growth Patern Switch
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def increase_in_gdp():
    """
    Real Name: Increase in GDP
    Original Eqn: GDP*(Autonomous Economic Growth-Limitations Economic Growth due to Energy Shortage)
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return gdp() * (
        autonomous_economic_growth() - limitations_economic_growth_due_to_energy_shortage())


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_biofuels2():
    """
    Real Name: Initial normalised costs relative in relation to learning effects Biofuels2
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('step')
def cost_development_learning_curve_nuclear():
    """
    Real Name: Cost development learning curve Nuclear
    Original Eqn: Normalised costs relative in relation to learning effects t1 Nuclear/Initial normalised costs relative in relation to learning effects Nuclear2
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_nuclear(
    ) / initial_normalised_costs_relative_in_relation_to_learning_effects_nuclear2()


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_other_renewables2():
    """
    Real Name: Initial normalised costs relative in relation to learning effects other Renewables2
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_nuclear2():
    """
    Real Name: Initial normalised costs relative in relation to learning effects Nuclear2
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('run')
def variance_power():
    """
    Real Name: Variance power
    Original Eqn: -1
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Value between -5.0 and -0.1
    """
    return -1


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_biofuels():
    """
    Real Name: Initial normalised costs relative in relation to learning effects Biofuels
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_other_renewables():
    """
    Real Name: Initial normalised costs relative in relation to learning effects other Renewables
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('run')
def initial_normalised_costs_relative_in_relation_to_learning_effects_nuclear():
    """
    Real Name: Initial normalised costs relative in relation to learning effects Nuclear
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('step')
def normalized_relation_between_costs_and_income_other_renewables():
    """
    Real Name: Normalized relation between costs and income other Renewables
    Original Eqn: IF THEN ELSE( Total costs energy supply other Renewables>0, ZIDZ(Total income energy supply other Renewables\ -Total costs energy supply other Renewables,Total costs energy supply other Renewables\ +Total income energy supply other Renewables), 0)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        total_costs_energy_supply_other_renewables() > 0,
        functions.zidz(
            total_income_energy_supply_other_renewables() -
            total_costs_energy_supply_other_renewables(),
            total_costs_energy_supply_other_renewables() +
            total_income_energy_supply_other_renewables()), 0)


@cache('run')
def average_eroei_energy_sources_lognormal():
    """
    Real Name: Average EROEI energy sources lognormal
    Original Eqn: 40
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('step')
def cumulative_extracted_fuel_t1_biofuels():
    """
    Real Name: Cumulative extracted fuel t1 Biofuels
    Original Eqn: DELAY N(Cumulative extracted fuel Biofuels, Short forecasting period, Initial cumulative extraction fuel Biofuels\ , Delay order forecasts)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return delay_cumulative_extracted_fuel_biofuels_short_forecasting_period_initial_cumulative_extraction_fuel_biofuels_delay_order_forecasts(
    )


@cache('run')
def potential_eroei_biofuels():
    """
    Real Name: Potential EROEI Biofuels
    Original Eqn: 50
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 50


@cache('run')
def potential_eroei_other_renewables():
    """
    Real Name: Potential EROEI other Renewables
    Original Eqn: 30
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 30


@cache('step')
def cumulative_extracted_fuel_nuclear():
    """
    Real Name: Cumulative extracted fuel Nuclear
    Original Eqn: INTEG ( Extraction capacity installed Nuclear, Initial cumulative extraction fuel Nuclear)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_cumulative_extracted_fuel_nuclear()


@cache('run')
def supply_elasticity_nuclear():
    """
    Real Name: Supply elasticity Nuclear
    Original Eqn: 0.0116461
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.0116461


@cache('run')
def initial_unit_costs_biofuels():
    """
    Real Name: Initial unit costs Biofuels
    Original Eqn: 31919.7
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 31919.7


@cache('run')
def initial_unit_costs_coal():
    """
    Real Name: Initial unit costs Coal
    Original Eqn: 1615.2
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 1615.2


@cache('step')
def change_in_average_learning_curve_parameter_biofuels():
    """
    Real Name: Change in average learning curve parameter Biofuels
    Original Eqn: (Cost development learning curve Biofuels-Average normalised learning curve on costs Biofuels\ )/One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (cost_development_learning_curve_biofuels() -
            average_normalised_learning_curve_on_costs_biofuels()) / one_year()


@cache('step')
def change_in_average_learning_curve_parameter_other_renewables():
    """
    Real Name: Change in average learning curve parameter other Renewables
    Original Eqn: (Cost development learning curve other Renewables-Average normalised learning curve on costs other Renewables\ )/One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (cost_development_learning_curve_other_renewables() -
            average_normalised_learning_curve_on_costs_other_renewables()) / one_year()


@cache('step')
def change_in_average_learning_curve_parameter_nuclear():
    """
    Real Name: Change in average learning curve parameter Nuclear
    Original Eqn: (Cost development learning curve Nuclear-Average normalised learning curve on costs Nuclear\ )/One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (cost_development_learning_curve_nuclear() -
            average_normalised_learning_curve_on_costs_nuclear()) / one_year()


@cache('step')
def change_in_cumulative_extracted_fuel_biofuels():
    """
    Real Name: Change in cumulative extracted fuel Biofuels
    Original Eqn: ZIDZ(Cumulative extracted fuel Biofuels-Cumulative extracted fuel t1 Biofuels,Cumulative extracted fuel Biofuels\ )/One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(
        cumulative_extracted_fuel_biofuels() - cumulative_extracted_fuel_t1_biofuels(),
        cumulative_extracted_fuel_biofuels()) / one_year()


@cache('step')
def change_in_cumulative_extracted_fuel_other_renewables():
    """
    Real Name: Change in cumulative extracted fuel other Renewables
    Original Eqn: ZIDZ(Cumulative extracted fuel other Renewables-Cumulative extracted fuel t1 other Renewables\ ,Cumulative extracted fuel other Renewables)/One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(
        cumulative_extracted_fuel_other_renewables() -
        cumulative_extracted_fuel_t1_other_renewables(),
        cumulative_extracted_fuel_other_renewables()) / one_year()


@cache('step')
def change_in_eroei_biofuels():
    """
    Real Name: Change in EROEI Biofuels
    Original Eqn: EROEI Biofuels*Change in cumulative extracted fuel Biofuels*Relative potential EROEI Biofuels
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return eroei_biofuels() * change_in_cumulative_extracted_fuel_biofuels(
    ) * relative_potential_eroei_biofuels()


@cache('step')
def change_in_eroei_other_renewables():
    """
    Real Name: Change in EROEI other Renewables
    Original Eqn: EROEI other Renewables*Change in cumulative extracted fuel other Renewables*Relative potential EROEI other Renewables
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return eroei_other_renewables() * change_in_cumulative_extracted_fuel_other_renewables(
    ) * relative_potential_eroei_other_renewables()


@cache('step')
def change_in_eroi_due_to_reserve_depletion_coal():
    """
    Real Name: Change in EROI due to reserve depletion Coal
    Original Eqn: (EROEI Coal-EROI resources Coal)/One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (eroei_coal() - eroi_resources_coal()) / one_year()


@cache('step')
def change_in_eroi_due_to_reserve_depletion_gas():
    """
    Real Name: Change in EROI due to reserve depletion Gas
    Original Eqn: (EROEI Gas-EROI resources Gas)/One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (eroei_gas() - eroi_resources_gas()) / one_year()


@cache('step')
def change_in_eroi_due_to_reserve_depletion_oil():
    """
    Real Name: Change in EROI due to reserve depletion Oil
    Original Eqn: (EROEI Oil-EROI resources Oil)/One Year
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (eroei_oil() - eroi_resources_oil()) / one_year()


@cache('step')
def change_in_normalized_relative_profits_biofuels():
    """
    Real Name: Change in normalized relative profits Biofuels
    Original Eqn: (Normalized relation between costs and income Biofuels - Long term normalized profits Biofuels\ )/Long term profits energy supply period Biofuels
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (normalized_relation_between_costs_and_income_biofuels() -
            long_term_normalized_profits_biofuels()
            ) / long_term_profits_energy_supply_period_biofuels()


@cache('step')
def change_in_normalized_relative_profits_coal():
    """
    Real Name: Change in normalized relative profits Coal
    Original Eqn: (Normalized relation between costs and income Coal - Long term normalized profits Coal\ )/Long term profits energy supply period Coal
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (normalized_relation_between_costs_and_income_coal() -
            long_term_normalized_profits_coal()) / long_term_profits_energy_supply_period_coal()


@cache('step')
def change_in_normalized_relative_profits_gas():
    """
    Real Name: Change in normalized relative profits Gas
    Original Eqn: (Normalized relation between costs and income Gas - Long term normalized profits Gas\ )/Long term profits energy supply period Gas
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (normalized_relation_between_costs_and_income_gas() -
            long_term_normalized_profits_gas()) / long_term_profits_energy_supply_period_gas()


@cache('step')
def change_in_normalized_relative_profits_oil():
    """
    Real Name: Change in normalized relative profits Oil
    Original Eqn: (Normalized relation between costs and income Oil - Long term normalized profits Oil\ )/Long term profits energy supply period Oil
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (normalized_relation_between_costs_and_income_oil() -
            long_term_normalized_profits_oil()) / long_term_profits_energy_supply_period_oil()


@cache('step')
def change_in_normalized_relative_profits_other_renewables():
    """
    Real Name: Change in normalized relative profits other Renewables
    Original Eqn: (Normalized relation between costs and income other Renewables - Long term normalized profits other Renewables\ )/Long term profits energy supply period other Renewables
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (normalized_relation_between_costs_and_income_other_renewables() -
            long_term_normalized_profits_other_renewables()
            ) / long_term_profits_energy_supply_period_other_renewables()


@cache('step')
def change_in_normalized_relative_profits_nuclear():
    """
    Real Name: Change in normalized relative profits Nuclear
    Original Eqn: (Normalized relation between costs and income Nuclear - Long term normalized profits Nuclear\ )/Long term profits energy supply period Nuclear
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return (
        normalized_relation_between_costs_and_income_nuclear() -
        long_term_normalized_profits_nuclear()) / long_term_profits_energy_supply_period_nuclear()


@cache('step')
def change_in_short_term_supply_biofuels():
    """
    Real Name: Change in short term supply Biofuels
    Original Eqn: Maximum relative mothballing Biofuels*Normalized relation between costs and income Biofuels
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return maximum_relative_mothballing_biofuels(
    ) * normalized_relation_between_costs_and_income_biofuels()


@cache('step')
def change_in_short_term_supply_coal():
    """
    Real Name: Change in short term supply Coal
    Original Eqn: Maximum relative mothballing Coal*Normalized relation between costs and income Coal
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return maximum_relative_mothballing_coal() * normalized_relation_between_costs_and_income_coal(
    )


@cache('step')
def change_in_short_term_supply_gas():
    """
    Real Name: Change in short term supply Gas
    Original Eqn: Maximum relative mothballing Gas*Normalized relation between costs and income Gas
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return maximum_relative_mothballing_gas() * normalized_relation_between_costs_and_income_gas()


@cache('step')
def change_in_short_term_supply_oil():
    """
    Real Name: Change in short term supply Oil
    Original Eqn: Maximum relative mothballing Oil*Normalized relation between costs and income Oil
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return maximum_relative_mothballing_oil() * normalized_relation_between_costs_and_income_oil()


@cache('step')
def change_in_short_term_supply_other_renewables():
    """
    Real Name: Change in short term supply other Renewables
    Original Eqn: Maximum relative mothballing other Renewables*Normalized relation between costs and income other Renewables
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return maximum_relative_mothballing_other_renewables(
    ) * normalized_relation_between_costs_and_income_other_renewables()


@cache('step')
def change_in_short_term_supply_nuclear():
    """
    Real Name: Change in short term supply Nuclear
    Original Eqn: Maximum relative mothballing Nuclear*Normalized relation between costs and income Nuclear
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return maximum_relative_mothballing_nuclear(
    ) * normalized_relation_between_costs_and_income_nuclear()


@cache('step')
def change_in_unit_costs_biofuels():
    """
    Real Name: Change in unit costs Biofuels
    Original Eqn: (Relative change in costs due to learning Biofuels-Relative change in EROI Biofuels)\ *Unit costs Biofuels
    Units: Dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (relative_change_in_costs_due_to_learning_biofuels() -
            relative_change_in_eroi_biofuels()) * unit_costs_biofuels()


@cache('step')
def change_in_unit_costs_coal():
    """
    Real Name: Change in unit costs Coal
    Original Eqn: -Relative change in EROEI Coal*Unit costs Coal
    Units: Dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return -relative_change_in_eroei_coal() * unit_costs_coal()


@cache('step')
def change_in_unit_costs_gas():
    """
    Real Name: Change in unit costs Gas
    Original Eqn: -Relative change in EROEI Gas*Unit costs Gas
    Units: Dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return -relative_change_in_eroei_gas() * unit_costs_gas()


@cache('step')
def change_in_unit_costs_oil():
    """
    Real Name: Change in unit costs Oil
    Original Eqn: -Relative change in EROEI Oil*Unit costs Oil
    Units: Dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return -relative_change_in_eroei_oil() * unit_costs_oil()


@cache('step')
def change_in_unit_costs_other_renewables():
    """
    Real Name: Change in unit costs other Renewables
    Original Eqn: (Relative change in costs due to learning other Renewables-Relative change in EROI other Renewables\ )*Unit costs other Renewables
    Units: Dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (relative_change_in_costs_due_to_learning_other_renewables() -
            relative_change_in_eroi_other_renewables()) * unit_costs_other_renewables()


@cache('step')
def change_in_unit_costs_nuclear():
    """
    Real Name: Change in unit costs Nuclear
    Original Eqn: Relative change in costs due to learning Nuclear*Unit costs Nuclear
    Units: Dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return relative_change_in_costs_due_to_learning_nuclear() * unit_costs_nuclear()


@cache('step')
def math_erf_inv_coal():
    """
    Real Name: MATH erf inv Coal
    Original Eqn: MATH sgn erf input Coal*(-MATH 2 over Pi times a-MATH LN 1 minus x squared Coal/2+SQRT\ ((MATH 2 over Pi times a+MATH LN 1 minus x squared Coal/2)^2-1/MATH a*MATH LN 1 minus x squared Coal\ ))^(1/2)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return math_sgn_erf_input_coal() * (
        -math_2_over_pi_times_a() - math_ln_1_minus_x_squared_coal() / 2 + np.sqrt(
            (math_2_over_pi_times_a() + math_ln_1_minus_x_squared_coal() / 2)**2 -
            1 / math_a() * math_ln_1_minus_x_squared_coal()))**(1 / 2)


@cache('step')
def math_erf_inv_gas():
    """
    Real Name: MATH erf inv Gas
    Original Eqn: MATH sgn erf input Gas*(-MATH 2 over Pi times a-MATH LN 1 minus x squared Gas/2+SQRT\ ((MATH 2 over Pi times a+MATH LN 1 minus x squared Gas/2)^2-1/MATH a*MATH LN 1 minus x squared Gas\ ))^(1/2)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return math_sgn_erf_input_gas() * (
        -math_2_over_pi_times_a() - math_ln_1_minus_x_squared_gas() / 2 + np.sqrt(
            (math_2_over_pi_times_a() + math_ln_1_minus_x_squared_gas() / 2)**2 -
            1 / math_a() * math_ln_1_minus_x_squared_gas()))**(1 / 2)


@cache('step')
def math_erf_inv_oil():
    """
    Real Name: MATH erf inv Oil
    Original Eqn: MATH sgn erf input Oil*(-MATH 2 over Pi times a-MATH LN 1 minus x squared Oil/2+SQRT\ ((MATH 2 over Pi times a+MATH LN 1 minus x squared Oil/2)^2-1/MATH a*MATH LN 1 minus x squared Oil\ ))^(1/2)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return math_sgn_erf_input_oil() * (
        -math_2_over_pi_times_a() - math_ln_1_minus_x_squared_oil() / 2 + np.sqrt(
            (math_2_over_pi_times_a() + math_ln_1_minus_x_squared_oil() / 2)**2 -
            1 / math_a() * math_ln_1_minus_x_squared_oil()))**(1 / 2)


@cache('step')
def math_ln_1_minus_x_squared_coal():
    """
    Real Name: MATH LN 1 minus x squared Coal
    Original Eqn: LN(1-IF THEN ELSE(MATH erf input Coal=1, 0, IF THEN ELSE(MATH erf input Coal=-1, 0 ,\ (MATH erf input Coal^2))))
    Units: Dmnl
    Limits: (None, None)
    Type: component

    IF THEN ELSE(MATH erf input Coal = 1, 0, IF THEN ELSE(MATH erf input Coal 
        = -1, 0, LN(1-(MATH erf input Coal^2))))
    """
    return np.log(1 - functions.if_then_else(
        math_erf_input_coal() == 1, 0,
        functions.if_then_else(math_erf_input_coal() == -1, 0, (math_erf_input_coal()**2))))


@cache('step')
def math_ln_1_minus_x_squared_gas():
    """
    Real Name: MATH LN 1 minus x squared Gas
    Original Eqn: LN(1 - IF THEN ELSE(MATH erf input Gas=1, 0, IF THEN ELSE(MATH erf input Gas=-1, 0, \ MATH erf input Gas^2)))
    Units: Dmnl
    Limits: (None, None)
    Type: component

    IF THEN ELSE(MATH erf input Gas = 1, 0, IF THEN ELSE(MATH erf input Gas = 
        -1, 0, LN(1-(MATH erf input Gas^2))))
    """
    return np.log(1 - functions.if_then_else(
        math_erf_input_gas() == 1, 0,
        functions.if_then_else(math_erf_input_gas() == -1, 0,
                               math_erf_input_gas()**2)))


@cache('step')
def math_ln_1_minus_x_squared_oil():
    """
    Real Name: MATH LN 1 minus x squared Oil
    Original Eqn: LN(1 - IF THEN ELSE(MATH erf input Oil=1, 0, IF THEN ELSE(MATH erf input Oil=-1, 0, \ MATH erf input Oil^2)))
    Units: Dmnl
    Limits: (None, None)
    Type: component

    IF THEN ELSE(MATH erf input Oil = 1, 0, IF THEN ELSE(MATH erf input Oil = 
        -1, 0,  LN(1-(MATH erf input Oil^2))))
    """
    return np.log(1 - functions.if_then_else(
        math_erf_input_oil() == 1, 0,
        functions.if_then_else(math_erf_input_oil() == -1, 0,
                               math_erf_input_oil()**2)))


@cache('step')
def math_mu_fossil_fuels():
    """
    Real Name: MATH mu fossil fuels
    Original Eqn: LN( (Relative crustal abundance fossil fuels^2)/(SQRT( Variance in EROEI distribution\ + (Relative crustal abundance fossil fuels^2))))
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return np.log((relative_crustal_abundance_fossil_fuels()**2) /
                  (np.sqrt(variance_in_eroei_distribution() +
                           (relative_crustal_abundance_fossil_fuels()**2))))


@cache('run')
def math_pi():
    """
    Real Name: MATH Pi
    Original Eqn: 3.14159
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3.14159


@cache('step')
def math_sgn_erf_input_coal():
    """
    Real Name: MATH sgn erf input Coal
    Original Eqn: IF THEN ELSE(MATH erf input Coal>0, -1, IF THEN ELSE( MATH erf input Coal<0, 1, 0))
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(math_erf_input_coal() > 0, -1,
                                  functions.if_then_else(math_erf_input_coal() < 0, 1, 0))


@cache('step')
def math_sgn_erf_input_gas():
    """
    Real Name: MATH sgn erf input Gas
    Original Eqn: IF THEN ELSE(MATH erf input Gas>0, -1, IF THEN ELSE( MATH erf input Gas<0, 1, 0))
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(math_erf_input_gas() > 0, -1,
                                  functions.if_then_else(math_erf_input_gas() < 0, 1, 0))


@cache('step')
def math_sgn_erf_input_oil():
    """
    Real Name: MATH sgn erf input Oil
    Original Eqn: IF THEN ELSE(MATH erf input Oil>0, -1, IF THEN ELSE( MATH erf input Oil<0, 1, 0))
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(math_erf_input_oil() > 0, -1,
                                  functions.if_then_else(math_erf_input_oil() < 0, 1, 0))


@cache('step')
def cost_development_learning_curve_biofuels():
    """
    Real Name: Cost development learning curve Biofuels
    Original Eqn: Normalised costs relative in relation to learning effects t1 Biofuels/Initial normalised costs relative in relation to learning effects Biofuels2
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_biofuels(
    ) / initial_normalised_costs_relative_in_relation_to_learning_effects_biofuels2()


@cache('step')
def cost_development_learning_curve_other_renewables():
    """
    Real Name: Cost development learning curve other Renewables
    Original Eqn: Normalised costs relative in relation to learning effects t1 other Renewables/Initial normalised costs relative in relation to learning effects other Renewables2
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_other_renewables(
    ) / initial_normalised_costs_relative_in_relation_to_learning_effects_other_renewables2()


@cache('run')
def maximum_relative_mothballing_biofuels():
    """
    Real Name: Maximum relative mothballing Biofuels
    Original Eqn: 0.3
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.3


@cache('step')
def cumulative_extracted_fuel_other_renewables():
    """
    Real Name: Cumulative extracted fuel other Renewables
    Original Eqn: INTEG ( Extraction capacity installed other Renewables, Initial cumulative extraction fuel other Renewables)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_cumulative_extracted_fuel_other_renewables()


@cache('step')
def cumulative_extracted_fuel_biofuels():
    """
    Real Name: Cumulative extracted fuel Biofuels
    Original Eqn: INTEG ( Extraction capacity installed Biofuels, Initial cumulative extraction fuel Biofuels)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_cumulative_extracted_fuel_biofuels()


@cache('step')
def cumulative_extracted_fuel_coal():
    """
    Real Name: Cumulative extracted fuel Coal
    Original Eqn: INTEG ( Extraction capacity installed Coal, Initial cumulative extraction fuel Coal)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_cumulative_extracted_fuel_coal()


@cache('step')
def cumulative_extracted_fuel_gas():
    """
    Real Name: Cumulative extracted fuel Gas
    Original Eqn: INTEG ( Extraction capacity installed Gas, Initial cumulative extraction fuel Gas)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_cumulative_extracted_fuel_gas()


@cache('step')
def cumulative_extracted_fuel_oil():
    """
    Real Name: Cumulative extracted fuel Oil
    Original Eqn: INTEG ( Extraction capacity installed Oil, Initial cumulative extraction fuel Oil)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_cumulative_extracted_fuel_oil()


@cache('run')
def supply_elasticity_biofuels():
    """
    Real Name: Supply elasticity Biofuels
    Original Eqn: 0.148704
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.148704


@cache('step')
def cumulative_extracted_fuel_t1_other_renewables():
    """
    Real Name: Cumulative extracted fuel t1 other Renewables
    Original Eqn: DELAY N(Cumulative extracted fuel other Renewables, Short forecasting period, Initial cumulative extraction fuel other Renewables\ , Delay order forecasts)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return delay_cumulative_extracted_fuel_other_renewables_short_forecasting_period_initial_cumulative_extraction_fuel_other_renewables_delay_order_forecasts(
    )


@cache('step')
def cumulative_extracted_fuel_t1_nuclear():
    """
    Real Name: Cumulative extracted fuel t1 Nuclear
    Original Eqn: DELAY N(Cumulative extracted fuel Nuclear, Short forecasting period, Initial cumulative extraction fuel Nuclear\ , Delay order forecasts)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return delay_cumulative_extracted_fuel_nuclear_short_forecasting_period_initial_cumulative_extraction_fuel_nuclear_delay_order_forecasts(
    )


@cache('run')
def supply_elasticity_oil():
    """
    Real Name: Supply elasticity Oil
    Original Eqn: 0.148704
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.148704


@cache('run')
def supply_elasticity_other_renewables():
    """
    Real Name: Supply elasticity other Renewables
    Original Eqn: 0.229605
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.229605


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_biofuels():
    """
    Real Name: Normalised costs relative in relation to learning effects Biofuels
    Original Eqn: Normalised costs relative in relation to learning t1 Biofuels*XIDZ(Cumulative extracted fuel Biofuels\ ,Cumulative extracted fuel t1 Biofuels,1)^Experience curve parameter extraction
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_t1_biofuels() * functions.xidz(
        cumulative_extracted_fuel_biofuels(), cumulative_extracted_fuel_t1_biofuels(),
        1)**experience_curve_parameter_extraction()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_other_renewables():
    """
    Real Name: Normalised costs relative in relation to learning effects other Renewables
    Original Eqn: Normalised costs relative in relation to learning t1 other Renewables*XIDZ( Cumulative extracted fuel other Renewables\ , Cumulative extracted fuel t1 other Renewables, 1)^Experience curve parameter extraction
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Normalised costs relative in relation to learning t1 other 
        Renewables*ZIDZ(Cumulative extracted fuel other Renewables, Cumulative 
        extracted fuel t1 other Renewables)^Experience curve parameter extraction
    """
    return normalised_costs_relative_in_relation_to_learning_t1_other_renewables(
    ) * functions.xidz(cumulative_extracted_fuel_other_renewables(),
                       cumulative_extracted_fuel_t1_other_renewables(),
                       1)**experience_curve_parameter_extraction()


@cache('step')
def mothballing_of_capacity_biofuels():
    """
    Real Name: Mothballing of capacity Biofuels
    Original Eqn: MAX(-Change in short term supply Biofuels, 0)*Extraction capacity installed Biofuels
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(-change_in_short_term_supply_biofuels(),
                      0) * extraction_capacity_installed_biofuels()


@cache('step')
def mothballing_of_capacity_coal():
    """
    Real Name: Mothballing of capacity Coal
    Original Eqn: MAX(-Change in short term supply Coal, 0)*Extraction capacity installed Coal
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(-change_in_short_term_supply_coal(),
                      0) * extraction_capacity_installed_coal()


@cache('step')
def mothballing_of_capacity_gas():
    """
    Real Name: Mothballing of capacity Gas
    Original Eqn: MAX(-Change in short term supply Gas, 0)*Extraction capacity installed Gas
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(-change_in_short_term_supply_gas(), 0) * extraction_capacity_installed_gas()


@cache('step')
def mothballing_of_capacity_oil():
    """
    Real Name: Mothballing of capacity Oil
    Original Eqn: MAX(-Change in short term supply Oil, 0)*Extraction capacity installed Oil
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(-change_in_short_term_supply_oil(), 0) * extraction_capacity_installed_oil()


@cache('step')
def mothballing_of_capacity_other_renewables():
    """
    Real Name: Mothballing of capacity other Renewables
    Original Eqn: MAX(-Change in short term supply other Renewables, 0)*Extraction capacity installed other Renewables
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(-change_in_short_term_supply_other_renewables(),
                      0) * extraction_capacity_installed_other_renewables()


@cache('step')
def mothballing_of_capacity_nuclear():
    """
    Real Name: Mothballing of capacity Nuclear
    Original Eqn: MAX(-Change in short term supply Nuclear, 0)*Extraction capacity installed Nuclear
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(-change_in_short_term_supply_nuclear(),
                      0) * extraction_capacity_installed_nuclear()


@cache('run')
def initial_cumulative_extraction_fuel_oil():
    """
    Real Name: Initial cumulative extraction fuel Oil
    Original Eqn: 1.75267e+08
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 1.75267e+08


@cache('run')
def initial_cumulative_extraction_fuel_other_renewables():
    """
    Real Name: Initial cumulative extraction fuel other Renewables
    Original Eqn: 1.60571e+07
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 1.60571e+07


@cache('run')
def initial_cumulative_extraction_fuel_nuclear():
    """
    Real Name: Initial cumulative extraction fuel Nuclear
    Original Eqn: 1.47936e+07
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 1.47936e+07


@cache('step')
def total_costs_energy_supply_gas():
    """
    Real Name: Total costs energy supply Gas
    Original Eqn: Extraction capacity installed Gas*Unit costs Gas
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return extraction_capacity_installed_gas() * unit_costs_gas()


@cache('step')
def total_costs_energy_supply_oil():
    """
    Real Name: Total costs energy supply Oil
    Original Eqn: Extraction capacity installed Oil*Unit costs Oil
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return extraction_capacity_installed_oil() * unit_costs_oil()


@cache('step')
def total_costs_energy_supply_other_renewables():
    """
    Real Name: Total costs energy supply other Renewables
    Original Eqn: Extraction capacity installed other Renewables*Unit costs other Renewables
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return extraction_capacity_installed_other_renewables() * unit_costs_other_renewables()


@cache('step')
def new_extraction_capacity_proposed_biofuels():
    """
    Real Name: New extraction capacity proposed Biofuels
    Original Eqn: new long term supply Biofuels*Extraction capacity installed Biofuels
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return new_long_term_supply_biofuels() * extraction_capacity_installed_biofuels()


@cache('step')
def new_extraction_capacity_proposed_coal():
    """
    Real Name: New extraction capacity proposed Coal
    Original Eqn: Extraction capacity installed Coal*new long term supply Coal
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return extraction_capacity_installed_coal() * new_long_term_supply_coal()


@cache('run')
def delay_order_forecasts():
    """
    Real Name: Delay order forecasts
    Original Eqn: 10
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 10


@cache('step')
def new_extraction_capacity_proposed_oil():
    """
    Real Name: New extraction capacity proposed Oil
    Original Eqn: Extraction capacity installed Oil*new long term supply Oil
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return extraction_capacity_installed_oil() * new_long_term_supply_oil()


@cache('step')
def new_extraction_capacity_proposed_other_renewables():
    """
    Real Name: New extraction capacity proposed other Renewables
    Original Eqn: new long term supply other Renewables*Extraction capacity installed other Renewables
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return new_long_term_supply_other_renewables(
    ) * extraction_capacity_installed_other_renewables()


@cache('step')
def new_extraction_capacity_proposed_nuclear():
    """
    Real Name: New extraction capacity proposed Nuclear
    Original Eqn: Extraction capacity installed Nuclear*new long term supply Nuclear
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return extraction_capacity_installed_nuclear() * new_long_term_supply_nuclear()


@cache('step')
def new_long_term_supply_biofuels():
    """
    Real Name: new long term supply Biofuels
    Original Eqn: MAX(Long term normalized profits Biofuels-Investment fraction normalized profits Biofuels\ , 0)*Supply elasticity Biofuels
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return np.maximum(
        long_term_normalized_profits_biofuels() -
        investment_fraction_normalized_profits_biofuels(), 0) * supply_elasticity_biofuels()


@cache('step')
def new_long_term_supply_coal():
    """
    Real Name: new long term supply Coal
    Original Eqn: MAX(Long term normalized profits Coal-Investment fraction normalized profits Coal, 0\ )*Supply elasticity Coal
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return np.maximum(
        long_term_normalized_profits_coal() - investment_fraction_normalized_profits_coal(),
        0) * supply_elasticity_coal()


@cache('step')
def new_long_term_supply_gas():
    """
    Real Name: new long term supply Gas
    Original Eqn: MAX(Long term normalized profits Gas-Investment fraction normalized profits Gas, 0)*\ Supply elasticity Gas
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return np.maximum(
        long_term_normalized_profits_gas() - investment_fraction_normalized_profits_gas(),
        0) * supply_elasticity_gas()


@cache('step')
def new_long_term_supply_oil():
    """
    Real Name: new long term supply Oil
    Original Eqn: MAX(Long term normalized profits Oil-Investment fraction normalized profits Oil, 0)*\ Supply elasticity Oil
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return np.maximum(
        long_term_normalized_profits_oil() - investment_fraction_normalized_profits_oil(),
        0) * supply_elasticity_oil()


@cache('step')
def new_long_term_supply_other_renewables():
    """
    Real Name: new long term supply other Renewables
    Original Eqn: MAX(Long term normalized profits other Renewables-Investment fraction normalized profits other Renewables\ , 0)*Supply elasticity other Renewables
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return np.maximum(
        long_term_normalized_profits_other_renewables() -
        investment_fraction_normalized_profits_other_renewables(),
        0) * supply_elasticity_other_renewables()


@cache('step')
def new_long_term_supply_nuclear():
    """
    Real Name: new long term supply Nuclear
    Original Eqn: MAX(Long term normalized profits Nuclear-Investment fraction normalized profits Nuclear\ , 0)*Supply elasticity Nuclear
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return np.maximum(
        long_term_normalized_profits_nuclear() - investment_fraction_normalized_profits_nuclear(),
        0) * supply_elasticity_nuclear()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_t1_other_renewables():
    """
    Real Name: Normalised costs relative in relation to learning effects t1 other Renewables
    Original Eqn: INTEG \ ( Normalised costs relative in relation to learning effects other Renewables-Normalised costs relative in relation to learning t1 other Renewables\ , Initial normalised costs relative in relation to learning effects other Renewables)
    Units: year
    Limits: (None, None)
    Type: component


    """
    return integ_normalised_costs_relative_in_relation_to_learning_effects_t1_other_renewables()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_t1_biofuels():
    """
    Real Name: Normalised costs relative in relation to learning effects t1 Biofuels
    Original Eqn: INTEG ( Normalised costs relative in relation to learning effects Biofuels-Normalised costs relative in relation to learning t1 Biofuels\ , Initial normalised costs relative in relation to learning effects Biofuels)
    Units: year
    Limits: (None, None)
    Type: component


    """
    return integ_normalised_costs_relative_in_relation_to_learning_effects_t1_biofuels()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_t1_nuclear():
    """
    Real Name: Normalised costs relative in relation to learning effects t1 Nuclear
    Original Eqn: INTEG ( Normalised costs relative in relation to learning effects Nuclear-Normalised costs relative in relation to learning t1 Nuclear\ , Initial normalised costs relative in relation to learning effects Nuclear)
    Units: year
    Limits: (None, None)
    Type: component


    """
    return integ_normalised_costs_relative_in_relation_to_learning_effects_t1_nuclear()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_effects_nuclear():
    """
    Real Name: Normalised costs relative in relation to learning effects Nuclear
    Original Eqn: Normalised costs relative in relation to learning t1 Nuclear*XIDZ( Cumulative extracted fuel Nuclear\ , Cumulative extracted fuel t1 Nuclear, 1)^Experience curve parameter extraction
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_t1_nuclear() * functions.xidz(
        cumulative_extracted_fuel_nuclear(), cumulative_extracted_fuel_t1_nuclear(),
        1)**experience_curve_parameter_extraction()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_t1_biofuels():
    """
    Real Name: Normalised costs relative in relation to learning t1 Biofuels
    Original Eqn: Normalised costs relative in relation to learning effects t1 Biofuels/Summed delay time new capacity
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_biofuels(
    ) / summed_delay_time_new_capacity()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_t1_other_renewables():
    """
    Real Name: Normalised costs relative in relation to learning t1 other Renewables
    Original Eqn: Normalised costs relative in relation to learning effects t1 other Renewables/Summed delay time new capacity
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_other_renewables(
    ) / summed_delay_time_new_capacity()


@cache('step')
def normalised_costs_relative_in_relation_to_learning_t1_nuclear():
    """
    Real Name: Normalised costs relative in relation to learning t1 Nuclear
    Original Eqn: Normalised costs relative in relation to learning effects t1 Nuclear/Summed delay time new capacity
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalised_costs_relative_in_relation_to_learning_effects_t1_nuclear(
    ) / summed_delay_time_new_capacity()


@cache('run')
def initial_long_term_normalized_profits_nuclear():
    """
    Real Name: Initial long term normalized profits Nuclear
    Original Eqn: 0.162188
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.162188


@cache('step')
def unit_costs_gas():
    """
    Real Name: Unit costs Gas
    Original Eqn: INTEG ( Change in unit costs Gas, Initial unit costs Gas)
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_unit_costs_gas()


@cache('step')
def unit_costs_oil():
    """
    Real Name: Unit costs Oil
    Original Eqn: INTEG ( Change in unit costs Oil, Initial unit costs Oil)
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_unit_costs_oil()


@cache('step')
def unit_costs_other_renewables():
    """
    Real Name: Unit costs other Renewables
    Original Eqn: INTEG ( Change in unit costs other Renewables, Initial unit costs other Renewables)
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_unit_costs_other_renewables()


@cache('step')
def unit_costs_nuclear():
    """
    Real Name: Unit costs Nuclear
    Original Eqn: INTEG ( Change in unit costs Nuclear, Initial unit costs Nuclear)
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_unit_costs_nuclear()


@cache('step')
def variance_in_eroei_distribution():
    """
    Real Name: Variance in EROEI distribution
    Original Eqn: Relative crustal abundance fossil fuels*Relative variance in EROEI distribution
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return relative_crustal_abundance_fossil_fuels() * relative_variance_in_eroei_distribution()


@cache('step')
def normalized_relation_between_costs_and_income_biofuels():
    """
    Real Name: Normalized relation between costs and income Biofuels
    Original Eqn: IF THEN ELSE( Total costs energy supply Biofuels>0, ZIDZ(Total income energy supply Biofuels\ -Total costs energy supply Biofuels,Total costs energy supply Biofuels+Total income energy supply Biofuels\ ), 0)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        total_costs_energy_supply_biofuels() > 0,
        functions.zidz(
            total_income_energy_supply_biofuels() - total_costs_energy_supply_biofuels(),
            total_costs_energy_supply_biofuels() + total_income_energy_supply_biofuels()), 0)


@cache('step')
def normalized_relation_between_costs_and_income_coal():
    """
    Real Name: Normalized relation between costs and income Coal
    Original Eqn: IF THEN ELSE( Total costs energy supply Coal>0, ZIDZ(Total income energy supply Coal\ -Total costs energy supply Coal,Total costs energy supply Coal+Total income energy supply Coal\ ), 0)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        total_costs_energy_supply_coal() > 0,
        functions.zidz(total_income_energy_supply_coal() - total_costs_energy_supply_coal(),
                       total_costs_energy_supply_coal() + total_income_energy_supply_coal()), 0)


@cache('step')
def normalized_relation_between_costs_and_income_gas():
    """
    Real Name: Normalized relation between costs and income Gas
    Original Eqn: IF THEN ELSE( Total costs energy supply Gas>0, ZIDZ(Total income energy supply Gas-Total costs energy supply Gas\ ,Total costs energy supply Gas+Total income energy supply Gas), 0)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        total_costs_energy_supply_gas() > 0,
        functions.zidz(total_income_energy_supply_gas() - total_costs_energy_supply_gas(),
                       total_costs_energy_supply_gas() + total_income_energy_supply_gas()), 0)


@cache('step')
def normalized_relation_between_costs_and_income_oil():
    """
    Real Name: Normalized relation between costs and income Oil
    Original Eqn: IF THEN ELSE( Total costs energy supply Oil>0, ZIDZ(Total income energy supply Oil-Total costs energy supply Oil\ ,Total costs energy supply Oil+Total income energy supply Oil), 0)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        total_costs_energy_supply_oil() > 0,
        functions.zidz(total_income_energy_supply_oil() - total_costs_energy_supply_oil(),
                       total_costs_energy_supply_oil() + total_income_energy_supply_oil()), 0)


@cache('run')
def maximum_relative_mothballing_coal():
    """
    Real Name: Maximum relative mothballing Coal
    Original Eqn: 0.3
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.3


@cache('step')
def normalized_relation_between_costs_and_income_nuclear():
    """
    Real Name: Normalized relation between costs and income Nuclear
    Original Eqn: IF THEN ELSE( Total costs energy supply Nuclear>0, ZIDZ(Total income energy supply Nuclear\ -Total costs energy supply Nuclear,Total costs energy supply Nuclear+Total income energy supply Nuclear\ ), 0)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        total_costs_energy_supply_nuclear() > 0,
        functions.zidz(total_income_energy_supply_nuclear() - total_costs_energy_supply_nuclear(),
                       total_costs_energy_supply_nuclear() + total_income_energy_supply_nuclear()),
        0)


@cache('run')
def short_forecasting_period():
    """
    Real Name: Short forecasting period
    Original Eqn: 1.85342
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 1.85342


@cache('run')
def summed_delay_time_new_capacity():
    """
    Real Name: Summed delay time new capacity
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 40


@cache('run')
def maximum_relative_mothballing_other_renewables():
    """
    Real Name: Maximum relative mothballing other Renewables
    Original Eqn: 0.3
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.3


@cache('run')
def supply_elasticity_coal():
    """
    Real Name: Supply elasticity Coal
    Original Eqn: 0.14
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.14


@cache('run')
def supply_elasticity_gas():
    """
    Real Name: Supply elasticity Gas
    Original Eqn: 0.0649225
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.0649225


@cache('step')
def relative_crustal_abundance_fossil_fuels():
    """
    Real Name: Relative crustal abundance fossil fuels
    Original Eqn: (Average EROEI energy sources lognormal-Minimum EROEI)/(Maximum EROEI-Minimum EROEI)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return (average_eroei_energy_sources_lognormal() - minimum_eroei()) / (
        maximum_eroei() - minimum_eroei())


@cache('step')
def relative_eroi_coal():
    """
    Real Name: Relative EROI Coal
    Original Eqn: EXP(MATH mu fossil fuels+MATH sigma fossil fuels * SQRT ( 2) *MATH erf inv Coal)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return np.exp(math_mu_fossil_fuels() +
                  math_sigma_fossil_fuels() * np.sqrt(2) * math_erf_inv_coal())


@cache('step')
def relative_eroi_gas():
    """
    Real Name: Relative EROI Gas
    Original Eqn: EXP(MATH mu fossil fuels+MATH sigma fossil fuels * SQRT ( 2) *MATH erf inv Gas)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return np.exp(math_mu_fossil_fuels() +
                  math_sigma_fossil_fuels() * np.sqrt(2) * math_erf_inv_gas())


@cache('run')
def initial_unit_costs_gas():
    """
    Real Name: Initial unit costs Gas
    Original Eqn: 7512.12
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 7512.12


@cache('run')
def initial_unit_costs_oil():
    """
    Real Name: Initial unit costs Oil
    Original Eqn: 5000
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 5000


@cache('run')
def initial_unit_costs_other_renewables():
    """
    Real Name: Initial unit costs other Renewables
    Original Eqn: 5152
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 5152


@cache('step')
def recommissioning_of_capacity_biofuels():
    """
    Real Name: Recommissioning of capacity Biofuels
    Original Eqn: MAX(Change in short term supply Biofuels, 0)*Mothballed capacity Biofuels
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(change_in_short_term_supply_biofuels(), 0) * mothballed_capacity_biofuels()


@cache('step')
def recommissioning_of_capacity_coal():
    """
    Real Name: Recommissioning of capacity Coal
    Original Eqn: MAX(Change in short term supply Coal, 0)*Mothballed capacity Coal
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(change_in_short_term_supply_coal(), 0) * mothballed_capacity_coal()


@cache('step')
def recommissioning_of_capacity_gas():
    """
    Real Name: Recommissioning of capacity Gas
    Original Eqn: MAX(Change in short term supply Gas, 0)*Mothballed capacity Gas
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(change_in_short_term_supply_gas(), 0) * mothballed_capacity_gas()


@cache('step')
def recommissioning_of_capacity_oil():
    """
    Real Name: Recommissioning of capacity Oil
    Original Eqn: MAX(Change in short term supply Oil, 0)*Mothballed capacity Oil
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(change_in_short_term_supply_oil(), 0) * mothballed_capacity_oil()


@cache('step')
def eroei_biofuels():
    """
    Real Name: EROEI Biofuels
    Original Eqn: INTEG ( Change in EROEI Biofuels, Initial EROEI Biofuels)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_eroei_biofuels()


@cache('step')
def eroei_coal():
    """
    Real Name: EROEI Coal
    Original Eqn: Relative EROI Coal*(Maximum EROEI-Minimum EROEI)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return relative_eroi_coal() * (maximum_eroei() - minimum_eroei())


@cache('step')
def eroei_gas():
    """
    Real Name: EROEI Gas
    Original Eqn: Relative EROI Gas*(Maximum EROEI-Minimum EROEI)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return relative_eroi_gas() * (maximum_eroei() - minimum_eroei())


@cache('step')
def eroei_oil():
    """
    Real Name: EROEI Oil
    Original Eqn: Relative EROI Oil*(Maximum EROEI-Minimum EROEI)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return relative_eroi_oil() * (maximum_eroei() - minimum_eroei())


@cache('step')
def eroei_other_renewables():
    """
    Real Name: EROEI other Renewables
    Original Eqn: INTEG ( Change in EROEI other Renewables, Initial EROEI other Renewables)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_eroei_other_renewables()


@cache('run')
def experience_curve_parameter_extraction():
    """
    Real Name: Experience curve parameter extraction
    Original Eqn: -0.512547
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return -0.512547


@cache('step')
def relative_change_in_eroei_coal():
    """
    Real Name: Relative change in EROEI Coal
    Original Eqn: ZIDZ(Change in EROI due to reserve depletion Coal, EROI resources Coal)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_eroi_due_to_reserve_depletion_coal(), eroi_resources_coal())


@cache('step')
def relative_change_in_eroei_gas():
    """
    Real Name: Relative change in EROEI Gas
    Original Eqn: ZIDZ(Change in EROI due to reserve depletion Gas, EROI resources Gas)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_eroi_due_to_reserve_depletion_gas(), eroi_resources_gas())


@cache('step')
def relative_change_in_eroei_oil():
    """
    Real Name: Relative change in EROEI Oil
    Original Eqn: ZIDZ(Change in EROI due to reserve depletion Oil, EROI resources Oil)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_eroi_due_to_reserve_depletion_oil(), eroi_resources_oil())


@cache('step')
def relative_change_in_eroi_biofuels():
    """
    Real Name: Relative change in EROI Biofuels
    Original Eqn: ZIDZ(Change in EROEI Biofuels, EROEI Biofuels)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_eroei_biofuels(), eroei_biofuels())


@cache('step')
def relative_change_in_eroi_other_renewables():
    """
    Real Name: Relative change in EROI other Renewables
    Original Eqn: ZIDZ(Change in EROEI other Renewables, EROEI other Renewables)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_eroei_other_renewables(), eroei_other_renewables())


@cache('run')
def long_term_profits_energy_supply_period_other_renewables():
    """
    Real Name: Long term profits energy supply period other Renewables
    Original Eqn: 8.2738
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 8.2738


@cache('run')
def minimum_eroei():
    """
    Real Name: Minimum EROEI
    Original Eqn: 1
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def total_costs_energy_supply_coal():
    """
    Real Name: Total costs energy supply Coal
    Original Eqn: Extraction capacity installed Coal*Unit costs Coal
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return extraction_capacity_installed_coal() * unit_costs_coal()


@cache('run')
def investment_fraction_normalized_profits_other_renewables():
    """
    Real Name: Investment fraction normalized profits other Renewables
    Original Eqn: -0.228167
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return -0.228167


@cache('step')
def math_2_over_pi_times_a():
    """
    Real Name: MATH 2 over Pi times a
    Original Eqn: 2/(MATH Pi*MATH a)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return 2 / (math_pi() * math_a())


@cache('step')
def relative_eroi_oil():
    """
    Real Name: Relative EROI Oil
    Original Eqn: EXP(MATH mu fossil fuels+MATH sigma fossil fuels * SQRT ( 2) *MATH erf inv Oil)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return np.exp(math_mu_fossil_fuels() +
                  math_sigma_fossil_fuels() * np.sqrt(2) * math_erf_inv_oil())


@cache('step')
def math_erf_input_oil():
    """
    Real Name: MATH erf input Oil
    Original Eqn: ZIDZ(2*Cumulative extracted fuel Oil, Total available resources Oil )-1
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(2 * cumulative_extracted_fuel_oil(), total_available_resources_oil()) - 1


@cache('step')
def relative_potential_eroei_biofuels():
    """
    Real Name: Relative potential EROEI Biofuels
    Original Eqn: (Potential EROEI Biofuels-EROEI Biofuels)/Potential EROEI Biofuels
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return (potential_eroei_biofuels() - eroei_biofuels()) / potential_eroei_biofuels()


@cache('step')
def relative_potential_eroei_other_renewables():
    """
    Real Name: Relative potential EROEI other Renewables
    Original Eqn: (Potential EROEI other Renewables-EROEI other Renewables)/Potential EROEI other Renewables
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return (potential_eroei_other_renewables() -
            eroei_other_renewables()) / potential_eroei_other_renewables()


@cache('run')
def initial_long_term_normalized_profits_gas():
    """
    Real Name: Initial long term normalized profits Gas
    Original Eqn: 0.0977153
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.0977153


@cache('run')
def initial_long_term_normalized_profits_oil():
    """
    Real Name: Initial long term normalized profits Oil
    Original Eqn: 0.298128
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.298128


@cache('run')
def initial_long_term_normalized_profits_other_renewables():
    """
    Real Name: Initial long term normalized profits other Renewables
    Original Eqn: 0.895687
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.895687


@cache('step')
def unit_costs_coal():
    """
    Real Name: Unit costs Coal
    Original Eqn: INTEG ( Change in unit costs Coal, Initial unit costs Coal)
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_unit_costs_coal()


@cache('step')
def relative_variance_in_eroei_distribution():
    """
    Real Name: Relative variance in EROEI distribution
    Original Eqn: 2*10^Variance power
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return 2 * 10**variance_power()


@cache('run')
def long_term_profits_energy_supply_period_oil():
    """
    Real Name: Long term profits energy supply period Oil
    Original Eqn: 8.2738
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 8.2738


@cache('run')
def investment_fraction_normalized_profits_gas():
    """
    Real Name: Investment fraction normalized profits Gas
    Original Eqn: 0.224828
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.224828


@cache('run')
def investment_fraction_normalized_profits_nuclear():
    """
    Real Name: Investment fraction normalized profits Nuclear
    Original Eqn: 0.377136
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.377136


@cache('step')
def math_sigma_fossil_fuels():
    """
    Real Name: MATH sigma fossil fuels
    Original Eqn: SQRT( LN(1 + Variance in EROEI distribution/ (Relative crustal abundance fossil fuels\ ^2) ))
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return np.sqrt(
        np.log(1 +
               variance_in_eroei_distribution() / (relative_crustal_abundance_fossil_fuels()**2)))


@cache('step')
def total_costs_energy_supply_nuclear():
    """
    Real Name: Total costs energy supply Nuclear
    Original Eqn: Extraction capacity installed Nuclear*Unit costs Nuclear
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return extraction_capacity_installed_nuclear() * unit_costs_nuclear()


@cache('run')
def maximum_eroei():
    """
    Real Name: Maximum EROEI
    Original Eqn: 50
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 50


@cache('run')
def initial_eroei_biofuels():
    """
    Real Name: Initial EROEI Biofuels
    Original Eqn: 2
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 2


@cache('run')
def initial_eroei_other_renewables():
    """
    Real Name: Initial EROEI other Renewables
    Original Eqn: 5
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 5


@cache('run')
def maximum_relative_mothballing_gas():
    """
    Real Name: Maximum relative mothballing Gas
    Original Eqn: 0.3
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.3


@cache('step')
def long_term_normalized_profits_nuclear():
    """
    Real Name: Long term normalized profits Nuclear
    Original Eqn: INTEG ( Change in normalized relative profits Nuclear, Initial long term normalized profits Nuclear)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_long_term_normalized_profits_nuclear()


@cache('run')
def maximum_relative_mothballing_oil():
    """
    Real Name: Maximum relative mothballing Oil
    Original Eqn: 0.3
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.3


@cache('run')
def long_term_profits_energy_supply_period_coal():
    """
    Real Name: Long term profits energy supply period Coal
    Original Eqn: 8.2738
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 8.2738


@cache('run')
def maximum_relative_mothballing_nuclear():
    """
    Real Name: Maximum relative mothballing Nuclear
    Original Eqn: 0.3
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.3


@cache('step')
def total_costs_energy_supply_biofuels():
    """
    Real Name: Total costs energy supply Biofuels
    Original Eqn: Extraction capacity installed Biofuels*Unit costs Biofuels
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return extraction_capacity_installed_biofuels() * unit_costs_biofuels()


@cache('step')
def unit_costs_biofuels():
    """
    Real Name: Unit costs Biofuels
    Original Eqn: INTEG ( Change in unit costs Biofuels, Initial unit costs Biofuels)
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_unit_costs_biofuels()


@cache('run')
def investment_fraction_normalized_profits_oil():
    """
    Real Name: Investment fraction normalized profits Oil
    Original Eqn: 0.452329
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.452329


@cache('run')
def long_term_profits_energy_supply_period_nuclear():
    """
    Real Name: Long term profits energy supply period Nuclear
    Original Eqn: 8.2738
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 8.2738


@cache('step')
def relative_change_in_costs_due_to_learning_biofuels():
    """
    Real Name: Relative change in costs due to learning Biofuels
    Original Eqn: ZIDZ(Change in average learning curve parameter Biofuels, Average normalised learning curve on costs Biofuels\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_average_learning_curve_parameter_biofuels(),
                          average_normalised_learning_curve_on_costs_biofuels())


@cache('step')
def total_income_energy_supply_other_renewables():
    """
    Real Name: Total income energy supply other Renewables
    Original Eqn: Energy Price other Renewables*New Energy Demand other Renewables
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return energy_price_other_renewables() * new_energy_demand_other_renewables()


@cache('step')
def total_income_energy_supply_nuclear():
    """
    Real Name: Total income energy supply Nuclear
    Original Eqn: Energy Price Nuclear*New Energy Demand Nuclear
    Units: Dollar/year
    Limits: (None, None)
    Type: component


    """
    return energy_price_nuclear() * new_energy_demand_nuclear()


@cache('step')
def math_erf_input_gas():
    """
    Real Name: MATH erf input Gas
    Original Eqn: ZIDZ(2*Cumulative extracted fuel Gas,Total available resources Gas )-1
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(2 * cumulative_extracted_fuel_gas(), total_available_resources_gas()) - 1


@cache('run')
def initial_long_term_normalized_profits_biofuels():
    """
    Real Name: Initial long term normalized profits Biofuels
    Original Eqn: 0.638689
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.638689


@cache('run')
def initial_cumulative_extraction_fuel_biofuels():
    """
    Real Name: Initial cumulative extraction fuel Biofuels
    Original Eqn: 486328
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 486328


@cache('run')
def initial_cumulative_extraction_fuel_coal():
    """
    Real Name: Initial cumulative extraction fuel Coal
    Original Eqn: 3.99812e+08
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 3.99812e+08


@cache('run')
def initial_cumulative_extraction_fuel_gas():
    """
    Real Name: Initial cumulative extraction fuel Gas
    Original Eqn: 6.72619e+07
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6.72619e+07


@cache('step')
def total_available_resources_oil():
    """
    Real Name: Total available resources Oil
    Original Eqn: Cumulative extracted fuel Oil+Discovered resources reserve base Oil
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return cumulative_extracted_fuel_oil() + discovered_resources_reserve_base_oil()


@cache('run')
def long_term_profits_energy_supply_period_gas():
    """
    Real Name: Long term profits energy supply period Gas
    Original Eqn: 8.2738
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 8.2738


@cache('step')
def math_erf_input_coal():
    """
    Real Name: MATH erf input Coal
    Original Eqn: ZIDZ(2*Cumulative extracted fuel Coal, Total available resources Coal)-1
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(2 * cumulative_extracted_fuel_coal(),
                          total_available_resources_coal()) - 1


@cache('step')
def total_available_resources_gas():
    """
    Real Name: Total available resources Gas
    Original Eqn: Cumulative extracted fuel Gas+Discovered resources reserve base Gas
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return cumulative_extracted_fuel_gas() + discovered_resources_reserve_base_gas()


@cache('step')
def recommissioning_of_capacity_other_renewables():
    """
    Real Name: Recommissioning of capacity other Renewables
    Original Eqn: MAX(Change in short term supply other Renewables, 0)*Mothballed capacity other Renewables
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(change_in_short_term_supply_other_renewables(),
                      0) * mothballed_capacity_other_renewables()


@cache('step')
def relative_change_in_costs_due_to_learning_other_renewables():
    """
    Real Name: Relative change in costs due to learning other Renewables
    Original Eqn: ZIDZ(Change in average learning curve parameter other Renewables, Average normalised learning curve on costs other Renewables\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_average_learning_curve_parameter_other_renewables(),
                          average_normalised_learning_curve_on_costs_other_renewables())


@cache('step')
def recommissioning_of_capacity_nuclear():
    """
    Real Name: Recommissioning of capacity Nuclear
    Original Eqn: MAX(Change in short term supply Nuclear, 0)*Mothballed capacity Nuclear
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return np.maximum(change_in_short_term_supply_nuclear(), 0) * mothballed_capacity_nuclear()


@cache('step')
def long_term_normalized_profits_coal():
    """
    Real Name: Long term normalized profits Coal
    Original Eqn: INTEG ( Change in normalized relative profits Coal, Initial long term normalized profits Coal)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_long_term_normalized_profits_coal()


@cache('run')
def investment_fraction_normalized_profits_biofuels():
    """
    Real Name: Investment fraction normalized profits Biofuels
    Original Eqn: 0
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def long_term_normalized_profits_gas():
    """
    Real Name: Long term normalized profits Gas
    Original Eqn: INTEG ( Change in normalized relative profits Gas, Initial long term normalized profits Gas)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_long_term_normalized_profits_gas()


@cache('step')
def long_term_normalized_profits_other_renewables():
    """
    Real Name: Long term normalized profits other Renewables
    Original Eqn: INTEG ( Change in normalized relative profits other Renewables, Initial long term normalized profits other Renewables)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_long_term_normalized_profits_other_renewables()


@cache('step')
def total_available_resources_coal():
    """
    Real Name: Total available resources Coal
    Original Eqn: Cumulative extracted fuel Coal+Discovered resources reserve base Coal
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return cumulative_extracted_fuel_coal() + discovered_resources_reserve_base_coal()


@cache('run')
def long_term_profits_energy_supply_period_biofuels():
    """
    Real Name: Long term profits energy supply period Biofuels
    Original Eqn: 8.2738
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 8.2738


@cache('run')
def initial_unit_costs_nuclear():
    """
    Real Name: Initial unit costs Nuclear
    Original Eqn: 13314.8
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 13314.8


@cache('step')
def math_a():
    """
    Real Name: MATH a
    Original Eqn: 8/(3*MATH Pi)*(MATH Pi-3)/(4-MATH Pi)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return 8 / (3 * math_pi()) * (math_pi() - 3) / (4 - math_pi())


@cache('step')
def long_term_normalized_profits_biofuels():
    """
    Real Name: Long term normalized profits Biofuels
    Original Eqn: INTEG ( Change in normalized relative profits Biofuels, Initial long term normalized profits Biofuels)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_long_term_normalized_profits_biofuels()


@cache('run')
def investment_fraction_normalized_profits_coal():
    """
    Real Name: Investment fraction normalized profits Coal
    Original Eqn: 0.33112
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.33112


@cache('step')
def relative_change_in_costs_due_to_learning_nuclear():
    """
    Real Name: Relative change in costs due to learning Nuclear
    Original Eqn: ZIDZ( Change in average learning curve parameter Nuclear, Average normalised learning curve on costs Nuclear\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(change_in_average_learning_curve_parameter_nuclear(),
                          average_normalised_learning_curve_on_costs_nuclear())


@cache('run')
def initial_long_term_normalized_profits_coal():
    """
    Real Name: Initial long term normalized profits Coal
    Original Eqn: 0.496472
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.496472


@cache('step')
def new_extraction_capacity_proposed_gas():
    """
    Real Name: New extraction capacity proposed Gas
    Original Eqn: new long term supply Gas*Extraction capacity installed Gas
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return new_long_term_supply_gas() * extraction_capacity_installed_gas()


@cache('step')
def long_term_normalized_profits_oil():
    """
    Real Name: Long term normalized profits Oil
    Original Eqn: INTEG ( Change in normalized relative profits Oil, Initial long term normalized profits Oil)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return integ_long_term_normalized_profits_oil()


@cache('run')
def co2_emissions_of_oil():
    """
    Real Name: CO2 emissions of Oil
    Original Eqn: 80.85
    Units: t/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 80.85


@cache('run')
def co2_emissions_of_coal():
    """
    Real Name: CO2 emissions of coal
    Original Eqn: 103.565
    Units: t/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 103.565


@cache('step')
def co2_emissions():
    """
    Real Name: CO2 emissions
    Original Eqn: CO2 emissions of natural gas*Resource consumption Gas+CO2 emissions of Oil*Resource consumption Oil\ +CO2 emissions of coal*Resource consumption Coal
    Units: t/year
    Limits: (None, None)
    Type: component


    """
    return co2_emissions_of_natural_gas() * resource_consumption_gas() + co2_emissions_of_oil(
    ) * resource_consumption_oil() + co2_emissions_of_coal() * resource_consumption_coal()


@cache('run')
def co2_emissions_of_natural_gas():
    """
    Real Name: CO2 emissions of natural gas
    Original Eqn: 53.06
    Units: t/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 53.06


@cache('step')
def functional_energy_price_coal():
    """
    Real Name: Functional Energy Price Coal
    Original Eqn: Energy Price Coal + CO2 emissions of coal*Costs CO2 emissions
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return energy_price_coal() + co2_emissions_of_coal() * costs_co2_emissions()


@cache('step')
def functional_energy_price_oil():
    """
    Real Name: Functional Energy Price Oil
    Original Eqn: Energy Price Oil + Costs CO2 emissions*CO2 emissions of Oil
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return energy_price_oil() + costs_co2_emissions() * co2_emissions_of_oil()


@cache('step')
def resource_consumption_gas():
    """
    Real Name: Resource consumption Gas
    Original Eqn: MIN(Available Gas, Energy Demand Gas)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.minimum(available_gas(), energy_demand_gas())


@cache('run')
def costs_co2_emissions():
    """
    Real Name: Costs CO2 emissions
    Original Eqn: 30
    Units: Dollar/t
    Limits: (None, None)
    Type: constant


    """
    return 30


@cache('step')
def functional_energy_price_gas():
    """
    Real Name: Functional Energy Price Gas
    Original Eqn: Energy Price Gas + Costs CO2 emissions*CO2 emissions of natural gas
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return energy_price_gas() + costs_co2_emissions() * co2_emissions_of_natural_gas()


@cache('step')
def undiscovered_resources_oil():
    """
    Real Name: Undiscovered resources Oil
    Original Eqn: INTEG ( -Increase in discovered and technically recoverable resources Oil, Initial Undiscovered resources Oil)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_undiscovered_resources_oil()


@cache('run')
def initial_undiscovered_resources_coal():
    """
    Real Name: Initial Undiscovered resources Coal
    Original Eqn: 1.43288e+10
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 1.43288e+10


@cache('run')
def initial_undiscovered_resources_gas():
    """
    Real Name: Initial Undiscovered resources Gas
    Original Eqn: 1.09e+07
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 1.09e+07


@cache('run')
def initial_undiscovered_resources_oil():
    """
    Real Name: Initial Undiscovered resources Oil
    Original Eqn: 0
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def discovered_resources_reserve_base_gas():
    """
    Real Name: Discovered resources reserve base Gas
    Original Eqn: INTEG ( Increase in discovered and technically recoverable gas-Non stockpiled gas extraction\ , Initial reserve base Gas)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_discovered_resources_reserve_base_gas()


@cache('step')
def undiscovered_resources_gas():
    """
    Real Name: Undiscovered resources Gas
    Original Eqn: INTEG ( -Increase in discovered and technically recoverable gas, Initial Undiscovered resources Gas)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_undiscovered_resources_gas()


@cache('step')
def undiscovered_resources_coal():
    """
    Real Name: Undiscovered resources Coal
    Original Eqn: INTEG ( -Increase in discovered and technically recoverable resources Coal, Initial Undiscovered resources Coal)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_undiscovered_resources_coal()


@cache('step')
def preference_for_gas():
    """
    Real Name: Preference for Gas
    Original Eqn: XIDZ(1, Functional Energy Price Gas, 1)
    Units: bbtu/Dollar
    Limits: (None, None)
    Type: component


    """
    return functions.xidz(1, functional_energy_price_gas(), 1)


@cache('step')
def effect_of_supply_shortage_on_decoupling():
    """
    Real Name: Effect of Supply Shortage on Decoupling
    Original Eqn: INTEG ( Decoupling Effect Materializing-Decrease in Shortage Effect, Initial Effect of Supply Shortage on Decoupling)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return integ_effect_of_supply_shortage_on_decoupling()


@cache('step')
def extraction_capacity_installed_gas():
    """
    Real Name: Extraction capacity installed Gas
    Original Eqn: INTEG ( Completing new extraction capacity Gas+Recommissioning of capacity Gas-Mothballing of capacity Gas\ , Initial extraction capacity Gas)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_installed_gas()


@cache('step')
def preference_for_other_renewables():
    """
    Real Name: Preference for other Renewables
    Original Eqn: XIDZ(1, Functional Energy Price other Renewables, 1)
    Units: bbtu/Dollar
    Limits: (None, None)
    Type: component


    """
    return functions.xidz(1, functional_energy_price_other_renewables(), 1)


@cache('run')
def initial_effect_of_supply_shortage_on_decoupling():
    """
    Real Name: Initial Effect of Supply Shortage on Decoupling
    Original Eqn: 0
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def normalized_preference_coal():
    """
    Real Name: Normalized Preference Coal
    Original Eqn: ZIDZ(Preference for Coal, total preferences)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(preference_for_coal(), total_preferences())


@cache('run')
def initial_energy_stocks_biofuels():
    """
    Real Name: Initial Energy stocks Biofuels
    Original Eqn: 12662.9
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 12662.9


@cache('run')
def initial_energy_stocks_coal():
    """
    Real Name: Initial Energy stocks Coal
    Original Eqn: 3.12307e+06
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 3.12307e+06


@cache('run')
def initial_energy_stocks_oil():
    """
    Real Name: Initial Energy stocks Oil
    Original Eqn: 4.56357e+06
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 4.56357e+06


@cache('step')
def normalized_preferenced_other_renewables():
    """
    Real Name: Normalized Preferenced other Renewables
    Original Eqn: ZIDZ(Preference for other Renewables, total preferences)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(preference_for_other_renewables(), total_preferences())


@cache('step')
def functional_energy_price_nuclear():
    """
    Real Name: Functional Energy Price Nuclear
    Original Eqn: Energy Price Nuclear
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return energy_price_nuclear()


@cache('step')
def functional_energy_price_other_renewables():
    """
    Real Name: Functional Energy Price other Renewables
    Original Eqn: Energy Price other Renewables
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return energy_price_other_renewables()


@cache('step')
def ideal_energy_demand_distribution_nuclear():
    """
    Real Name: Ideal Energy Demand Distribution Nuclear
    Original Eqn: Normalized Preference Nuclear
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalized_preference_nuclear()


@cache('step')
def preference_for_biofuels():
    """
    Real Name: Preference for Biofuels
    Original Eqn: XIDZ(1, Functional Energy Price Biofuels, 1)
    Units: bbtu/Dollar
    Limits: (None, None)
    Type: component


    """
    return functions.xidz(1, functional_energy_price_biofuels(), 1)


@cache('step')
def preference_for_coal():
    """
    Real Name: Preference for Coal
    Original Eqn: XIDZ(1, Functional Energy Price Coal, 1)
    Units: bbtu/Dollar
    Limits: (None, None)
    Type: component


    """
    return functions.xidz(1, functional_energy_price_coal(), 1)


@cache('run')
def initial_mothballed_capacity_gas():
    """
    Real Name: Initial mothballed capacity Gas
    Original Eqn: 16700
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 16700


@cache('step')
def preference_for_nuclear():
    """
    Real Name: Preference for Nuclear
    Original Eqn: XIDZ(1, Functional Energy Price Nuclear, 1)
    Units: bbtu/Dollar
    Limits: (None, None)
    Type: component


    """
    return functions.xidz(1, functional_energy_price_nuclear(), 1)


@cache('step')
def preference_for_oil():
    """
    Real Name: Preference for Oil
    Original Eqn: XIDZ(1, Functional Energy Price Oil, 1)
    Units: bbtu/Dollar
    Limits: (None, None)
    Type: component


    """
    return functions.xidz(1, functional_energy_price_oil(), 1)


@cache('step')
def ideal_energy_demand_distribution_coal():
    """
    Real Name: Ideal Energy Demand Distribution Coal
    Original Eqn: Normalized Preference Coal
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalized_preference_coal()


@cache('step')
def normalized_preference_biofuels():
    """
    Real Name: Normalized Preference Biofuels
    Original Eqn: ZIDZ(Preference for Biofuels, total preferences)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(preference_for_biofuels(), total_preferences())


@cache('step')
def total_preferences():
    """
    Real Name: total preferences
    Original Eqn: Preference for Biofuels+Preference for Coal+Preference for Gas+Preference for Nuclear\ +Preference for Oil+Preference for other Renewables
    Units: bbtu/Dollar
    Limits: (None, None)
    Type: component


    """
    return preference_for_biofuels() + preference_for_coal() + preference_for_gas(
    ) + preference_for_nuclear() + preference_for_oil() + preference_for_other_renewables()


@cache('step')
def mothballed_capacity_coal():
    """
    Real Name: Mothballed capacity Coal
    Original Eqn: INTEG ( Mothballing of capacity Coal-Deterioration of unused capacity Coal-Recommissioning of capacity Coal\ , Initial mothballed capacity Coal)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_mothballed_capacity_coal()


@cache('run')
def initial_mothballed_capacity_coal():
    """
    Real Name: Initial mothballed capacity Coal
    Original Eqn: 110100
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 110100


@cache('step')
def mothballed_capacity_oil():
    """
    Real Name: Mothballed capacity Oil
    Original Eqn: INTEG ( Mothballing of capacity Oil-Deterioration of unused capacity Oil-Recommissioning of capacity Oil\ , Initial mothballed capacity Oil)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_mothballed_capacity_oil()


@cache('run')
def initial_mothballed_capacity_oil():
    """
    Real Name: Initial mothballed capacity Oil
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def ideal_energy_demand_distribution_biofuels():
    """
    Real Name: Ideal Energy Demand Distribution Biofuels
    Original Eqn: Normalized Preference Biofuels
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalized_preference_biofuels()


@cache('step')
def ideal_energy_demand_distribution_other_renewables():
    """
    Real Name: Ideal Energy Demand Distribution other Renewables
    Original Eqn: Normalized Preferenced other Renewables
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalized_preferenced_other_renewables()


@cache('step')
def ideal_energy_demand_distribution_gas():
    """
    Real Name: Ideal Energy Demand Distribution Gas
    Original Eqn: Normalized Preference Gas
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalized_preference_gas()


@cache('step')
def ideal_energy_demand_distribution_oil():
    """
    Real Name: Ideal Energy Demand Distribution Oil
    Original Eqn: Normalized Preference Oil
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return normalized_preference_oil()


@cache('step')
def mothballed_capacity_gas():
    """
    Real Name: Mothballed capacity Gas
    Original Eqn: INTEG ( Mothballing of capacity Gas-Deterioration of unused capacity Gas-Recommissioning of capacity Gas\ , Initial mothballed capacity Gas)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_mothballed_capacity_gas()


@cache('step')
def energy_stocks_coal():
    """
    Real Name: Energy stocks Coal
    Original Eqn: INTEG ( Energy import Coal+Resource extraction Coal-Energy export Coal-Resource consumption Coal\ , Initial Energy stocks Coal)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_stocks_coal()


@cache('step')
def energy_stocks_oil():
    """
    Real Name: Energy stocks Oil
    Original Eqn: INTEG ( Energy import Oil+Resource extraction Oil-Energy export Oil-Resource consumption Oil\ , Initial Energy stocks Oil)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_stocks_oil()


@cache('step')
def normalized_preference_gas():
    """
    Real Name: Normalized Preference Gas
    Original Eqn: ZIDZ(Preference for Gas, total preferences)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(preference_for_gas(), total_preferences())


@cache('step')
def energy_stocks_biofuels():
    """
    Real Name: Energy stocks Biofuels
    Original Eqn: INTEG ( Energy import Biofuels+Production of biofuels-Energy export Biofuels-Resource consumption Biofuels\ , Initial Energy stocks Biofuels)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_stocks_biofuels()


@cache('step')
def normalized_preference_oil():
    """
    Real Name: Normalized Preference Oil
    Original Eqn: ZIDZ(Preference for Oil, total preferences)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(preference_for_oil(), total_preferences())


@cache('step')
def normalized_preference_nuclear():
    """
    Real Name: Normalized Preference Nuclear
    Original Eqn: ZIDZ(Preference for Nuclear, total preferences)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(preference_for_nuclear(), total_preferences())


@cache('step')
def functional_energy_price_biofuels():
    """
    Real Name: Functional Energy Price Biofuels
    Original Eqn: Energy Price Biofuels
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return energy_price_biofuels()


@cache('step')
def gas_to_trade():
    """
    Real Name: Gas to trade
    Original Eqn: Non stockpiled gas extraction-Energy Demand Gas
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return non_stockpiled_gas_extraction() - energy_demand_gas()


@cache('run')
def energy_price_biofuels():
    """
    Real Name: Energy Price Biofuels
    Original Eqn: 42000
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 42000


@cache('run')
def energy_price_coal():
    """
    Real Name: Energy Price Coal
    Original Eqn: 3767
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 3767


@cache('run')
def energy_price_gas():
    """
    Real Name: Energy Price Gas
    Original Eqn: 8895
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 8895


@cache('run')
def energy_price_nuclear():
    """
    Real Name: Energy Price Nuclear
    Original Eqn: 17500
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17500


@cache('run')
def energy_price_oil():
    """
    Real Name: Energy Price Oil
    Original Eqn: 14106.4
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 14106.4


@cache('run')
def energy_price_other_renewables():
    """
    Real Name: Energy Price other Renewables
    Original Eqn: 21982
    Units: Dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 21982


@cache('step')
def total_ideal_demand_distribution():
    """
    Real Name: total ideal demand distribution
    Original Eqn: Ideal Energy Demand Distribution Biofuels+Ideal Energy Demand Distribution Coal+Ideal Energy Demand Distribution Gas\ +Ideal Energy Demand Distribution Nuclear+Ideal Energy Demand Distribution Oil+Ideal Energy Demand Distribution other Renewables
    Units: 1
    Limits: (None, None)
    Type: component


    """
    return ideal_energy_demand_distribution_biofuels() + ideal_energy_demand_distribution_coal(
    ) + ideal_energy_demand_distribution_gas() + ideal_energy_demand_distribution_nuclear(
    ) + ideal_energy_demand_distribution_oil() + ideal_energy_demand_distribution_other_renewables(
    )


@cache('step')
def current_energy_demand_oil():
    """
    Real Name: Current Energy Demand Oil
    Original Eqn: Energy Demand*(Current Energy Supply Distribution Oil*(1-Previous Demand Factor)+Previous Demand Factor\ *Normalized Previous Demand Oil)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * (current_energy_supply_distribution_oil() *
                              (1 - previous_demand_factor()) +
                              previous_demand_factor() * normalized_previous_demand_oil())


@cache('step')
def current_energy_demand_other_renewables():
    """
    Real Name: Current Energy Demand other Renewables
    Original Eqn: Energy Demand*(Current Energy Supply Distribution other Renewables*(1-Previous Demand Factor\ )+Previous Demand Factor*Normalized Previous Demand other Renewables)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * (
        current_energy_supply_distribution_other_renewables() * (1 - previous_demand_factor()) +
        previous_demand_factor() * normalized_previous_demand_other_renewables())


@cache('step')
def energy_demand_biofuels():
    """
    Real Name: Energy Demand Biofuels
    Original Eqn: New Energy Demand Biofuels
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return new_energy_demand_biofuels()


@cache('step')
def energy_demand_coal():
    """
    Real Name: Energy Demand Coal
    Original Eqn: New Energy Demand Coal
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return new_energy_demand_coal()


@cache('step')
def energy_demand_gas():
    """
    Real Name: Energy Demand Gas
    Original Eqn: New Energy Demand Gas
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return new_energy_demand_gas()


@cache('step')
def energy_demand_nuclear():
    """
    Real Name: Energy Demand Nuclear
    Original Eqn: New Energy Demand Nuclear
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return new_energy_demand_nuclear()


@cache('step')
def energy_demand_oil():
    """
    Real Name: Energy Demand Oil
    Original Eqn: New Energy Demand Oil
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return new_energy_demand_oil()


@cache('step')
def new_energy_demand_biofuels():
    """
    Real Name: New Energy Demand Biofuels
    Original Eqn: (1-Maximum Change in Demand)*Current Energy Demand Biofuels+Ideal Energy Demand Biofuels\ *Maximum Change in Demand
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return (1 - maximum_change_in_demand()) * current_energy_demand_biofuels(
    ) + ideal_energy_demand_biofuels() * maximum_change_in_demand()


@cache('run')
def maximum_change_in_demand():
    """
    Real Name: Maximum Change in Demand
    Original Eqn: 0.5
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.5


@cache('step')
def current_energy_demand_biofuels():
    """
    Real Name: Current Energy Demand Biofuels
    Original Eqn: Energy Demand*(Current Energy Supply Distribution Biofuels*(1-Previous Demand Factor\ )+Normalized Previous Demand Biofuels*Previous Demand Factor)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * (current_energy_supply_distribution_biofuels() *
                              (1 - previous_demand_factor()) +
                              normalized_previous_demand_biofuels() * previous_demand_factor())


@cache('step')
def current_energy_demand_coal():
    """
    Real Name: Current Energy Demand Coal
    Original Eqn: Energy Demand*(Current Energy Supply Distribution Coal*(1-Previous Demand Factor)+Normalized Previous Demand Coal\ *Previous Demand Factor)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * (current_energy_supply_distribution_coal() *
                              (1 - previous_demand_factor()) +
                              normalized_previous_demand_coal() * previous_demand_factor())


@cache('step')
def current_energy_demand_gas():
    """
    Real Name: Current Energy Demand Gas
    Original Eqn: Energy Demand*(Current Energy Supply Distribution Gas*(1-Previous Demand Factor) + Previous Demand Factor\ *Normalized Previous Demand Gas)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * (current_energy_supply_distribution_gas() *
                              (1 - previous_demand_factor()) +
                              previous_demand_factor() * normalized_previous_demand_gas())


@cache('step')
def energy_demand_other_renewables():
    """
    Real Name: Energy Demand other Renewables
    Original Eqn: New Energy Demand other Renewables
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return new_energy_demand_other_renewables()


@cache('step')
def new_energy_demand_coal():
    """
    Real Name: New Energy Demand Coal
    Original Eqn: (1-Maximum Change in Demand)*Current Energy Demand Coal+Ideal Energy Demand Coal*Maximum Change in Demand
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return (1 - maximum_change_in_demand()) * current_energy_demand_coal(
    ) + ideal_energy_demand_coal() * maximum_change_in_demand()


@cache('step')
def new_energy_demand_gas():
    """
    Real Name: New Energy Demand Gas
    Original Eqn: (1-Maximum Change in Demand)*Current Energy Demand Gas+Maximum Change in Demand*Ideal Energy Demand Gas
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return (1 - maximum_change_in_demand()) * current_energy_demand_gas(
    ) + maximum_change_in_demand() * ideal_energy_demand_gas()


@cache('step')
def new_energy_demand_nuclear():
    """
    Real Name: New Energy Demand Nuclear
    Original Eqn: (1-Maximum Change in Demand)*Current Energy Demand Nuclear+Maximum Change in Demand*\ Ideal Energy Demand Nuclear
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return (1 - maximum_change_in_demand()) * current_energy_demand_nuclear(
    ) + maximum_change_in_demand() * ideal_energy_demand_nuclear()


@cache('step')
def new_energy_demand_oil():
    """
    Real Name: New Energy Demand Oil
    Original Eqn: (1-Maximum Change in Demand)*Current Energy Demand Oil+Ideal Energy Demand Oil*Maximum Change in Demand
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return (1 - maximum_change_in_demand()) * current_energy_demand_oil(
    ) + ideal_energy_demand_oil() * maximum_change_in_demand()


@cache('step')
def new_energy_demand_other_renewables():
    """
    Real Name: New Energy Demand other Renewables
    Original Eqn: (1-Maximum Change in Demand)*Current Energy Demand other Renewables+Ideal Energy Demand other Renewables *Maximum Change in Demand
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return (1 - maximum_change_in_demand()) * current_energy_demand_other_renewables(
    ) + ideal_energy_demand_other_renewables() * maximum_change_in_demand()


@cache('step')
def current_energy_demand_nuclear():
    """
    Real Name: Current Energy Demand Nuclear
    Original Eqn: Energy Demand*(Current Energy Supply Distribution Nuclear*(1-Previous Demand Factor)\ +Previous Demand Factor*Normalized Previous Demand Nuclear)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * (current_energy_supply_distribution_nuclear() *
                              (1 - previous_demand_factor()) +
                              previous_demand_factor() * normalized_previous_demand_nuclear())


@cache('step')
def ideal_energy_demand_gas():
    """
    Real Name: Ideal Energy Demand Gas
    Original Eqn: Energy Demand*Ideal Energy Demand Distribution Gas
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * ideal_energy_demand_distribution_gas()


@cache('step')
def ideal_energy_demand_biofuels():
    """
    Real Name: Ideal Energy Demand Biofuels
    Original Eqn: Energy Demand*Ideal Energy Demand Distribution Biofuels
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * ideal_energy_demand_distribution_biofuels()


@cache('step')
def ideal_energy_demand_coal():
    """
    Real Name: Ideal Energy Demand Coal
    Original Eqn: Energy Demand*Ideal Energy Demand Distribution Coal
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * ideal_energy_demand_distribution_coal()


@cache('step')
def ideal_energy_demand_oil():
    """
    Real Name: Ideal Energy Demand Oil
    Original Eqn: Energy Demand*Ideal Energy Demand Distribution Oil
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * ideal_energy_demand_distribution_oil()


@cache('step')
def ideal_energy_demand_other_renewables():
    """
    Real Name: Ideal Energy Demand other Renewables
    Original Eqn: Energy Demand*Ideal Energy Demand Distribution other Renewables
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * ideal_energy_demand_distribution_other_renewables()


@cache('step')
def total_new_energy_demand():
    """
    Real Name: Total New Energy Demand
    Original Eqn: New Energy Demand Biofuels+New Energy Demand Coal+New Energy Demand Gas+New Energy Demand Nuclear\ +New Energy Demand Oil+New Energy Demand other Renewables
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return new_energy_demand_biofuels() + new_energy_demand_coal() + new_energy_demand_gas(
    ) + new_energy_demand_nuclear() + new_energy_demand_oil() + new_energy_demand_other_renewables(
    )


@cache('step')
def ideal_energy_demand_nuclear():
    """
    Real Name: Ideal Energy Demand Nuclear
    Original Eqn: Energy Demand*Ideal Energy Demand Distribution Nuclear
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() * ideal_energy_demand_distribution_nuclear()


@cache('step')
def current_energy_supply_distribution_nuclear():
    """
    Real Name: Current Energy Supply Distribution Nuclear
    Original Eqn: ZIDZ(Extraction capacity installed Nuclear, Total Energy Supply)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(extraction_capacity_installed_nuclear(), total_energy_supply())


@cache('step')
def available_resources_from_stocks_biofuels():
    """
    Real Name: Available resources from stocks Biofuels
    Original Eqn: Energy stocks Biofuels/One Year
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_stocks_biofuels() / one_year()


@cache('step')
def available_resources_from_stocks_coal():
    """
    Real Name: Available resources from stocks Coal
    Original Eqn: Energy stocks Coal/One Year
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_stocks_coal() / one_year()


@cache('step')
def available_resources_from_stocks_oil():
    """
    Real Name: Available resources from stocks Oil
    Original Eqn: Energy stocks Oil/One Year
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_stocks_oil() / one_year()


@cache('step')
def relative_biofuels_shortage():
    """
    Real Name: Relative Biofuels Shortage
    Original Eqn: XIDZ(Biofuels to trade, Available resources from stocks Biofuels, 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.xidz(biofuels_to_trade(), available_resources_from_stocks_biofuels(), 1)


@cache('step')
def relative_coal_shortage():
    """
    Real Name: Relative Coal Shortage
    Original Eqn: ZIDZ(Coal to trade, Available resources from stocks Coal)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(coal_to_trade(), available_resources_from_stocks_coal())


@cache('step')
def relative_other_renewables_shortage():
    """
    Real Name: Relative other Renewables Shortage
    Original Eqn: XIDZ(other Renewables Shortage, Extraction capacity installed other Renewables, 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.xidz(other_renewables_shortage(),
                          extraction_capacity_installed_other_renewables(), 1)


@cache('step')
def relative_shortages_oil():
    """
    Real Name: Relative Shortages Oil
    Original Eqn: XIDZ(Oil to trade, Available resources from stocks Oil, 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.xidz(oil_to_trade(), available_resources_from_stocks_oil(), 1)


@cache('step')
def current_energy_supply_distribution_other_renewables():
    """
    Real Name: Current Energy Supply Distribution other Renewables
    Original Eqn: ZIDZ(Extraction capacity installed other Renewables, Total Energy Supply)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(extraction_capacity_installed_other_renewables(), total_energy_supply())


@cache('step')
def resource_consumption_reduction_factor_biofuels():
    """
    Real Name: Resource consumption reduction factor Biofuels
    Original Eqn: ZIDZ(Energy stocks Biofuels, Average throughput time stocks Biofuels*Energy Demand Biofuels\ )
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(energy_stocks_biofuels(),
                          average_throughput_time_stocks_biofuels() * energy_demand_biofuels())


@cache('step')
def decrease_in_shortage_effect():
    """
    Real Name: Decrease in Shortage Effect
    Original Eqn: Effect of Supply Shortage on Decoupling/Delay Time Decoupling due to Shortage
    Units: 1/(year*year)
    Limits: (None, None)
    Type: component


    """
    return effect_of_supply_shortage_on_decoupling() / delay_time_decoupling_due_to_shortage()


@cache('run')
def delay_order_decoupling_due_to_shortage():
    """
    Real Name: Delay Order Decoupling due to Shortage
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('step')
def nuclear_shortage():
    """
    Real Name: Nuclear Shortage
    Original Eqn: Energy Demand Nuclear-Extraction capacity installed Nuclear
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand_nuclear() - extraction_capacity_installed_nuclear()


@cache('run')
def factor_limiting_economic_growth_due_to_energy_shortage():
    """
    Real Name: Factor limiting Economic Growth due to Energy Shortage
    Original Eqn: 0.1
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.1


@cache('run')
def delay_time_decoupling_due_to_shortage():
    """
    Real Name: Delay Time Decoupling due to Shortage
    Original Eqn: 10
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 10


@cache('step')
def future_shortage_effect():
    """
    Real Name: Future Shortage Effect
    Original Eqn: Relative Supply Shortage*Effect of Energy Shortage on Future Decoupling/Delay Time Decoupling due to Shortage
    Units: 1/(year*year)
    Limits: (None, None)
    Type: component


    """
    return relative_supply_shortage() * effect_of_energy_shortage_on_future_decoupling(
    ) / delay_time_decoupling_due_to_shortage()


@cache('step')
def total_energy_supply_distribution():
    """
    Real Name: Total Energy Supply Distribution
    Original Eqn: Current Energy Supply Distribution Biofuels+Current Energy Supply Distribution Coal+\ Current Energy Supply Distribution Gas+Current Energy Supply Distribution Nuclear+Current Energy Supply Distribution Oil\ +Current Energy Supply Distribution other Renewables
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return current_energy_supply_distribution_biofuels() + current_energy_supply_distribution_coal(
    ) + current_energy_supply_distribution_gas() + current_energy_supply_distribution_nuclear(
    ) + current_energy_supply_distribution_oil(
    ) + current_energy_supply_distribution_other_renewables()


@cache('step')
def relative_supply_shortage():
    """
    Real Name: Relative Supply Shortage
    Original Eqn: MIN(MAX(XIDZ(Energy Shortage, Total Energy Supply, 1),0),1)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return np.minimum(
        np.maximum(functions.xidz(energy_shortage(), total_energy_supply(), 1), 0), 1)


@cache('step')
def resource_consumption_reduction_factor_oil():
    """
    Real Name: Resource consumption reduction factor Oil
    Original Eqn: ZIDZ(Energy stocks Oil, Average throughput time stocks Oil*Energy Demand Oil)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(energy_stocks_oil(),
                          average_throughput_time_stocks_oil() * energy_demand_oil())


@cache('run')
def effect_of_energy_shortage_on_future_decoupling():
    """
    Real Name: Effect of Energy Shortage on Future Decoupling
    Original Eqn: 0.5
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.5


@cache('step')
def resource_consumption_oil():
    """
    Real Name: Resource consumption Oil
    Original Eqn: MIN(Energy Demand Oil, Energy Demand Oil*Resource consumption reduction factor Oil)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.minimum(energy_demand_oil(),
                      energy_demand_oil() * resource_consumption_reduction_factor_oil())


@cache('step')
def resource_consumption_reduction_factor_coal():
    """
    Real Name: Resource consumption reduction factor Coal
    Original Eqn: ZIDZ(Energy stocks Coal, Average throughput time stocks Coal*Energy Demand Coal)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(energy_stocks_coal(),
                          average_throughput_time_stocks_coal() * energy_demand_coal())


@cache('step')
def other_renewables_shortage():
    """
    Real Name: other Renewables Shortage
    Original Eqn: Energy Demand other Renewables-Extraction capacity installed other Renewables
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand_other_renewables() - extraction_capacity_installed_other_renewables()


@cache('step')
def relative_shortage_nuclear():
    """
    Real Name: Relative Shortage Nuclear
    Original Eqn: XIDZ(Nuclear Shortage, Extraction capacity installed Nuclear, 1)
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.xidz(nuclear_shortage(), extraction_capacity_installed_nuclear(), 1)


@cache('step')
def limitations_economic_growth_due_to_energy_shortage():
    """
    Real Name: Limitations Economic Growth due to Energy Shortage
    Original Eqn: Relative Supply Shortage*Factor limiting Economic Growth due to Energy Shortage
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return relative_supply_shortage() * factor_limiting_economic_growth_due_to_energy_shortage()


@cache('step')
def resource_consumption_coal():
    """
    Real Name: Resource consumption Coal
    Original Eqn: MIN(Energy Demand Coal, Energy Demand Coal*Resource consumption reduction factor Coal\ )
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.minimum(energy_demand_coal(),
                      energy_demand_coal() * resource_consumption_reduction_factor_coal())


@cache('step')
def resource_consumption_biofuels():
    """
    Real Name: Resource consumption Biofuels
    Original Eqn: MAX(MIN(Energy Demand Biofuels, Energy Demand Biofuels*Resource consumption reduction factor Biofuels\ ),0)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.maximum(
        np.minimum(energy_demand_biofuels(),
                   energy_demand_biofuels() * resource_consumption_reduction_factor_biofuels()), 0)


@cache('step')
def future_effect_of_shortage_on_decoupling():
    """
    Real Name: Future Effect of Shortage on Decoupling
    Original Eqn: INTEG ( Future Shortage Effect-Decoupling Effect Materializing, Initial Shortage Effect on Decoupling)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return integ_future_effect_of_shortage_on_decoupling()


@cache('step')
def energy_shortage():
    """
    Real Name: Energy Shortage
    Original Eqn: Energy Demand-Total Energy Supply
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return energy_demand() - total_energy_supply()


@cache('run')
def initial_shortage_effect_on_decoupling():
    """
    Real Name: Initial Shortage Effect on Decoupling
    Original Eqn: 0
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def initial_energy_intensity_gdp():
    """
    Real Name: Initial Energy Intensity GDP
    Original Eqn: 3.46e-06
    Units: bbtu/Dollar
    Limits: (None, None)
    Type: constant


    """
    return 3.46e-06


@cache('step')
def energy_demand():
    """
    Real Name: Energy Demand
    Original Eqn: GDP*Energy Intensity GDP/One Year
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return gdp() * energy_intensity_gdp() / one_year()


@cache('run')
def gas_export():
    """
    Real Name: Gas Export
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def initial_gdp():
    """
    Real Name: Initial GDP
    Original Eqn: 3.71e+12
    Units: Dollar
    Limits: (None, None)
    Type: constant


    """
    return 3.71e+12


@cache('step')
def gdp():
    """
    Real Name: GDP
    Original Eqn: INTEG ( Increase in GDP, Initial GDP)
    Units: Dollar
    Limits: (None, None)
    Type: component


    """
    return integ_gdp()


@cache('run')
def one_year():
    """
    Real Name: One Year
    Original Eqn: 1
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def energy_intensity_gdp():
    """
    Real Name: Energy Intensity GDP
    Original Eqn: INTEG ( -Decrease Energy Intensity GDP, Initial Energy Intensity GDP)
    Units: bbtu/Dollar
    Limits: (None, None)
    Type: component


    """
    return integ_energy_intensity_gdp()


@cache('run')
def gas_import():
    """
    Real Name: Gas Import
    Original Eqn: 2.37e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 2.37e+06


@cache('step')
def decrease_energy_intensity_gdp():
    """
    Real Name: Decrease Energy Intensity GDP
    Original Eqn: Energy Intensity GDP*decrease factor
    Units: bbtu/(year*Dollar)
    Limits: (None, None)
    Type: component


    """
    return energy_intensity_gdp() * decrease_factor()


@cache('run')
def average_rb_over_p_coal():
    """
    Real Name: Average Rb over P Coal
    Original Eqn: 206
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 206


@cache('run')
def average_rb_over_p_oil():
    """
    Real Name: Average Rb over P Oil
    Original Eqn: 0
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def average_rb_over_p_gas():
    """
    Real Name: Average Rb over P gas
    Original Eqn: 5.1
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 5.1


@cache('run')
def average_throughput_time_stocks_biofuels():
    """
    Real Name: Average throughput time stocks Biofuels
    Original Eqn: 0.1
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 0.1


@cache('run')
def average_throughput_time_stocks_coal():
    """
    Real Name: Average throughput time stocks Coal
    Original Eqn: 0.1
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 0.1


@cache('run')
def delay_order_new_capacity_biofuels():
    """
    Real Name: Delay order new capacity Biofuels
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def delay_order_new_capacity_coal():
    """
    Real Name: Delay order new capacity Coal
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def delay_order_new_capacity_gas():
    """
    Real Name: Delay order new capacity Gas
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def delay_order_new_capacity_oil():
    """
    Real Name: Delay order new capacity Oil
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def delay_order_new_capacity_other_renewables():
    """
    Real Name: Delay order new capacity other Renewables
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def delay_order_new_capacity_nuclear():
    """
    Real Name: Delay order new capacity Nuclear
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def delay_time_new_capacity_biofuels():
    """
    Real Name: Delay time new capacity Biofuels
    Original Eqn: 15.5868
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 15.5868


@cache('run')
def delay_time_new_capacity_coal():
    """
    Real Name: Delay time new capacity Coal
    Original Eqn: 15.5868
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 15.5868


@cache('run')
def delay_time_new_capacity_gas():
    """
    Real Name: Delay time new capacity Gas
    Original Eqn: 15
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 15


@cache('run')
def delay_time_new_capacity_oil():
    """
    Real Name: Delay time new capacity Oil
    Original Eqn: 15.5868
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 15.5868


@cache('run')
def delay_time_new_capacity_other_renewables():
    """
    Real Name: Delay time new capacity other Renewables
    Original Eqn: 15
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 15


@cache('run')
def delay_time_new_capacity_nuclear():
    """
    Real Name: Delay time new capacity Nuclear
    Original Eqn: 15.5868
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 15.5868


@cache('step')
def deterioration_of_unused_capacity_biofuels():
    """
    Real Name: Deterioration of unused capacity Biofuels
    Original Eqn: Mothballed capacity Biofuels/Time for deteriation of unused capacity Biofuels
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return mothballed_capacity_biofuels() / time_for_deteriation_of_unused_capacity_biofuels()


@cache('step')
def deterioration_of_unused_capacity_coal():
    """
    Real Name: Deterioration of unused capacity Coal
    Original Eqn: Mothballed capacity Coal/Time for deteriation of unused capacity Coal
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return mothballed_capacity_coal() / time_for_deteriation_of_unused_capacity_coal()


@cache('step')
def deterioration_of_unused_capacity_gas():
    """
    Real Name: Deterioration of unused capacity Gas
    Original Eqn: Mothballed capacity Gas/Time for deteriation of unused capacity Gas
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return mothballed_capacity_gas() / time_for_deteriation_of_unused_capacity_gas()


@cache('step')
def deterioration_of_unused_capacity_oil():
    """
    Real Name: Deterioration of unused capacity Oil
    Original Eqn: Mothballed capacity Oil/Time for deteriation of unused capacity Oil
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return mothballed_capacity_oil() / time_for_deteriation_of_unused_capacity_oil()


@cache('step')
def deterioration_of_unused_capacity_other_renewables():
    """
    Real Name: Deterioration of unused capacity other Renewables
    Original Eqn: Mothballed capacity other Renewables/Time for deteriation of unused capacity other Renewables
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return mothballed_capacity_other_renewables(
    ) / time_for_deteriation_of_unused_capacity_other_renewables()


@cache('step')
def deterioration_of_unused_capacity_nuclear():
    """
    Real Name: Deterioration of unused capacity Nuclear
    Original Eqn: Mothballed capacity Nuclear/Time for deteriation of unused capacity Nuclear
    Units: bbtu/(year*year)
    Limits: (None, None)
    Type: component


    """
    return mothballed_capacity_nuclear() / time_for_deteriation_of_unused_capacity_nuclear()


@cache('step')
def discovered_resources_reserve_base_coal():
    """
    Real Name: Discovered resources reserve base Coal
    Original Eqn: INTEG ( Increase in discovered and technically recoverable resources Coal-Resource extraction Coal\ , Initial reserve base Coal)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_discovered_resources_reserve_base_coal()


@cache('step')
def discovered_resources_reserve_base_oil():
    """
    Real Name: Discovered resources reserve base Oil
    Original Eqn: INTEG ( Increase in discovered and technically recoverable resources Oil-Resource extraction Oil\ , Initial reserve base Oil)
    Units: bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_discovered_resources_reserve_base_oil()


@cache('step')
def energy_import_biofuels():
    """
    Real Name: Energy import Biofuels
    Original Eqn: Total import Biofuels
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return total_import_biofuels()


@cache('step')
def energy_import_coal():
    """
    Real Name: Energy import Coal
    Original Eqn: Total import Coal
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return total_import_coal()


@cache('step')
def energy_import_oil():
    """
    Real Name: Energy import Oil
    Original Eqn: Total import Oil
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return total_import_oil()


@cache('step')
def extraction_capacity_in_preparation_biofuels():
    """
    Real Name: Extraction capacity in preparation Biofuels
    Original Eqn: INTEG ( New extraction capacity proposed Biofuels-Completing new extraction capacity Biofuels\ , Initial extraction capacity in preparation Biofuels)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_in_preparation_biofuels()


@cache('step')
def extraction_capacity_in_preparation_coal():
    """
    Real Name: Extraction capacity in preparation Coal
    Original Eqn: INTEG ( New extraction capacity proposed Coal-Completing new extraction capacity Coal, Initial extraction capacity in preparation Coal)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_in_preparation_coal()


@cache('step')
def extraction_capacity_in_preparation_gas():
    """
    Real Name: Extraction capacity in preparation Gas
    Original Eqn: INTEG ( New extraction capacity proposed Gas-Completing new extraction capacity Gas, Initial extraction capacity in preparation Gas)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_in_preparation_gas()


@cache('step')
def extraction_capacity_in_preparation_oil():
    """
    Real Name: Extraction capacity in preparation Oil
    Original Eqn: INTEG ( New extraction capacity proposed Oil-Completing new extraction capacity Oil, Initial extraction capacity in preparation Oil)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_in_preparation_oil()


@cache('step')
def extraction_capacity_in_preparation_other_renewables():
    """
    Real Name: Extraction capacity in preparation other Renewables
    Original Eqn: INTEG ( New extraction capacity proposed other Renewables-Completing new extraction capacity other Renewables\ , Initial extraction capacity in preparation other Renewables)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_in_preparation_other_renewables()


@cache('step')
def extraction_capacity_in_preparation_nuclear():
    """
    Real Name: Extraction capacity in preparation Nuclear
    Original Eqn: INTEG ( New extraction capacity proposed Nuclear-Completing new extraction capacity Nuclear, Initial extraction capacity in preparation Nuclear)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_in_preparation_nuclear()


@cache('step')
def extraction_capacity_installed_biofuels():
    """
    Real Name: Extraction capacity installed Biofuels
    Original Eqn: INTEG ( Completing new extraction capacity Biofuels+Recommissioning of capacity Biofuels-Mothballing of capacity Biofuels\ , Initial extraction capacity Biofuels )
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_installed_biofuels()


@cache('step')
def extraction_capacity_installed_coal():
    """
    Real Name: Extraction capacity installed Coal
    Original Eqn: INTEG ( Completing new extraction capacity Coal+Recommissioning of capacity Coal-Mothballing of capacity Coal\ , Initial extraction capacity Coal)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_installed_coal()


@cache('step')
def extraction_capacity_installed_oil():
    """
    Real Name: Extraction capacity installed Oil
    Original Eqn: INTEG ( Completing new extraction capacity Oil+Recommissioning of capacity Oil-Mothballing of capacity Oil\ , Initial extraction capacity Oil)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_installed_oil()


@cache('step')
def extraction_capacity_installed_other_renewables():
    """
    Real Name: Extraction capacity installed other Renewables
    Original Eqn: INTEG ( Completing new extraction capacity other Renewables+Recommissioning of capacity other Renewables\ -Mothballing of capacity other Renewables, Initial extraction capacity other Renewables)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_installed_other_renewables()


@cache('step')
def extraction_capacity_installed_nuclear():
    """
    Real Name: Extraction capacity installed Nuclear
    Original Eqn: INTEG ( Completing new extraction capacity Nuclear+Recommissioning of capacity Nuclear-Mothballing of capacity Nuclear\ , Initial extraction capacity Nuclear)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_extraction_capacity_installed_nuclear()


@cache('run')
def initial_mothballed_capacity_biofuels():
    """
    Real Name: Initial mothballed capacity Biofuels
    Original Eqn: 8208.65
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 8208.65


@cache('run')
def initial_mothballed_capacity_other_renewables():
    """
    Real Name: Initial mothballed capacity other Renewables
    Original Eqn: 101635
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 101635


@cache('run')
def initial_mothballed_capacity_nuclear():
    """
    Real Name: Initial mothballed capacity Nuclear
    Original Eqn: 53506.7
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 53506.7


@cache('run')
def initial_extraction_capacity_biofuels():
    """
    Real Name: Initial extraction capacity Biofuels
    Original Eqn: 126629
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 126629


@cache('run')
def initial_extraction_capacity_coal():
    """
    Real Name: Initial extraction capacity Coal
    Original Eqn: 1.69844e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 1.69844e+06


@cache('run')
def initial_extraction_capacity_gas():
    """
    Real Name: Initial extraction capacity Gas
    Original Eqn: 257941
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 257941


@cache('run')
def initial_extraction_capacity_oil():
    """
    Real Name: Initial extraction capacity Oil
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def initial_extraction_capacity_other_renewables():
    """
    Real Name: Initial extraction capacity other Renewables
    Original Eqn: 1.56784e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 1.56784e+06


@cache('run')
def initial_extraction_capacity_in_preparation_biofuels():
    """
    Real Name: Initial extraction capacity in preparation Biofuels
    Original Eqn: 10754.1
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 10754.1


@cache('run')
def initial_extraction_capacity_in_preparation_coal():
    """
    Real Name: Initial extraction capacity in preparation Coal
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def initial_extraction_capacity_in_preparation_gas():
    """
    Real Name: Initial extraction capacity in preparation Gas
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def initial_extraction_capacity_in_preparation_oil():
    """
    Real Name: Initial extraction capacity in preparation Oil
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def initial_extraction_capacity_in_preparation_other_renewables():
    """
    Real Name: Initial extraction capacity in preparation other Renewables
    Original Eqn: 1.00117e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 1.00117e+06


@cache('run')
def initial_extraction_capacity_in_preparation_nuclear():
    """
    Real Name: Initial extraction capacity in preparation Nuclear
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def initial_extraction_capacity_nuclear():
    """
    Real Name: Initial extraction capacity Nuclear
    Original Eqn: 825411
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 825411


@cache('run')
def initial_relation_between_reserve_base_and_resource_size_coal():
    """
    Real Name: Initial relation between reserve base and resource size Coal
    Original Eqn: 10
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 10


@cache('run')
def initial_relation_between_reserve_base_and_resource_size_gas():
    """
    Real Name: Initial relation between reserve base and resource size Gas
    Original Eqn: 10
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 10


@cache('run')
def initial_relation_between_reserve_base_and_resource_size_oil():
    """
    Real Name: Initial relation between reserve base and resource size Oil
    Original Eqn: 10
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 10


@cache('run')
def initial_reserve_base_coal():
    """
    Real Name: Initial reserve base Coal
    Original Eqn: 1.43288e+09
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 1.43288e+09


@cache('run')
def initial_reserve_base_gas():
    """
    Real Name: Initial reserve base Gas
    Original Eqn: 1.09e+06
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 1.09e+06


@cache('run')
def initial_reserve_base_oil():
    """
    Real Name: Initial reserve base Oil
    Original Eqn: 0
    Units: bbtu
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def mothballed_capacity_biofuels():
    """
    Real Name: Mothballed capacity Biofuels
    Original Eqn: INTEG ( Mothballing of capacity Biofuels-Deterioration of unused capacity Biofuels-Recommissioning of capacity Biofuels\ , Initial mothballed capacity Biofuels)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_mothballed_capacity_biofuels()


@cache('step')
def mothballed_capacity_other_renewables():
    """
    Real Name: Mothballed capacity other Renewables
    Original Eqn: INTEG ( Mothballing of capacity other Renewables-Deterioration of unused capacity other Renewables\ -Recommissioning of capacity other Renewables, Initial mothballed capacity other Renewables)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_mothballed_capacity_other_renewables()


@cache('step')
def mothballed_capacity_nuclear():
    """
    Real Name: Mothballed capacity Nuclear
    Original Eqn: INTEG ( Mothballing of capacity Nuclear-Deterioration of unused capacity Nuclear-Recommissioning of capacity Nuclear\ , Initial mothballed capacity Nuclear)
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return integ_mothballed_capacity_nuclear()


@cache('step')
def non_stockpiled_gas_extraction():
    """
    Real Name: Non stockpiled gas extraction
    Original Eqn: MIN(Extraction capacity installed Gas, ZIDZ( Extraction capacity installed Gas*Discovered resources reserve base Gas\ , Extraction capacity installed Gas*Average Rb over P gas))
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.minimum(
        extraction_capacity_installed_gas(),
        functions.zidz(
            extraction_capacity_installed_gas() * discovered_resources_reserve_base_gas(),
            extraction_capacity_installed_gas() * average_rb_over_p_gas()))


@cache('step')
def production_of_biofuels():
    """
    Real Name: Production of biofuels
    Original Eqn: Extraction capacity installed Biofuels
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return extraction_capacity_installed_biofuels()


@cache('step')
def resource_extraction_coal():
    """
    Real Name: Resource extraction Coal
    Original Eqn: MIN(Extraction capacity installed Coal, ZIDZ(Extraction capacity installed Coal*Discovered resources reserve base Coal\ , Extraction capacity installed Coal*Average Rb over P Coal))
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.minimum(
        extraction_capacity_installed_coal(),
        functions.zidz(
            extraction_capacity_installed_coal() * discovered_resources_reserve_base_coal(),
            extraction_capacity_installed_coal() * average_rb_over_p_coal()))


@cache('step')
def resource_extraction_oil():
    """
    Real Name: Resource extraction Oil
    Original Eqn: MIN(Extraction capacity installed Oil, ZIDZ(Extraction capacity installed Oil*Discovered resources reserve base Oil\ , Extraction capacity installed Oil*Average Rb over P Oil))
    Units: bbtu/year
    Limits: (None, None)
    Type: component


    """
    return np.minimum(
        extraction_capacity_installed_oil(),
        functions.zidz(
            extraction_capacity_installed_oil() * discovered_resources_reserve_base_oil(),
            extraction_capacity_installed_oil() * average_rb_over_p_oil()))


@cache('run')
def time_for_deteriation_of_unused_capacity_biofuels():
    """
    Real Name: Time for deteriation of unused capacity Biofuels
    Original Eqn: 25.9823
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 25.9823


@cache('run')
def time_for_deteriation_of_unused_capacity_coal():
    """
    Real Name: Time for deteriation of unused capacity Coal
    Original Eqn: 25.9823
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 25.9823


@cache('run')
def time_for_deteriation_of_unused_capacity_gas():
    """
    Real Name: Time for deteriation of unused capacity Gas
    Original Eqn: 25.9823
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 25.9823


@cache('run')
def time_for_deteriation_of_unused_capacity_oil():
    """
    Real Name: Time for deteriation of unused capacity Oil
    Original Eqn: 25
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 25


@cache('run')
def time_for_deteriation_of_unused_capacity_other_renewables():
    """
    Real Name: Time for deteriation of unused capacity other Renewables
    Original Eqn: 25.9823
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 25.9823


@cache('run')
def time_for_deteriation_of_unused_capacity_nuclear():
    """
    Real Name: Time for deteriation of unused capacity Nuclear
    Original Eqn: 25.9823
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 25.9823


@cache('run')
def total_export_biofuels():
    """
    Real Name: Total export Biofuels
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def total_export_coal():
    """
    Real Name: Total export Coal
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def total_export_oil():
    """
    Real Name: Total export Oil
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def total_import_biofuels():
    """
    Real Name: Total import Biofuels
    Original Eqn: 0
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def total_import_coal():
    """
    Real Name: Total import Coal
    Original Eqn: 1.42463e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 1.42463e+06


@cache('run')
def total_import_oil():
    """
    Real Name: Total import Oil
    Original Eqn: 4.56357e+06
    Units: bbtu/year
    Limits: (None, None)
    Type: constant


    """
    return 4.56357e+06


@cache('run')
def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 2055
    Units: year
    Limits: (None, None)
    Type: constant

    The final time for the simulation.
    """
    return 2055


@cache('run')
def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 2015
    Units: year
    Limits: (None, None)
    Type: constant

    The initial time for the simulation.
    """
    return 2015


@cache('run')
def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: 0.25
    Units: year
    Limits: (0.0, None)
    Type: constant

    The frequency with which output is stored.
    """
    return 0.25


@cache('run')
def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 0.0625
    Units: year
    Limits: (0.0, None)
    Type: constant

    The time step for the simulation.
    """
    return 0.0625


delay_cumulative_extracted_fuel_gas_short_forecasting_period_initial_cumulative_extraction_fuel_gas_delay_order_forecasts = functions.Delay(
    lambda: cumulative_extracted_fuel_gas(), lambda: short_forecasting_period(),
    lambda: initial_cumulative_extraction_fuel_gas(), lambda: delay_order_forecasts())

integ_average_normalised_learning_curve_on_costs_coal = functions.Integ(
    lambda: change_in_average_learning_curve_parameter_coal(),
    lambda: initial_average_normalised_learning_curve_on_costs_coal())

integ_average_normalised_learning_curve_on_costs_gas = functions.Integ(
    lambda: change_in_average_learning_curve_parameter_gas(),
    lambda: initial_average_normalised_learning_curve_on_costs_gas())

integ_average_normalised_learning_curve_on_costs_oil = functions.Integ(
    lambda: change_in_average_learning_curve_parameter_oil(),
    lambda: initial_average_normalised_learning_curve_on_costs_oil())

delay_cumulative_extracted_fuel_coal_short_forecasting_period_initial_cumulative_extraction_fuel_coal_delay_order_forecasts = functions.Delay(
    lambda: cumulative_extracted_fuel_coal(), lambda: short_forecasting_period(),
    lambda: initial_cumulative_extraction_fuel_coal(), lambda: delay_order_forecasts())


integ_normalised_costs_relative_in_relation_to_learning_effects_t1_gas = functions.Integ(lambda: normalised_costs_relative_in_relation_to_learning_effects_gas()-normalised_costs_relative_in_relation_to_learning_t1_gas(), lambda: initial_normalised_costs_relative_in_relation_to_learning_effects_gas())

delay_cumulative_extracted_fuel_oil_short_forecasting_period_initial_cumulative_extraction_fuel_oil_delay_order_forecasts = functions.Delay(
    lambda: cumulative_extracted_fuel_oil(), lambda: short_forecasting_period(),
    lambda: initial_cumulative_extraction_fuel_oil(), lambda: delay_order_forecasts())


integ_normalised_costs_relative_in_relation_to_learning_effects_t1_oil = functions.Integ(lambda: normalised_costs_relative_in_relation_to_learning_effects_oil()-normalised_costs_relative_in_relation_to_learning_t1_oil(), lambda: initial_normalised_costs_relative_in_relation_to_learning_effects_oil())


integ_normalised_costs_relative_in_relation_to_learning_effects_t1_coal = functions.Integ(lambda: normalised_costs_relative_in_relation_to_learning_effects_coal()-normalised_costs_relative_in_relation_to_learning_t1_coal(), lambda: initial_normalised_costs_relative_in_relation_to_learning_effects_coal())

delay_npmaximum0future_shortage_effect_delay_time_decoupling_due_to_shortage_initial_decoupling_effect_materializing_delay_order_decoupling_due_to_shortage = functions.Delay(
    lambda: np.maximum(0, future_shortage_effect()),
    lambda: delay_time_decoupling_due_to_shortage(),
    lambda: initial_decoupling_effect_materializing(),
    lambda: delay_order_decoupling_due_to_shortage())

delay_npmaximum0new_extraction_capacity_proposed_nuclear_delay_time_new_capacity_nuclear_initial_completing_new_extraction_capacity_nuclear_delay_order_new_capacity_nuclear = functions.Delay(
    lambda: np.maximum(0, new_extraction_capacity_proposed_nuclear()),
    lambda: delay_time_new_capacity_nuclear(),
    lambda: initial_completing_new_extraction_capacity_nuclear(),
    lambda: delay_order_new_capacity_nuclear())

delay_npmaximum0new_extraction_capacity_proposed_oil_delay_time_new_capacity_oil_initial_completing_new_extraction_capacity_oil_delay_order_new_capacity_oil = functions.Delay(
    lambda: np.maximum(0, new_extraction_capacity_proposed_oil()),
    lambda: delay_time_new_capacity_oil(),
    lambda: initial_completing_new_extraction_capacity_oil(),
    lambda: delay_order_new_capacity_oil())

delay_npmaximum0new_extraction_capacity_proposed_other_renewables_delay_time_new_capacity_other_renewables_initial_completing_new_extraction_capacity_other_renewables_delay_order_new_capacity_other_renewables = functions.Delay(
    lambda: np.maximum(0, new_extraction_capacity_proposed_other_renewables()),
    lambda: delay_time_new_capacity_other_renewables(),
    lambda: initial_completing_new_extraction_capacity_other_renewables(),
    lambda: delay_order_new_capacity_other_renewables())

delay_npmaximum0new_extraction_capacity_proposed_biofuels_delay_time_new_capacity_biofuels_initial_completing_new_extraction_capacity_biofuels_delay_order_new_capacity_biofuels = functions.Delay(
    lambda: np.maximum(0, new_extraction_capacity_proposed_biofuels()),
    lambda: delay_time_new_capacity_biofuels(),
    lambda: initial_completing_new_extraction_capacity_biofuels(),
    lambda: delay_order_new_capacity_biofuels())

delay_npmaximum0new_extraction_capacity_proposed_gas_delay_time_new_capacity_gas_initial_completing_new_extraction_capacity_gas_delay_order_new_capacity_gas = functions.Delay(
    lambda: np.maximum(0, new_extraction_capacity_proposed_gas()),
    lambda: delay_time_new_capacity_gas(),
    lambda: initial_completing_new_extraction_capacity_gas(),
    lambda: delay_order_new_capacity_gas())

delay_npmaximum0new_extraction_capacity_proposed_coal_delay_time_new_capacity_coal_initial_completing_new_extraction_capacity_coal_delay_order_new_capacity_coal = functions.Delay(
    lambda: np.maximum(0, new_extraction_capacity_proposed_coal()),
    lambda: delay_time_new_capacity_coal(),
    lambda: initial_completing_new_extraction_capacity_coal(),
    lambda: delay_order_new_capacity_coal())

integ_eroi_resources_coal = functions.Integ(lambda: change_in_eroi_due_to_reserve_depletion_coal(),
                                            lambda: initial_eroi_resources_coal())

integ_eroi_resources_gas = functions.Integ(lambda: change_in_eroi_due_to_reserve_depletion_gas(),
                                           lambda: initial_eroi_gas())

integ_eroi_resources_oil = functions.Integ(lambda: change_in_eroi_due_to_reserve_depletion_oil(),
                                           lambda: initial_eroi_resources_oil())

integ_average_normalised_learning_curve_on_costs_biofuels = functions.Integ(
    lambda: change_in_average_learning_curve_parameter_biofuels(),
    lambda: initial_average_normalised_learning_curve_on_costs_biofuels())

integ_average_normalised_learning_curve_on_costs_other_renewables = functions.Integ(
    lambda: change_in_average_learning_curve_parameter_other_renewables(),
    lambda: initial_average_normalised_learning_curve_on_costs_other_renewables())

integ_average_normalised_learning_curve_on_costs_nuclear = functions.Integ(
    lambda: change_in_average_learning_curve_parameter_nuclear(),
    lambda: initial_average_normalised_learning_curve_on_costs_nuclear())

delay_cumulative_extracted_fuel_biofuels_short_forecasting_period_initial_cumulative_extraction_fuel_biofuels_delay_order_forecasts = functions.Delay(
    lambda: cumulative_extracted_fuel_biofuels(), lambda: short_forecasting_period(),
    lambda: initial_cumulative_extraction_fuel_biofuels(), lambda: delay_order_forecasts())

integ_cumulative_extracted_fuel_nuclear = functions.Integ(
    lambda: extraction_capacity_installed_nuclear(),
    lambda: initial_cumulative_extraction_fuel_nuclear())

integ_cumulative_extracted_fuel_other_renewables = functions.Integ(
    lambda: extraction_capacity_installed_other_renewables(),
    lambda: initial_cumulative_extraction_fuel_other_renewables())

integ_cumulative_extracted_fuel_biofuels = functions.Integ(
    lambda: extraction_capacity_installed_biofuels(),
    lambda: initial_cumulative_extraction_fuel_biofuels())

integ_cumulative_extracted_fuel_coal = functions.Integ(
    lambda: extraction_capacity_installed_coal(),
    lambda: initial_cumulative_extraction_fuel_coal())

integ_cumulative_extracted_fuel_gas = functions.Integ(
    lambda: extraction_capacity_installed_gas(), lambda: initial_cumulative_extraction_fuel_gas())

integ_cumulative_extracted_fuel_oil = functions.Integ(
    lambda: extraction_capacity_installed_oil(), lambda: initial_cumulative_extraction_fuel_oil())

delay_cumulative_extracted_fuel_other_renewables_short_forecasting_period_initial_cumulative_extraction_fuel_other_renewables_delay_order_forecasts = functions.Delay(
    lambda: cumulative_extracted_fuel_other_renewables(), lambda: short_forecasting_period(),
    lambda: initial_cumulative_extraction_fuel_other_renewables(), lambda: delay_order_forecasts())

delay_cumulative_extracted_fuel_nuclear_short_forecasting_period_initial_cumulative_extraction_fuel_nuclear_delay_order_forecasts = functions.Delay(
    lambda: cumulative_extracted_fuel_nuclear(), lambda: short_forecasting_period(),
    lambda: initial_cumulative_extraction_fuel_nuclear(), lambda: delay_order_forecasts())


integ_normalised_costs_relative_in_relation_to_learning_effects_t1_other_renewables = functions.Integ(lambda: normalised_costs_relative_in_relation_to_learning_effects_other_renewables()-normalised_costs_relative_in_relation_to_learning_t1_other_renewables(), lambda: initial_normalised_costs_relative_in_relation_to_learning_effects_other_renewables())


integ_normalised_costs_relative_in_relation_to_learning_effects_t1_biofuels = functions.Integ(lambda: normalised_costs_relative_in_relation_to_learning_effects_biofuels()-normalised_costs_relative_in_relation_to_learning_t1_biofuels(), lambda: initial_normalised_costs_relative_in_relation_to_learning_effects_biofuels())


integ_normalised_costs_relative_in_relation_to_learning_effects_t1_nuclear = functions.Integ(lambda: normalised_costs_relative_in_relation_to_learning_effects_nuclear()-normalised_costs_relative_in_relation_to_learning_t1_nuclear(), lambda: initial_normalised_costs_relative_in_relation_to_learning_effects_nuclear())

integ_unit_costs_gas = functions.Integ(lambda: change_in_unit_costs_gas(),
                                       lambda: initial_unit_costs_gas())

integ_unit_costs_oil = functions.Integ(lambda: change_in_unit_costs_oil(),
                                       lambda: initial_unit_costs_oil())

integ_unit_costs_other_renewables = functions.Integ(
    lambda: change_in_unit_costs_other_renewables(), lambda: initial_unit_costs_other_renewables())

integ_unit_costs_nuclear = functions.Integ(lambda: change_in_unit_costs_nuclear(),
                                           lambda: initial_unit_costs_nuclear())

integ_eroei_biofuels = functions.Integ(lambda: change_in_eroei_biofuels(),
                                       lambda: initial_eroei_biofuels())

integ_eroei_other_renewables = functions.Integ(lambda: change_in_eroei_other_renewables(),
                                               lambda: initial_eroei_other_renewables())

integ_unit_costs_coal = functions.Integ(lambda: change_in_unit_costs_coal(),
                                        lambda: initial_unit_costs_coal())

integ_long_term_normalized_profits_nuclear = functions.Integ(
    lambda: change_in_normalized_relative_profits_nuclear(),
    lambda: initial_long_term_normalized_profits_nuclear())

integ_unit_costs_biofuels = functions.Integ(lambda: change_in_unit_costs_biofuels(),
                                            lambda: initial_unit_costs_biofuels())

integ_long_term_normalized_profits_coal = functions.Integ(
    lambda: change_in_normalized_relative_profits_coal(),
    lambda: initial_long_term_normalized_profits_coal())

integ_long_term_normalized_profits_gas = functions.Integ(
    lambda: change_in_normalized_relative_profits_gas(),
    lambda: initial_long_term_normalized_profits_gas())

integ_long_term_normalized_profits_other_renewables = functions.Integ(
    lambda: change_in_normalized_relative_profits_other_renewables(),
    lambda: initial_long_term_normalized_profits_other_renewables())

integ_long_term_normalized_profits_biofuels = functions.Integ(
    lambda: change_in_normalized_relative_profits_biofuels(),
    lambda: initial_long_term_normalized_profits_biofuels())

integ_long_term_normalized_profits_oil = functions.Integ(
    lambda: change_in_normalized_relative_profits_oil(),
    lambda: initial_long_term_normalized_profits_oil())

integ_undiscovered_resources_oil = functions.Integ(
    lambda: -increase_in_discovered_and_technically_recoverable_resources_oil(),
    lambda: initial_undiscovered_resources_oil())


integ_discovered_resources_reserve_base_gas = functions.Integ(lambda: increase_in_discovered_and_technically_recoverable_gas()-non_stockpiled_gas_extraction(), lambda: initial_reserve_base_gas())

integ_undiscovered_resources_gas = functions.Integ(
    lambda: -increase_in_discovered_and_technically_recoverable_gas(),
    lambda: initial_undiscovered_resources_gas())

integ_undiscovered_resources_coal = functions.Integ(
    lambda: -increase_in_discovered_and_technically_recoverable_resources_coal(),
    lambda: initial_undiscovered_resources_coal())

integ_effect_of_supply_shortage_on_decoupling = functions.Integ(
    lambda: decoupling_effect_materializing() - decrease_in_shortage_effect(),
    lambda: initial_effect_of_supply_shortage_on_decoupling())


integ_extraction_capacity_installed_gas = functions.Integ(lambda: completing_new_extraction_capacity_gas()+recommissioning_of_capacity_gas()-mothballing_of_capacity_gas(), lambda: initial_extraction_capacity_gas())


integ_mothballed_capacity_coal = functions.Integ(lambda: mothballing_of_capacity_coal()-deterioration_of_unused_capacity_coal()-recommissioning_of_capacity_coal(), lambda: initial_mothballed_capacity_coal())


integ_mothballed_capacity_oil = functions.Integ(lambda: mothballing_of_capacity_oil()-deterioration_of_unused_capacity_oil()-recommissioning_of_capacity_oil(), lambda: initial_mothballed_capacity_oil())


integ_mothballed_capacity_gas = functions.Integ(lambda: mothballing_of_capacity_gas()-deterioration_of_unused_capacity_gas()-recommissioning_of_capacity_gas(), lambda: initial_mothballed_capacity_gas())


integ_energy_stocks_coal = functions.Integ(lambda: energy_import_coal()+resource_extraction_coal()-energy_export_coal()-resource_consumption_coal(), lambda: initial_energy_stocks_coal())


integ_energy_stocks_oil = functions.Integ(lambda: energy_import_oil()+resource_extraction_oil()-energy_export_oil()-resource_consumption_oil(), lambda: initial_energy_stocks_oil())


integ_energy_stocks_biofuels = functions.Integ(lambda: energy_import_biofuels()+production_of_biofuels()-energy_export_biofuels()-resource_consumption_biofuels(), lambda: initial_energy_stocks_biofuels())

integ_future_effect_of_shortage_on_decoupling = functions.Integ(
    lambda: future_shortage_effect() - decoupling_effect_materializing(),
    lambda: initial_shortage_effect_on_decoupling())

integ_gdp = functions.Integ(lambda: increase_in_gdp(), lambda: initial_gdp())

integ_energy_intensity_gdp = functions.Integ(lambda: -decrease_energy_intensity_gdp(),
                                             lambda: initial_energy_intensity_gdp())


integ_discovered_resources_reserve_base_coal = functions.Integ(lambda: increase_in_discovered_and_technically_recoverable_resources_coal()-resource_extraction_coal(), lambda: initial_reserve_base_coal())


integ_discovered_resources_reserve_base_oil = functions.Integ(lambda: increase_in_discovered_and_technically_recoverable_resources_oil()-resource_extraction_oil(), lambda: initial_reserve_base_oil())


integ_extraction_capacity_in_preparation_biofuels = functions.Integ(lambda: new_extraction_capacity_proposed_biofuels()-completing_new_extraction_capacity_biofuels(), lambda: initial_extraction_capacity_in_preparation_biofuels())

integ_extraction_capacity_in_preparation_coal = functions.Integ(
    lambda: new_extraction_capacity_proposed_coal() - completing_new_extraction_capacity_coal(),
    lambda: initial_extraction_capacity_in_preparation_coal())

integ_extraction_capacity_in_preparation_gas = functions.Integ(
    lambda: new_extraction_capacity_proposed_gas() - completing_new_extraction_capacity_gas(),
    lambda: initial_extraction_capacity_in_preparation_gas())

integ_extraction_capacity_in_preparation_oil = functions.Integ(
    lambda: new_extraction_capacity_proposed_oil() - completing_new_extraction_capacity_oil(),
    lambda: initial_extraction_capacity_in_preparation_oil())


integ_extraction_capacity_in_preparation_other_renewables = functions.Integ(lambda: new_extraction_capacity_proposed_other_renewables()-completing_new_extraction_capacity_other_renewables(), lambda: initial_extraction_capacity_in_preparation_other_renewables())


integ_extraction_capacity_in_preparation_nuclear = functions.Integ(lambda: new_extraction_capacity_proposed_nuclear()-completing_new_extraction_capacity_nuclear(), lambda: initial_extraction_capacity_in_preparation_nuclear())


integ_extraction_capacity_installed_biofuels = functions.Integ(lambda: completing_new_extraction_capacity_biofuels()+recommissioning_of_capacity_biofuels()-mothballing_of_capacity_biofuels(), lambda: initial_extraction_capacity_biofuels())


integ_extraction_capacity_installed_coal = functions.Integ(lambda: completing_new_extraction_capacity_coal()+recommissioning_of_capacity_coal()-mothballing_of_capacity_coal(), lambda: initial_extraction_capacity_coal())


integ_extraction_capacity_installed_oil = functions.Integ(lambda: completing_new_extraction_capacity_oil()+recommissioning_of_capacity_oil()-mothballing_of_capacity_oil(), lambda: initial_extraction_capacity_oil())


integ_extraction_capacity_installed_other_renewables = functions.Integ(lambda: completing_new_extraction_capacity_other_renewables()+recommissioning_of_capacity_other_renewables()-mothballing_of_capacity_other_renewables(), lambda: initial_extraction_capacity_other_renewables())


integ_extraction_capacity_installed_nuclear = functions.Integ(lambda: completing_new_extraction_capacity_nuclear()+recommissioning_of_capacity_nuclear()-mothballing_of_capacity_nuclear(), lambda: initial_extraction_capacity_nuclear())


integ_mothballed_capacity_biofuels = functions.Integ(lambda: mothballing_of_capacity_biofuels()-deterioration_of_unused_capacity_biofuels()-recommissioning_of_capacity_biofuels(), lambda: initial_mothballed_capacity_biofuels())


integ_mothballed_capacity_other_renewables = functions.Integ(lambda: mothballing_of_capacity_other_renewables()-deterioration_of_unused_capacity_other_renewables()-recommissioning_of_capacity_other_renewables(), lambda: initial_mothballed_capacity_other_renewables())


integ_mothballed_capacity_nuclear = functions.Integ(lambda: mothballing_of_capacity_nuclear()-deterioration_of_unused_capacity_nuclear()-recommissioning_of_capacity_nuclear(), lambda: initial_mothballed_capacity_nuclear())
