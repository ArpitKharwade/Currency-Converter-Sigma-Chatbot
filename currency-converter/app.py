



#Main code

# from flask import Flask, request, jsonify
# import requests
#
#
# app = Flask(__name__)
#
#
# @app.route('/',methods=['POST'])
# def index():
#     data = request.get_json()
#     source_currency = data['queryResult']['parameters']['unit-currency']['currency']
#     amount = data['queryResult']['parameters']['unit-currency']['amount']
#     target_currency = data['queryResult']['parameters']['currency-name']
#
#     # print(source_currency)
#     # print(amount)
#     # print(target_currency)
#
#     cf = fetch_conversion_factor(source_currency,target_currency)
#     final_amount = amount * cf
#
#
#     response = {
#         'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
#     }
#     return jsonify(response)
# def fetch_conversion_factor(source, target):
#     url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_HHdebq47uPNEPxeJBQZoYs8DIGz4M34vBlNx70iV&currencies={}&base_currency={}".format(source,target)
#
#     response = requests.get(url)
#     response = response.json()
#
#     return response['{}_{}'.format(source,target)]
#
#
# if __name__ == "__main__":
#     app.run(debug=True)




#Deepseek code

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    cf = fetch_conversion_factor(source_currency, target_currency)
    if cf is None:
        response = {
            'fulfillmentText': "Sorry, I couldn't retrieve the conversion rate. Please check the currencies and try again."
        }
        return jsonify(response)

    final_amount = amount * cf
    final_amount = round(final_amount,2)

    response = {
        'fulfillmentText': "{} {} is {:.2f} {}".format(amount, source_currency, final_amount, target_currency)
    }
    return jsonify(response)


def fetch_conversion_factor(source, target):
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_HHdebq47uPNEPxeJBQZoYs8DIGz4M34vBlNx70iV&currencies={}&base_currency={}".format(
        target, source)

    response = requests.get(url)
    if response.status_code != 200:
        return None

    response_data = response.json()
    if 'data' not in response_data or target not in response_data['data']:
        return None

    return response_data['data'][target]


if __name__ == "__main__":
    app.run(debug=True)