"""
Python model "EnergyPriceModelV3.py"
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
    'Changes in fictional prices Nuclear AP':
    'changes_in_fictional_prices_nuclear_ap',
    'Energy resource prices Nuclear AP':
    'energy_resource_prices_nuclear_ap',
    'Change in energy resource prices Nuclear ME':
    'change_in_energy_resource_prices_nuclear_me',
    'Change in energy resource prices Gas AF':
    'change_in_energy_resource_prices_gas_af',
    'Change in energy resource prices Gas AP':
    'change_in_energy_resource_prices_gas_ap',
    'Changes in fictional prices Gas AP':
    'changes_in_fictional_prices_gas_ap',
    'Energy resource prices Gas ME':
    'energy_resource_prices_gas_me',
    'Change in energy resource prices Gas ME':
    'change_in_energy_resource_prices_gas_me',
    'Change in energy resource prices other Renewables AP':
    'change_in_energy_resource_prices_other_renewables_ap',
    'Changes in fictional prices other Renewables AP':
    'changes_in_fictional_prices_other_renewables_ap',
    'Energy resource prices other Renewables AP':
    'energy_resource_prices_other_renewables_ap',
    'Change in energy resource prices Nuclear AF':
    'change_in_energy_resource_prices_nuclear_af',
    'Change in energy resource prices Nuclear AP':
    'change_in_energy_resource_prices_nuclear_ap',
    'Energy resource prices Nuclear AF':
    'energy_resource_prices_nuclear_af',
    'Fictional prices Nuclear AF':
    'fictional_prices_nuclear_af',
    'Fictional prices Nuclear AP':
    'fictional_prices_nuclear_ap',
    'Changes in fictional prices Nuclear ME':
    'changes_in_fictional_prices_nuclear_me',
    'Changes in fictional prices Gas AF':
    'changes_in_fictional_prices_gas_af',
    'Energy resource prices Gas AF':
    'energy_resource_prices_gas_af',
    'Energy resource prices Gas AP':
    'energy_resource_prices_gas_ap',
    'Change in energy resource prices other Renewables AF':
    'change_in_energy_resource_prices_other_renewables_af',
    'Changes in fictional prices Gas ME':
    'changes_in_fictional_prices_gas_me',
    'Relative change in fictional prices Gas ME':
    'relative_change_in_fictional_prices_gas_me',
    'Fictional prices Gas ME':
    'fictional_prices_gas_me',
    'Change in energy resource prices other Renewables ME':
    'change_in_energy_resource_prices_other_renewables_me',
    'Changes in fictional prices Nuclear AF':
    'changes_in_fictional_prices_nuclear_af',
    'Energy resource prices other Renewables ME':
    'energy_resource_prices_other_renewables_me',
    'Fictional prices other Renewables ME':
    'fictional_prices_other_renewables_me',
    'Initial energy resource prices Nuclear AF':
    'initial_energy_resource_prices_nuclear_af',
    'Initial energy resource prices Nuclear AP':
    'initial_energy_resource_prices_nuclear_ap',
    'Energy resource prices Nuclear ME':
    'energy_resource_prices_nuclear_me',
    'Fictional prices Nuclear ME':
    'fictional_prices_nuclear_me',
    'Fictional prices Gas AF':
    'fictional_prices_gas_af',
    'Fictional prices Gas AP':
    'fictional_prices_gas_ap',
    'Changes in fictional prices other Renewables AF':
    'changes_in_fictional_prices_other_renewables_af',
    'Energy resource prices other Renewables AF':
    'energy_resource_prices_other_renewables_af',
    'Fictional prices other Renewables AF':
    'fictional_prices_other_renewables_af',
    'Fictional prices other Renewables AP':
    'fictional_prices_other_renewables_ap',
    'Changes in fictional prices other Renewables ME':
    'changes_in_fictional_prices_other_renewables_me',
    'Initial shadow fictional prices other Renewables AP':
    'initial_shadow_fictional_prices_other_renewables_ap',
    'Relative change in fictional prices other Renewables AP':
    'relative_change_in_fictional_prices_other_renewables_ap',
    'Initial energy resource prices other Renewables ME':
    'initial_energy_resource_prices_other_renewables_me',
    'Initial shadow fictional prices Nuclear AF':
    'initial_shadow_fictional_prices_nuclear_af',
    'Initial shadow fictional prices Nuclear AP':
    'initial_shadow_fictional_prices_nuclear_ap',
    'Relative change in fictional prices Nuclear AP':
    'relative_change_in_fictional_prices_nuclear_ap',
    'Initial energy resource prices Nuclear ME':
    'initial_energy_resource_prices_nuclear_me',
    'Initial energy resource prices Gas AF':
    'initial_energy_resource_prices_gas_af',
    'Initial energy resource prices Gas AP':
    'initial_energy_resource_prices_gas_ap',
    'Initial shadow fictional prices Gas AP':
    'initial_shadow_fictional_prices_gas_ap',
    'Relative change in fictional prices Gas AP':
    'relative_change_in_fictional_prices_gas_ap',
    'Initial energy resource prices Gas ME':
    'initial_energy_resource_prices_gas_me',
    'Initial energy resource prices other Renewables AP':
    'initial_energy_resource_prices_other_renewables_ap',
    'Shadow fictional prices Gas ME':
    'shadow_fictional_prices_gas_me',
    'Shadow fictional prices other Renewables AF':
    'shadow_fictional_prices_other_renewables_af',
    'Shadow fictional prices other Renewables AP':
    'shadow_fictional_prices_other_renewables_ap',
    'Initial shadow fictional prices other Renewables ME':
    'initial_shadow_fictional_prices_other_renewables_me',
    'Relative change in fictional prices Nuclear AF':
    'relative_change_in_fictional_prices_nuclear_af',
    'Shadow fictional prices Nuclear AF':
    'shadow_fictional_prices_nuclear_af',
    'Shadow fictional prices Nuclear AP':
    'shadow_fictional_prices_nuclear_ap',
    'Initial shadow fictional prices Nuclear ME':
    'initial_shadow_fictional_prices_nuclear_me',
    'Initial shadow fictional prices Gas AF':
    'initial_shadow_fictional_prices_gas_af',
    'Relative change in fictional prices Gas AF':
    'relative_change_in_fictional_prices_gas_af',
    'Shadow fictional prices Gas AF':
    'shadow_fictional_prices_gas_af',
    'Initial energy resource prices other Renewables AF':
    'initial_energy_resource_prices_other_renewables_af',
    'Initial shadow fictional prices Gas ME':
    'initial_shadow_fictional_prices_gas_me',
    'Relative change in fictional prices other Renewables AF':
    'relative_change_in_fictional_prices_other_renewables_af',
    'Relative change in fictional prices other Renewables ME':
    'relative_change_in_fictional_prices_other_renewables_me',
    'Relative change in fictional prices Nuclear ME':
    'relative_change_in_fictional_prices_nuclear_me',
    'Shadow fictional prices Nuclear ME':
    'shadow_fictional_prices_nuclear_me',
    'Shadow fictional prices other Renewables ME':
    'shadow_fictional_prices_other_renewables_me',
    'Initial shadow fictional prices other Renewables AF':
    'initial_shadow_fictional_prices_other_renewables_af',
    'Shadow fictional prices Gas AP':
    'shadow_fictional_prices_gas_ap',
    'Change in energy resource prices Biofuels':
    'change_in_energy_resource_prices_biofuels',
    'Change in energy resource prices Coal':
    'change_in_energy_resource_prices_coal',
    'Change in energy resource prices Gas NA':
    'change_in_energy_resource_prices_gas_na',
    'Change in energy resource prices Gas SCA':
    'change_in_energy_resource_prices_gas_sca',
    'Change in energy resource prices Gas E':
    'change_in_energy_resource_prices_gas_e',
    'Change in energy resource prices Gas CIS':
    'change_in_energy_resource_prices_gas_cis',
    'Change in energy resource prices Gas':
    'change_in_energy_resource_prices_gas',
    'Change in energy resource prices Nuclear NA':
    'change_in_energy_resource_prices_nuclear_na',
    'Change in energy resource prices Nuclear SCA':
    'change_in_energy_resource_prices_nuclear_sca',
    'Change in energy resource prices Nuclear E':
    'change_in_energy_resource_prices_nuclear_e',
    'Change in energy resource prices Nuclear CIS':
    'change_in_energy_resource_prices_nuclear_cis',
    'Change in energy resource prices Nuclear':
    'change_in_energy_resource_prices_nuclear',
    'Change in energy resource prices Oil':
    'change_in_energy_resource_prices_oil',
    'Change in energy resource prices other Renewables NA':
    'change_in_energy_resource_prices_other_renewables_na',
    'Change in energy resource prices other Renewables SCA':
    'change_in_energy_resource_prices_other_renewables_sca',
    'Change in energy resource prices other Renewables E':
    'change_in_energy_resource_prices_other_renewables_e',
    'Change in energy resource prices other Renewables CIS':
    'change_in_energy_resource_prices_other_renewables_cis',
    'Change in energy resource prices other Renewables':
    'change_in_energy_resource_prices_other_renewables',
    'Changes in fictional prices Biofuels':
    'changes_in_fictional_prices_biofuels',
    'Changes in fictional prices Coal':
    'changes_in_fictional_prices_coal',
    'Changes in fictional prices Gas NA':
    'changes_in_fictional_prices_gas_na',
    'Changes in fictional prices Gas SCA':
    'changes_in_fictional_prices_gas_sca',
    'Changes in fictional prices Gas E':
    'changes_in_fictional_prices_gas_e',
    'Changes in fictional prices Gas CIS':
    'changes_in_fictional_prices_gas_cis',
    'Changes in fictional prices Gas':
    'changes_in_fictional_prices_gas',
    'Changes in fictional prices Nuclear NA':
    'changes_in_fictional_prices_nuclear_na',
    'Changes in fictional prices Nuclear SCA':
    'changes_in_fictional_prices_nuclear_sca',
    'Changes in fictional prices Nuclear E':
    'changes_in_fictional_prices_nuclear_e',
    'Changes in fictional prices Nuclear CIS':
    'changes_in_fictional_prices_nuclear_cis',
    'Changes in fictional prices Nuclear':
    'changes_in_fictional_prices_nuclear',
    'Changes in fictional prices Oil':
    'changes_in_fictional_prices_oil',
    'Changes in fictional prices other Renewables NA':
    'changes_in_fictional_prices_other_renewables_na',
    'Changes in fictional prices other Renewables SCA':
    'changes_in_fictional_prices_other_renewables_sca',
    'Changes in fictional prices other Renewables E':
    'changes_in_fictional_prices_other_renewables_e',
    'Changes in fictional prices other Renewables CIS':
    'changes_in_fictional_prices_other_renewables_cis',
    'Changes in fictional prices other Renewables':
    'changes_in_fictional_prices_other_renewables',
    'Energy resource prices Biofuels':
    'energy_resource_prices_biofuels',
    'Energy resource prices Coal':
    'energy_resource_prices_coal',
    'Energy resource prices Gas NA':
    'energy_resource_prices_gas_na',
    'Energy resource prices Gas SCA':
    'energy_resource_prices_gas_sca',
    'Energy resource prices Gas E':
    'energy_resource_prices_gas_e',
    'Energy resource prices Gas CIS':
    'energy_resource_prices_gas_cis',
    'Energy resource prices Gas':
    'energy_resource_prices_gas',
    'Energy resource prices Nuclear NA':
    'energy_resource_prices_nuclear_na',
    'Energy resource prices Nuclear SCA':
    'energy_resource_prices_nuclear_sca',
    'Energy resource prices Nuclear E':
    'energy_resource_prices_nuclear_e',
    'Energy resource prices Nuclear CIS':
    'energy_resource_prices_nuclear_cis',
    'Energy resource prices Nuclear':
    'energy_resource_prices_nuclear',
    'Energy resource prices Oil':
    'energy_resource_prices_oil',
    'Energy resource prices other Renewables NA':
    'energy_resource_prices_other_renewables_na',
    'Energy resource prices other Renewables SCA':
    'energy_resource_prices_other_renewables_sca',
    'Energy resource prices other Renewables E':
    'energy_resource_prices_other_renewables_e',
    'Energy resource prices other Renewables CIS':
    'energy_resource_prices_other_renewables_cis',
    'Energy resource prices other Renewables':
    'energy_resource_prices_other_renewables',
    'Fictional prices Biofuels':
    'fictional_prices_biofuels',
    'Fictional prices Coal':
    'fictional_prices_coal',
    'Fictional prices Gas NA':
    'fictional_prices_gas_na',
    'Fictional prices Gas SCA':
    'fictional_prices_gas_sca',
    'Fictional prices Gas E':
    'fictional_prices_gas_e',
    'Fictional prices Gas CIS':
    'fictional_prices_gas_cis',
    'Fictional prices Gas':
    'fictional_prices_gas',
    'Fictional prices Nuclear NA':
    'fictional_prices_nuclear_na',
    'Fictional prices Nuclear SCA':
    'fictional_prices_nuclear_sca',
    'Fictional prices Nuclear E':
    'fictional_prices_nuclear_e',
    'Fictional prices Nuclear CIS':
    'fictional_prices_nuclear_cis',
    'Fictional prices Nuclear':
    'fictional_prices_nuclear',
    'Fictional prices Oil':
    'fictional_prices_oil',
    'Fictional prices other Renewables NA':
    'fictional_prices_other_renewables_na',
    'Fictional prices other Renewables SCA':
    'fictional_prices_other_renewables_sca',
    'Fictional prices other Renewables E':
    'fictional_prices_other_renewables_e',
    'Fictional prices other Renewables CIS':
    'fictional_prices_other_renewables_cis',
    'Fictional prices other Renewables':
    'fictional_prices_other_renewables',
    'Initial energy resource prices Biofuels':
    'initial_energy_resource_prices_biofuels',
    'Initial energy resource prices Coal':
    'initial_energy_resource_prices_coal',
    'Initial energy resource prices Gas NA':
    'initial_energy_resource_prices_gas_na',
    'Initial energy resource prices Gas SCA':
    'initial_energy_resource_prices_gas_sca',
    'Initial energy resource prices Gas E':
    'initial_energy_resource_prices_gas_e',
    'Initial energy resource prices Gas CIS':
    'initial_energy_resource_prices_gas_cis',
    'Initial energy resource prices Gas':
    'initial_energy_resource_prices_gas',
    'Initial energy resource prices Nuclear NA':
    'initial_energy_resource_prices_nuclear_na',
    'Initial energy resource prices Nuclear SCA':
    'initial_energy_resource_prices_nuclear_sca',
    'Initial energy resource prices Nuclear E':
    'initial_energy_resource_prices_nuclear_e',
    'Initial energy resource prices Nuclear CIS':
    'initial_energy_resource_prices_nuclear_cis',
    'Initial energy resource prices Nuclear':
    'initial_energy_resource_prices_nuclear',
    'Initial energy resource prices Oil':
    'initial_energy_resource_prices_oil',
    'Initial energy resource prices other Renewables NA':
    'initial_energy_resource_prices_other_renewables_na',
    'Initial energy resource prices other Renewables SCA':
    'initial_energy_resource_prices_other_renewables_sca',
    'Initial energy resource prices other Renewables E':
    'initial_energy_resource_prices_other_renewables_e',
    'Initial energy resource prices other Renewables CIS':
    'initial_energy_resource_prices_other_renewables_cis',
    'Initial energy resource prices other Renewables':
    'initial_energy_resource_prices_other_renewables',
    'Initial shadow fictional prices Biofuels':
    'initial_shadow_fictional_prices_biofuels',
    'Initial shadow fictional prices Coal':
    'initial_shadow_fictional_prices_coal',
    'Initial shadow fictional prices Gas NA':
    'initial_shadow_fictional_prices_gas_na',
    'Initial shadow fictional prices Gas SCA':
    'initial_shadow_fictional_prices_gas_sca',
    'Initial shadow fictional prices Gas E':
    'initial_shadow_fictional_prices_gas_e',
    'Initial shadow fictional prices Gas CIS':
    'initial_shadow_fictional_prices_gas_cis',
    'Initial shadow fictional prices Gas':
    'initial_shadow_fictional_prices_gas',
    'Initial shadow fictional prices Nuclear NA':
    'initial_shadow_fictional_prices_nuclear_na',
    'Initial shadow fictional prices Nuclear SCA':
    'initial_shadow_fictional_prices_nuclear_sca',
    'Initial shadow fictional prices Nuclear E':
    'initial_shadow_fictional_prices_nuclear_e',
    'Initial shadow fictional prices Nuclear CIS':
    'initial_shadow_fictional_prices_nuclear_cis',
    'Initial shadow fictional prices Nuclear':
    'initial_shadow_fictional_prices_nuclear',
    'Initial shadow fictional prices Oil':
    'initial_shadow_fictional_prices_oil',
    'Initial shadow fictional prices other Renewables NA':
    'initial_shadow_fictional_prices_other_renewables_na',
    'Initial shadow fictional prices other Renewables SCA':
    'initial_shadow_fictional_prices_other_renewables_sca',
    'Initial shadow fictional prices other Renewables E':
    'initial_shadow_fictional_prices_other_renewables_e',
    'Initial shadow fictional prices other Renewables CIS':
    'initial_shadow_fictional_prices_other_renewables_cis',
    'Initial shadow fictional prices other Renewables':
    'initial_shadow_fictional_prices_other_renewables',
    'Relative change in fictional prices Biofuels':
    'relative_change_in_fictional_prices_biofuels',
    'Relative change in fictional prices Coal':
    'relative_change_in_fictional_prices_coal',
    'Relative change in fictional prices Gas NA':
    'relative_change_in_fictional_prices_gas_na',
    'Relative change in fictional prices Gas SCA':
    'relative_change_in_fictional_prices_gas_sca',
    'Relative change in fictional prices Gas E':
    'relative_change_in_fictional_prices_gas_e',
    'Relative change in fictional prices Gas CIS':
    'relative_change_in_fictional_prices_gas_cis',
    'Relative change in fictional prices Gas':
    'relative_change_in_fictional_prices_gas',
    'Relative change in fictional prices Nuclear NA':
    'relative_change_in_fictional_prices_nuclear_na',
    'Relative change in fictional prices Nuclear SCA':
    'relative_change_in_fictional_prices_nuclear_sca',
    'Relative change in fictional prices Nuclear E':
    'relative_change_in_fictional_prices_nuclear_e',
    'Relative change in fictional prices Nuclear CIS':
    'relative_change_in_fictional_prices_nuclear_cis',
    'Relative change in fictional prices Nuclear':
    'relative_change_in_fictional_prices_nuclear',
    'Relative change in fictional prices Oil':
    'relative_change_in_fictional_prices_oil',
    'Relative change in fictional prices other Renewables NA':
    'relative_change_in_fictional_prices_other_renewables_na',
    'Relative change in fictional prices other Renewables SCA':
    'relative_change_in_fictional_prices_other_renewables_sca',
    'Relative change in fictional prices other Renewables E':
    'relative_change_in_fictional_prices_other_renewables_e',
    'Relative change in fictional prices other Renewables CIS':
    'relative_change_in_fictional_prices_other_renewables_cis',
    'Relative change in fictional prices other Renewables':
    'relative_change_in_fictional_prices_other_renewables',
    'Shadow fictional prices Biofuels':
    'shadow_fictional_prices_biofuels',
    'Shadow fictional prices Coal':
    'shadow_fictional_prices_coal',
    'Shadow fictional prices Gas NA':
    'shadow_fictional_prices_gas_na',
    'Shadow fictional prices Gas SCA':
    'shadow_fictional_prices_gas_sca',
    'Shadow fictional prices Gas E':
    'shadow_fictional_prices_gas_e',
    'Shadow fictional prices Gas CIS':
    'shadow_fictional_prices_gas_cis',
    'Shadow fictional prices Gas':
    'shadow_fictional_prices_gas',
    'Shadow fictional prices Nuclear NA':
    'shadow_fictional_prices_nuclear_na',
    'Shadow fictional prices Nuclear SCA':
    'shadow_fictional_prices_nuclear_sca',
    'Shadow fictional prices Nuclear E':
    'shadow_fictional_prices_nuclear_e',
    'Shadow fictional prices Nuclear CIS':
    'shadow_fictional_prices_nuclear_cis',
    'Shadow fictional prices Nuclear':
    'shadow_fictional_prices_nuclear',
    'Shadow fictional prices Oil':
    'shadow_fictional_prices_oil',
    'Shadow fictional prices other Renewables NA':
    'shadow_fictional_prices_other_renewables_na',
    'Shadow fictional prices other Renewables SCA':
    'shadow_fictional_prices_other_renewables_sca',
    'Shadow fictional prices other Renewables E':
    'shadow_fictional_prices_other_renewables_e',
    'Shadow fictional prices other Renewables CIS':
    'shadow_fictional_prices_other_renewables_cis',
    'Shadow fictional prices other Renewables':
    'shadow_fictional_prices_other_renewables',
    'Short term period':
    'short_term_period',
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
def changes_in_fictional_prices_nuclear_ap():
    """
    Real Name: Changes in fictional prices Nuclear AP
    Original Eqn: (Fictional prices Nuclear AP-Shadow fictional prices Nuclear AP)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_nuclear_ap() -
            shadow_fictional_prices_nuclear_ap()) / short_term_period()


@cache('step')
def energy_resource_prices_nuclear_ap():
    """
    Real Name: Energy resource prices Nuclear AP
    Original Eqn: INTEG ( Change in energy resource prices Nuclear AP, Initial energy resource prices Nuclear AP)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_nuclear_ap()


@cache('step')
def change_in_energy_resource_prices_nuclear_me():
    """
    Real Name: Change in energy resource prices Nuclear ME
    Original Eqn: Energy resource prices Nuclear ME*Relative change in fictional prices Nuclear ME
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_nuclear_me() * relative_change_in_fictional_prices_nuclear_me()


@cache('step')
def change_in_energy_resource_prices_gas_af():
    """
    Real Name: Change in energy resource prices Gas AF
    Original Eqn: Energy resource prices Gas AF*Relative change in fictional prices Gas AF
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_gas_af() * relative_change_in_fictional_prices_gas_af()


@cache('step')
def change_in_energy_resource_prices_gas_ap():
    """
    Real Name: Change in energy resource prices Gas AP
    Original Eqn: Energy resource prices Gas AP*Relative change in fictional prices Gas AP
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_gas_ap() * relative_change_in_fictional_prices_gas_ap()


@cache('step')
def changes_in_fictional_prices_gas_ap():
    """
    Real Name: Changes in fictional prices Gas AP
    Original Eqn: (Fictional prices Gas AP-Shadow fictional prices Gas AP)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_gas_ap() - shadow_fictional_prices_gas_ap()) / short_term_period()


@cache('step')
def energy_resource_prices_gas_me():
    """
    Real Name: Energy resource prices Gas ME
    Original Eqn: INTEG ( Change in energy resource prices Gas ME, Initial energy resource prices Gas ME)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_gas_me()


@cache('step')
def change_in_energy_resource_prices_gas_me():
    """
    Real Name: Change in energy resource prices Gas ME
    Original Eqn: Energy resource prices Gas ME*Relative change in fictional prices Gas ME
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_gas_me() * relative_change_in_fictional_prices_gas_me()


@cache('step')
def change_in_energy_resource_prices_other_renewables_ap():
    """
    Real Name: Change in energy resource prices other Renewables AP
    Original Eqn: Energy resource prices other Renewables AP*Relative change in fictional prices other Renewables AP
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_other_renewables_ap(
    ) * relative_change_in_fictional_prices_other_renewables_ap()


@cache('step')
def changes_in_fictional_prices_other_renewables_ap():
    """
    Real Name: Changes in fictional prices other Renewables AP
    Original Eqn: (Fictional prices other Renewables AP-Shadow fictional prices other Renewables AP)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_other_renewables_ap() -
            shadow_fictional_prices_other_renewables_ap()) / short_term_period()


@cache('step')
def energy_resource_prices_other_renewables_ap():
    """
    Real Name: Energy resource prices other Renewables AP
    Original Eqn: INTEG ( Change in energy resource prices other Renewables AP, Initial energy resource prices other Renewables AP)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_other_renewables_ap()


@cache('step')
def change_in_energy_resource_prices_nuclear_af():
    """
    Real Name: Change in energy resource prices Nuclear AF
    Original Eqn: Energy resource prices Nuclear AF*Relative change in fictional prices Nuclear AF
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_nuclear_af() * relative_change_in_fictional_prices_nuclear_af()


@cache('step')
def change_in_energy_resource_prices_nuclear_ap():
    """
    Real Name: Change in energy resource prices Nuclear AP
    Original Eqn: Energy resource prices Nuclear AP*Relative change in fictional prices Nuclear AP
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_nuclear_ap() * relative_change_in_fictional_prices_nuclear_ap()


@cache('step')
def energy_resource_prices_nuclear_af():
    """
    Real Name: Energy resource prices Nuclear AF
    Original Eqn: INTEG ( Change in energy resource prices Nuclear AF, Initial energy resource prices Nuclear AF)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_nuclear_af()


@cache('run')
def fictional_prices_nuclear_af():
    """
    Real Name: Fictional prices Nuclear AF
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def fictional_prices_nuclear_ap():
    """
    Real Name: Fictional prices Nuclear AP
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('step')
def changes_in_fictional_prices_nuclear_me():
    """
    Real Name: Changes in fictional prices Nuclear ME
    Original Eqn: (Fictional prices Nuclear ME-Shadow fictional prices Nuclear ME)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_nuclear_me() -
            shadow_fictional_prices_nuclear_me()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_gas_af():
    """
    Real Name: Changes in fictional prices Gas AF
    Original Eqn: (Fictional prices Gas AF-Shadow fictional prices Gas AF)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_gas_af() - shadow_fictional_prices_gas_af()) / short_term_period()


@cache('step')
def energy_resource_prices_gas_af():
    """
    Real Name: Energy resource prices Gas AF
    Original Eqn: INTEG ( Change in energy resource prices Gas AF, Initial energy resource prices Gas AF)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_gas_af()


@cache('step')
def energy_resource_prices_gas_ap():
    """
    Real Name: Energy resource prices Gas AP
    Original Eqn: INTEG ( Change in energy resource prices Gas AP, Initial energy resource prices Gas AP)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_gas_ap()


@cache('step')
def change_in_energy_resource_prices_other_renewables_af():
    """
    Real Name: Change in energy resource prices other Renewables AF
    Original Eqn: Energy resource prices other Renewables AF*Relative change in fictional prices other Renewables AF
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_other_renewables_af(
    ) * relative_change_in_fictional_prices_other_renewables_af()


@cache('step')
def changes_in_fictional_prices_gas_me():
    """
    Real Name: Changes in fictional prices Gas ME
    Original Eqn: (Fictional prices Gas ME-Shadow fictional prices Gas ME)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_gas_me() - shadow_fictional_prices_gas_me()) / short_term_period()


@cache('step')
def relative_change_in_fictional_prices_gas_me():
    """
    Real Name: Relative change in fictional prices Gas ME
    Original Eqn: ZIDZ(Changes in fictional prices Gas ME, Shadow fictional prices Gas ME)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_gas_me(), shadow_fictional_prices_gas_me())


@cache('run')
def fictional_prices_gas_me():
    """
    Real Name: Fictional prices Gas ME
    Original Eqn: 6700.64
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6700.64


@cache('step')
def change_in_energy_resource_prices_other_renewables_me():
    """
    Real Name: Change in energy resource prices other Renewables ME
    Original Eqn: Energy resource prices other Renewables ME*Relative change in fictional prices other Renewables ME
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_other_renewables_me(
    ) * relative_change_in_fictional_prices_other_renewables_me()


@cache('step')
def changes_in_fictional_prices_nuclear_af():
    """
    Real Name: Changes in fictional prices Nuclear AF
    Original Eqn: (Fictional prices Nuclear AF-Shadow fictional prices Nuclear AF)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_nuclear_af() -
            shadow_fictional_prices_nuclear_af()) / short_term_period()


@cache('step')
def energy_resource_prices_other_renewables_me():
    """
    Real Name: Energy resource prices other Renewables ME
    Original Eqn: INTEG ( Change in energy resource prices other Renewables ME, Initial energy resource prices other Renewables ME)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_other_renewables_me()


@cache('run')
def fictional_prices_other_renewables_me():
    """
    Real Name: Fictional prices other Renewables ME
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def initial_energy_resource_prices_nuclear_af():
    """
    Real Name: Initial energy resource prices Nuclear AF
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_energy_resource_prices_nuclear_ap():
    """
    Real Name: Initial energy resource prices Nuclear AP
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('step')
def energy_resource_prices_nuclear_me():
    """
    Real Name: Energy resource prices Nuclear ME
    Original Eqn: INTEG ( Change in energy resource prices Nuclear ME, Initial energy resource prices Nuclear ME)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_nuclear_me()


@cache('run')
def fictional_prices_nuclear_me():
    """
    Real Name: Fictional prices Nuclear ME
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def fictional_prices_gas_af():
    """
    Real Name: Fictional prices Gas AF
    Original Eqn: 6700.64
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6700.64


@cache('run')
def fictional_prices_gas_ap():
    """
    Real Name: Fictional prices Gas AP
    Original Eqn: 6700.64
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6700.64


@cache('step')
def changes_in_fictional_prices_other_renewables_af():
    """
    Real Name: Changes in fictional prices other Renewables AF
    Original Eqn: (Fictional prices other Renewables AF-Shadow fictional prices other Renewables AF)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_other_renewables_af() -
            shadow_fictional_prices_other_renewables_af()) / short_term_period()


@cache('step')
def energy_resource_prices_other_renewables_af():
    """
    Real Name: Energy resource prices other Renewables AF
    Original Eqn: INTEG ( Change in energy resource prices other Renewables AF, Initial energy resource prices other Renewables AF)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_other_renewables_af()


@cache('run')
def fictional_prices_other_renewables_af():
    """
    Real Name: Fictional prices other Renewables AF
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def fictional_prices_other_renewables_ap():
    """
    Real Name: Fictional prices other Renewables AP
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('step')
def changes_in_fictional_prices_other_renewables_me():
    """
    Real Name: Changes in fictional prices other Renewables ME
    Original Eqn: (Fictional prices other Renewables ME-Shadow fictional prices other Renewables ME)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_other_renewables_me() -
            shadow_fictional_prices_other_renewables_me()) / short_term_period()


@cache('run')
def initial_shadow_fictional_prices_other_renewables_ap():
    """
    Real Name: Initial shadow fictional prices other Renewables AP
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('step')
def relative_change_in_fictional_prices_other_renewables_ap():
    """
    Real Name: Relative change in fictional prices other Renewables AP
    Original Eqn: ZIDZ(Changes in fictional prices other Renewables AP, Shadow fictional prices other Renewables AP\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_other_renewables_ap(),
                          shadow_fictional_prices_other_renewables_ap())


@cache('run')
def initial_energy_resource_prices_other_renewables_me():
    """
    Real Name: Initial energy resource prices other Renewables ME
    Original Eqn: 21982
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 21982


@cache('run')
def initial_shadow_fictional_prices_nuclear_af():
    """
    Real Name: Initial shadow fictional prices Nuclear AF
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_shadow_fictional_prices_nuclear_ap():
    """
    Real Name: Initial shadow fictional prices Nuclear AP
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('step')
def relative_change_in_fictional_prices_nuclear_ap():
    """
    Real Name: Relative change in fictional prices Nuclear AP
    Original Eqn: ZIDZ(Changes in fictional prices Nuclear AP, Shadow fictional prices Nuclear AP)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_nuclear_ap(),
                          shadow_fictional_prices_nuclear_ap())


@cache('run')
def initial_energy_resource_prices_nuclear_me():
    """
    Real Name: Initial energy resource prices Nuclear ME
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_energy_resource_prices_gas_af():
    """
    Real Name: Initial energy resource prices Gas AF
    Original Eqn: 11000
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 11000


@cache('run')
def initial_energy_resource_prices_gas_ap():
    """
    Real Name: Initial energy resource prices Gas AP
    Original Eqn: 11000
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 11000


@cache('run')
def initial_shadow_fictional_prices_gas_ap():
    """
    Real Name: Initial shadow fictional prices Gas AP
    Original Eqn: 6700.64
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6700.64


@cache('step')
def relative_change_in_fictional_prices_gas_ap():
    """
    Real Name: Relative change in fictional prices Gas AP
    Original Eqn: ZIDZ(Changes in fictional prices Gas AP, Shadow fictional prices Gas AP)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_gas_ap(), shadow_fictional_prices_gas_ap())


@cache('run')
def initial_energy_resource_prices_gas_me():
    """
    Real Name: Initial energy resource prices Gas ME
    Original Eqn: 11000
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 11000


@cache('run')
def initial_energy_resource_prices_other_renewables_ap():
    """
    Real Name: Initial energy resource prices other Renewables AP
    Original Eqn: 21982
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 21982


@cache('step')
def shadow_fictional_prices_gas_me():
    """
    Real Name: Shadow fictional prices Gas ME
    Original Eqn: INTEG ( Changes in fictional prices Gas ME, Initial shadow fictional prices Gas ME)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_gas_me()


@cache('step')
def shadow_fictional_prices_other_renewables_af():
    """
    Real Name: Shadow fictional prices other Renewables AF
    Original Eqn: INTEG ( Changes in fictional prices other Renewables AF, Initial shadow fictional prices other Renewables AF)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_other_renewables_af()


@cache('step')
def shadow_fictional_prices_other_renewables_ap():
    """
    Real Name: Shadow fictional prices other Renewables AP
    Original Eqn: INTEG ( Changes in fictional prices other Renewables AP, Initial shadow fictional prices other Renewables AP)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_other_renewables_ap()


@cache('run')
def initial_shadow_fictional_prices_other_renewables_me():
    """
    Real Name: Initial shadow fictional prices other Renewables ME
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('step')
def relative_change_in_fictional_prices_nuclear_af():
    """
    Real Name: Relative change in fictional prices Nuclear AF
    Original Eqn: ZIDZ(Changes in fictional prices Nuclear AF, Shadow fictional prices Nuclear AF)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_nuclear_af(),
                          shadow_fictional_prices_nuclear_af())


@cache('step')
def shadow_fictional_prices_nuclear_af():
    """
    Real Name: Shadow fictional prices Nuclear AF
    Original Eqn: INTEG ( Changes in fictional prices Nuclear AF, Initial shadow fictional prices Nuclear AF)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_nuclear_af()


@cache('step')
def shadow_fictional_prices_nuclear_ap():
    """
    Real Name: Shadow fictional prices Nuclear AP
    Original Eqn: INTEG ( Changes in fictional prices Nuclear AP, Initial shadow fictional prices Nuclear AP)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_nuclear_ap()


@cache('run')
def initial_shadow_fictional_prices_nuclear_me():
    """
    Real Name: Initial shadow fictional prices Nuclear ME
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_shadow_fictional_prices_gas_af():
    """
    Real Name: Initial shadow fictional prices Gas AF
    Original Eqn: 6700.64
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6700.64


@cache('step')
def relative_change_in_fictional_prices_gas_af():
    """
    Real Name: Relative change in fictional prices Gas AF
    Original Eqn: ZIDZ(Changes in fictional prices Gas AF, Shadow fictional prices Gas AF)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_gas_af(), shadow_fictional_prices_gas_af())


@cache('step')
def shadow_fictional_prices_gas_af():
    """
    Real Name: Shadow fictional prices Gas AF
    Original Eqn: INTEG ( Changes in fictional prices Gas AF, Initial shadow fictional prices Gas AF)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_gas_af()


@cache('run')
def initial_energy_resource_prices_other_renewables_af():
    """
    Real Name: Initial energy resource prices other Renewables AF
    Original Eqn: 21982
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 21982


@cache('run')
def initial_shadow_fictional_prices_gas_me():
    """
    Real Name: Initial shadow fictional prices Gas ME
    Original Eqn: 6700.64
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6700.64


@cache('step')
def relative_change_in_fictional_prices_other_renewables_af():
    """
    Real Name: Relative change in fictional prices other Renewables AF
    Original Eqn: ZIDZ(Changes in fictional prices other Renewables AF, Shadow fictional prices other Renewables AF\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_other_renewables_af(),
                          shadow_fictional_prices_other_renewables_af())


@cache('step')
def relative_change_in_fictional_prices_other_renewables_me():
    """
    Real Name: Relative change in fictional prices other Renewables ME
    Original Eqn: ZIDZ(Changes in fictional prices other Renewables ME, Shadow fictional prices other Renewables ME\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_other_renewables_me(),
                          shadow_fictional_prices_other_renewables_me())


@cache('step')
def relative_change_in_fictional_prices_nuclear_me():
    """
    Real Name: Relative change in fictional prices Nuclear ME
    Original Eqn: ZIDZ(Changes in fictional prices Nuclear ME, Shadow fictional prices Nuclear ME)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_nuclear_me(),
                          shadow_fictional_prices_nuclear_me())


@cache('step')
def shadow_fictional_prices_nuclear_me():
    """
    Real Name: Shadow fictional prices Nuclear ME
    Original Eqn: INTEG ( Changes in fictional prices Nuclear ME, Initial shadow fictional prices Nuclear ME)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_nuclear_me()


@cache('step')
def shadow_fictional_prices_other_renewables_me():
    """
    Real Name: Shadow fictional prices other Renewables ME
    Original Eqn: INTEG ( Changes in fictional prices other Renewables ME, Initial shadow fictional prices other Renewables ME)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_other_renewables_me()


@cache('run')
def initial_shadow_fictional_prices_other_renewables_af():
    """
    Real Name: Initial shadow fictional prices other Renewables AF
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('step')
def shadow_fictional_prices_gas_ap():
    """
    Real Name: Shadow fictional prices Gas AP
    Original Eqn: INTEG ( Changes in fictional prices Gas AP, Initial shadow fictional prices Gas AP)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_gas_ap()


@cache('step')
def change_in_energy_resource_prices_biofuels():
    """
    Real Name: Change in energy resource prices Biofuels
    Original Eqn: Energy resource prices Biofuels*Relative change in fictional prices Biofuels
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_biofuels() * relative_change_in_fictional_prices_biofuels()


@cache('step')
def change_in_energy_resource_prices_coal():
    """
    Real Name: Change in energy resource prices Coal
    Original Eqn: Energy resource prices Coal*Relative change in fictional prices Coal
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_coal() * relative_change_in_fictional_prices_coal()


@cache('step')
def change_in_energy_resource_prices_gas_na():
    """
    Real Name: Change in energy resource prices Gas NA
    Original Eqn: Energy resource prices Gas NA*Relative change in fictional prices Gas NA
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_gas_na() * relative_change_in_fictional_prices_gas_na()


@cache('step')
def change_in_energy_resource_prices_gas_sca():
    """
    Real Name: Change in energy resource prices Gas SCA
    Original Eqn: Energy resource prices Gas SCA*Relative change in fictional prices Gas SCA
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_gas_sca() * relative_change_in_fictional_prices_gas_sca()


@cache('step')
def change_in_energy_resource_prices_gas_e():
    """
    Real Name: Change in energy resource prices Gas E
    Original Eqn: Energy resource prices Gas E*Relative change in fictional prices Gas E
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_gas_e() * relative_change_in_fictional_prices_gas_e()


@cache('step')
def change_in_energy_resource_prices_gas_cis():
    """
    Real Name: Change in energy resource prices Gas CIS
    Original Eqn: Energy resource prices Gas CIS*Relative change in fictional prices Gas CIS
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_gas_cis() * relative_change_in_fictional_prices_gas_cis()


@cache('step')
def change_in_energy_resource_prices_gas():
    """
    Real Name: Change in energy resource prices Gas
    Original Eqn: Energy resource prices Gas*Relative change in fictional prices Gas
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_gas() * relative_change_in_fictional_prices_gas()


@cache('step')
def change_in_energy_resource_prices_nuclear_na():
    """
    Real Name: Change in energy resource prices Nuclear NA
    Original Eqn: Energy resource prices Nuclear NA*Relative change in fictional prices Nuclear NA
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_nuclear_na() * relative_change_in_fictional_prices_nuclear_na()


@cache('step')
def change_in_energy_resource_prices_nuclear_sca():
    """
    Real Name: Change in energy resource prices Nuclear SCA
    Original Eqn: Energy resource prices Nuclear SCA*Relative change in fictional prices Nuclear SCA
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_nuclear_sca() * relative_change_in_fictional_prices_nuclear_sca()


@cache('step')
def change_in_energy_resource_prices_nuclear_e():
    """
    Real Name: Change in energy resource prices Nuclear E
    Original Eqn: Energy resource prices Nuclear E*Relative change in fictional prices Nuclear E
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_nuclear_e() * relative_change_in_fictional_prices_nuclear_e()


@cache('step')
def change_in_energy_resource_prices_nuclear_cis():
    """
    Real Name: Change in energy resource prices Nuclear CIS
    Original Eqn: Energy resource prices Nuclear CIS*Relative change in fictional prices Nuclear CIS
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_nuclear_cis() * relative_change_in_fictional_prices_nuclear_cis()


@cache('step')
def change_in_energy_resource_prices_nuclear():
    """
    Real Name: Change in energy resource prices Nuclear
    Original Eqn: Energy resource prices Nuclear*Relative change in fictional prices Nuclear
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_nuclear() * relative_change_in_fictional_prices_nuclear()


@cache('step')
def change_in_energy_resource_prices_oil():
    """
    Real Name: Change in energy resource prices Oil
    Original Eqn: Energy resource prices Oil*Relative change in fictional prices Oil
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_oil() * relative_change_in_fictional_prices_oil()


@cache('step')
def change_in_energy_resource_prices_other_renewables_na():
    """
    Real Name: Change in energy resource prices other Renewables NA
    Original Eqn: Energy resource prices other Renewables NA*Relative change in fictional prices other Renewables NA
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_other_renewables_na(
    ) * relative_change_in_fictional_prices_other_renewables_na()


@cache('step')
def change_in_energy_resource_prices_other_renewables_sca():
    """
    Real Name: Change in energy resource prices other Renewables SCA
    Original Eqn: Energy resource prices other Renewables SCA*Relative change in fictional prices other Renewables SCA
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_other_renewables_sca(
    ) * relative_change_in_fictional_prices_other_renewables_sca()


@cache('step')
def change_in_energy_resource_prices_other_renewables_e():
    """
    Real Name: Change in energy resource prices other Renewables E
    Original Eqn: Energy resource prices other Renewables E*Relative change in fictional prices other Renewables E
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_other_renewables_e(
    ) * relative_change_in_fictional_prices_other_renewables_e()


@cache('step')
def change_in_energy_resource_prices_other_renewables_cis():
    """
    Real Name: Change in energy resource prices other Renewables CIS
    Original Eqn: Energy resource prices other Renewables CIS*Relative change in fictional prices other Renewables CIS
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_other_renewables_cis(
    ) * relative_change_in_fictional_prices_other_renewables_cis()


@cache('step')
def change_in_energy_resource_prices_other_renewables():
    """
    Real Name: Change in energy resource prices other Renewables
    Original Eqn: Energy resource prices other Renewables*Relative change in fictional prices other Renewables
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return energy_resource_prices_other_renewables(
    ) * relative_change_in_fictional_prices_other_renewables()


@cache('step')
def changes_in_fictional_prices_biofuels():
    """
    Real Name: Changes in fictional prices Biofuels
    Original Eqn: (Fictional prices Biofuels-Shadow fictional prices Biofuels)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_biofuels() - shadow_fictional_prices_biofuels()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_coal():
    """
    Real Name: Changes in fictional prices Coal
    Original Eqn: (Fictional prices Coal-Shadow fictional prices Coal)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_coal() - shadow_fictional_prices_coal()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_gas_na():
    """
    Real Name: Changes in fictional prices Gas NA
    Original Eqn: (Fictional prices Gas NA-Shadow fictional prices Gas NA)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_gas_na() - shadow_fictional_prices_gas_na()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_gas_sca():
    """
    Real Name: Changes in fictional prices Gas SCA
    Original Eqn: (Fictional prices Gas SCA-Shadow fictional prices Gas SCA)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_gas_sca() - shadow_fictional_prices_gas_sca()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_gas_e():
    """
    Real Name: Changes in fictional prices Gas E
    Original Eqn: (Fictional prices Gas E-Shadow fictional prices Gas E)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_gas_e() - shadow_fictional_prices_gas_e()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_gas_cis():
    """
    Real Name: Changes in fictional prices Gas CIS
    Original Eqn: (Fictional prices Gas CIS-Shadow fictional prices Gas CIS)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_gas_cis() - shadow_fictional_prices_gas_cis()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_gas():
    """
    Real Name: Changes in fictional prices Gas
    Original Eqn: (Fictional prices Gas-Shadow fictional prices Gas)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_gas() - shadow_fictional_prices_gas()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_nuclear_na():
    """
    Real Name: Changes in fictional prices Nuclear NA
    Original Eqn: (Fictional prices Nuclear NA-Shadow fictional prices Nuclear NA)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_nuclear_na() -
            shadow_fictional_prices_nuclear_na()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_nuclear_sca():
    """
    Real Name: Changes in fictional prices Nuclear SCA
    Original Eqn: (Fictional prices Nuclear SCA-Shadow fictional prices Nuclear SCA)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_nuclear_sca() -
            shadow_fictional_prices_nuclear_sca()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_nuclear_e():
    """
    Real Name: Changes in fictional prices Nuclear E
    Original Eqn: (Fictional prices Nuclear E-Shadow fictional prices Nuclear E)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (
        fictional_prices_nuclear_e() - shadow_fictional_prices_nuclear_e()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_nuclear_cis():
    """
    Real Name: Changes in fictional prices Nuclear CIS
    Original Eqn: (Fictional prices Nuclear CIS-Shadow fictional prices Nuclear CIS)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_nuclear_cis() -
            shadow_fictional_prices_nuclear_cis()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_nuclear():
    """
    Real Name: Changes in fictional prices Nuclear
    Original Eqn: (Fictional prices Nuclear-Shadow fictional prices Nuclear)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_nuclear() - shadow_fictional_prices_nuclear()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_oil():
    """
    Real Name: Changes in fictional prices Oil
    Original Eqn: (Fictional prices Oil-Shadow fictional prices Oil)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_oil() - shadow_fictional_prices_oil()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_other_renewables_na():
    """
    Real Name: Changes in fictional prices other Renewables NA
    Original Eqn: (Fictional prices other Renewables NA-Shadow fictional prices other Renewables NA)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_other_renewables_na() -
            shadow_fictional_prices_other_renewables_na()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_other_renewables_sca():
    """
    Real Name: Changes in fictional prices other Renewables SCA
    Original Eqn: (Fictional prices other Renewables SCA-Shadow fictional prices other Renewables SCA)\ /Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_other_renewables_sca() -
            shadow_fictional_prices_other_renewables_sca()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_other_renewables_e():
    """
    Real Name: Changes in fictional prices other Renewables E
    Original Eqn: (Fictional prices other Renewables E-Shadow fictional prices other Renewables E)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_other_renewables_e() -
            shadow_fictional_prices_other_renewables_e()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_other_renewables_cis():
    """
    Real Name: Changes in fictional prices other Renewables CIS
    Original Eqn: (Fictional prices other Renewables CIS-Shadow fictional prices other Renewables CIS)\ /Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_other_renewables_cis() -
            shadow_fictional_prices_other_renewables_cis()) / short_term_period()


@cache('step')
def changes_in_fictional_prices_other_renewables():
    """
    Real Name: Changes in fictional prices other Renewables
    Original Eqn: (Fictional prices other Renewables-Shadow fictional prices other Renewables)/Short term period
    Units: dollar/(bbtu*year)
    Limits: (None, None)
    Type: component


    """
    return (fictional_prices_other_renewables() -
            shadow_fictional_prices_other_renewables()) / short_term_period()


@cache('step')
def energy_resource_prices_biofuels():
    """
    Real Name: Energy resource prices Biofuels
    Original Eqn: INTEG ( Change in energy resource prices Biofuels, Initial energy resource prices Biofuels)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_biofuels()


@cache('step')
def energy_resource_prices_coal():
    """
    Real Name: Energy resource prices Coal
    Original Eqn: INTEG ( Change in energy resource prices Coal, Initial energy resource prices Coal)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_coal()


@cache('step')
def energy_resource_prices_gas_na():
    """
    Real Name: Energy resource prices Gas NA
    Original Eqn: INTEG ( Change in energy resource prices Gas NA, Initial energy resource prices Gas NA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_gas_na()


@cache('step')
def energy_resource_prices_gas_sca():
    """
    Real Name: Energy resource prices Gas SCA
    Original Eqn: INTEG ( Change in energy resource prices Gas SCA, Initial energy resource prices Gas SCA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_gas_sca()


@cache('step')
def energy_resource_prices_gas_e():
    """
    Real Name: Energy resource prices Gas E
    Original Eqn: INTEG ( Change in energy resource prices Gas E, Initial energy resource prices Gas E)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_gas_e()


@cache('step')
def energy_resource_prices_gas_cis():
    """
    Real Name: Energy resource prices Gas CIS
    Original Eqn: INTEG ( Change in energy resource prices Gas CIS, Initial energy resource prices Gas CIS)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_gas_cis()


@cache('step')
def energy_resource_prices_gas():
    """
    Real Name: Energy resource prices Gas
    Original Eqn: INTEG ( Change in energy resource prices Gas, Initial energy resource prices Gas)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_gas()


@cache('step')
def energy_resource_prices_nuclear_na():
    """
    Real Name: Energy resource prices Nuclear NA
    Original Eqn: INTEG ( Change in energy resource prices Nuclear NA, Initial energy resource prices Nuclear NA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_nuclear_na()


@cache('step')
def energy_resource_prices_nuclear_sca():
    """
    Real Name: Energy resource prices Nuclear SCA
    Original Eqn: INTEG ( Change in energy resource prices Nuclear SCA, Initial energy resource prices Nuclear SCA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_nuclear_sca()


@cache('step')
def energy_resource_prices_nuclear_e():
    """
    Real Name: Energy resource prices Nuclear E
    Original Eqn: INTEG ( Change in energy resource prices Nuclear E, Initial energy resource prices Nuclear E)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_nuclear_e()


@cache('step')
def energy_resource_prices_nuclear_cis():
    """
    Real Name: Energy resource prices Nuclear CIS
    Original Eqn: INTEG ( Change in energy resource prices Nuclear CIS, Initial energy resource prices Nuclear CIS)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_nuclear_cis()


@cache('step')
def energy_resource_prices_nuclear():
    """
    Real Name: Energy resource prices Nuclear
    Original Eqn: INTEG ( Change in energy resource prices Nuclear, Initial energy resource prices Nuclear)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_nuclear()


@cache('step')
def energy_resource_prices_oil():
    """
    Real Name: Energy resource prices Oil
    Original Eqn: INTEG ( Change in energy resource prices Oil, Initial energy resource prices Oil)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_oil()


@cache('step')
def energy_resource_prices_other_renewables_na():
    """
    Real Name: Energy resource prices other Renewables NA
    Original Eqn: INTEG ( Change in energy resource prices other Renewables NA, Initial energy resource prices other Renewables NA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_other_renewables_na()


@cache('step')
def energy_resource_prices_other_renewables_sca():
    """
    Real Name: Energy resource prices other Renewables SCA
    Original Eqn: INTEG ( Change in energy resource prices other Renewables SCA, Initial energy resource prices other Renewables SCA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_other_renewables_sca()


@cache('step')
def energy_resource_prices_other_renewables_e():
    """
    Real Name: Energy resource prices other Renewables E
    Original Eqn: INTEG ( Change in energy resource prices other Renewables E, Initial energy resource prices other Renewables E)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_other_renewables_e()


@cache('step')
def energy_resource_prices_other_renewables_cis():
    """
    Real Name: Energy resource prices other Renewables CIS
    Original Eqn: INTEG ( Change in energy resource prices other Renewables CIS, Initial energy resource prices other Renewables CIS)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_other_renewables_cis()


@cache('step')
def energy_resource_prices_other_renewables():
    """
    Real Name: Energy resource prices other Renewables
    Original Eqn: INTEG ( Change in energy resource prices other Renewables, Initial energy resource prices other Renewables)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_energy_resource_prices_other_renewables()


@cache('run')
def fictional_prices_biofuels():
    """
    Real Name: Fictional prices Biofuels
    Original Eqn: 33988.9
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 33988.9


@cache('run')
def fictional_prices_coal():
    """
    Real Name: Fictional prices Coal
    Original Eqn: 1577.6
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 1577.6


@cache('run')
def fictional_prices_gas_na():
    """
    Real Name: Fictional prices Gas NA
    Original Eqn: 7650.53
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 7650.53


@cache('run')
def fictional_prices_gas_sca():
    """
    Real Name: Fictional prices Gas SCA
    Original Eqn: 14628.7
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 14628.7


@cache('run')
def fictional_prices_gas_e():
    """
    Real Name: Fictional prices Gas E
    Original Eqn: 10903.4
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 10903.4


@cache('run')
def fictional_prices_gas_cis():
    """
    Real Name: Fictional prices Gas CIS
    Original Eqn: 6700.64
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6700.64


@cache('run')
def fictional_prices_gas():
    """
    Real Name: Fictional prices Gas
    Original Eqn: 10903.4
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 10903.4


@cache('run')
def fictional_prices_nuclear_na():
    """
    Real Name: Fictional prices Nuclear NA
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def fictional_prices_nuclear_sca():
    """
    Real Name: Fictional prices Nuclear SCA
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def fictional_prices_nuclear_e():
    """
    Real Name: Fictional prices Nuclear E
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def fictional_prices_nuclear_cis():
    """
    Real Name: Fictional prices Nuclear CIS
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def fictional_prices_nuclear():
    """
    Real Name: Fictional prices Nuclear
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def fictional_prices_oil():
    """
    Real Name: Fictional prices Oil
    Original Eqn: 5598.52
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 5598.52


@cache('run')
def fictional_prices_other_renewables_na():
    """
    Real Name: Fictional prices other Renewables NA
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def fictional_prices_other_renewables_sca():
    """
    Real Name: Fictional prices other Renewables SCA
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def fictional_prices_other_renewables_e():
    """
    Real Name: Fictional prices other Renewables E
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def fictional_prices_other_renewables_cis():
    """
    Real Name: Fictional prices other Renewables CIS
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def fictional_prices_other_renewables():
    """
    Real Name: Fictional prices other Renewables
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def initial_energy_resource_prices_biofuels():
    """
    Real Name: Initial energy resource prices Biofuels
    Original Eqn: 33988.9
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 33988.9


@cache('run')
def initial_energy_resource_prices_coal():
    """
    Real Name: Initial energy resource prices Coal
    Original Eqn: 3767
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 3767


@cache('run')
def initial_energy_resource_prices_gas_na():
    """
    Real Name: Initial energy resource prices Gas NA
    Original Eqn: 4330
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 4330


@cache('run')
def initial_energy_resource_prices_gas_sca():
    """
    Real Name: Initial energy resource prices Gas SCA
    Original Eqn: 11000
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 11000


@cache('run')
def initial_energy_resource_prices_gas_e():
    """
    Real Name: Initial energy resource prices Gas E
    Original Eqn: 8895
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 8895


@cache('run')
def initial_energy_resource_prices_gas_cis():
    """
    Real Name: Initial energy resource prices Gas CIS
    Original Eqn: 11000
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 11000


@cache('run')
def initial_energy_resource_prices_gas():
    """
    Real Name: Initial energy resource prices Gas
    Original Eqn: 8895
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 8895


@cache('run')
def initial_energy_resource_prices_nuclear_na():
    """
    Real Name: Initial energy resource prices Nuclear NA
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_energy_resource_prices_nuclear_sca():
    """
    Real Name: Initial energy resource prices Nuclear SCA
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_energy_resource_prices_nuclear_e():
    """
    Real Name: Initial energy resource prices Nuclear E
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_energy_resource_prices_nuclear_cis():
    """
    Real Name: Initial energy resource prices Nuclear CIS
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_energy_resource_prices_nuclear():
    """
    Real Name: Initial energy resource prices Nuclear
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_energy_resource_prices_oil():
    """
    Real Name: Initial energy resource prices Oil
    Original Eqn: 14106.4
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 14106.4


@cache('run')
def initial_energy_resource_prices_other_renewables_na():
    """
    Real Name: Initial energy resource prices other Renewables NA
    Original Eqn: 21982
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 21982


@cache('run')
def initial_energy_resource_prices_other_renewables_sca():
    """
    Real Name: Initial energy resource prices other Renewables SCA
    Original Eqn: 21982
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 21982


@cache('run')
def initial_energy_resource_prices_other_renewables_e():
    """
    Real Name: Initial energy resource prices other Renewables E
    Original Eqn: 21982
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 21982


@cache('run')
def initial_energy_resource_prices_other_renewables_cis():
    """
    Real Name: Initial energy resource prices other Renewables CIS
    Original Eqn: 21982
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 21982


@cache('run')
def initial_energy_resource_prices_other_renewables():
    """
    Real Name: Initial energy resource prices other Renewables
    Original Eqn: 21982
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 21982


@cache('run')
def initial_shadow_fictional_prices_biofuels():
    """
    Real Name: Initial shadow fictional prices Biofuels
    Original Eqn: 33988.9
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 33988.9


@cache('run')
def initial_shadow_fictional_prices_coal():
    """
    Real Name: Initial shadow fictional prices Coal
    Original Eqn: 1577.6
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 1577.6


@cache('run')
def initial_shadow_fictional_prices_gas_na():
    """
    Real Name: Initial shadow fictional prices Gas NA
    Original Eqn: 7650.53
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 7650.53


@cache('run')
def initial_shadow_fictional_prices_gas_sca():
    """
    Real Name: Initial shadow fictional prices Gas SCA
    Original Eqn: 14628.7
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 14628.7


@cache('run')
def initial_shadow_fictional_prices_gas_e():
    """
    Real Name: Initial shadow fictional prices Gas E
    Original Eqn: 10903.4
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 10903.4


@cache('run')
def initial_shadow_fictional_prices_gas_cis():
    """
    Real Name: Initial shadow fictional prices Gas CIS
    Original Eqn: 6700.64
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6700.64


@cache('run')
def initial_shadow_fictional_prices_gas():
    """
    Real Name: Initial shadow fictional prices Gas
    Original Eqn: 10903.4
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 10903.4


@cache('run')
def initial_shadow_fictional_prices_nuclear_na():
    """
    Real Name: Initial shadow fictional prices Nuclear NA
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_shadow_fictional_prices_nuclear_sca():
    """
    Real Name: Initial shadow fictional prices Nuclear SCA
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_shadow_fictional_prices_nuclear_e():
    """
    Real Name: Initial shadow fictional prices Nuclear E
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_shadow_fictional_prices_nuclear_cis():
    """
    Real Name: Initial shadow fictional prices Nuclear CIS
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_shadow_fictional_prices_nuclear():
    """
    Real Name: Initial shadow fictional prices Nuclear
    Original Eqn: 17345.5
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 17345.5


@cache('run')
def initial_shadow_fictional_prices_oil():
    """
    Real Name: Initial shadow fictional prices Oil
    Original Eqn: 5598.52
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 5598.52


@cache('run')
def initial_shadow_fictional_prices_other_renewables_na():
    """
    Real Name: Initial shadow fictional prices other Renewables NA
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def initial_shadow_fictional_prices_other_renewables_sca():
    """
    Real Name: Initial shadow fictional prices other Renewables SCA
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def initial_shadow_fictional_prices_other_renewables_e():
    """
    Real Name: Initial shadow fictional prices other Renewables E
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def initial_shadow_fictional_prices_other_renewables_cis():
    """
    Real Name: Initial shadow fictional prices other Renewables CIS
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('run')
def initial_shadow_fictional_prices_other_renewables():
    """
    Real Name: Initial shadow fictional prices other Renewables
    Original Eqn: 6711.62
    Units: dollar/bbtu
    Limits: (None, None)
    Type: constant


    """
    return 6711.62


@cache('step')
def relative_change_in_fictional_prices_biofuels():
    """
    Real Name: Relative change in fictional prices Biofuels
    Original Eqn: ZIDZ(Changes in fictional prices Biofuels, Shadow fictional prices Biofuels)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_biofuels(),
                          shadow_fictional_prices_biofuels())


@cache('step')
def relative_change_in_fictional_prices_coal():
    """
    Real Name: Relative change in fictional prices Coal
    Original Eqn: ZIDZ(Changes in fictional prices Coal, Shadow fictional prices Coal)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_coal(), shadow_fictional_prices_coal())


@cache('step')
def relative_change_in_fictional_prices_gas_na():
    """
    Real Name: Relative change in fictional prices Gas NA
    Original Eqn: ZIDZ(Changes in fictional prices Gas NA, Shadow fictional prices Gas NA)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_gas_na(), shadow_fictional_prices_gas_na())


@cache('step')
def relative_change_in_fictional_prices_gas_sca():
    """
    Real Name: Relative change in fictional prices Gas SCA
    Original Eqn: ZIDZ(Changes in fictional prices Gas SCA, Shadow fictional prices Gas SCA)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_gas_sca(), shadow_fictional_prices_gas_sca())


@cache('step')
def relative_change_in_fictional_prices_gas_e():
    """
    Real Name: Relative change in fictional prices Gas E
    Original Eqn: ZIDZ(Changes in fictional prices Gas E, Shadow fictional prices Gas E)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_gas_e(), shadow_fictional_prices_gas_e())


@cache('step')
def relative_change_in_fictional_prices_gas_cis():
    """
    Real Name: Relative change in fictional prices Gas CIS
    Original Eqn: ZIDZ(Changes in fictional prices Gas CIS, Shadow fictional prices Gas CIS)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_gas_cis(), shadow_fictional_prices_gas_cis())


@cache('step')
def relative_change_in_fictional_prices_gas():
    """
    Real Name: Relative change in fictional prices Gas
    Original Eqn: ZIDZ(Changes in fictional prices Gas, Shadow fictional prices Gas)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_gas(), shadow_fictional_prices_gas())


@cache('step')
def relative_change_in_fictional_prices_nuclear_na():
    """
    Real Name: Relative change in fictional prices Nuclear NA
    Original Eqn: ZIDZ(Changes in fictional prices Nuclear NA, Shadow fictional prices Nuclear NA)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_nuclear_na(),
                          shadow_fictional_prices_nuclear_na())


@cache('step')
def relative_change_in_fictional_prices_nuclear_sca():
    """
    Real Name: Relative change in fictional prices Nuclear SCA
    Original Eqn: ZIDZ(Changes in fictional prices Nuclear SCA, Shadow fictional prices Nuclear SCA)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_nuclear_sca(),
                          shadow_fictional_prices_nuclear_sca())


@cache('step')
def relative_change_in_fictional_prices_nuclear_e():
    """
    Real Name: Relative change in fictional prices Nuclear E
    Original Eqn: ZIDZ(Changes in fictional prices Nuclear E, Shadow fictional prices Nuclear E)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_nuclear_e(),
                          shadow_fictional_prices_nuclear_e())


@cache('step')
def relative_change_in_fictional_prices_nuclear_cis():
    """
    Real Name: Relative change in fictional prices Nuclear CIS
    Original Eqn: ZIDZ(Changes in fictional prices Nuclear CIS, Shadow fictional prices Nuclear CIS)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_nuclear_cis(),
                          shadow_fictional_prices_nuclear_cis())


@cache('step')
def relative_change_in_fictional_prices_nuclear():
    """
    Real Name: Relative change in fictional prices Nuclear
    Original Eqn: ZIDZ(Changes in fictional prices Nuclear, Shadow fictional prices Nuclear)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_nuclear(), shadow_fictional_prices_nuclear())


@cache('step')
def relative_change_in_fictional_prices_oil():
    """
    Real Name: Relative change in fictional prices Oil
    Original Eqn: ZIDZ(Changes in fictional prices Oil, Shadow fictional prices Oil)
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_oil(), shadow_fictional_prices_oil())


@cache('step')
def relative_change_in_fictional_prices_other_renewables_na():
    """
    Real Name: Relative change in fictional prices other Renewables NA
    Original Eqn: ZIDZ(Changes in fictional prices other Renewables NA, Shadow fictional prices other Renewables NA\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_other_renewables_na(),
                          shadow_fictional_prices_other_renewables_na())


@cache('step')
def relative_change_in_fictional_prices_other_renewables_sca():
    """
    Real Name: Relative change in fictional prices other Renewables SCA
    Original Eqn: ZIDZ(Changes in fictional prices other Renewables SCA, Shadow fictional prices other Renewables SCA\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_other_renewables_sca(),
                          shadow_fictional_prices_other_renewables_sca())


@cache('step')
def relative_change_in_fictional_prices_other_renewables_e():
    """
    Real Name: Relative change in fictional prices other Renewables E
    Original Eqn: ZIDZ(Changes in fictional prices other Renewables E, Shadow fictional prices other Renewables E\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_other_renewables_e(),
                          shadow_fictional_prices_other_renewables_e())


@cache('step')
def relative_change_in_fictional_prices_other_renewables_cis():
    """
    Real Name: Relative change in fictional prices other Renewables CIS
    Original Eqn: ZIDZ(Changes in fictional prices other Renewables CIS, Shadow fictional prices other Renewables CIS\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_other_renewables_cis(),
                          shadow_fictional_prices_other_renewables_cis())


@cache('step')
def relative_change_in_fictional_prices_other_renewables():
    """
    Real Name: Relative change in fictional prices other Renewables
    Original Eqn: ZIDZ(Changes in fictional prices other Renewables, Shadow fictional prices other Renewables\ )
    Units: 1/year
    Limits: (None, None)
    Type: component


    """
    return functions.zidz(changes_in_fictional_prices_other_renewables(),
                          shadow_fictional_prices_other_renewables())


@cache('step')
def shadow_fictional_prices_biofuels():
    """
    Real Name: Shadow fictional prices Biofuels
    Original Eqn: INTEG ( Changes in fictional prices Biofuels, Initial shadow fictional prices Biofuels)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_biofuels()


@cache('step')
def shadow_fictional_prices_coal():
    """
    Real Name: Shadow fictional prices Coal
    Original Eqn: INTEG ( Changes in fictional prices Coal, Initial shadow fictional prices Coal)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_coal()


@cache('step')
def shadow_fictional_prices_gas_na():
    """
    Real Name: Shadow fictional prices Gas NA
    Original Eqn: INTEG ( Changes in fictional prices Gas NA, Initial shadow fictional prices Gas NA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_gas_na()


@cache('step')
def shadow_fictional_prices_gas_sca():
    """
    Real Name: Shadow fictional prices Gas SCA
    Original Eqn: INTEG ( Changes in fictional prices Gas SCA, Initial shadow fictional prices Gas SCA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_gas_sca()


@cache('step')
def shadow_fictional_prices_gas_e():
    """
    Real Name: Shadow fictional prices Gas E
    Original Eqn: INTEG ( Changes in fictional prices Gas E, Initial shadow fictional prices Gas E)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_gas_e()


@cache('step')
def shadow_fictional_prices_gas_cis():
    """
    Real Name: Shadow fictional prices Gas CIS
    Original Eqn: INTEG ( Changes in fictional prices Gas CIS, Initial shadow fictional prices Gas CIS)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_gas_cis()


@cache('step')
def shadow_fictional_prices_gas():
    """
    Real Name: Shadow fictional prices Gas
    Original Eqn: INTEG ( Changes in fictional prices Gas, Initial shadow fictional prices Gas)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_gas()


@cache('step')
def shadow_fictional_prices_nuclear_na():
    """
    Real Name: Shadow fictional prices Nuclear NA
    Original Eqn: INTEG ( Changes in fictional prices Nuclear NA, Initial shadow fictional prices Nuclear NA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_nuclear_na()


@cache('step')
def shadow_fictional_prices_nuclear_sca():
    """
    Real Name: Shadow fictional prices Nuclear SCA
    Original Eqn: INTEG ( Changes in fictional prices Nuclear SCA, Initial shadow fictional prices Nuclear SCA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_nuclear_sca()


@cache('step')
def shadow_fictional_prices_nuclear_e():
    """
    Real Name: Shadow fictional prices Nuclear E
    Original Eqn: INTEG ( Changes in fictional prices Nuclear E, Initial shadow fictional prices Nuclear E)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_nuclear_e()


@cache('step')
def shadow_fictional_prices_nuclear_cis():
    """
    Real Name: Shadow fictional prices Nuclear CIS
    Original Eqn: INTEG ( Changes in fictional prices Nuclear CIS, Initial shadow fictional prices Nuclear CIS)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_nuclear_cis()


@cache('step')
def shadow_fictional_prices_nuclear():
    """
    Real Name: Shadow fictional prices Nuclear
    Original Eqn: INTEG ( Changes in fictional prices Nuclear, Initial shadow fictional prices Nuclear)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_nuclear()


@cache('step')
def shadow_fictional_prices_oil():
    """
    Real Name: Shadow fictional prices Oil
    Original Eqn: INTEG ( Changes in fictional prices Oil, Initial shadow fictional prices Oil)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_oil()


@cache('step')
def shadow_fictional_prices_other_renewables_na():
    """
    Real Name: Shadow fictional prices other Renewables NA
    Original Eqn: INTEG ( Changes in fictional prices other Renewables NA, Initial shadow fictional prices other Renewables NA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_other_renewables_na()


@cache('step')
def shadow_fictional_prices_other_renewables_sca():
    """
    Real Name: Shadow fictional prices other Renewables SCA
    Original Eqn: INTEG ( Changes in fictional prices other Renewables SCA, Initial shadow fictional prices other Renewables SCA)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_other_renewables_sca()


@cache('step')
def shadow_fictional_prices_other_renewables_e():
    """
    Real Name: Shadow fictional prices other Renewables E
    Original Eqn: INTEG ( Changes in fictional prices other Renewables E, Initial shadow fictional prices other Renewables E)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_other_renewables_e()


@cache('step')
def shadow_fictional_prices_other_renewables_cis():
    """
    Real Name: Shadow fictional prices other Renewables CIS
    Original Eqn: INTEG ( Changes in fictional prices other Renewables CIS, Initial shadow fictional prices other Renewables CIS)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_other_renewables_cis()


@cache('step')
def shadow_fictional_prices_other_renewables():
    """
    Real Name: Shadow fictional prices other Renewables
    Original Eqn: INTEG ( Changes in fictional prices other Renewables, Initial shadow fictional prices other Renewables)
    Units: dollar/bbtu
    Limits: (None, None)
    Type: component


    """
    return integ_shadow_fictional_prices_other_renewables()


@cache('run')
def short_term_period():
    """
    Real Name: Short term period
    Original Eqn: 0.25
    Units: year
    Limits: (None, None)
    Type: constant


    """
    return 0.25


@cache('run')
def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 2050
    Units: year
    Limits: (None, None)
    Type: constant

    The final time for the simulation.
    """
    return 2050


@cache('run')
def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 2010
    Units: year
    Limits: (None, None)
    Type: constant

    The initial time for the simulation.
    """
    return 2010


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


integ_energy_resource_prices_nuclear_ap = functions.Integ(
    lambda: change_in_energy_resource_prices_nuclear_ap(),
    lambda: initial_energy_resource_prices_nuclear_ap())

integ_energy_resource_prices_gas_me = functions.Integ(
    lambda: change_in_energy_resource_prices_gas_me(),
    lambda: initial_energy_resource_prices_gas_me())

integ_energy_resource_prices_other_renewables_ap = functions.Integ(
    lambda: change_in_energy_resource_prices_other_renewables_ap(),
    lambda: initial_energy_resource_prices_other_renewables_ap())

integ_energy_resource_prices_nuclear_af = functions.Integ(
    lambda: change_in_energy_resource_prices_nuclear_af(),
    lambda: initial_energy_resource_prices_nuclear_af())

integ_energy_resource_prices_gas_af = functions.Integ(
    lambda: change_in_energy_resource_prices_gas_af(),
    lambda: initial_energy_resource_prices_gas_af())

integ_energy_resource_prices_gas_ap = functions.Integ(
    lambda: change_in_energy_resource_prices_gas_ap(),
    lambda: initial_energy_resource_prices_gas_ap())

integ_energy_resource_prices_other_renewables_me = functions.Integ(
    lambda: change_in_energy_resource_prices_other_renewables_me(),
    lambda: initial_energy_resource_prices_other_renewables_me())

integ_energy_resource_prices_nuclear_me = functions.Integ(
    lambda: change_in_energy_resource_prices_nuclear_me(),
    lambda: initial_energy_resource_prices_nuclear_me())

integ_energy_resource_prices_other_renewables_af = functions.Integ(
    lambda: change_in_energy_resource_prices_other_renewables_af(),
    lambda: initial_energy_resource_prices_other_renewables_af())

integ_shadow_fictional_prices_gas_me = functions.Integ(
    lambda: changes_in_fictional_prices_gas_me(), lambda: initial_shadow_fictional_prices_gas_me())

integ_shadow_fictional_prices_other_renewables_af = functions.Integ(
    lambda: changes_in_fictional_prices_other_renewables_af(),
    lambda: initial_shadow_fictional_prices_other_renewables_af())

integ_shadow_fictional_prices_other_renewables_ap = functions.Integ(
    lambda: changes_in_fictional_prices_other_renewables_ap(),
    lambda: initial_shadow_fictional_prices_other_renewables_ap())

integ_shadow_fictional_prices_nuclear_af = functions.Integ(
    lambda: changes_in_fictional_prices_nuclear_af(),
    lambda: initial_shadow_fictional_prices_nuclear_af())

integ_shadow_fictional_prices_nuclear_ap = functions.Integ(
    lambda: changes_in_fictional_prices_nuclear_ap(),
    lambda: initial_shadow_fictional_prices_nuclear_ap())

integ_shadow_fictional_prices_gas_af = functions.Integ(
    lambda: changes_in_fictional_prices_gas_af(), lambda: initial_shadow_fictional_prices_gas_af())

integ_shadow_fictional_prices_nuclear_me = functions.Integ(
    lambda: changes_in_fictional_prices_nuclear_me(),
    lambda: initial_shadow_fictional_prices_nuclear_me())

integ_shadow_fictional_prices_other_renewables_me = functions.Integ(
    lambda: changes_in_fictional_prices_other_renewables_me(),
    lambda: initial_shadow_fictional_prices_other_renewables_me())

integ_shadow_fictional_prices_gas_ap = functions.Integ(
    lambda: changes_in_fictional_prices_gas_ap(), lambda: initial_shadow_fictional_prices_gas_ap())

integ_energy_resource_prices_biofuels = functions.Integ(
    lambda: change_in_energy_resource_prices_biofuels(),
    lambda: initial_energy_resource_prices_biofuels())

integ_energy_resource_prices_coal = functions.Integ(
    lambda: change_in_energy_resource_prices_coal(), lambda: initial_energy_resource_prices_coal())

integ_energy_resource_prices_gas_na = functions.Integ(
    lambda: change_in_energy_resource_prices_gas_na(),
    lambda: initial_energy_resource_prices_gas_na())

integ_energy_resource_prices_gas_sca = functions.Integ(
    lambda: change_in_energy_resource_prices_gas_sca(),
    lambda: initial_energy_resource_prices_gas_sca())

integ_energy_resource_prices_gas_e = functions.Integ(
    lambda: change_in_energy_resource_prices_gas_e(),
    lambda: initial_energy_resource_prices_gas_e())

integ_energy_resource_prices_gas_cis = functions.Integ(
    lambda: change_in_energy_resource_prices_gas_cis(),
    lambda: initial_energy_resource_prices_gas_cis())

integ_energy_resource_prices_gas = functions.Integ(lambda: change_in_energy_resource_prices_gas(),
                                                   lambda: initial_energy_resource_prices_gas())

integ_energy_resource_prices_nuclear_na = functions.Integ(
    lambda: change_in_energy_resource_prices_nuclear_na(),
    lambda: initial_energy_resource_prices_nuclear_na())

integ_energy_resource_prices_nuclear_sca = functions.Integ(
    lambda: change_in_energy_resource_prices_nuclear_sca(),
    lambda: initial_energy_resource_prices_nuclear_sca())

integ_energy_resource_prices_nuclear_e = functions.Integ(
    lambda: change_in_energy_resource_prices_nuclear_e(),
    lambda: initial_energy_resource_prices_nuclear_e())

integ_energy_resource_prices_nuclear_cis = functions.Integ(
    lambda: change_in_energy_resource_prices_nuclear_cis(),
    lambda: initial_energy_resource_prices_nuclear_cis())

integ_energy_resource_prices_nuclear = functions.Integ(
    lambda: change_in_energy_resource_prices_nuclear(),
    lambda: initial_energy_resource_prices_nuclear())

integ_energy_resource_prices_oil = functions.Integ(lambda: change_in_energy_resource_prices_oil(),
                                                   lambda: initial_energy_resource_prices_oil())

integ_energy_resource_prices_other_renewables_na = functions.Integ(
    lambda: change_in_energy_resource_prices_other_renewables_na(),
    lambda: initial_energy_resource_prices_other_renewables_na())

integ_energy_resource_prices_other_renewables_sca = functions.Integ(
    lambda: change_in_energy_resource_prices_other_renewables_sca(),
    lambda: initial_energy_resource_prices_other_renewables_sca())

integ_energy_resource_prices_other_renewables_e = functions.Integ(
    lambda: change_in_energy_resource_prices_other_renewables_e(),
    lambda: initial_energy_resource_prices_other_renewables_e())

integ_energy_resource_prices_other_renewables_cis = functions.Integ(
    lambda: change_in_energy_resource_prices_other_renewables_cis(),
    lambda: initial_energy_resource_prices_other_renewables_cis())

integ_energy_resource_prices_other_renewables = functions.Integ(
    lambda: change_in_energy_resource_prices_other_renewables(),
    lambda: initial_energy_resource_prices_other_renewables())

integ_shadow_fictional_prices_biofuels = functions.Integ(
    lambda: changes_in_fictional_prices_biofuels(),
    lambda: initial_shadow_fictional_prices_biofuels())

integ_shadow_fictional_prices_coal = functions.Integ(
    lambda: changes_in_fictional_prices_coal(), lambda: initial_shadow_fictional_prices_coal())

integ_shadow_fictional_prices_gas_na = functions.Integ(
    lambda: changes_in_fictional_prices_gas_na(), lambda: initial_shadow_fictional_prices_gas_na())

integ_shadow_fictional_prices_gas_sca = functions.Integ(
    lambda: changes_in_fictional_prices_gas_sca(),
    lambda: initial_shadow_fictional_prices_gas_sca())

integ_shadow_fictional_prices_gas_e = functions.Integ(
    lambda: changes_in_fictional_prices_gas_e(), lambda: initial_shadow_fictional_prices_gas_e())

integ_shadow_fictional_prices_gas_cis = functions.Integ(
    lambda: changes_in_fictional_prices_gas_cis(),
    lambda: initial_shadow_fictional_prices_gas_cis())

integ_shadow_fictional_prices_gas = functions.Integ(lambda: changes_in_fictional_prices_gas(),
                                                    lambda: initial_shadow_fictional_prices_gas())

integ_shadow_fictional_prices_nuclear_na = functions.Integ(
    lambda: changes_in_fictional_prices_nuclear_na(),
    lambda: initial_shadow_fictional_prices_nuclear_na())

integ_shadow_fictional_prices_nuclear_sca = functions.Integ(
    lambda: changes_in_fictional_prices_nuclear_sca(),
    lambda: initial_shadow_fictional_prices_nuclear_sca())

integ_shadow_fictional_prices_nuclear_e = functions.Integ(
    lambda: changes_in_fictional_prices_nuclear_e(),
    lambda: initial_shadow_fictional_prices_nuclear_e())

integ_shadow_fictional_prices_nuclear_cis = functions.Integ(
    lambda: changes_in_fictional_prices_nuclear_cis(),
    lambda: initial_shadow_fictional_prices_nuclear_cis())

integ_shadow_fictional_prices_nuclear = functions.Integ(
    lambda: changes_in_fictional_prices_nuclear(),
    lambda: initial_shadow_fictional_prices_nuclear())

integ_shadow_fictional_prices_oil = functions.Integ(lambda: changes_in_fictional_prices_oil(),
                                                    lambda: initial_shadow_fictional_prices_oil())

integ_shadow_fictional_prices_other_renewables_na = functions.Integ(
    lambda: changes_in_fictional_prices_other_renewables_na(),
    lambda: initial_shadow_fictional_prices_other_renewables_na())

integ_shadow_fictional_prices_other_renewables_sca = functions.Integ(
    lambda: changes_in_fictional_prices_other_renewables_sca(),
    lambda: initial_shadow_fictional_prices_other_renewables_sca())

integ_shadow_fictional_prices_other_renewables_e = functions.Integ(
    lambda: changes_in_fictional_prices_other_renewables_e(),
    lambda: initial_shadow_fictional_prices_other_renewables_e())

integ_shadow_fictional_prices_other_renewables_cis = functions.Integ(
    lambda: changes_in_fictional_prices_other_renewables_cis(),
    lambda: initial_shadow_fictional_prices_other_renewables_cis())

integ_shadow_fictional_prices_other_renewables = functions.Integ(
    lambda: changes_in_fictional_prices_other_renewables(),
    lambda: initial_shadow_fictional_prices_other_renewables())
