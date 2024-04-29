import mercadopago

ACCES_TOKEN = ''
PUBLIC_KEY = ''

sdk = mercadopago.SDK(ACCES_TOKEN)


def get_init_point(url, data):
    preference_data = {
        "items": [
            {
                "title": "BackTest Wizard",
                "quantity": 1,
                "unit_price": 75,
            }
        ],
        "back_urls": {
            "success": f"{url}notification",
            "failure": f"{url}notification"
        },
        "binary_mode": True,
        "auto_return": "approved",
        "external_reference": f"{data}",
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    #preference_id = preference['id']
    init_point = preference['init_point']
    return init_point
