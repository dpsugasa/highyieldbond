#!/usr/bin/env python

import QuantLib as ql

import market_data.yield_curve as yc
import market_data.bond_terms as bt
import credit_data.credit_curve as cc

'''
pricing functions
'''

def value_bond(a, s, grid_points, bond, ts_handle):
    model = ql.HullWhite(ts_handle, a, s)
    engine = ql.TreeCallableFixedRateBondEngine(model, grid_points)
    bond.setPricingEngine(engine)
    return bond


'''
Set settlement and day count:
'''

settlement_days = 2
face_amount = bt.par
accrual_daycount = ql.Actual360()#ql.ActualActual(ql.ActualActual.Bond)

fixedRateBond = ql.FixedRateBond(settlement_days, face_amount, bt.schedule, bt.coupons, accrual_daycount)
#
bondEngine = ql.DiscountingBondEngine(yc.spotCurveHandle)
fixedRateBond.setPricingEngine(bondEngine)
print ("No calls/no credit Bond price: ", fixedRateBond.NPV())


bond = ql.CallableFixedRateBond(
    settlement_days, face_amount,
    bt.schedule, bt.coupons, accrual_daycount,
    ql.Following, face_amount, bt.issueDate,
    bt.callability_schedule)

#def value_bond(a, s, grid_points, bond):
#    model = ql.HullWhite(yc.spotCurveHandle, a, s)
#    engine = ql.TreeCallableFixedRateBondEngine(model, grid_points)
#    bond.setPricingEngine(engine)
#    return bond

value_bond(0.01, 0.08, 1000, bond, yc.spotCurveHandle)
print ("Calls/no credit Bond price: ",bond.NPV())
value_bond(0.01, 0.08, 1000, bond, cc.spotCurve_credit_handle)
print ("Calls/no credit Bond price: ",bond.NPV())

#print ("Calls/no credit Bond price: ",bond.NPV())