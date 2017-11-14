import sendgrid

API_KEY = 'API_KEY'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def best_country(str_date):

    response = sg.client.geo.stats.get(query_params={
        'start_date': '2017-11-01',
        'end_date': '2017-11-30'
    })
    import json

    print(json.loads(response.body))
    return 'UA'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Your best country in 2017-11-01 was ' + best_country('2017-11-01'))
    print('Check your results')