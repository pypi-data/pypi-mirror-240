from typing import Union

import requests

from requests.models import Request

from bs4 import BeautifulSoup

from custom.exceptions import TokenException
from custom.types import RutStatusDict
from custom import utils


  
def get_person_rut_status(token:str, nit:str, attempts:int=utils.DEFAULT_ATTEMPTS, timeout:int=utils.DEFAULT_TIMEOUT)->Union[RutStatusDict, None]:
    
    """This function will returns a Person Rut Status information stored inside a Dict
    
    Args:
        token: a string to make a successfull request
        
        nit: a string that represents the Colombia Unique Taxpayer Number is number assigned to persons who must pay taxes.
        
        attempts: an integer which represents the number of seconds to retry the function (5 by default)
        
        timeout: an integer which representes the number of seconds to sleep in case of a request timeout (10 by default)

    Raises:
        TokenException: When the request's token is missing or is a blank string

    Returns:
        RutStatusDict: A typed dictionary with the main key and values from an actual legal or natural person
        None: if there is an error on the code in execution
    """
    
    if not token:
        raise TokenException('The Token is Missing!')
    
    if attempts == 0:
        print('All attempts completed! ')
        return
    
    try:
        response = requests.post(url=utils.WEB_RUT_MUISCA_URL, data={**utils.PAYLOAD_DATA, utils.as_form_field('numNit'): nit, utils.TOKEN_FIELD: token}, timeout=timeout)
        
        if isinstance(response, Request):
            response.raise_for_status()
            
    except requests.Timeout:
        return get_person_rut_status(token=token, nit=nit, attempts=attempts-1)
    except Exception as e:
        print(e)
    else:
        soup = BeautifulSoup(response.text, features='html.parser') if response else None
        return None if not soup else utils.get_person_rut_status_from_soup(soup=soup)