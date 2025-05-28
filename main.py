async def app(scope: list, receive, send):
    assert scope["type"] == 'http'

    try:
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers':[
                (b'content-type',b'text-plain'),
                (b'content-length',b'13')
            ]
        })

        await send({
            'type':'http.response.body',
            'body':b'Hello, world!'
        })
    
    except:
        print("Failed to start server.")
