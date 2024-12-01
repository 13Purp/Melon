from collections import defaultdict
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
import pandas as pd
from collections import defaultdict

from MelonApp.models import Firma, Pos, Promocija, PopustFirma, Transakcije


@login_required
def landingPage(request):
    firma = Firma.objects.filter(username=request.user.username).first()

    context = {}
    if firma:
        context['strana_sveta'] = firma.strana_sveta
        context['sprat'] = firma.sprat
        context['tip'] = firma.tip
        context['naziv'] = firma.naziv

    pos_terminals = Pos.objects.filter(idf=firma)

    if pos_terminals:
        context['pos_terminals'] = pos_terminals

    promotions = Promocija.objects.filter(idf=firma.id)
    if promotions:
        context['promotions'] = promotions

    return render(request, 'index.html', context)


@login_required
def get_promo_details(request, promo_id):
    promocija = get_object_or_404(Promocija, id=promo_id)

    firme = PopustFirma.objects.filter(idp=promo_id).select_related('idf')
    firme_list = [{'naziv': firma.idf.naziv} for firma in firme]

    data = {
        "id": promocija.id,
        "ukupno": promocija.ukupno,
        "iskorisceno": promocija.iskorisceno,
        "flat_popust": promocija.flat_popust,
        "procenat_popust": promocija.procenat_popust,
        "minimalan_iznos": promocija.minimalan_iznos,
        "od": promocija.od.strftime('%Y-%m-%d') if promocija.od else None,
        "do": promocija.do.strftime('%Y-%m-%d') if promocija.do else None,
        "firme": firme_list,
    }
    return JsonResponse(data)


def dodajPromociju(request):
    pass


def aboutPage(request):
    return render(request, 'oNama.html')


def sveZivo(request):
    return render(request, 'landingPage.html')


def clan(request):
    return render(request, 'pregledClana.html')


def members(request):
    return None


def tournaments(request):
    return None


def matchup(request):
    return render(request, 'matchupTree.html')


def vesti(request):
    return render(request, 'vesti.html')


def najave(request):
    return render(request, 'vesti.html')


def kalendar(request):
    return render(request, 'vesti.html')


def galerija(request):
    return None


def opomene(request):
    return None


def faq(request):
    return None


@login_required
def dodajPopust(request):
    prijavljenaFirmaId = request.session['id']
    firme = Firma.objects.exclude(id=prijavljenaFirmaId)

    if request.method == 'POST':
        firms = request.POST.getlist('firmsList')
        ukupno = request.POST.get('totalCount')
        minimalan_iznos = request.POST.get('minAmount') or None
        flat_popust = request.POST.get('flatDiscount') or None
        procenat_popust = request.POST.get('percentDiscount') or None
        max_iznos = request.POST.get('maxAmount') or None
        datum_od = datetime.strptime(request.POST.get('startDate'), '%Y-%m-%d')
        datum_do = datetime.strptime(request.POST.get('endDate'), '%Y-%m-%d')

        promocija = Promocija.objects.create(
            idf_id=prijavljenaFirmaId,
            ukupno=ukupno,
            iskorisceno=0,
            minimalan_iznos=minimalan_iznos,
            flat_popust=flat_popust,
            procenat_popust=procenat_popust,
            max_iznos=max_iznos,
            od=datum_od,
            do=datum_do
        )
        for firma_id in firms:
            PopustFirma.objects.create(idp=promocija, idf_id=firma_id)
        
    return render(request, 'dodajPopust.html', {'firme':firme})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        firma_user = None

        try:
            firma_user = Firma.objects.get(username=username, password=password)
        except Firma.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Nevalidni podaci za logovanje'})

        user = None
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
        else:
            user = User.objects.create_user(username=username, password=password, email=firma_user.username)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['logovan'] = 1
            request.session['id'] = firma_user.id
            return HttpResponseRedirect(reverse('landingPage'))
        else:
            return render(request, 'login.html', {'error_message': 'Autentifikacija neuspešna'})

    return render(request, 'login.html')

@login_required
def stats(request):
    firma = Firma.objects.filter(username=request.user.username).first()
    promotions = Promocija.objects.filter(idf = firma.id)

    chart_data = []
    for promo in promotions:
        if promo.ukupno and promo.ukupno > 0:
            percentage_used = promo.iskorisceno / promo.ukupno * 100
            chart_data.append({
                "name": f"Promo {promo.id}",
                "value": percentage_used
            })

    transactionsNoDiscount = Transakcije.objects.filter(id_f=firma.id, popust=False)

    # Dictionary to store the counts of transactions per date
    transaction_counts = defaultdict(int)

    # Loop through the transactions and group by date
    for trans in transactionsNoDiscount:
        # Extract the date (ignoring time part)
        date_only = trans.datum_vreme.date()

        # Increment the count for that date
        transaction_counts[date_only] += 1

    # Prepare data for the chart
    trans_chart_data = [{'date': date, 'count': count} for date, count in transaction_counts.items()]


    # Sort the data by date
    trans_chart_data.sort(key=lambda x: x['date'])

    # Print the result (optional)
    print("Transdata: ")
    print(trans_chart_data)

    transactionsNoDiscount = Transakcije.objects.filter(id_f=firma.id)

    # Dictionary to store the counts of transactions per date
    transaction_counts = defaultdict(int)

    # Loop through the transactions and group by date
    for trans in transactionsNoDiscount:
        # Extract the date (ignoring time part)
        date_only = trans.datum_vreme.date()

        # Increment the count for that date
        transaction_counts[date_only] += 1

    # Prepare data for the chart
    trans_chart_dataall = [{'date': date, 'count': count} for date, count in transaction_counts.items()]

    # Sort the data by date
    trans_chart_dataall.sort(key=lambda x: x['date'])

    # Print the result (optional)
    print("TransdataAll: ")
    print(trans_chart_dataall)


    return render(request, 'stats.html', {
        "chart_data": chart_data,
        "trans_chart_data": trans_chart_data,
        "trans_chart_dataall":trans_chart_dataall
    })



# statistics

def get_top_transitions_as_json(target_store, exclude_stores=None, n=5):
    # Load the CSV file (adjust the file path if necessary)
    df = pd.read_csv('static/csv/gen2.csv')

    # Preprocess the data
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by=['customer_id', 'timestamp'])

    markov_order = 3
    food_stores = ['McDonalds', 'KFC', 'AsianFood', 'BurritoMadre', 'Obrock']  # penalty

    transitions = defaultdict(lambda: defaultdict(int))

    for customer_id, group in df.groupby('customer_id'):
        visited_stores = group['store'].tolist()
        for i in range(markov_order, len(visited_stores)):
            previous_stores = tuple(visited_stores[i - markov_order:i])
            current_store = visited_stores[i]

            if current_store == previous_stores[-1]:
                continue

            # Apply penalty for transitions involving food stores
            if any(store in food_stores for store in previous_stores) or current_store in food_stores:
                probability_penalty = 0.05  # Increased penalty for food stores
            else:
                probability_penalty = 1.0

            transitions[previous_stores][current_store] += probability_penalty

    store_statistics = {}
    for sequence, incoming_transitions in transitions.items():
        total_visits = sum(incoming_transitions.values())
        if total_visits > 0:
            store_statistics[sequence] = {
                next_store: count / total_visits
                for next_store, count in incoming_transitions.items()
            }

    # Exclude stores if not provided (default: food stores)
    if exclude_stores is None:
        exclude_stores = food_stores

    # Get top transitions
    direct_transitions = defaultdict(float)

    for sequence, stats in store_statistics.items():
        for next_store, probability in stats.items():
            if next_store == target_store:
                for prev_store in sequence:
                    if prev_store not in exclude_stores:
                        direct_transitions[prev_store] += probability

    total_probability = sum(direct_transitions.values())
    if total_probability > 0:
        for store in direct_transitions:
            direct_transitions[store] /= total_probability

    data = []
    for store, probability in direct_transitions.items():
        data.append({
            'store': store,
            'probability': probability
        })

    # Sort the results and limit to top n
    data = sorted(data, key=lambda x: x['probability'], reverse=True)[:n]

    return data


def statistics(request, store_name):
    # You can add other parameters to the request if needed
    # For example: threshold, exclude_stores, etc.

    data = get_top_transitions_as_json(store_name)

    # Return JSON response
    return JsonResponse(data, safe=False)


