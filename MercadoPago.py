import mercadopago

ACCES_TOKEN = 'APP_USR-3566721383827287-091401-35fe59cc6025036eed77d461f7651b85-1198072599'
PUBLIC_KEY = 'APP_USR-a496fb36-b123-4ebf-bd22-68e0772067ef'

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
