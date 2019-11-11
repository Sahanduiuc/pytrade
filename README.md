<img src="https://combinatronics.com/ranaroussi/pytrade/master/logo.svg" height="120">

# PyTrade: Pythonic Trading Framework

This is the home of **PyTrade** - a Python Trading Framework.

PyTrade is based on my [vision for the future of QTPyLib](https://aroussi.com/post/the-future-of-qtpylib), though I felt its best to start fresh with a new name and no shared code.

**PyTrade** will use a microservice architecture where every part of the trading system can be used separately
(market data handling, backtesting, etc). Additionally, every data vendor and broker will be installed via a separate sub-package.

For example, ``$ pip install pytrade`` will install the core package which includes the back-tester and base classes,
whereas ``$ pip install pytrade-ib`` will add support for Interactive Brokers, and ``$ pip install pytrade-bitmex`` will add support for BitMEX, etc...

I'm using the same approach for loggers and datastores: ``$ pip install pytrade-sqlalchemy pytrade-pystore pytrade-mongodb``, etc.
