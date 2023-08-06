Mastodonplus.py
===========
Fork of Python wrapper for the Mastodon ( https://github.com/tootsuite/mastodon/ ) API.
This fork's goal is to add new Mastodon API endpoints to the excellent halcy's wrapper.

.. code-block:: python

    # Register your app! This only needs to be done once. Uncomment the code and substitute in your information.
    
    from mastodon import Mastodon

    '''
    Mastodon.create_app(
         'pytooterapp',
         api_base_url = 'https://mastodon.social',
         to_file = 'pytooter_clientcred.secret'
    )
    '''

    # Then login. This can be done every time, or use persisted.

    from mastodon import Mastodon
    
    mastodon = Mastodon(
        client_id = 'pytooter_clientcred.secret',
        api_base_url = 'https://mastodon.social'
    )
    mastodon.log_in(
        'my_login_email@example.com',
        'incrediblygoodpassword',
        to_file = 'pytooter_usercred.secret'
    )

    # To post, create an actual API instance.

    from mastodon import Mastodon
    
    mastodon = Mastodon(
        access_token = 'pytooter_usercred.secret',
        api_base_url = 'https://mastodon.social'
    )
    mastodon.toot('Tooting from python using #mastodonpy !')

You can install Mastodonplus.py via pypi:

.. code-block:: Bash
   
   # Python 3
   pip3 install Mastodonplus.py  

*** 26.8.2022. Added New endpoints: /api/v1/admin/domain_blocks (list, show by id, delete and create)

