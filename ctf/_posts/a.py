from flask import Flask, request, render_template_string
app = Flask(__name__)
app.secret_key = 'flag\{ultimate_jinja_storm3\}'
@app.route('/')
def index():
    a = request.args.get('adj1') or None
    b = request.args.get('adj2') or None
    c = request.args.get('place') or None
    d = request.args.get('topping1') or None
    e = request.args.get('topping2') or None
    f = request.args.get('person') or None
    template = ''' <h1>Mad libs</h1><br><p>I just got back from a ___{a}___(adj1) party with EverSec. Can you believe we got to eat __{b}___(adj2) pizza in ____{c}___(place)?! Everyone got to choose their own toppings. I made ___{d}___(topping1) and __{e}___(topping2) pizza, which is my favorite! How fun! If that wasn't good enough already, ___{f}____(person) was there teaching exploits! </p> '''.format(a = a, b = b, c=c, d=d, e=e, f=f)
    return render_template_string(template)
if __name__ == '__main__': 
    pp.run(host='0.0.0.0', port=8080)