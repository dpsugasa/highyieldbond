# highyieldbond

Simple python package for pricing high yield bonds using QuantLib

### Requires:

  * Bloomberg access for yield curve and credit market data
  * PlotLy for visualization (in progress)

### File and Directory Description:

  * market_data - directory that holds the yield curve and bond terms files
      * yield_curve.py - yield curve object; data pulled from Bloomberg
      * bond_terms.py - bond terms and callability schedule
  * credit_data - directory that holds the credit curve files
      * credit_curve.py - credit curve object; data pulled from Bloomberg
  * pricer.py - file that generates bond prices (fixed, callable, risky callable)
  * visualize.py - file that publishes bond analytics and graphs to PlotLy (in progress)


![return_performance](https://user-images.githubusercontent.com/26715208/53972341-7fb1c500-40f6-11e9-9bb2-cce001082fdb.png)
