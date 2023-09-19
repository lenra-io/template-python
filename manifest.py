manifest = {
    'json': 
    {
        'routes': [
            {
                'path': '/counter/global',
                'view': {
                    '_type': 'view',
                    'name': 'counter',
                    'find': {
                        'coll': 'counter',
                        'query': {
                            'user': 'global'
                        }
                    }
                }
            },
            {
                'path': '/counter/me',
                'view': {
                    '_type': 'view',
                    'name': 'counter',
                    'find': {
                        'coll': 'counter',
                        'query': {
                            'user': '@me'
                        }
                    }
                }
            }
        ]
    },
    'lenra': 
    {
        'routes': [
            {
                'path': '/',
                'view': {
                    '_type': 'view',
                    'name': 'main'
                }
            }
        ]
    }
}