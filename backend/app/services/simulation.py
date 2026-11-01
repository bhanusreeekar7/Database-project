import numpy as np
def simulate(initial, contribution, annual_return, volatility, years, simulations, goal_target=None):
    months=years*12; r=annual_return/100/12; sigma=volatility/100/(12**.5)
    returns=np.random.normal(r,sigma,(simulations,months)); paths=np.full((simulations,months+1),initial,dtype=float)
    for month in range(months): paths[:,month+1]=paths[:,month]*(1+returns[:,month])+contribution
    final=paths[:,-1]; q=np.percentile(final,[10,25,50,75,90])
    return {'percentiles':dict(zip(['p10','p25','median','p75','p90'],map(lambda x:round(float(x),2),q))), 'goal_probability':round(float((final>=goal_target).mean()*100),2) if goal_target else None, 'sample_paths':paths[:min(40,simulations),::max(1,months//60)].round(2).tolist(), 'distribution':np.histogram(final,bins=24)[0].tolist(), 'bins':np.histogram(final,bins=24)[1].round(2).tolist()}
