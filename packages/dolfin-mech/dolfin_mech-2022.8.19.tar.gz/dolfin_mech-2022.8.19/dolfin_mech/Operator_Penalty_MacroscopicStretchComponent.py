#coding=utf8

################################################################################
###                                                                          ###
### Created by Martin Genet, 2018-2022                                       ###
###                                                                          ###
### École Polytechnique, Palaiseau, France                                   ###
###                                                                          ###
###                                                                          ###
### And Mahdi Manoochehrtayebi, 2021-2022                                    ###
###                                                                          ###
### École Polytechnique, Palaiseau, France                                   ###
###                                                                          ###
################################################################################

import dolfin

import dolfin_mech as dmech
from .Operator import Operator

################################################################################

class MacroscopicStretchComponentPenaltyOperator(Operator):

    def __init__(self,
            U_bar,
            U_bar_test,
            comp_i, comp_j,
            measure,
            comp_val=None, comp_ini=None, comp_fin=None,
            pen_val=None, pen_ini=None, pen_fin=None):

        self.measure = measure

        self.tv_comp = dmech.TimeVaryingConstant(
            val=comp_val, val_ini=comp_ini, val_fin=comp_fin)
        comp = self.tv_comp.val

        self.tv_pen = dmech.TimeVaryingConstant(
            val=pen_val, val_ini=pen_ini, val_fin=pen_fin)
        pen = self.tv_pen.val

        Pi = (pen/2) * (U_bar[comp_i,comp_j] - comp)**2 * self.measure
        self.res_form = dolfin.derivative(Pi, U_bar[comp_i,comp_j], U_bar_test[comp_i,comp_j])



    def set_value_at_t_step(self,
            t_step):

        self.tv_comp.set_value_at_t_step(t_step)
        self.tv_pen.set_value_at_t_step(t_step)
