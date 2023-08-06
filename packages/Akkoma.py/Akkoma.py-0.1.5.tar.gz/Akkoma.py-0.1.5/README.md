# Akkoma.py
Python wrapper for the Akkoma (https://akkoma.dev/AkkomaGang/akkoma) API.  

    # Register your app! This only needs to be done once. Uncomment the code and substitute in your information.
    
    from akkoma import Akkoma

    '''
    client_id, client_secret = Akkoma.create_app(
        'app_name',
        to_file="app_clientcred.txt",
        api_base_url = 'https://yourakkoma.instance'
        )
    '''

    # Then login. This can be done every time, or use persisted.

    from akkoma import Akkoma
    
    akkoma = Akkoma(client_id = "app_clientcred.txt", api_base_url = 'https://yourakkoma.instance')

    grant_type = 'password'

    akkoma.log_in(
        client_id,
        client_secret,
        grant_type,
        'user',
        'password',
    to_file = "app_usercred.txt"
    )   

    # To post, create an actual API instance.

    from akkoma import Akkoma
    
    akkoma = Akkoma(
        access_token = 'app_usercred.txt',
        api_base_url = 'https://yourakkoma.instance'
    )
    akkoma.status_post('Posting from python using Akkoma.py !')


