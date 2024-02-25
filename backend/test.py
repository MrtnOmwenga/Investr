from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/eod_data', methods=['GET'])
def eod_data():
  data = [
    {'open': 199.6, 'high': 201.14, 'low': 198.57, 'close': 199.89, 'volume': 37616800.0, 'adj_high': 201.135, 'adj_low': 198.565, 'adj_close': 199.89, 'adj_open': 199.6, 'adj_volume': 37667681.0, 'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'IWM', 'exchange': 'ARCX', 'date': '2024-02-23T00:00:00+0000'},
    {'open': 415.67, 'high': 415.86, 'low': 408.97, 'close': 410.34, 'volume': 16295879.0, 'adj_high': 415.86, 'adj_low': 408.97, 'adj_close': 410.34, 'adj_open': 415.67, 'adj_volume': 16295879.0, 'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'MSFT', 'exchange': 'XNAS', 'date': '2024-02-23T00:00:00+0000'},
    {'open': 143.67, 'high': 144.68, 'low': 143.43, 'close': 143.96, 'volume': 19493752.0, 'adj_high': 144.68, 'adj_low': 143.43, 'adj_close': 143.96, 'adj_open': 143.67, 'adj_volume': 19493752.0, 'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'GOOGL', 'exchange': 'XNAS', 'date': '2024-02-23T00:00:00+0000'},
    [],
    [],
    {'open': 185.01, 'high': 185.04, 'low': 182.23, 'close': 182.52, 'volume': 45074500.0, 'adj_high': 185.04, 'adj_low': 182.23, 'adj_close': 182.52, 'adj_open': 185.01, 'adj_volume': 45119677.0, 'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'AAPL', 'exchange': 'XNAS', 'date': '2024-02-23T00:00:00+0000'},
    {'open': 439.65, 'high': 440.59, 'low': 435.79, 'close': 436.78, 'volume': 39794400.0, 'adj_high': 440.59, 'adj_low': 435.79, 'adj_close': 436.78, 'adj_open': 439.65, 'adj_volume': 39853861.0, 'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'QQQ', 'exchange': 'XNAS', 'date': '2024-02-23T00:00:00+0000'},
    {'open': 23.97, 'high': 23.97, 'low': 23.31, 'close': 23.32, 'volume': 212790.0, 'adj_high': None, 'adj_low': None, 'adj_close': 23.32, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'ETH', 'exchange': 'XNYS', 'date': '2021-10-15T00:00:00+0000'},
    {'open': 509.27, 'high': 510.13, 'low': 507.1, 'close': 507.85, 'volume': 61321818.0, 'adj_high': 510.13, 'adj_low': 507.1, 'adj_close': 507.85, 'adj_open': 509.27, 'adj_volume': 61321818.0, 'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'SPY', 'exchange': 'ARCX', 'date': '2024-02-23T00:00:00+0000'},
    [],
    {'open': 32.14, 'high': 32.18, 'low': 31.84, 'close': 31.84, 'volume': 198980.0, 'adj_high': 32.18, 'adj_low': 31.84, 'adj_close': 31.84, 'adj_open': 32.14, 'adj_volume': 198980.0, 'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'LTC', 'exchange': 'XNYS', 'date': '2024-02-23T00:00:00+0000'},
    {'open': 92.397, 'high': 92.397, 'low': 92.317, 'close': 92.317, 'volume': 366.0, 'adj_high': None, 'adj_low': None, 'adj_close': 92.317, 'adj_open': None, 'adj_volume': None, 'split_factor': 1.0, 'dividend': 0.0, 'symbol': 'BTC', 'exchange': 'ARCX', 'date': '2022-06-27T00:00:00+0000'}
  ]
  return jsonify({ "data": data })

if __name__ == '__main__':
  app.run(debug=True)