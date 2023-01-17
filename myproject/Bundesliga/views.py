import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def get_last_results(request):
    matchday = request.GET.get('matchday')
    matchdays = [str(i) for i in range(1, 33)]
    if matchday not in matchdays:
        url = f'https://www.openligadb.de/api/getmatchdata/bl1'
    else:
        url = f'https://www.openligadb.de/api/getmatchdata/bl1/2022/{matchday}'
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        return render(request, 'results.html', {'results': results, 'matchdays': matchdays})
    else:
        return render(request, 'error.html', {'message': 'Unable to retrieve results from OpenLigaDB API'})

