""" Lambda function """
import os
import json
import datetime
import exceptions
import unidecode
import get_contracts
import send_email

def lambda_handler(event, context):
    """Sample pure Lambda function """

    convenente = os.environ["convenente"]
    dest = os.environ["dest"]

    subject = "Monitor do Portal da Transparencia"
    message = ""
    status_code = ""

    try:
        contracts = get_contracts.get_contracts(convenente)
    except exceptions.RequestError:
        message = 'Request Error different than 200'
        status_code = 998
    except Exception as error:
        message = error.message + error.args
        status_code = 999
    else:
        status_code = 200
        status = []
        for contract in contracts:
            status.append(unidecode.unidecode(contract["situacao"]["descricao"]))

        if 'INADIMPLENTE' in status:
            message = "Tem convenio com status INADIMPLENTE"
            send_email.send_email(dest, subject, message)
        else:
            message = "Monitor do Portal da Transparencia esta rodando"
            if datetime.date.today().weekday() == 0:
                send_email.send_email(dest, subject, message)

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": message,
        }),
    }
