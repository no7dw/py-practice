from empyrical import (
    alpha,
    beta,
    alpha_beta_aligned,
    annual_volatility,
    cum_returns,
    annual_return,
    downside_risk,
    max_drawdown,
    sharpe_ratio,
    sortino_ratio,
    calmar_ratio,
    omega_ratio,
    tail_ratio
)
import pandas as pd
returns = pd.Series(
    index=pd.date_range('2017-03-10', '2017-03-19'),
    data=(-0.012143, 0.045350, 0.030957, 0.004902, 0.002341, -0.02103, 0.00148, 0.004820, -0.00023, 0.01201)
)

benchmark_returns = pd.Series(
    index=pd.date_range('2017-03-10', '2017-03-19'),
    data=(-0.031940, 0.025350, -0.020957, -0.000902, 0.007341, -0.01103, 0.00248, 0.008820, -0.00123, 0.01091)
)
creturns = cum_returns(returns)
max_drawdown(returns)
annual_return(returns)
annual_volatility(returns, period='daily')
calmar_ratio(returns)
omega_ratio(returns=returns, risk_free=0.01)
sharpe_ratio(returns=returns, risk_free=0.01)
sortino_ratio(returns=returns)
downside_risk(returns=returns)
alpha(returns=returns, factor_returns=benchmark_returns, risk_free=0.01)
beta(returns=returns, factor_returns=benchmark_returns, risk_free=0.01)
tail_ratio(returns=returns)

