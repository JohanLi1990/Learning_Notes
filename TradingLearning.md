# Algorithmic Trading

## Chapter 1: Backtesting and Automated Execution

- **Importance of Backtesting:**
	Backtesting is vital for assessing the performance of a trading strategy on historical data, helping to avoid common pitfalls and ensuring the statistical significance of the results. This process allows traders to analyze the strategy's robustness over different market phases, providing a more comprehensive understanding of its potential performance. By backtesting, traders can refine their strategies, identify areas for improvemenet and make more informed decisions. 

- **Common Pitfalls**
  - Look-ahead Bias: using future data to determine today's trading signal
  - Data-Snooping Bias and the Beauty of Linearity: 
    - A model with too many parameters.
    - Make the model as simple as possible (Occam's razor) 
  - Stock Splits and Dividend Adjustments: 
    - should adjust testing data based on those events, 
    - otherwise there will be an erronous tradng signal. [Earnings](earnings.com)

	- **Survivorship Bias in Stock Database**
  	- If you do not include stocks that are delisted, then your strategy may not work on all stocks
  	- You can buy reasonably priced historical data that are free of survivorship bias from csidata.com (which provides a list of delisted stocks). Other vendors include kibot.com, tickdata.com, and crsp.com.
	- Venue Dependence of Currency QUotes (ECN, or exchanges)
	- Short-Sale Constraints

- **When not to back test a strategy**
  - When strategy are trash from first look: low Sharpe ratio, long maximum drawdown duration
  - When strategy cannot event out perform the market
  - A strategy with too many variables and parameters. will suffer from data-snooping.
  - We cannot really backtest a high-frequency trading strategy.

- **What to choose a platform?**
  - AlgoTrader (Interactive Brokers)
  - Moomoo

## Chapter 2: The Basics of Mean Reversion

- Most price series are not mean reverting, but are geometric random walks
- Wrong assumption: **if something is mean reverting, it must be stationary**, this is not true!!
- Mean reversion answers:
  
  > “After a big move, which direction is more likely next?”

- Stationarity answers:
  
  > “Can I trust my historical statistics at all?”

  You need both for a robust strategy.

- Mean reversion on returns/spread is much safer!
- Mean reversion on rpices is Dangerous unless transformed!
- **Anything that accumulates histroy is non-stationary**, anything that resets every step is closer to stationary.
- Price is position, Return is movement, Position drifts, movement oscillates

| Concept        | What it asks                        |
| -------------- | ----------------------------------- |
| Hurst Exponent | “Does movement persist or reverse?” |
| Variance Ratio | “Do moves reinforce or cancel?”     |

## Chapter 3: Implementing a mean reverting strategy

- "All-in" vs "Scaling-in" (AKA averaging in)
  Scaling in works better in practice, despite what the mathematics say.
- Cointegration / pair trading

## Chapter 4: Mean reversion of stocks and ETFS

- For stocks, too much risk to do pair trading
- BUT for ETF, pair trading / triplet trading is still profitable. 
- Intraday Mean reversion (buy on Gap model)
- Index Arbitrage
  - If SPY becomes more expensive than its underlying stocks
    - you short SPY and buy underlying basket
  - If SPY becomes cheaper than its underlying stocks
    - you buy SPY and short the basket
  - You profit when prices converge
  - High Frequency Trading territory, if you want to measure all 500 stocks under SPY
  - **BUT**, a subset is doable
    - instead of replicating all 500 stocks of S&P 500
    - Maybe you pick top 50 most liquid stocks
    - Or largest 100 by market cap
    - or tech-heavy subset
    - or high-beta subset
    Now you compute a syntetic mini-index. and compare that to futures.
    
    This works because sometimes
    - Mega caps move first
    - small caps lag
    - tech leads
    - defensive lags
  
    "If obvious arb is gone, engineer you own synthetic inefficiency"

    Another example
    - If ES jumps and SPY lags:
    - Most likely Buy SPY (follow futures)
    - If ES trades above fair carry-adjusted value:
    - Short ES + long SPY (arb)
    

- Cross Sectional Mean Reversion
  - Linear strategy
  - if Stock A up 4%, and Stock B up 2 %, you short stock A twice as you short Stock B.

## Glossary

- **Sharpe Ratio**:
  
  The Sharpe ratio is defined as a measure of the return per unit of risk for an investment . It is calculated by dividing the excess return of a portfolio by its volatility, which is a measure of the portfolio's risk . The formula for the Sharpe ratio is `(R_p - R_f) / σ_p`, where `R_p` is the average return of the portfolio, `R_f` is the risk-free rate, and `σ_p` is the volatility of the portfolio .

  Sharpe hdes tail risk; two strategies with same Sharpe can have very different drawdowns.

- **Johansen's Test**
  
  Stock prices usually wonder, but some prices **move together long term**
  Examples: Two shares classes of the same company; Oil spot price vs oil futures; ETD vs its underlying basket
  Johansen’s test checks:
  - “Is there one or more stable relationship hidden inside these drifting series?”
  - Instead of looking at prices individually, it asks:
    - Can I form a weighted combination of them
    - That combination does NOT drift endlessly
    - And instead wiggles around a stable level
  - If yes → they are cointegrated
  
  Johansen's test checks whether multiple wandering price series are secretly tied together by stable long-term relationships - and tells you how many such ties exist.

- **Index Arbitrage**

- **Contango**: Future concepts, future months are more expensive than near month
  - Example:
    - March oil = $70
    - April oil = $72
    - May oil = $74
  - So if you want to stay long every month, you have will have to pay $2 every month!
  - That $2 is negative roll return
  - It is cost of carry
  - Contango exists usually due to storage cost, financing cost, insurance cost, (e.g. holding physical oil costs money)
- **Backwardation**
  - Opposite of Contango
  - Future months are cheaper than near month
  - When you sell march at $70, buy April At $68, you gain $2, that is positive roll return.
  - Backwardation exists usually due to Supply shortage; immediate demand spike; convenience yield (peopl wnat oil NOW)

  
