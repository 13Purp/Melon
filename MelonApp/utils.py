import sqlite3
import json
from collections import defaultdict

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Fetch the stores and transactions data
cursor.execute("SELECT id, naziv, tip FROM firma")
stores = cursor.fetchall()  # Fetch all stores

cursor.execute("SELECT id_t, id_f, encrypted_card, datum_vreme FROM transakcije")
transactions = cursor.fetchall()  # Fetch all transactions


# Store store names, ids, and types in a dictionary for easy lookup
store_names = {store[0]: store[1] for store in stores}
store_types = {store[0]: store[2] for store in stores}

# Get the list of food stores dynamically (those with 'food' type)
food_stores = [store_id for store_id, store_type in store_types.items() if store_type == 'food']

# Set up the transitions dictionary
markov_order = 3
transitions = defaultdict(lambda: defaultdict(int))

# Group transactions by encrypted_card (customer_id)
transactions_by_customer = defaultdict(list)

for transaction in transactions:
    # Extract the relevant data from the transaction
    id_t, id_store, encrypted_card, datetime = transaction

    # Append the transaction to the customer's list of transactions
    transactions_by_customer[encrypted_card].append((id_store, datetime))

# Process transitions for each customer
for customer_id, customer_transactions in transactions_by_customer.items():
    # Sort transactions by datetime
    customer_transactions.sort(key=lambda x: x[1])

    # Extract the store sequence (store IDs) for the customer
    visited_stores = [store_id for store_id, _ in customer_transactions]

    # Process transitions using Markov order
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

# Now, store_statistics should be calculated as before
store_statistics = {}
for sequence, incoming_transitions in transitions.items():
    total_visits = sum(incoming_transitions.values())
    if total_visits > 0:
        store_statistics[sequence] = {
            next_store: count / total_visits
            for next_store, count in incoming_transitions.items()
        }

# The rest of the code remains the same


from collections import defaultdict
from .models import Firma

def get_top_transitions_as_json(store_id, n=5):
    # Get the store type (food or other) using the store_id
    try:
        store = Firma.objects.get(id=store_id)
        store_type = store.tip
    except Firma.DoesNotExist:
        return {'error': 'Firma not found'}

    # List of store IDs that represent food stores (this can be derived dynamically based on the type)
    food_stores = Firma.objects.filter(tip='food').values_list('id', flat=True)

    direct_transitions = defaultdict(float)

    # Process transitions (assuming store_statistics is calculated somewhere else in the model)
    for sequence, stats in store_statistics.items():
        for next_store_id, probability in stats.items():
            print(f"Processing transition from {sequence} to {next_store_id} with probability {probability}")
            if next_store_id == store_id:  # We're interested in the current store's transitions
                for prev_store_id in sequence:
                    # Check if previous stores are in the food stores list and apply penalty
                    if prev_store_id in food_stores or next_store_id in food_stores:
                        probability_penalty = 0.05  # Apply penalty for food stores
                    else:
                        probability_penalty = 1.0

                    # Apply the penalty
                    direct_transitions[prev_store_id] += probability * probability_penalty

    # Normalize the probabilities
    total_probability = sum(direct_transitions.values())
    if total_probability > 0:
        for store in direct_transitions:
            direct_transitions[store] /= total_probability

    # Create the final data list and sort
    data = [{'store': Firma.objects.get(id=store).naziv, 'probability': probability*100} for store, probability in direct_transitions.items()]
    data = sorted(data, key=lambda x: x['probability'], reverse=True)[:n]

    return data
