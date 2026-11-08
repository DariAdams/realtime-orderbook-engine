
# Real-Time Order Book Engine

A Python-based order book simulator with real-time market data streaming, order management, unit tests, and performance benchmarking.

## Features

- Add and cancel buy/sell orders
- Best bid and best ask calculations
- Bid-ask spread calculation
- Aggregated market depth
- WebSocket market data streaming
- Input validation using Decimal prices
- Automated tests with pytest
- Performance benchmarking

## Tech Stack

Python 3.14, asyncio, WebSockets, pytest

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run the Order Book

```bash
python main.py
```

## Run Tests

```bash
python -m pytest -v
```

Current results: 13 tests passed.

## Run Benchmark

```bash
python benchmarks/benchmark_orderbook.py
```

### Sample Benchmark Results

Measured on a local Windows machine:

- Orders inserted: 10,000
- Total insertion time: 0.024876 seconds
- Average insertion time: approximately 2.49 microseconds
- 200 best-price queries: 0.096805 seconds

Results vary by hardware and runtime conditions.

## WebSocket Demo

Start the server:

```bash
python -m market_data.websocket_server
```

Open a second terminal and start the client:

```bash
python -m market_data.websocket_client
```

The client processes 20 simulated market data messages.

## Limitations

This project is an educational order book simulator, not a production trading engine.

It does not currently implement order matching, trade execution, or price-time priority. Best-price queries scan the stored orders and have O(n) time complexity.

The market data feed is simulated rather than connected to a live exchange.

## Future Improvements

- Price-level indexing
- Order matching engine
- Automated WebSocket integration tests
- Continuous integration with GitHub Actions
- Latency optimization
