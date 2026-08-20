# Melon

Turning a shopping mall's point-of-sale (POS) terminals into a network that predicts where a shopper will go next — and offers them a discount to go there.

Built at the **Payten hackathon**.

## The idea

POS terminals normally work in isolation: one shop, one payment, done. Melon connects every terminal in a mall so that a card payment in one store becomes a signal about the whole visit.

When a customer pays at a shop, the system looks at the sequence of stores that card has visited and predicts which shops they are most likely to visit next. Those predicted shops can then push a targeted discount straight to that card, while the customer is still in the mall.

The mall gets higher footfall, the shops get customers who are already nearby and likely to buy, and the shopper gets an offer that is actually relevant to where they are going.

## How the prediction works

Shopper movement between stores is modelled as a **Markov chain**: each shop is a state, and card transaction history gives the transition probabilities between them. Given the store a customer just paid at, the model ranks the most probable next stores, and discounts are targeted at those.

## Tech stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** JavaScript, HTML, CSS

## Running it locally

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

## Team

Built by [@13Purp](https://github.com/13Purp), [@kalumatic](https://github.com/kalumatic) and [@AcaUrosevic](https://github.com/AcaUrosevic).

## Status

Hackathon prototype — built under time pressure and not maintained since.
