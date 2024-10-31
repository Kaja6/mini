from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Placeholder route to handle form submission
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    amount = request.form.get('amount')  # get the amount from the form
    # For now, just print the amount (we'll integrate Stripe here later)
    print(f"Selected amount: {amount}")
    return f"Amount {int(amount) / 100}€ selected!"

if __name__ == '__main__':
    app.run(debug=True)
